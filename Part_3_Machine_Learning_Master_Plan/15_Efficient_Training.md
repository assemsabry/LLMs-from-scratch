# 15. Efficient Training (Scaling)

Once models become large, training is no longer only a machine learning problem.
It becomes a systems problem involving memory, communication, throughput, and numerical stability.

This is especially true for large language models.

---

## 15.1 Why Single-GPU Training Stops Working

As model size and dataset size grow, a single GPU eventually becomes insufficient because of:

- limited VRAM
- limited compute throughput
- slow wall-clock training time
- optimizer state overhead

So scaling requires distributing the workload intelligently.

---

## 15.2 Distributed Data Parallel (DDP)

Distributed Data Parallel is one of the most common scaling approaches.

### Core idea

- copy the same model across multiple GPUs
- split batches across those GPUs
- let each GPU compute gradients on its shard
- synchronize gradients before the optimizer step

### Benefit

This reduces training time by increasing parallel throughput.

### Limitation

DDP helps when the model fits on each GPU.
If the model itself is too large for a single device, DDP alone is not enough.

---

## 15.3 Sharding and ZeRO-Style Methods

When the full model cannot fit on one GPU, you need more advanced memory-saving strategies.

Approaches such as FSDP and ZeRO-style systems shard parts of training state across devices.

This can include sharding:

- model parameters
- gradients
- optimizer states

### Why this matters

A large fraction of training memory is not just the raw model weights.
You also pay for gradients and optimizer buffers.

Sharding distributes those costs across hardware.

---

## 15.4 Mixed Precision

Mixed precision training uses lower-precision arithmetic such as FP16 or BF16 in selected parts of the training process.

Benefits:

- lower memory usage
- higher throughput
- better hardware utilization

This is one of the most important practical techniques in modern training pipelines.

It speeds up training substantially while usually preserving model quality when implemented correctly.

---

## 15.5 Gradient Accumulation

Sometimes the ideal batch size does not fit in memory.
Gradient accumulation solves this by processing multiple smaller microbatches and accumulating their gradients before taking an optimizer step.

This allows you to simulate a larger effective batch size without needing all samples in memory at once.

---

## 15.6 Communication Overhead

Distributed training is not free.
As you add more devices, communication can become a bottleneck.

Important factors include:

- network bandwidth
- interconnect speed
- synchronization frequency
- cluster topology

This is why scaling is not just about adding more GPUs.
It is about adding them in a way that still produces useful efficiency.

---

## 15.7 Checkpointing and Recovery

Large training runs are expensive and fragile.
Efficient training systems must also support:

- checkpoint saving
- fault recovery
- resumable training
- experiment tracking

At scale, operational reliability becomes part of training efficiency.
Losing a long run due to poor checkpoint strategy is an efficiency failure.

---

## 15.8 Why Efficient Training Is Interdisciplinary

Efficient training sits at the intersection of:

- deep learning
- GPU programming
- distributed systems
- numerical computing

This is why strong LLM engineers often need both model intuition and systems intuition.

---

## 15.9 Practical Mental Model

At small scale, training is mainly about the model.
At large scale, training is about the model plus the machine that carries it.

The best scaling strategies are the ones that preserve learning quality while minimizing wasted memory, wasted communication, and wasted time.
