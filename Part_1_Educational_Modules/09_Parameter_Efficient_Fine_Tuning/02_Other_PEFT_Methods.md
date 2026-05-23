# 2. Other PEFT Methods

While LoRA is the dominant standard, several other Parameter-Efficient Fine-Tuning techniques exist.

---

## 2.1 Prefix Tuning

Prefix Tuning focuses on the input sequences rather than the internal weight matrices.

### The Mechanism
*   Instead of modifying the model's weights, Prefix Tuning prepends a set of continuous, trainable "virtual tokens" (the prefix) to the input sequence at every layer of the transformer.
*   The base model remains completely frozen. Only the prefix vectors are trained.
*   **Intuition:** It is similar to Prompt Engineering, but instead of forcing you to find the perfect human words for a prompt, the model uses backpropagation to discover the mathematically perfect "virtual prompt" for the specific task.

### Advantages vs Disadvantages
*   **Advantage:** Requires even fewer trainable parameters than LoRA.
*   **Disadvantage:** The prefix takes up space in the model's Context Window, leaving less room for the actual user input.

## 2.2 Prompt Tuning

Prompt Tuning is a simplified, lighter version of Prefix Tuning.
*   **Difference from Prefix Tuning:** While Prefix Tuning adds virtual tokens to *every* layer of the transformer, Prompt Tuning only prepends virtual tokens to the very first input embedding layer.
*   It is slightly less powerful than Prefix Tuning but even more parameter-efficient. It performs best on very massive models (100B+ parameters).

## 2.3 Adapters (Standard)

Adapters were one of the first PEFT methods, introduced before LoRA.

### The Mechanism
*   Small, fully connected feed-forward networks (the "adapters") are physically inserted *between* the existing layers of the frozen transformer.
*   Typically, an adapter consists of a down-projection layer (compressing the data), a non-linear activation (like ReLU), and an up-projection layer (expanding the data back to its original size).

### Disadvantages
*   **Inference Latency:** Because adapters physically add new layers that the data must sequentially pass through, they slow down the model during inference. LoRA avoids this because LoRA matrices can be mathematically merged into the base weights after training, resulting in zero inference latency.
