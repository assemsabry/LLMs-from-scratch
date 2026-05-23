# 1. Inference Optimization

Training a model is expensive, but it only happens once. Inference (generating text for users) happens billions of times. Optimizing inference is critical to making AI economically viable.

---

## 1.1 The Bottleneck: Memory Bandwidth

During generation, an LLM predicts one word at a time (Autoregressive generation). For every single new word, the GPU must load the *entire* massive model weight matrix from the GPU's memory (VRAM) into its compute cores, multiply it, and write the result back. 

The math itself is fast, but waiting for the massive weights to travel across the GPU memory bus is incredibly slow. LLM inference is "Memory Bandwidth Bound," not "Compute Bound."

## 1.2 The KV Cache

To generate the next word, the Transformer needs to look at the Attention states (Keys and Values) of *every previous word* in the sentence.
*   **Without caching:** For every new word, the model recalculates the Keys and Values for the entire preceding paragraph. This wastes massive amounts of compute.
*   **With KV Cache:** The model calculates the Keys and Values for a word once, and stores them in GPU memory (the KV Cache). For the next word, it just looks up the past states from memory.
*   **The tradeoff:** The KV cache consumes enormous amounts of VRAM. A large context window with many concurrent users can consume more VRAM than the model weights themselves.

## 1.3 Flash Attention

Standard Self-Attention requires creating an $N \times N$ matrix (where $N$ is the sequence length). If you have a 100,000-token context window, this matrix requires hundreds of gigabytes of VRAM to store temporarily, crashing the GPU.

**Flash Attention** is a revolutionary algorithm that restructures the math. By intelligently breaking the matrix into blocks and utilizing the ultra-fast, tiny SRAM located directly on the GPU compute cores, it calculates exact attention without ever writing the massive $N \times N$ matrix to the main VRAM. 
*   It significantly speeds up processing.
*   It slashes memory usage, making massive context windows (like Claude's 200K) physically possible.
