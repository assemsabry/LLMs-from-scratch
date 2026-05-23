# Dataset Collection

The intelligence of a Large Language Model is entirely bounded by the quality and quantity of the data it reads during pretraining. You cannot train a state-of-the-art model on bad data.

---

## 2.1 Data Sources

To train a general-purpose LLM, you need text from a vast array of sources to capture different writing styles, facts, and logical structures.

*   **Common Crawl:** The backbone of almost all LLMs. It is a massive, open-source archive of billions of scraped web pages. It provides sheer volume but is notoriously messy and requires extreme cleaning.
*   **Wikipedia Dumps:** The gold standard for factual, high-quality, well-structured English. Every LLM trains on Wikipedia.
*   **Books Datasets (e.g., Project Gutenberg, Books3):** Books are crucial because they provide long-form narrative coherence. They teach the model how to maintain context over thousands of words, rather than just short web articles.
*   **Code Datasets (GitHub):** Training on code (even if you don't want a coding model) is essential. Code has strict syntax and mathematical logic. Feeding code to an LLM drastically improves its general reasoning and logic capabilities.
*   **Conversations Datasets:** Forums (Reddit, StackOverflow) and dialogue datasets teach the model how humans interact, ask questions, and form conversational structures.

## 2.2 Dataset Types

During the complete lifecycle of a model, you will use different types of datasets for different phases:

1.  **Raw Text:** Unstructured data (Wikipedia, web pages, books). Used exclusively during the massive **Pretraining** phase to teach the model how language works.
2.  **Instruction Data:** Highly structured prompt/response pairs (e.g., `Prompt: Summarize this text. Response: [Summary]`). Used during **Supervised Fine-Tuning (SFT)** to teach the model to follow orders.
3.  **Dialogue Data:** Multi-turn conversational logs. Used to teach the model how to act as a chatbot with memory.

## 2.3 Scaling Data

How much data do you actually need? 

The relationship between model parameters and the number of training tokens is defined by the **Chinchilla Scaling Laws**. To train a compute-optimal model, you need roughly 20 tokens for every 1 parameter in your model.

*   **Minimum Viable Product:** If you are building a small 500M parameter model for testing, you need at least **10 Billion tokens**.
*   **Strong Production Model:** For a 7 Billion parameter model (like LLaMA-2 7B), you need at least 140 Billion tokens. Modern strong models push this even further to **1 Trillion+ tokens**.
