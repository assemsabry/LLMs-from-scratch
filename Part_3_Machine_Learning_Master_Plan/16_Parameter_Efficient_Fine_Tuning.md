# 16. Parameter-Efficient Fine-Tuning (PEFT)

Full fine-tuning of an LLM requires updating billions of parameters, demanding massive, expensive server clusters. PEFT solves this.

---

## 16.1 LoRA (Low-Rank Adaptation)
The absolute standard for modern fine-tuning.
*   **The Concept:** Instead of updating the massive original weight matrices of the LLM, we freeze the original model completely. We then inject two tiny, low-rank matrices into the network.
*   **The Math:** We train *only* these tiny matrices (e.g., millions of parameters instead of billions). During inference, the tiny matrices are mathematically multiplied and added back into the frozen weights.
*   **The Result:** You can fine-tune a 7B parameter LLM on a single consumer GPU in a few hours.

## 16.2 QLoRA (Quantized LoRA)
An extension of LoRA.
*   The base model is mathematically compressed (Quantized) down to 4-bit precision to save even more memory. 
*   The tiny LoRA adapters are trained in normal 16-bit precision.
*   This allows massive 70B parameter models to be fine-tuned on relatively standard hardware.

## 16.3 Adapters & Prefix Tuning
*   **Adapters:** Small feed-forward layers inserted directly between transformer blocks.
*   **Prefix Tuning:** Appending a sequence of continuous task-specific vectors (virtual tokens) to the input sequence that can be trained while the model stays frozen.
