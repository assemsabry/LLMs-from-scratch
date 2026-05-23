# Large Language Models: Core Concepts

Large Language Models (LLMs) are the most advanced application of Deep Learning today. Built entirely on the Transformer architecture, they have achieved unprecedented capabilities in natural language understanding and generation.

---

## 1. Tokens and Vocabulary

Before text can be processed by a neural network, it must be converted into numbers. This process is called Tokenization.

*   **Tokens:** A token is the fundamental unit of data processed by an LLM. A token is not necessarily a full word. It can be a whole word (e.g., "apple"), a subword (e.g., "ing"), or even a single character. 
*   **Why not just words?** If we used whole words, our model's vocabulary would need to contain millions of unique entries, including every possible misspelling or conjugation. Subword tokenization (like BPE) strikes a balance, allowing the model to handle unseen words by breaking them down into known pieces.
*   **Rule of Thumb:** In English, 1 token roughly equals 0.75 words.

## 2. Context Length (Context Window)

The Context Length is the absolute maximum number of tokens an LLM can process in a single pass. 

*   **Why is there a limit?** The Self-Attention mechanism in a Transformer scales quadratically (`O(N^2)`). If you double the number of input tokens, the memory and compute required to calculate the attention matrix quadruple.
*   **Importance:** If you ask a question about a document that exceeds the context length, the model cannot read the whole document at once. Early models (GPT-2) had context lengths of 1,024 tokens. Modern models (like Gemini 1.5 Pro) boast massive context windows of up to 2 million tokens.

## 3. The Attention Mechanism in LLMs

As covered in the Neural Network Architectures module, LLMs rely entirely on Self-Attention to understand context.

In the context of LLMs, attention allows the model to map the grammatical and semantic relationships between all tokens in the prompt. When predicting the next word, it assigns massive mathematical weight to the most crucial context words earlier in the sequence, completely bypassing the "forgetfulness" issues of older RNNs.

## 4. Scaling Laws

The fundamental driving force behind the recent explosion in AI capabilities is governed by "Scaling Laws." Research has empirically shown that the performance of an LLM scales predictably with three primary factors:

1.  **Compute (C):** The total amount of processing power used during training (measured in FLOPs).
2.  **Dataset Size (D):** The total number of tokens the model reads during training.
3.  **Model Size (N):** The total number of parameters (weights and biases) in the model.

**The bitter lesson of scaling:** You cannot simply increase model size to make it smarter. If you build a 1-Trillion parameter model but train it on a tiny dataset, it will perform terribly. If you train a tiny 1-Billion parameter model on massive datasets for too long, it will stop improving (diminishing returns).

To optimize training, researchers follow "Chinchilla Scaling Laws" (named after a famous DeepMind paper), which dictate the mathematically optimal ratio between Model Size and Dataset Size for a given compute budget. The general rule of thumb is that **Dataset Size should scale linearly with Model Size** (e.g., a 10 Billion parameter model should be trained on roughly 200 Billion tokens).
