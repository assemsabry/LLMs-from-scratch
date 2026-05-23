# Efficient Training: Mixed Precision and Gradients

Training Large Language Models requires massive amounts of GPU memory (VRAM). A 7B parameter model takes up roughly 14GB of VRAM just to store its weights in standard precision, and significantly more to store the optimizer states and gradients during training. 

To train these models on physical hardware, engineers use several critical optimization techniques.

---

## 1. Mixed Precision Training

Computers store numbers with varying levels of precision. By default, deep learning frameworks use 32-bit floating-point numbers (**FP32**). 

*   **The Problem with FP32:** It is highly accurate, but it takes up 4 bytes of memory per parameter. For billions of parameters, this is inefficient. It is also slower to compute.
*   **The Solution (FP16 / BF16):** We can cut the memory requirement in half by using 16-bit floating-point numbers. However, pure FP16 has a limited numerical range and can suffer from "underflow" (numbers becoming so small they round to zero) causing the training to collapse.
*   **Mixed Precision:** We keep a "master copy" of the weights in high-precision FP32 for the optimizer to update. But during the computationally heavy Forward and Backward passes, we temporarily cast the weights to FP16 or BF16 (Brain Floating Point, developed by Google).
*   **The Result:** Memory usage is nearly halved, and training speed is drastically increased because modern GPUs contain specialized hardware (Tensor Cores) optimized for 16-bit matrix multiplication.

## 2. Gradient Accumulation

Batch size is critical for stable training. But what if you want to train with a batch size of 1024, but your GPU can only fit a batch size of 32 before crashing with an "Out of Memory" (OOM) error?

*   **The Solution:** Gradient Accumulation allows you to simulate a massive batch size using a small GPU.
*   **How it works:**
    1.  Pass a micro-batch (e.g., 32) through the model.
    2.  Compute the Loss and perform the Backward pass to calculate gradients.
    3.  **Crucial Step:** Do *not* run the optimizer yet. Do *not* zero the gradients.
    4.  Pass the next micro-batch of 32 through the model. Add its gradients to the existing gradients.
    5.  Repeat this process 32 times.
    6.  Now, your accumulated gradients represent a total batch size of `32 x 32 = 1024`.
    7.  Finally, run `optimizer.step()` and then `optimizer.zero_grad()`.
*   **The Result:** You achieve the exact same mathematical update as if you had processed 1024 examples simultaneously, but you only ever needed enough VRAM to hold 32 examples at a time.

## 3. Gradient Clipping

The problem of "Exploding Gradients" occurs when the calculated gradients become astronomically large, causing the optimizer to take a massive step that throws the model weights completely out of balance, ruining the training run.

*   **The Solution:** Gradient Clipping.
*   **How it works:** Before passing the gradients to the optimizer, you set a maximum threshold (e.g., a norm of 1.0). If the gradients exceed this threshold, they are proportionally scaled down.
*   **The Result:** The model still moves in the correct direction to reduce the loss, but the magnitude of the step is capped, ensuring stable and safe training.
