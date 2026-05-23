# 1. Advanced Topics: MoE and RAG

As AI models reach the limits of sheer scale, engineers rely on advanced architectural hacks to improve performance without melting the servers.

---

## 1.1 Mixture of Experts (MoE)

Scaling a dense model (where every parameter is used for every token) becomes impossibly expensive. MoE solves this by creating a "sparse" network.

### The Mechanism
Instead of having one giant feed-forward layer, an MoE model has multiple smaller "Expert" networks (e.g., 8 experts). 
*   **The Router:** Before the data hits the experts, a "Gating Mechanism" (the Router) mathematically decides which 2 experts are best suited to handle this specific word. 
*   If the user asks a math question, the Router sends the data to the "Math Expert" and the "Logic Expert". The other 6 experts are completely ignored.

### The Advantage
A model like Mixtral 8x7B has 47 Billion parameters in total. However, because it only activates 2 experts per token, it runs with the speed and inference cost of a 14 Billion parameter model, while possessing the vast knowledge of a 47B model.

## 1.2 Retrieval-Augmented Generation (RAG)

LLMs suffer from two fatal flaws:
1.  **Hallucination:** They confidently invent false information.
2.  **Knowledge Cutoff:** They are entirely ignorant of any events that occurred after their training data was collected.

RAG fixes both issues by giving the LLM an open-book test.

### The Mechanism
1.  **Vector Database:** You take your private company documents, convert them into mathematical embeddings, and store them in a Vector Database (like Pinecone or Milvus).
2.  **Retrieval:** When a user asks a question, the system searches the Vector Database for the most relevant document chunks.
3.  **Augmentation:** The system pastes those relevant chunks directly into the LLM's prompt window.
4.  **Generation:** The LLM reads the retrieved documents and generates an answer strictly based on those facts, heavily reducing hallucinations.
