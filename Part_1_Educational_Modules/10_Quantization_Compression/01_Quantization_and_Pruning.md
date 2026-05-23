# 1. Quantization and Pruning

Deep learning models are historically trained in 32-bit floating-point (FP32) precision. A 7-billion parameter model in FP32 requires 28 GB of VRAM just to load. To deploy these models efficiently on consumer hardware, we must compress them.

---

## 1.1 Quantization

Quantization is the process of mapping high-precision numbers to lower-precision numbers. It trades a tiny amount of mathematical accuracy for massive gains in memory reduction and inference speed.

### Precision Levels
*   **FP16 / BF16 (16-bit):** The modern standard for training. Reduces model size by 50% with almost zero degradation in performance.
*   **INT8 (8-bit):** Converts the floating-point weights into 8-bit integers. Shrinks the model by 75%.
*   **INT4 (4-bit):** The bleeding edge of LLM deployment. Shrinks a model by nearly 87.5%.

### Post-Training Quantization (PTQ)
The model is fully trained in 16-bit, and then mathematically compressed to 8-bit or 4-bit after training is complete.
*   **GGUF:** The most popular format for running quantized LLMs on CPU/Apple Silicon (using `llama.cpp`).
*   **AWQ / GPTQ:** Highly optimized quantization formats specifically designed for running fast inference on NVIDIA GPUs.

### Quantization-Aware Training (QAT)
If PTQ causes too much degradation (the model gets "stupider"), QAT is used. During the actual training process, the model simulates the lower precision. This allows the model to adjust its weights to account for the rounding errors before the training finishes.

## 1.2 Pruning

If Quantization reduces the *size* of the numbers, Pruning reduces the *amount* of numbers.

### The Mechanism
Pruning involves identifying weights (connections between neurons) that contribute very little to the model's output, and permanently deleting them (setting them to exactly 0).
*   **Magnitude Pruning:** The simplest method. Find all weights closest to 0.0 and delete them.
*   **Structured Pruning:** Instead of deleting random individual weights, this deletes entire rows, columns, or attention heads. This is required to actually see speedups on modern GPUs, as GPUs struggle to process unstructured, randomly missing data.

### The Result
A pruned network becomes "sparse". A network with 50% sparsity has had half of its connections removed. While extremely popular in computer vision, pruning is notoriously difficult to apply to LLMs without causing severe brain damage to the model.
