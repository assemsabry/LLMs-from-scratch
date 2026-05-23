# 15. Efficient Training (Scaling)

You cannot train a massive model on a single GPU. It physically will not fit.

---

## 15.1 Distributed Data Parallel (DDP)
*   **The Problem:** Training takes 10 years on one GPU.
*   **The Solution:** Copy the exact same model to 8 different GPUs. Split the dataset into 8 chunks. Each GPU trains on a different chunk of data, calculates gradients, and syncs them across all GPUs. Training now takes a fraction of the time.

## 15.2 Fully Sharded Data Parallel (FSDP / DeepSpeed)
*   **The Problem:** The model itself is 140GB, but a GPU only has 80GB of VRAM. It won't even fit to start training.
*   **The Solution:** Shard (slice) the model itself. GPU 1 holds Layer 1-10. GPU 2 holds Layer 11-20. The optimizer states and gradients are also sliced. This is the ZeRO optimization methodology.

## 15.3 Mixed Precision
*   Instead of doing math in 32-bit floats (FP32), deep learning can be done in 16-bit (FP16 or BF16). This instantly halves the memory required and doubles the training speed with negligible loss in accuracy.
