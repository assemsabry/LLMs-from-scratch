# Model Training Details: The Pipeline

Training a neural network is an iterative process of making predictions, measuring errors, and adjusting weights. 

---

## 1. Core Terminology

Before diving into the pipeline, let's establish the fundamental vocabulary of model training:

*   **Parameters:** The internal variables the model learns during training. These are the **weights** and **biases**. A "7B" model means it has 7 Billion parameters.
*   **Gradients:** The mathematical direction and magnitude of how we should change the parameters to reduce the loss. Computed during backpropagation.
*   **Epoch:** One complete pass through the *entire* training dataset. 
*   **Batch Size:** Because datasets are too massive to fit into GPU memory all at once, we split the dataset into smaller chunks called "batches". The batch size is the number of samples processed before updating the model's weights.
*   **Step (or Iteration):** One update of the model's weights. If you have 1000 training examples and a batch size of 10, it will take 100 steps to complete 1 epoch.

## 2. The Training Pipeline Step-by-Step

A standard deep learning training loop follows these exact steps, repeated millions or billions of times:

### Step 1: Data Preparation
*   **Data Collection & Cleaning:** Gathering raw data and removing noise (e.g., removing HTML tags from scraped web text).
*   **Tokenization:** Converting the raw text into integer Token IDs.
*   **Dataset Batching:** Grouping the tokenized sequences into batches of a uniform size (using padding if necessary).

### Step 2: The Forward Pass
*   We feed a single batch of data (e.g., a batch of 32 sentences) into the model.
*   The data flows forward through the embedding layers, the attention mechanisms, and the feedforward networks.
*   The model outputs its **Logits** (raw, unnormalized predictions for what the next token should be).

### Step 3: Loss Computation
*   We compare the model's predictions (Logits) to the actual true target labels.
*   We apply a Loss Function (usually **Cross Entropy Loss** for LLMs) to mathematically quantify how wrong the model was on this specific batch.

### Step 4: Backpropagation (The Backward Pass)
*   We use calculus (the Chain Rule) to compute the gradient of the loss with respect to every single parameter in the model.
*   This asks the mathematical question: "If I change this specific weight by a tiny amount, how much will my total loss decrease?"

### Step 5: Optimizer Step
*   We take the gradients calculated in Step 4 and feed them into the Optimizer (e.g., **AdamW**).
*   The optimizer updates the actual weights of the model. It moves them a tiny bit in the direction that reduces the loss, with the size of that step controlled by the **Learning Rate**.

### Step 6: Zero Gradients
*   In PyTorch, gradients accumulate by default. Before processing the next batch, we must explicitly wipe the old gradients to zero, otherwise, the next step will be calculated incorrectly.

*Rinse and repeat for millions of batches until the loss converges.*
