# 17. Model Compression

After training, many models are too large, too slow, or too expensive to deploy directly.
Model compression is the set of techniques used to reduce size and inference cost while preserving as much quality as possible.

Compression is not only an optimization trick.
It is often what makes real deployment possible.

---

## 17.1 Why Compression Matters

Without compression, large models can be limited by:

- GPU memory
- inference latency
- server cost
- bandwidth for distribution
- device constraints on edge hardware

Compression helps move a model from research settings into practical use.

---

## 17.2 Quantization

Quantization is the most important compression method in modern LLM deployment.

### Core idea

Model weights are often stored in high precision such as FP32 or FP16.
Quantization stores them in fewer bits such as:

- 8-bit
- 4-bit
- sometimes lower in specialized settings

### Benefits

- smaller memory footprint
- faster inference
- lower deployment cost

### Tradeoff

If quantization is too aggressive or poorly calibrated, model quality can drop.

Modern methods try to preserve quality while pushing memory cost down.
Popular deployment ecosystems often revolve around formats and methods such as:

- GGUF
- AWQ
- GPTQ
- bitsandbytes-based loading flows

---

## 17.3 Pruning

Pruning removes weights, neurons, or structures that contribute little to the final prediction.

Types of pruning can include:

- unstructured pruning
- structured pruning
- head pruning
- channel pruning

### Why pruning is interesting

Neural networks are often overparameterized.
That means some parts of the network may be less important than others.

### Tradeoff

Pruning can reduce size, but practical speed gains depend on the runtime system.
A sparse theoretical model is not always faster unless the hardware and kernels exploit that sparsity well.

---

## 17.4 Knowledge Distillation

Distillation transfers behavior from a large teacher model into a smaller student model.

The teacher can provide:

- soft targets
- probability distributions
- synthetic examples
- reasoning traces in some workflows

The student then learns to imitate useful aspects of the teacher at much lower inference cost.

This is powerful because it can produce compact models that are much more capable than their size alone would suggest.

---

## 17.5 Low-Rank and Factorized Compression

Some compression methods approximate large matrices using smaller factorized structures.

The idea is similar in spirit to saying:

- this matrix does not need full complexity
- a lower-rank approximation may preserve most of the useful signal

This can reduce storage and sometimes computation, depending on implementation.

---

## 17.6 Compression in LLM Systems

In LLM deployment, compression is often combined with:

- KV-cache optimization
- efficient serving frameworks
- batching
- speculative decoding
- architecture-aware runtime kernels

So compression is one layer in a larger inference optimization stack.

---

## 17.7 What To Optimize For

Compression should be judged by tradeoffs, not by size reduction alone.

Important questions:

- How much quality is lost?
- How much memory is saved?
- How much speed is gained?
- Does the deployment hardware benefit from this method?
- Is the output still reliable for the target application?

The best compression method depends on the product constraints.

---

## 17.8 Practical Mental Model

Compression is the art of preserving the most useful intelligence while removing expensive redundancy.

In production AI, a slightly smaller model that runs cheaply and reliably is often more valuable than a larger model that is too slow or too expensive to use at scale.
