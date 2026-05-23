# 1. Practical Capstone Projects

Theory is useless without execution. To solidify your understanding of AI Engineering, you must build projects from scratch. Here is a progression of practical projects to test your skills.

---

## Project 1: Neural Network from Scratch (No PyTorch)
**Goal:** Understand the pure mathematics of Deep Learning.
*   **Task:** Write a simple Feedforward Neural Network using only Python and NumPy.
*   **Requirements:** You must manually write the forward pass matrix multiplications and manually calculate the backpropagation gradients using the chain rule. 
*   **Dataset:** Train it to achieve 95%+ accuracy on the MNIST handwritten digit dataset.

## Project 2: Train a Small GPT Model
**Goal:** Understand the Transformer architecture and autoregressive generation.
*   **Task:** Build a decoder-only Transformer from scratch in PyTorch, inspired by Andrej Karpathy's nanoGPT.
*   **Requirements:** Implement Self-Attention, Positional Encodings, and the training loop.
*   **Dataset:** Train it on the works of Shakespeare until it can generate convincing, albeit nonsensical, Shakespearean dialogue.

## Project 3: Parameter-Efficient Fine-Tuning (PEFT)
**Goal:** Learn how to customize massive, state-of-the-art open-source models.
*   **Task:** Take a pre-trained base model (like Llama-3-8B) and fine-tune it to answer medical questions.
*   **Requirements:** Use QLoRA to train the model on a single consumer GPU (like an RTX 3090 or 4090). Track your training loss.
*   **Dataset:** A specialized medical Q&A dataset from Hugging Face.

## Project 4: Build an Advanced RAG System
**Goal:** Solve the hallucination problem and build enterprise-ready AI.
*   **Task:** Build a chatbot that can accurately answer questions about your company's private PDF handbooks.
*   **Requirements:** Chunk the PDFs, convert them to embeddings, and store them in a local Vector Database (like ChromaDB). Write a retrieval script that injects the most relevant chunks into the prompt of a local LLM before generation.

## Project 5: Deploying an API
**Goal:** Learn MLOps and model serving.
*   **Task:** Take your fine-tuned medical model from Project 3 and deploy it to the web.
*   **Requirements:** Quantize the model to 4-bit (AWQ or GGUF) for speed. Wrap the model in a highly concurrent serving engine (like vLLM) and expose an endpoint using FastAPI. Write a simple HTML/JS frontend that allows a user to query the model.
