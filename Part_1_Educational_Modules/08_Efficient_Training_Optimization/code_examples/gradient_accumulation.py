import torch
import torch.nn as nn
import torch.optim as optim

def demonstrate_efficient_training():
    """
    Demonstrates Gradient Accumulation and Automatic Mixed Precision (AMP),
    two crucial techniques for training large models on consumer hardware.
    """
    print("--- Efficient Training Optimization Example ---")

    # 1. Hyperparameters for Accumulation
    # Suppose we WANT a batch size of 64, but our GPU can only fit 16.
    desired_batch_size = 64
    micro_batch_size = 16
    accumulation_steps = desired_batch_size // micro_batch_size # 64 / 16 = 4 steps
    
    input_size = 100
    output_size = 10
    
    # 2. Setup Model, Optimizer, and Loss
    model = nn.Sequential(
        nn.Linear(input_size, 512),
        nn.ReLU(),
        nn.Linear(512, output_size)
    )
    
    # If a GPU is available, move the model to it. AMP requires CUDA.
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    optimizer = optim.AdamW(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()
    
    # 3. Setup Mixed Precision Scaler
    # This prevents underflow when using float16 by scaling the gradients up before backward pass,
    # and scaling them back down before the optimizer step.
    scaler = torch.cuda.amp.GradScaler(enabled=torch.cuda.is_available())

    print(f"Target Batch Size: {desired_batch_size}")
    print(f"Micro-Batch Size: {micro_batch_size}")
    print(f"Accumulation Steps Required: {accumulation_steps}\n")

    # Simulate a training loop
    model.train()
    optimizer.zero_grad() # Zero gradients at the very beginning
    
    for step in range(1, accumulation_steps + 1):
        
        # Simulate loading a micro-batch of data (e.g., 16 examples)
        X_micro = torch.randn(micro_batch_size, input_size).to(device)
        y_micro = torch.randint(0, output_size, (micro_batch_size,)).to(device)
        
        # --- MIXED PRECISION FORWARD PASS ---
        # autocast() automatically chooses the best precision (FP16 or FP32) for each operation
        with torch.cuda.amp.autocast(enabled=torch.cuda.is_available()):
            predictions = model(X_micro)
            loss = criterion(predictions, y_micro)
            
            # CRITICAL: We must divide the loss by the number of accumulation steps.
            # Otherwise, we aren't averaging the loss across the full desired batch, we are summing it,
            # which would make the gradients 4x too large!
            loss = loss / accumulation_steps
            
        # --- MIXED PRECISION BACKWARD PASS ---
        # We scale the loss and call backward to compute gradients.
        # Notice we DO NOT step the optimizer yet. The gradients are accumulating.
        scaler.scale(loss).backward()
        
        print(f"Step {step}/{accumulation_steps} completed. Gradients accumulated. (Micro-Loss: {loss.item():.4f})")
        
        # --- ACCUMULATION COMPLETE ---
        # Once we have accumulated enough steps to equal our desired batch size,
        # we finally update the weights.
        if step % accumulation_steps == 0:
            print("\nAccumulation target reached! Updating model weights...")
            
            # 1. Unscale the gradients and call optimizer.step()
            scaler.step(optimizer)
            
            # 2. Update the scaler for the next iteration
            scaler.update()
            
            # 3. Explicitly zero the gradients to start fresh for the next batch
            optimizer.zero_grad()
            
            print("Model weights updated successfully.")

if __name__ == "__main__":
    demonstrate_efficient_training()
