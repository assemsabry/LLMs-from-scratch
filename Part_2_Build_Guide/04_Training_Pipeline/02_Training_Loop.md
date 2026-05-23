# The Training Pipeline and Optimizers

With the dataset cleaned, the tokenizer trained, the model architecture defined, and the loss function selected, we now construct the main engine: **The Training Loop**.

---

## 8.1 The Training Loop Steps

Training a neural network is an iterative process. For weeks or months, a supercomputer runs this exact loop millions of times:

1.  **Sample Data:** Grab a random batch of sequences from the massive dataset.
2.  **Forward Pass:** Pass the text through the model to get its predictions for the "next tokens".
3.  **Compute Loss:** Compare the model's predictions to the actual correct tokens using Cross-Entropy Loss.
4.  **Zero Gradients:** Clear out the old math from the previous loop.
5.  **Backward Pass (Backpropagation):** Use Calculus to determine exactly how much each weight in the model contributed to the error. This generates "Gradients."
6.  **Optimizer Step:** Adjust the weights slightly in the correct direction to minimize the error.

## 9.1 Optimizers

The algorithm that decides *how much* to adjust the weights is the Optimizer. 

For LLMs, **AdamW** is the absolute industry standard.
*   **Adam (Adaptive Moment Estimation):** Instead of using a single learning rate for every weight, Adam tracks the historical gradients and adjusts the learning rate for each specific parameter dynamically.
*   **W (Weight Decay):** A regularization technique that penalizes the model for letting weights grow too large, preventing overfitting.

## 9.2 The Learning Rate Schedule

The Learning Rate dictates how large of a step the Optimizer takes. If the step is too small, the model will take centuries to train. If it's too large, the model will crash and fail to learn.

LLMs use a highly specific schedule for the Learning Rate over the course of training:
1.  **Warmup:** You cannot start at a high learning rate. The model starts with random weights; a massive update will destroy its stability. You linearly increase the learning rate from 0 to your maximum target over the first few thousand steps.
2.  **Cosine Decay:** After reaching the peak, you slowly and smoothly decrease the learning rate following a cosine curve until it reaches near-zero at the end of training. This allows the model to make large, fast discoveries early on, and fine-tune precise details at the very end.
