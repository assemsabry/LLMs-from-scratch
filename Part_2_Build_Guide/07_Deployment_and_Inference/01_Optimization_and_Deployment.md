# Deployment, Inference, and Optimization

After pretraining, SFT, and Alignment, your model is ready. However, running a 7B or 70B parameter model in production is a massive engineering challenge. 

If you load a PyTorch model dynamically and run a loop to generate tokens one by one, your users will wait 30 seconds to get a response. You must optimize the model for *Inference*.

---

## 15.1 Post-Training Quantization (PTQ)

The most effective way to deploy a model is to shrink it.
*   **The Problem:** A 7B model in FP16 (16-bit) requires about 14GB of VRAM just to load the weights. This means you cannot run it on a cheap GPU or a standard Macbook.
*   **The Solution (Quantization):** You mathematically compress the weights from 16-bit down to 8-bit, 4-bit, or even 2-bit integers.
    *   **4-bit Quantization:** Shrinks a 7B model from 14GB to just ~4GB. Now it can run on a laptop.
    *   **Techniques:** GGUF (llama.cpp) and AWQ (Activation-aware Weight Quantization) are the industry standards. They ensure that even though you compress the numbers, the mathematical output of the model barely degrades.

## 15.2 Inference Engines

Do not use standard PyTorch in production. You must use a dedicated Inference Engine written in C++ or Rust that highly optimizes the matrix math and GPU memory.

1.  **vLLM:** The industry standard for serving models in the cloud. It uses a technique called **PagedAttention** (borrowing concepts from Operating System memory paging) to drastically reduce memory fragmentation. This allows you to serve 5x more concurrent users on the same GPU.
2.  **llama.cpp:** The industry standard for running models locally on CPU, Macbook (Apple Silicon), or small consumer GPUs. It natively supports GGUF 4-bit quantization.

## 15.3 The Generation Algorithm (Decoding)

When a user sends a prompt, the model outputs probabilities for the *next token*. How do you pick the token?

*   **Greedy Decoding:** Always pick the token with the highest probability (e.g., 99%). This is fast and deterministic, but makes the model sound robotic and repetitive.
*   **Temperature Scaling:** You apply a mathematical formula to the probabilities. 
    *   `Temperature = 0`: Same as greedy decoding.
    *   `Temperature = 1.0`: Standard.
    *   `Temperature > 1`: Flattens the probabilities, making the model take "risks" and pick less likely words, increasing creativity.
*   **Top-K and Top-P (Nucleus Sampling):** Instead of picking from the entire 32,000 word vocabulary (which could result in picking garbage if you take a risk), you force the model to only pick from the Top 50 words (Top-K), or from the top words whose probabilities sum up to 90% (Top-P).
