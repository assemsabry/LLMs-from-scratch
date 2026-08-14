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

### Why quantization matters beyond cost

Quantization does not only reduce hardware cost.
It also affects:

- startup time
- memory bandwidth pressure
- portability
- local deployment feasibility
- edge and on-device use cases

This is one reason smaller local AI workflows became much more important in 2026.

## 15.2 Inference Engines

Do not use standard PyTorch in production. You must use a dedicated Inference Engine written in C++ or Rust that highly optimizes the matrix math and GPU memory.

1.  **vLLM:** The industry standard for serving models in the cloud. It uses a technique called **PagedAttention** (borrowing concepts from Operating System memory paging) to drastically reduce memory fragmentation. This allows you to serve 5x more concurrent users on the same GPU.
2.  **llama.cpp:** The industry standard for running models locally on CPU, Macbook (Apple Silicon), or small consumer GPUs. It natively supports GGUF 4-bit quantization.

### Why inference is now a full discipline

Many beginners think model quality is the hard part and serving is easy.
That is false.

In real products, inference engineering often decides:

- latency
- throughput
- concurrency
- hardware cost
- user experience

The difference between a good model and a good product is often deployment quality.

## 15.3 The Generation Algorithm (Decoding)

When a user sends a prompt, the model outputs probabilities for the *next token*. How do you pick the token?

*   **Greedy Decoding:** Always pick the token with the highest probability (e.g., 99%). This is fast and deterministic, but makes the model sound robotic and repetitive.
*   **Temperature Scaling:** You apply a mathematical formula to the probabilities. 
    *   `Temperature = 0`: Same as greedy decoding.
    *   `Temperature = 1.0`: Standard.
    *   `Temperature > 1`: Flattens the probabilities, making the model take "risks" and pick less likely words, increasing creativity.
*   **Top-K and Top-P (Nucleus Sampling):** Instead of picking from the entire 32,000 word vocabulary (which could result in picking garbage if you take a risk), you force the model to only pick from the Top 50 words (Top-K), or from the top words whose probabilities sum up to 90% (Top-P).

### Practical decoding intuition

You should choose decoding settings based on the job:

- **low temperature:** factual answers, extraction, code, structured output
- **medium temperature:** normal assistant tasks
- **higher temperature:** brainstorming, creative writing, ideation

Good deployment is not only about the model weights.
It is also about choosing sensible decoding defaults for each task.

## 15.4 KV Cache and Why Inference Gets Faster After the First Token

Decoder-only LLMs generate one token at a time.
Naively, that sounds very slow.

The reason inference is still practical is the **KV Cache**.

### The idea

At each transformer layer, the model computes Keys and Values for previous tokens.
Instead of recomputing them from scratch every step, the system stores them in memory.

Then, when generating the next token:

- the model reuses previous Keys and Values
- only the new token needs fresh attention work

### Why this matters

KV cache is one of the most important deployment concepts in modern LLM serving because it directly affects:

- latency
- memory consumption
- long conversation cost
- concurrency limits

This is also why serving long-context conversations can become memory-heavy even after quantization.

## 15.5 Continuous Batching and Modern Serving

Modern inference engines do not simply handle one user request at a time.
They try to pack many requests together efficiently.

### Why this matters

If 100 users ask for completions at the same time, naive serving wastes GPU capacity.

Modern systems use ideas like:

- continuous batching
- request scheduling
- cache reuse
- token-level interleaving

This is a major reason engines like vLLM became so important.

## 15.6 Local Deployment vs Cloud Deployment

In 2026, this became a very important design choice.

### Local deployment advantages

- privacy
- low recurring cost
- offline availability
- easier experimentation

### Cloud deployment advantages

- higher scale
- stronger hardware
- easier centralized updates
- access to larger models

### Good modern strategy

Many practical systems now combine both:

- a local or smaller model for fast, private, cheap tasks
- a stronger hosted model for harder reasoning or larger workloads

## 15.7 What a Production-Ready Deployment Stack Usually Needs

A real deployment stack often includes much more than "run model and return text."

Typical production components include:

1. model loading
2. tokenizer service
3. batching scheduler
4. KV cache management
5. safety filtering
6. logging and observability
7. rate limiting
8. fallback strategies
9. health checks
10. autoscaling

This is why deployment is a systems problem, not just an ML problem.

## 15.8 What Learners Should Build Next

If you want to truly understand LLM deployment, build these in order:

1. a local inference demo
2. a quantized model test
3. a small API server
4. a comparison between decoding settings
5. a latency benchmark with and without batching

That progression teaches the real difference between:

- training a model
- shipping a model
