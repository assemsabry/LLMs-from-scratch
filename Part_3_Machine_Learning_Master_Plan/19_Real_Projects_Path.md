# 19. Real Projects Path

Theory without implementation is useless. The best way to learn Machine Learning is by building progressively harder projects.

---

## 19.1 Level 1: Classical ML (Scikit-Learn)
*   **House Price Predictor:** Use Linear Regression or Random Forests on tabular data. Learn data cleaning and cross-validation.
*   **Customer Segmentation:** Use K-Means clustering to group customers based on purchasing history. Learn unsupervised evaluation.

## 19.2 Level 2: Basic Deep Learning (PyTorch)
*   **MNIST Digit Recognizer:** Build a simple FNN, then a CNN to classify handwritten digits. Learn the training loop, loss functions, and backpropagation.
*   **Sentiment Analysis:** Use an RNN/LSTM on IMDB movie reviews to classify text as positive or negative. Learn basic tokenization and embeddings.

## 19.3 Level 3: Advanced Deep Learning (Transformers)
*   **Build a Nano-GPT:** Follow Andrej Karpathy's guide to build a character-level Transformer from scratch. Understand self-attention mathematics.
*   **Fine-Tune an LLM:** Take an open-source model like LLaMA-3 (8B) and use LoRA to fine-tune it on a specific dataset (e.g., medical Q&A). Learn PEFT and HuggingFace pipelines.

## 19.4 Level 4: Full Stack AI Engineer
*   **RAG System:** Build a Retrieval-Augmented Generation pipeline using LangChain, a vector database (Chroma/Pinecone), and an LLM API.
*   **Deploy a Model:** Containerize your fine-tuned model using Docker and deploy it to a cloud server using FastAPI or vLLM.
