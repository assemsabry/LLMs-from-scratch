import torch
import torch.nn as nn

def demonstrate_lora():
    """
    Demonstrates the mathematical concept of LoRA (Low-Rank Adaptation) using PyTorch.
    Note: In production, you would use the 'peft' library from HuggingFace.
    """
    print("--- LoRA (Low-Rank Adaptation) Demonstration ---")
    
    # 1. Simulate a massive base model layer (e.g., inside a Transformer block)
    # Suppose this is a dense linear layer with 4096 input and 4096 output dimensions.
    # Total parameters: 4096 * 4096 = 16.7 million parameters (just for ONE layer!)
    d_model = 4096
    base_layer = nn.Linear(d_model, d_model, bias=False)
    
    # In LoRA, the base model is completely frozen to save memory
    for param in base_layer.parameters():
        param.requires_grad = False
    
    print(f"Base Layer Parameters: {sum(p.numel() for p in base_layer.parameters()):,}")
    
    # 2. Inject LoRA adapters
    # Instead of training a 4096x4096 matrix, we train two tiny matrices:
    # A (4096 x r) and B (r x 4096)
    # 'r' is the rank, typically a very small number like 8 or 16.
    rank = 8
    
    # Adapter A maps from d_model down to the tiny rank
    lora_A = nn.Linear(d_model, rank, bias=False)
    # Adapter B maps from the tiny rank back up to d_model
    lora_B = nn.Linear(rank, d_model, bias=False)
    
    # Initialize mathematically: A is random, B is all zeros.
    # This ensures that at step 0, the adapter does absolutely nothing to the base model.
    nn.init.normal_(lora_A.weight, std=0.02)
    nn.init.zeros_(lora_B.weight)
    
    lora_params = sum(p.numel() for p in lora_A.parameters()) + sum(p.numel() for p in lora_B.parameters())
    print(f"LoRA Adapter Parameters (r={rank}): {lora_params:,}")
    print(f"Reduction in trainable parameters: {(lora_params / (d_model * d_model)) * 100:.3f}%\n")
    
    # 3. The Forward Pass
    # Simulate a token embedding passing through the layer
    batch_size = 2
    seq_len = 10
    x = torch.randn(batch_size, seq_len, d_model)
    
    # Original Base Model output (frozen)
    base_output = base_layer(x)
    
    # LoRA output (trained)
    # The input goes through A, then B. We multiply by a scaling factor.
    alpha = 16 # Scaling factor hyperparameter
    scaling = alpha / rank
    lora_output = lora_B(lora_A(x)) * scaling
    
    # The final output is just the base math ADDED to the adapter math
    final_output = base_output + lora_output
    
    print(f"Input shape: {x.shape}")
    print(f"Final Output shape: {final_output.shape}")
    print("\nDuring training, ONLY lora_A and lora_B are updated by the optimizer.")
    print("This allows fine-tuning massive LLMs on consumer GPUs.")

if __name__ == "__main__":
    demonstrate_lora()
