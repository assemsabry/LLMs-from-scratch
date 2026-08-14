# Dataset Collection

The intelligence of a Large Language Model is entirely bounded by the quality and quantity of the data it reads during pretraining. You cannot train a state-of-the-art model on bad data.

Data collection is not just a download problem.
It is a strategy problem.

---

## 2.1 Data Sources

To train a general-purpose LLM, you need text from a vast array of sources to capture different writing styles, facts, and logical structures.

*   **Common Crawl:** The backbone of almost all LLMs. It is a massive, open-source archive of billions of scraped web pages. It provides sheer volume but is notoriously messy and requires extreme cleaning.
*   **Wikipedia Dumps:** The gold standard for factual, high-quality, well-structured English. Every LLM trains on Wikipedia.
*   **Books Datasets (e.g., Project Gutenberg, Books3):** Books are crucial because they provide long-form narrative coherence. They teach the model how to maintain context over thousands of words, rather than just short web articles.
*   **Code Datasets (GitHub):** Training on code (even if you don't want a coding model) is essential. Code has strict syntax and mathematical logic. Feeding code to an LLM drastically improves its general reasoning and logic capabilities.
*   **Conversations Datasets:** Forums (Reddit, StackOverflow) and dialogue datasets teach the model how humans interact, ask questions, and form conversational structures.

### Why source diversity matters

Different sources teach different strengths:

- books teach long-form coherence
- code teaches structure and precision
- forums teach interaction style
- encyclopedic sources teach dense factual style
- web pages provide scale and topical breadth

That is why strong models usually need a balanced mixture, not only one source type.

## 2.2 Dataset Types

During the complete lifecycle of a model, you will use different types of datasets for different phases:

1.  **Raw Text:** Unstructured data (Wikipedia, web pages, books). Used exclusively during the massive **Pretraining** phase to teach the model how language works.
2.  **Instruction Data:** Highly structured prompt/response pairs (e.g., `Prompt: Summarize this text. Response: [Summary]`). Used during **Supervised Fine-Tuning (SFT)** to teach the model to follow orders.
3.  **Dialogue Data:** Multi-turn conversational logs. Used to teach the model how to act as a chatbot with memory.

### Practical note

Do not confuse:

- pretraining data
- post-training instruction data
- retrieval data

They serve different roles in the system and should be curated differently.

## 2.3 Scaling Data

How much data do you actually need? 

The relationship between model parameters and the number of training tokens is defined by the **Chinchilla Scaling Laws**. To train a compute-optimal model, you need roughly 20 tokens for every 1 parameter in your model.

*   **Minimum Viable Product:** If you are building a small 500M parameter model for testing, you need at least **10 Billion tokens**.
*   **Strong Production Model:** For a 7 Billion parameter model (like LLaMA-2 7B), you need at least 140 Billion tokens. Modern strong models push this even further to **1 Trillion+ tokens**.

### Why more data is not always better

More raw text is useful only if:

- it is not mostly duplicated
- it is not low-quality noise
- it matches your target behavior reasonably well

Low-quality scale can still damage a model.

## 2.4 What Learners Should Collect First

If you are building a small educational model, start with a manageable corpus that includes:

- clean prose
- some code
- some instructional text
- domain text if you have a specific goal

That gives you a better learning signal than downloading massive garbage and pretending scale alone will save the model.
