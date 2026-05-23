# 1. LoRA and QLoRA

Large Language Models (LLMs) have billions of parameters. Fine-tuning all of them (Full Fine-Tuning) requires massive, expensive GPU clusters. Parameter-Efficient Fine-Tuning (PEFT) techniques solve this problem by freezing the original model and only training a tiny fraction of new parameters.

---

## 1.1 LoRA (Low-Rank Adaptation)

LoRA is the most popular PEFT technique. Instead of changing the original massive weight matrices, LoRA injects two much smaller matrices into the model.

### The Mechanism
1.  **Freeze the Base Model:** The billions of weights in the pre-trained LLM are locked. No gradients are calculated for them, saving enormous memory.
2.  **Inject Rank Matrices:** For a specific dense layer (like in the self-attention mechanism), LoRA adds two small matrices, $A$ and $B$.
    *   If the original layer has dimensions $d \times d$ (e.g., $4096 \times 4096$), updating it requires $16.7$ million parameters.
    *   LoRA introduces a "Rank" ($r$), usually a small number like 8 or 16. Matrix $A$ is $d \times r$ and Matrix $B$ is $r \times d$.
    *   The total trainable parameters become $(4096 \times 8) + (8 \times 4096) = 65,536$. This is a **99.6% reduction** in trainable parameters.
3.  **Forward Pass:** The input is passed through both the frozen weights and the LoRA matrices. The results are added together.

### The Advantage
*   Drastically reduces GPU memory requirements.
*   Training is much faster.
*   You can train multiple different LoRA "adapters" for different tasks (e.g., one for coding, one for medical data) and swap them in and out of the same frozen base model instantly.

## 1.2 QLoRA (Quantized LoRA)

QLoRA pushes the efficiency of LoRA to the absolute extreme, allowing a 65-Billion parameter model to be fine-tuned on a single 48GB GPU.

### The Mechanism
QLoRA introduces several memory-saving innovations:
1.  **4-bit NormalFloat (NF4) Quantization:** The frozen base model is mathematically compressed from 16-bit down to a highly optimized 4-bit format. This shrinks the model's physical size in VRAM by 75%.
2.  **Double Quantization:** It even quantizes the quantization constants to save a tiny bit more memory.
3.  **Paged Optimizers:** It uses NVIDIA Unified Memory to automatically page optimizer states to CPU RAM if the GPU runs out of memory, preventing crashes.

### How it trains
While the base model is frozen in 4-bit, the small LoRA matrices ($A$ and $B$) are trained in standard 16-bit (BF16 or FP16). During the forward and backward passes, the 4-bit weights are temporarily decompressed back to 16-bit for the math, but the permanent storage remains in 4-bit.
