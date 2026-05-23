import torch
import torch.nn as nn
from torch.optim import AdamW
from torch.optim.lr_scheduler import CosineAnnealingLR

def demonstrate_training_loop():
    """
    Demonstrates the core mechanics of a PyTorch training loop for an LLM.
    We use dummy tensors instead of a real dataset and model to keep it minimal.
    """
    print("--- LLM Training Loop Demonstration ---")
    
    # 1. Mock Setup
    vocab_size = 32000
    batch_size = 4
    seq_length = 512
    d_model = 768
    
    # A tiny dummy model: Embedding -> Linear layer mapping back to vocab
    model = nn.Sequential(
        nn.Embedding(vocab_size, d_model),
        nn.Linear(d_model, vocab_size)
    )
    
    # 2. Loss Function & Optimizer
    # CrossEntropyLoss automatically applies Softmax and Negative Log-Likelihood
    criterion = nn.CrossEntropyLoss()
    
    # AdamW is the industry standard for LLMs
    optimizer = AdamW(model.parameters(), lr=3e-4, weight_decay=0.1)
    
    # 3. Learning Rate Scheduler (Cosine Decay)
    epochs = 5
    scheduler = CosineAnnealingLR(optimizer, T_max=epochs)
    
    # 4. The Training Loop
    print("\nStarting Training Loop...")
    for epoch in range(epochs):
        
        # --- Simulating a DataLoader fetching a batch ---
        # input_ids: The sequence of tokens [Batch, Seq_Len]
        # target_ids: The correct 'next tokens' to predict [Batch, Seq_Len]
        input_ids = torch.randint(0, vocab_size, (batch_size, seq_length))
        target_ids = torch.randint(0, vocab_size, (batch_size, seq_length))
        
        # --- Step 1: Zero Gradients ---
        optimizer.zero_grad()
        
        # --- Step 2: Forward Pass ---
        # Output shape: [Batch, Seq_Len, Vocab_Size]
        logits = model(input_ids)
        
        # --- Step 3: Compute Loss ---
        # PyTorch CrossEntropy expects shapes [Batch * Seq_Len, Vocab_Size] and [Batch * Seq_Len]
        loss = criterion(
            logits.view(-1, vocab_size), 
            target_ids.view(-1)
        )
        
        # --- Step 4: Backward Pass (Backpropagation) ---
        loss.backward()
        
        # --- Step 5: Optimizer Step ---
        optimizer.step()
        
        # Update Learning Rate Scheduler
        scheduler.step()
        
        current_lr = scheduler.get_last_lr()[0]
        print(f"Epoch {epoch+1}/{epochs} | Loss: {loss.item():.4f} | LR: {current_lr:.6f}")

    print("\nTraining complete! (If this were real, you would now save the model checkpoint).")

if __name__ == "__main__":
    demonstrate_training_loop()
