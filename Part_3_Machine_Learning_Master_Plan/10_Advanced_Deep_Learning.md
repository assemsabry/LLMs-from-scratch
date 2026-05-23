# 10. Advanced Deep Learning

This section bridges the gap between basic Neural Networks and modern Large Language Models.

---

## 10.1 Transformers Deep Dive

The Transformer architecture changed AI forever by removing the need for sequential processing (RNNs).

*   **Self-Attention:** A mathematical mechanism allowing the model to look at every word in a sequence and calculate its relevance to the current word being processed.
*   **Multi-Head Attention:** Instead of doing attention once, the model does it (e.g., 12 times) in parallel. One head might focus on grammar, another on nouns, another on relationships.
*   **Positional Encoding:** Because the Transformer processes everything at once, it doesn't know word order naturally. We mathematically inject a "position signature" into each word's embedding.

## 10.2 Core LLM Concepts

*   **Tokens:** The fundamental unit of data for an LLM (subwords, not full words).
*   **Context Length:** The maximum number of tokens the model can process in one pass (e.g., 4096 or 128k).
*   **Embeddings:** The dense mathematical vectors that represent the "meaning" of a token.
*   **Logits:** The raw, unnormalized output scores from the final layer of the network before they are converted into probabilities via Softmax.

## 10.3 Training LLMs (The Pipeline)

Training a modern LLM involves three distinct phases:

1.  **Pretraining:** The model trains on raw internet data using Next-Token Prediction. It learns grammar, facts, logic, and coding.
2.  **Fine-Tuning (SFT):** The model is trained on a high-quality dataset of Instruction-Response pairs to teach it how to act like a helpful assistant rather than a text predictor.
3.  **RLHF (Reinforcement Learning from Human Feedback):** The model is aligned to human preferences to ensure it is safe, polite, and refuses dangerous requests.
