# Efficient Training: Parallelism

When a model grows beyond 1-2 Billion parameters, it physically cannot fit inside the memory of a single GPU, even with mixed precision. Training a modern LLM (like a 70B or 175B model) requires networking hundreds or thousands of GPUs together.

To divide the computational labor across these GPUs, engineers use three primary forms of Parallelism.

---

## 1. Data Parallelism (DDP/FSDP)

This is the most common and simple form of parallelism.
*   **The Concept:** The model is entirely duplicated across every single GPU. If you have 8 GPUs, you have 8 complete copies of the model.
*   **How it works:** 
    1.  The massive dataset is split into 8 different chunks.
    2.  GPU 1 processes a batch from Chunk 1, while GPU 2 processes a batch from Chunk 2, etc.
    3.  Each GPU calculates its own gradients based on the data it saw.
    4.  **The Bottleneck:** Before the optimizer can step, all 8 GPUs must communicate over the network to average their gradients together. This ensures all 8 copies of the model update exactly the same way and remain synchronized.
*   **When to use it:** When the model is small enough to fit comfortably on a single GPU, but you want to train it on a massive dataset much faster.
*   **Modern Upgrade (FSDP):** Fully Sharded Data Parallelism (FSDP) or DeepSpeed ZeRO. Instead of duplicating the entire model, it shards (slices) the model's weights and optimizer states across the GPUs, only gathering the specific layers it needs at the exact moment of computation. This drastically reduces memory overhead, allowing much larger models to be trained using Data Parallelism techniques.

## 2. Tensor Parallelism (Model Parallelism)

What happens when a single layer of a model is so massive that the matrix multiplication physically cannot happen on one GPU?
*   **The Concept:** You split the actual matrices (the tensors) across multiple GPUs.
*   **How it works:** Imagine a massive matrix multiplication: `A * B = C`. 
    1.  We split Matrix `B` down the middle into `B1` and `B2`.
    2.  GPU 1 computes `A * B1 = C1`.
    3.  GPU 2 computes `A * B2 = C2`.
    4.  The GPUs communicate instantly to stitch `C1` and `C2` together to form the final result `C`.
*   **The Bottleneck:** This requires intense, constant, ultra-high-speed communication between the GPUs. Because of this, Tensor Parallelism is almost exclusively used *within* a single physical server node (e.g., 8 GPUs connected via NVLink), rather than across standard network cables.

## 3. Pipeline Parallelism

What happens when a model is so deep (e.g., 96 layers) that it won't fit on one GPU?
*   **The Concept:** You slice the model horizontally. GPU 1 handles the first 24 layers, GPU 2 handles the next 24 layers, etc.
*   **How it works:** 
    1.  GPU 1 computes the forward pass for layers 1-24. 
    2.  GPU 1 sends the resulting activations over the network to GPU 2.
    3.  GPU 2 computes layers 25-48, and so on.
*   **The Problem (The Bubble):** While GPU 1 is processing, GPUs 2, 3, and 4 are sitting completely idle waiting for data. This wasted time is called the "Pipeline Bubble."
*   **The Solution:** Micro-batching. We split the batch into tiny pieces. GPU 1 processes micro-batch A and sends it to GPU 2. While GPU 2 is working on micro-batch A, GPU 1 immediately starts working on micro-batch B. This keeps all GPUs busy and shrinks the bubble.

## Summary: 3D Parallelism

To train a state-of-the-art model like GPT-4 or LLaMA-3, engineers do not pick just one of these techniques. They use **3D Parallelism**, combining all three simultaneously:
1.  They split the layers across GPUs (Pipeline Parallelism).
2.  Within those layers, they split the math across GPUs (Tensor Parallelism).
3.  They take that entire massive distributed setup, clone it, and feed different data to each clone (Data Parallelism).
