# Optimization, Scaling, and Hardware

Training a 7 Billion parameter model on a single GPU would take several decades. To train models in a reasonable timeframe, we must scale the training loop across dozens, hundreds, or thousands of GPUs.

---

## 10.1 Scaling Techniques

You cannot simply plug 100 GPUs into a motherboard. You must use specialized algorithms to distribute the math across them over a network.

*   **Data Parallelism (DDP):** The simplest method. You copy the entire model onto every GPU. You then split your dataset. GPU A trains on Document 1, GPU B trains on Document 2. After one forward/backward pass, the GPUs sync their gradients over the network and update their weights simultaneously.
*   **Model Parallelism (Tensor Parallelism):** If your model is so large (e.g., 70B) that it cannot fit on a single GPU, you slice the model itself in half. GPU A computes the first half of the matrix multiplication, GPU B computes the second half, and they share the result.
*   **Gradient Accumulation:** If you only have 1 GPU and want to train with a massive Batch Size (which requires more memory than you have), you can trick the math. You do a forward/backward pass on a small batch, but *you do not update the optimizer*. You keep accumulating the gradients in memory over 10 tiny batches, and then do one massive optimizer step.

## 10.2 Mixed Precision Training

Historically, neural networks were trained using FP32 (32-bit floating-point numbers). This is highly precise but uses enormous amounts of VRAM.

*   **FP16 / BF16 (16-bit precision):** Modern LLM training uses Mixed Precision. The heavy matrix multiplications are done in 16-bit (cutting memory usage and compute time in half).
*   **BF16 (Bfloat16):** The current industry standard developed by Google. It sacrifices some fractional precision in exchange for a larger dynamic range, preventing the model from crashing due to gradient underflow/overflow (a common issue with standard FP16).

## 11.1 Hardware Requirements

To give you an idea of the physical hardware required to train models from scratch:

| Model Size | Typical Training GPUs Needed | Training Time Estimate |
| :--- | :--- | :--- |
| **100M** | 1x RTX 4090 / A100 | ~24 hours |
| **1B** | 4x A100 (80GB) | ~3 to 5 days |
| **7B** | 64x A100 (80GB) | ~2 to 4 weeks |
| **70B** | 1,024x H100 (80GB) | ~2 to 3 months |

## 12.1 Training Stability Tricks

When training across hundreds of GPUs, the math often becomes unstable, causing the loss curve to spike to infinity (a "divergence"). To prevent this:

1.  **Gradient Clipping:** If a gradient update is mathematically too large, you "clip" it to a maximum threshold. This prevents a single bad batch of data from destroying the model's weights.
2.  **Proper Initialization:** You must initialize the model's starting weights carefully (e.g., Xavier/Glorot initialization) rather than purely random numbers.
3.  **Learning Rate Warmup:** As mentioned in the previous section, starting the learning rate at 0 and ramping up slowly prevents early divergence.
