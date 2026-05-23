# Model Architecture

Modern LLMs (like GPT, LLaMA, and Mistral) are all variants of the **Decoder-Only Transformer** architecture. 

Once your text is tokenized into integer IDs, the neural network takes over. Here is the mathematical journey a token takes through the model.

---

## 5.1 The Core Components

An LLM consists of three main stages:
1.  **Embedding Layer:** Converts the integer token ID into a dense vector (e.g., a list of 4096 floating-point numbers). This vector represents the "meaning" of the token.
2.  **Positional Encoding:** Because Transformers process all tokens simultaneously, they have no concept of word order. We mathematically add a "position vector" to the embedding so the model knows which word came first.
3.  **Transformer Blocks (The Core):** A series of identical layers (e.g., 32 layers stacked on top of each other). The output of Block 1 feeds into Block 2, and so on.

## 5.2 The Transformer Block

Each individual block in the stack does the heavy lifting. It consists of:

*   **Layer Normalization:** Stabilizes the neural network by keeping the numerical values of the vectors from growing too large.
*   **Multi-Head Self-Attention:** The most critical part. This allows tokens to "look" at other tokens in the sequence to gather context. (e.g., the word "bank" looks at the word "river" to realize it means a riverbank, not a financial institution).
*   **Feedforward Network (FFN):** A standard Multi-Layer Perceptron (MLP) applied to each token independently. If Attention is how tokens talk to each other, the FFN is how the model recalls facts memorized during training.
*   **Residual Connections:** Instead of just passing the output of the Attention layer to the next step, we mathematically ADD the original input back to the output (`x = x + attention(x)`). This prevents the "vanishing gradient" problem in deep networks.

## 5.3 The Attention Formula

The mathematical heart of the model is the Scaled Dot-Product Attention formula:

`Attention(Q, K, V) = softmax( (Q * K^T) / sqrt(d_k) ) * V`

*   **Q (Query):** What the current token is looking for.
*   **K (Key):** What other tokens contain.
*   **V (Value):** The actual information the other tokens hold.
*   *Analogy:* Q is your search query in a library, K is the title on the spine of the book, V is the text inside the book.

## 5.4 Model Hyperparameters

When building your LLM, you must define these numbers. They determine the final parameter count.

| Parameter | Description | Typical Small Model (e.g., 100M) | Typical Large Model (e.g., 7B) |
| :--- | :--- | :--- | :--- |
| **Layers** | Number of Transformer blocks stacked | 12 | 32 |
| **Hidden Size** | Size of the embedding vector (d_model) | 768 | 4096 |
| **Heads** | Number of parallel attention heads | 12 | 32 |
| **Context Length** | Maximum tokens the model can read at once | 1024 | 8192 |
