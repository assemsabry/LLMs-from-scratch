# 2. Serving Frameworks and Advanced Decoding

Once optimizations are mathematically applied, they need to be implemented via software frameworks.

---

## 2.1 Speculative Decoding

Standard generation produces 1 token per forward pass. Speculative Decoding is a clever trick to generate multiple tokens per pass.

1.  You run a tiny, ultra-fast "Draft Model" to quickly guess the next 4 tokens (e.g., "The capital of France is [Paris]").
2.  You pass this guess to the massive, slow "Target Model".
3.  The Target Model processes all 4 tokens in a *single* forward pass to verify if the Draft Model was right.
4.  If the Draft Model was correct, you just generated 4 tokens in the time it usually takes to generate 1.

### Why speculative decoding matters

Autoregressive generation is inherently sequential, which makes it slow.

Speculative decoding is valuable because it tries to recover some parallelism during inference without changing the final model itself.

### The tradeoff

Speculative decoding works best when:

- the draft model is cheap
- the draft model is often correct
- verification is efficient

If the draft model guesses badly too often, the benefit shrinks.

## 2.2 Serving Engines

To host an LLM efficiently, you do not write raw PyTorch code. You use highly optimized serving engines written in C++ and CUDA.

### vLLM
The current industry standard for open-source LLM serving.
*   **PagedAttention:** Its defining feature. Just like an operating system manages RAM in "pages" to prevent memory fragmentation, vLLM manages the KV Cache in blocks. This prevents VRAM waste and allows vLLM to serve significantly more concurrent users than standard frameworks.

### Why vLLM became so important

vLLM matters because modern serving is not only about making one request fast.
It is also about serving many users efficiently at the same time.

That makes memory management and batching first-class engineering concerns.

### TGI (Text Generation Inference)
Developed by Hugging Face, TGI is a powerful, production-ready framework that supports tensor parallelism, continuous batching, and Flash Attention out of the box.

### TensorRT-LLM
NVIDIA's proprietary framework. It provides the absolute maximum possible performance and throughput on NVIDIA hardware, but requires compiling models into a specific engine format before they can be run.

## 2.3 How to Choose a Serving Stack

The right serving framework depends on the use case.

- **vLLM:** strong general default for open-source cloud serving
- **TGI:** strong production option with Hugging Face ecosystem alignment
- **TensorRT-LLM:** best when maximizing performance on NVIDIA infrastructure
- **llama.cpp:** best for local and lightweight deployment

## 2.4 What Learners Should Understand

Do not reduce serving frameworks to a list of names.

Each framework reflects deeper engineering tradeoffs around:

- memory layout
- batching strategy
- hardware coupling
- deployment complexity
- performance targets

Understanding those tradeoffs is more important than memorizing branding.
