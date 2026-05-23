# Neural Network Architectures: Transformers

In 2017, a team at Google Brain published a paper titled "Attention Is All You Need." This paper introduced the Transformer architecture, completely replacing LSTMs and sparking the modern AI revolution. Every single modern Large Language Model (GPT-4, Claude, Gemini, LLaMA) is a Transformer.

---

## 1. The Core Innovation: Getting Rid of Sequential Processing

The fatal flaw of RNNs and LSTMs was that they had to read text sequentially, word by word. You couldn't process the 10th word until you had finished processing the 9th word. This meant they could not take advantage of the massive parallel processing power of modern GPUs.

Transformers threw away the sequential recurrent structure entirely. Instead, they ingest the **entire sequence of text all at once** and process every word in parallel.

## 2. Self-Attention

If the network processes all words at the same time, how does it know which words relate to each other? How does it understand context? The answer is the **Self-Attention Mechanism**.

When the network processes a specific word (let's say the word "bank"), it looks at every other word in the entire sentence simultaneously. It mathematically computes a "relevance score" (attention weight) between "bank" and all those other words.
*   If the sentence is "I went to the bank to deposit money," the word "bank" will pay high attention to "deposit" and "money."
*   If the sentence is "I sat on the river bank," the word "bank" will pay high attention to "river."

### How Attention is Calculated: Q, K, V
Self-attention relies on a database-like retrieval concept using three vectors for every word: Query (Q), Key (K), and Value (V).
1.  **Query (What I am looking for):** The current word asks a question about what context it needs.
2.  **Key (What I contain):** Every word broadcasts its properties.
3.  **Value (My actual meaning):** The actual information the word contains.

The mathematical operation is essentially `Softmax((Q * K^T) / sqrt(d)) * V`. The dot product of the Query and the Key determines how much "attention" the Query word should pay to the Key word.

## 3. Multi-Head Attention

A single word can mean multiple things simultaneously in a complex sentence. It might be the subject of a verb, while also being an adjective modifying a noun.

A single attention mechanism might only focus on one type of relationship. **Multi-Head Attention** solves this by running multiple self-attention mechanisms (heads) in parallel. For example, in a 12-head transformer:
*   Head 1 might learn to pay attention to grammar and syntax.
*   Head 2 might learn to pay attention to historical facts.
*   Head 3 might learn to pay attention to sentiment.

The outputs of all these heads are then concatenated and pushed through a standard Feedforward network.

## 4. Positional Encoding

Because the Transformer reads all words simultaneously, it has absolutely no idea what order the words are in. To the base transformer, "The dog bit the man" and "The man bit the dog" look mathematically identical.

To fix this, we inject **Positional Encodings**. Before the words are fed into the network, a mathematical pattern (often based on sine and cosine waves) is added to the word's representation. This pattern uniquely identifies the word's position in the sequence, allowing the network to distinguish between word order without sacrificing parallel processing speed.

## Summary of a Transformer Block

A standard Transformer block consists of the following flow:
1.  **Input Embeddings + Positional Encoding**
2.  **Multi-Head Self-Attention**
3.  **Add & Norm:** A residual connection (adding the input to the output) followed by Layer Normalization to stabilize training.
4.  **Feedforward Neural Network (FNN)**
5.  **Add & Norm:** Another residual connection and normalization step.

Modern LLMs are created by stacking dozens or even hundreds of these Transformer blocks on top of each other.
