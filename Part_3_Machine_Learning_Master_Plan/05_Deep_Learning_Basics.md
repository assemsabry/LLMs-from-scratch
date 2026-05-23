# 5. Deep Learning (Neural Networks)

Classical Machine Learning struggles with highly unstructured data like images, audio, and raw text. This is where Deep Learning, powered by Artificial Neural Networks, dominates.

---

## 5.1 The Perceptron (The Artificial Neuron)

The fundamental building block of all deep learning is the artificial neuron (perceptron). It attempts to mimic a biological neuron.

A single neuron takes multiple inputs, multiplies them by learned **Weights**, adds a learned **Bias**, and sums the result.

$$ z = \sum_{i} w_i x_i + b $$

The result $z$ is then passed through a mathematical function called an **Activation Function** to determine if the neuron "fires" or not.

$$ a = f(z) $$

## 5.2 Activation Functions

If neural networks only used linear math (multiplication and addition), stacking 100 layers would be mathematically identical to just having 1 layer. Activation functions inject **non-linearity**, allowing networks to learn incredibly complex patterns.

*   **ReLU (Rectified Linear Unit):** The most common activation. Returns $x$ if $x > 0$, otherwise returns 0. Fast and solves the vanishing gradient problem.
*   **Sigmoid:** Squashes output between 0 and 1. Used in binary classification and gating mechanisms.
*   **Tanh:** Squashes output between -1 and 1. Often used in RNNs.
*   **Softmax:** Used at the final layer of a multi-class network (and extensively in Transformers). It converts a list of numbers into a valid probability distribution (where all numbers sum to 1).
*   **GELU (Gaussian Error Linear Unit):** A smoother version of ReLU. This is the activation function predominantly used in modern LLMs like GPT and LLaMA.

## 5.3 Loss Functions in DL

Just like classical ML, the network needs a mathematical error score.
*   **MSE (Mean Squared Error):** Used when the neural network is predicting a continuous number (Regression).
*   **Cross Entropy:** Used when the neural network is predicting categories (Classification). This is the loss function used to train LLMs (predicting the next word category).
*   **KL Divergence:** Measures how one probability distribution diverges from an expected reference probability distribution (often used in VAEs and RLHF).

## 5.4 Optimizers

The algorithm that updates the weights.
*   **SGD (Stochastic Gradient Descent):** The basic optimization algorithm.
*   **Adam:** The standard optimizer for most deep learning. It adapts the learning rate for each individual weight dynamically.
*   **AdamW:** Adam + Weight Decay. The undisputed king of optimizers for training massive Transformers and LLMs.
*   **RMSProp:** An older adaptive optimizer, often used in RNNs.

## 5.5 Backpropagation

This is how the network learns.
1.  The network makes a prediction (Forward Pass).
2.  The loss is calculated.
3.  **Backpropagation** uses Calculus (the Chain Rule) to trace the error backward through every single layer of the network. It calculates exactly how much each specific weight contributed to the error.
4.  The Optimizer uses these calculations (gradients) to update the weights.
