import torch
import torch.nn as nn

class TransformerBlock(nn.Module):
    """
    A single Decoder-Only Transformer Block.
    Modern LLMs stack many of these on top of each other.
    """
    def __init__(self, d_model: int, n_heads: int):
        super().__init__()
        
        # 1. Multi-Head Self Attention
        # PyTorch provides an optimized implementation of the Attention formula
        self.attn = nn.MultiheadAttention(
            embed_dim=d_model, 
            num_heads=n_heads, 
            batch_first=True
        )
        
        # 2. Feedforward Network (MLP)
        # Typically expands the hidden dimension by 4x, applies an activation, and projects back
        self.ff = nn.Sequential(
            nn.Linear(d_model, d_model * 4),
            nn.GELU(), # Gaussian Error Linear Unit (modern replacement for ReLU)
            nn.Linear(d_model * 4, d_model)
        )
        
        # 3. Layer Normalization
        # Applied before Attention and before the Feedforward network (Pre-Norm architecture)
        self.ln1 = nn.LayerNorm(d_model)
        self.ln2 = nn.LayerNorm(d_model)

    def forward(self, x: torch.Tensor, attn_mask: torch.Tensor = None) -> torch.Tensor:
        """
        The mathematical forward pass of the block.
        x shape: (batch_size, sequence_length, d_model)
        """
        # --- Stage 1: Attention ---
        # Normalize input
        norm_x = self.ln1(x)
        
        # In self-attention, the Query, Key, and Value are all derived from the same input (norm_x)
        attn_out, _ = self.attn(
            query=norm_x, 
            key=norm_x, 
            value=norm_x, 
            attn_mask=attn_mask,
            need_weights=False
        )
        
        # Residual Connection 1
        x = x + attn_out
        
        # --- Stage 2: Feedforward ---
        # Normalize intermediate state
        norm_x2 = self.ln2(x)
        
        # Apply FFN
        ff_out = self.ff(norm_x2)
        
        # Residual Connection 2
        x = x + ff_out
        
        return x

def demonstrate_model():
    print("--- PyTorch Transformer Block Initialization ---")
    
    # Define Hyperparameters for a tiny model
    d_model = 768  # Hidden size (Embedding dimension)
    n_heads = 12   # Number of attention heads
    batch_size = 2
    seq_length = 512
    
    print(f"\nInitializing block with d_model={d_model}, n_heads={n_heads}...")
    block = TransformerBlock(d_model=d_model, n_heads=n_heads)
    
    # Create a dummy tensor representing a batch of embedded tokens
    # Shape: [Batch, Seq_Len, Hidden_Size]
    dummy_input = torch.randn(batch_size, seq_length, d_model)
    print(f"Input shape: {dummy_input.shape} [Batch, Seq_Len, Hidden_Size]")
    
    # Pass data through the block
    output = block(dummy_input)
    print(f"Output shape: {output.shape} (Shape remains identical due to residual connections)")
    
    print("\nIn a full LLM, this block is repeated N times (e.g., 32 layers).")

if __name__ == "__main__":
    demonstrate_model()
