# Model Architecture

Modern LLMs (like GPT, LLaMA, and Mistral) are all variants of the **Decoder-Only Transformer** architecture. 

Once your text is tokenized into integer IDs, the neural network takes over. Here is the mathematical journey a token takes through the model.

---

## 5.1 The Core Components

An LLM consists of three main stages:
1.  **Embedding Layer:** Converts the integer token ID into a dense vector (e.g., a list of 4096 floating-point numbers). This vector represents the "meaning" of the token.
2.  **Positional Encoding:** Because Transformers process all tokens simultaneously, they have no concept of word order. We mathematically add a "position vector" to the embedding so the model knows which word came first.
3.  **Transformer Blocks (The Core):** A series of identical layers (e.g., 32 layers stacked on top of each other). The output of Block 1 feeds into Block 2, and so on.

### Why decoder-only won for generative LLMs

Decoder-only models became dominant for open-ended generation because they are naturally aligned with the autoregressive objective:

- read previous tokens
- predict the next token

This makes them especially strong for:

- chat
- code generation
- long-form writing
- agent planning traces

## 5.1.1 Input to Output Flow

A useful mental model is:

1. token IDs enter
2. embeddings turn them into vectors
3. position information is added
4. stacked transformer blocks refine the representation
5. a final linear layer maps vectors back to vocabulary logits
6. decoding chooses the next token

That complete path is the heart of a GPT-style model.

## 5.2 The Transformer Block

Each individual block in the stack does the heavy lifting. It consists of:

*   **Layer Normalization:** Stabilizes the neural network by keeping the numerical values of the vectors from growing too large.
*   **Multi-Head Self-Attention:** The most critical part. This allows tokens to "look" at other tokens in the sequence to gather context. (e.g., the word "bank" looks at the word "river" to realize it means a riverbank, not a financial institution).
*   **Feedforward Network (FFN):** A standard Multi-Layer Perceptron (MLP) applied to each token independently. If Attention is how tokens talk to each other, the FFN is how the model recalls facts memorized during training.
*   **Residual Connections:** Instead of just passing the output of the Attention layer to the next step, we mathematically ADD the original input back to the output (`x = x + attention(x)`). This prevents the "vanishing gradient" problem in deep networks.

### Why block design matters

A modern transformer block is not arbitrary.
It is carefully designed to balance:

- representation quality
- training stability
- parallel compute efficiency
- depth scalability

Small changes to block design can have major effects on:

- trainability
- memory use
- long-context behavior
- inference speed

## 5.3 The Attention Formula

The mathematical heart of the model is the Scaled Dot-Product Attention formula:

`Attention(Q, K, V) = softmax( (Q * K^T) / sqrt(d_k) ) * V`

*   **Q (Query):** What the current token is looking for.
*   **K (Key):** What other tokens contain.
*   **V (Value):** The actual information the other tokens hold.
*   *Analogy:* Q is your search query in a library, K is the title on the spine of the book, V is the text inside the book.

### Why this formula is so powerful

It allows every token to dynamically decide which earlier information matters most.

That is one reason transformers work across so many domains:

- language
- code
- images
- audio
- video

The routing mechanism is general.

## 5.4 Model Hyperparameters

When building your LLM, you must define these numbers. They determine the final parameter count.

| Parameter | Description | Typical Small Model (e.g., 100M) | Typical Large Model (e.g., 7B) |
| :--- | :--- | :--- | :--- |
| **Layers** | Number of Transformer blocks stacked | 12 | 32 |
| **Hidden Size** | Size of the embedding vector (d_model) | 768 | 4096 |
| **Heads** | Number of parallel attention heads | 12 | 32 |
| **Context Length** | Maximum tokens the model can read at once | 1024 | 8192 |

### Important architecture tradeoffs

When designing a model, you are always balancing:

- depth
- width
- context length
- memory cost
- training budget
- serving cost

You cannot maximize everything at once.

## 5.5 What Learners Should Build First

If you are learning from scratch, start with a very small decoder-only transformer:

- small vocab
- short context
- small hidden size
- few layers

This lets you understand the architecture before dealing with expensive scale.

The educational goal is not to match frontier size immediately.
The goal is to understand the mathematical pipeline clearly.
