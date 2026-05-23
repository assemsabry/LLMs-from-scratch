# 7. Deep Learning Training Pipeline

Regardless of whether you are training a small image classifier or a massive LLM, the training pipeline follows the exact same mathematical sequence.

---

## The Standard Pipeline

1.  **Data Collection:** Gathering raw text, images, or tabular data.
2.  **Data Cleaning:** Removing null values, handling outliers, resizing images, or stripping HTML from text.
3.  **Feature Extraction / Embedding:** Converting raw data into a numerical format the model can understand (e.g., token IDs to embeddings).
4.  **Model Design:** Defining the architecture (e.g., 12 layers of Transformers, hidden size of 768).
5.  **Forward Pass:** Passing a batch of data through the network. The model multiplies weights, adds biases, applies activations, and generates a final prediction.
6.  **Loss Computation:** The prediction is compared against the actual correct answer using a Loss Function (like Cross Entropy). This outputs a single numerical error score.
7.  **Backpropagation:** The Calculus step. The Chain Rule is applied backward from the Loss through every layer to calculate the gradients (how much each weight contributed to the error).
8.  **Optimizer Step:** The optimizer (like AdamW) takes the gradients and slightly adjusts every weight in the network in the direction that minimizes the loss.

This process repeats for millions of iterations until the loss converges to a minimum.
