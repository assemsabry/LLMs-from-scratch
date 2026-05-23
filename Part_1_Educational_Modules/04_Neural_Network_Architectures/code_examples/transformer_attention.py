import torch
import torch.nn as nn
import torch.nn.functional as F
import math

def scaled_dot_product_attention(query, key, value, mask=None):
    """
    Computes Scaled Dot-Product Attention, the core math behind Transformers.
    Formula: Attention(Q, K, V) = softmax(Q * K^T / sqrt(d_k)) * V
    """
    # d_k is the dimension of the key vectors (used for scaling to prevent vanishing gradients in softmax)
    d_k = query.size(-1)
    
    # 1. Calculate Attention Scores (Q * K^T)
    # query shape: (batch, seq_len, d_k)
    # key.transpose shape: (batch, d_k, seq_len)
    # scores shape: (batch, seq_len, seq_len) -> An attention matrix showing how much each word attends to every other word
    scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
    
    # 2. Apply Mask (Optional, used in decoders so words can't look at future words)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9) # Fill with negative infinity so softmax becomes 0
        
    # 3. Apply Softmax to get Attention Weights (Probabilities that sum to 1)
    attention_weights = F.softmax(scores, dim=-1)
    
    # 4. Multiply Weights by Values
    # attention_weights shape: (batch, seq_len, seq_len)
    # value shape: (batch, seq_len, d_v)
    # output shape: (batch, seq_len, d_v)
    output = torch.matmul(attention_weights, value)
    
    return output, attention_weights

if __name__ == "__main__":
    print("--- Testing Scaled Dot-Product Attention ---")
    
    batch_size = 2
    sequence_length = 4 # e.g., a 4-word sentence
    embed_dim = 16      # Dimensions of Q, K, V vectors
    
    # Create dummy tensors representing Query, Key, and Value
    Q = torch.randn(batch_size, sequence_length, embed_dim)
    K = torch.randn(batch_size, sequence_length, embed_dim)
    V = torch.randn(batch_size, sequence_length, embed_dim)
    
    output, attn_weights = scaled_dot_product_attention(Q, K, V)
    
    print(f"Inputs (Q, K, V) shape: {Q.shape}")
    print(f"Output shape (Same as V): {output.shape}")
    print(f"Attention Weights Matrix shape: {attn_weights.shape}")
    print("\nAttention Matrix for the first sequence in the batch (Rows sum to 1):")
    print(attn_weights[0])
