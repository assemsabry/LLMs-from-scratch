# 14. Deployment

A model has zero value if it remains inside a Jupyter Notebook.

---

## 14.1 Inference APIs
You must wrap the model in a server architecture so other software can interact with it.
*   **FastAPI / Flask:** Standard Python web frameworks.
*   **vLLM / TensorRT-LLM:** Highly optimized C++ engines specifically designed for serving Large Language Models. They handle batching and GPU memory management automatically.

## 14.2 Containerization
*   **Docker:** You must package your model, API, and all dependencies (PyTorch, CUDA versions) into a Docker container to ensure it runs exactly the same on a cloud server as it does on your laptop.

## 14.3 Monitoring (MLOps)
Models degrade over time.
*   **Data Drift:** When the incoming real-world data no longer matches the data the model was trained on (e.g., a new slang word becomes popular).
*   **Logging:** Tracking input queries, output responses, latency, and GPU usage over time.
