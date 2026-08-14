# Advanced Topics: Beyond the Base Model

The AI landscape evolves on a weekly basis. Even if you build a perfect model from scratch, it will be obsolete without implementing advanced application techniques.

---

## 16.1 RAG (Retrieval-Augmented Generation)

An LLM's knowledge is frozen at the time it finishes training. If you ask a model trained in 2023 who won the Super Bowl in 2024, it will either guess or hallucinate.

**RAG** solves this problem without retraining the model.
1.  **The Database:** You take all your company's documents, slice them into paragraphs, convert them into vector embeddings, and store them in a Vector Database (like Pinecone or Qdrant).
2.  **The Retrieval:** When a user asks a question, you convert their question into a vector and search the database for the 3 most relevant paragraphs.
3.  **The Generation:** You inject those 3 paragraphs directly into the Prompt. `Prompt: Based on the following documents: [Doc1, Doc2, Doc3], answer the user's question.`
4.  **Result:** The LLM now has perfect, up-to-date memory and cites its sources.

### What modern RAG adds

In real systems, modern RAG often includes:

- better chunking
- metadata filtering
- reranking
- source display
- refresh jobs
- multi-step retrieval

So the real skill is not only "vector search."
It is designing a retrieval pipeline that returns the right evidence at the right time.

## 16.2 Autonomous Agents

LLMs do not just have to answer questions; they can perform actions.
By using tools (function calling), an LLM can become an Agent.

*   You provide the LLM with a list of tools it can use (e.g., `search_web()`, `run_python_code()`, `send_email()`).
*   Instead of generating text for the user, the LLM generates a JSON object instructing the system to execute a tool.
*   The system runs the Python code or searches Google, and feeds the result *back* into the LLM.
*   The LLM reads the result and decides what to do next.

### Why agents changed the field

This is one of the most important shifts in modern AI.

The system is no longer only completing text.
It is now participating in workflows.

That means useful AI products increasingly depend on:

- tool use
- multi-step planning
- verification
- memory
- safety gates

### Important warning

An autonomous agent without constraints is not a product.
It is a liability.

Modern agent systems need:

- permission boundaries
- logging
- retry rules
- human approval for risky actions

## 17.1 Building LLMs: The Final Summary

Building an LLM from scratch is a monumental task. The pipeline follows a strict mathematical progression:

1.  **Data:** Terabytes of text must be aggressively cleaned and deduplicated.
2.  **Tokenization:** The text is sliced into integers using BPE (SentencePiece).
3.  **Architecture:** The integers pass through Embeddings, Positional Encoding, and stacked Multi-Head Self-Attention layers.
4.  **Training:** The model loops billions of times, predicting the next token and adjusting its weights via Backpropagation and the AdamW optimizer to minimize Cross-Entropy Loss.
5.  **Scaling:** The math is distributed across hundreds of GPUs using Data and Tensor Parallelism.
6.  **SFT & Alignment:** The Base Model is fine-tuned (often using LoRA) to follow instructions, and aligned to human preferences via DPO or RLHF.
7.  **Deployment:** The final weights are Quantized to 4-bit and served via a highly optimized C++ inference engine like vLLM.
8.  **Modern Systems Layer:** Useful AI products now also add retrieval, tools, memory, safety, and deployment governance.

You now possess the complete theoretical and practical roadmap to building Large Language Models.

### Final modern takeaway

In 2026, building an LLM system well usually means building more than the model itself.

The strongest systems combine:

- model quality
- retrieval
- tool use
- inference optimization
- safety controls
- product integration
