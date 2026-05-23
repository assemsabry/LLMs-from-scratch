# 2. Serving Frameworks and Advanced Decoding

Once optimizations are mathematically applied, they need to be implemented via software frameworks.

---

## 2.1 Speculative Decoding

Standard generation produces 1 token per forward pass. Speculative Decoding is a clever trick to generate multiple tokens per pass.

1.  You run a tiny, ultra-fast "Draft Model" to quickly guess the next 4 tokens (e.g., "The capital of France is [Paris]").
2.  You pass this guess to the massive, slow "Target Model".
3.  The Target Model processes all 4 tokens in a *single* forward pass to verify if the Draft Model was right.
4.  If the Draft Model was correct, you just generated 4 tokens in the time it usually takes to generate 1.

## 2.2 Serving Engines

To host an LLM efficiently, you do not write raw PyTorch code. You use highly optimized serving engines written in C++ and CUDA.

### vLLM
The current industry standard for open-source LLM serving.
*   **PagedAttention:** Its defining feature. Just like an operating system manages RAM in "pages" to prevent memory fragmentation, vLLM manages the KV Cache in blocks. This prevents VRAM waste and allows vLLM to serve significantly more concurrent users than standard frameworks.

### TGI (Text Generation Inference)
Developed by Hugging Face, TGI is a powerful, production-ready framework that supports tensor parallelism, continuous batching, and Flash Attention out of the box.

### TensorRT-LLM
NVIDIA's proprietary framework. It provides the absolute maximum possible performance and throughput on NVIDIA hardware, but requires compiling models into a specific engine format before they can be run.
