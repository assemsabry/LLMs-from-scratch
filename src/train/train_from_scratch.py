import os
import torch
from torch.utils.data import DataLoader
from datasets import load_from_disk
import sys

# Import our NanoLLM model
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model.nano_llm import NanoLLM, NanoLLMConfig

def train():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {device}")
    
    # 1. Load the processed dataset
    data_dir = "./data/processed"
    if not os.path.exists(data_dir):
        print(f"Error: Dataset not found at {data_dir}. Run src/data/prepare_dataset.py first.")
        return
        
    print("Loading dataset...")
    dataset = load_from_disk(data_dir)
    
    # Simple PyTorch DataLoader
    # We use a small batch size for demonstration
    batch_size = 8
    
    def collate_fn(batch):
        # Stack inputs into tensors
        input_ids = torch.stack([item['input_ids'] for item in batch])
        # Shift inputs for targets (predict next token)
        x = input_ids[:, :-1].contiguous()
        y = input_ids[:, 1:].contiguous()
        return x, y
        
    dataloader = DataLoader(dataset['train'], batch_size=batch_size, shuffle=True, collate_fn=collate_fn)
    
    # 2. Initialize the Model
    config = NanoLLMConfig()
    model = NanoLLM(config).to(device)
    print(f"Model initialized with {sum(p.numel() for p in model.parameters())/1e6:.2f} M parameters")
    
    # 3. Setup Optimizer
    learning_rate = 5e-4
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)
    
    # 4. Training Loop
    epochs = 1
    max_steps = 1000 # Just train for a few steps for demonstration
    
    model.train()
    step = 0
    
    print("Starting training loop...")
    for epoch in range(epochs):
        for batch_idx, (x, y) in enumerate(dataloader):
            x, y = x.to(device), y.to(device)
            
            # Forward pass
            logits, loss = model(x, targets=y)
            
            # Backward pass
            optimizer.zero_grad(set_to_none=True)
            loss.backward()
            
            # Gradient clipping to prevent exploding gradients
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            
            optimizer.step()
            
            if step % 50 == 0:
                print(f"Epoch {epoch} | Step {step} | Loss: {loss.item():.4f}")
                
            step += 1
            if step >= max_steps:
                break
                
    # 5. Save Model Checkpoint
    os.makedirs("./checkpoints", exist_ok=True)
    checkpoint_path = "./checkpoints/nano_llm_final.pt"
    
    checkpoint = {
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'config': config
    }
    
    torch.save(checkpoint, checkpoint_path)
    print(f"Training complete. Model saved to {checkpoint_path}")

if __name__ == "__main__":
    train()
