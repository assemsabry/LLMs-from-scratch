# Deep Learning: Neural Network Basics

Deep Learning is a specialized subfield of Machine Learning based on Artificial Neural Networks (ANNs). It is the technology behind modern AI breakthroughs like Large Language Models, self-driving cars, and advanced image generation.

---

## 1. The Artificial Neuron

The fundamental building block of a neural network is the artificial neuron, also called a "node" or "perceptron." It is loosely inspired by biological neurons in the human brain.

A single neuron takes multiple numerical inputs, processes them, and produces a single numerical output.

### The Mathematics of a Neuron

The operation of a neuron consists of two distinct mathematical steps: Summation and Activation.

**Step 1: Summation (Linear Transformation)**
Every input connected to a neuron has a corresponding **Weight** (w). The neuron multiplies each input (x) by its weight and sums them all up. Finally, it adds a constant value called a **Bias** (b).

`z = (w1 * x1) + (w2 * x2) + ... + (wn * xn) + b`

*   **Weights (w):** Determine the importance of a given input. If a feature is highly relevant, the network will learn to assign it a large weight.
*   **Bias (b):** Shifts the activation function to the left or right, allowing the neuron to trigger even if all inputs are zero.
*   *Note: In the context of LLMs, when we talk about a "7 Billion Parameter" model, those parameters are exactly these weights and biases.*

**Step 2: Activation Function (Non-linear Transformation)**
The result of the summation (`z`) is just a linear combination. If we stacked millions of linear neurons together, the entire network would collapse mathematically into a single linear function, making it impossible to learn complex patterns.

To fix this, we pass `z` through an **Activation Function** `f(z)`, which introduces non-linearity.
`a = f(z)`

## 2. Activation Functions

Different activation functions serve different purposes depending on where they are placed in the network.

*   **ReLU (Rectified Linear Unit):** The most common activation function in deep learning. It simply outputs the input if it is positive, and outputs 0 if it is negative. `f(z) = max(0, z)`. It is computationally cheap and helps solve the vanishing gradient problem.
*   **Sigmoid:** Compresses the output to a value between 0 and 1. Historically popular, but now mostly used only in the final output layer for binary classification. It suffers from vanishing gradients.
*   **Tanh (Hyperbolic Tangent):** Similar to Sigmoid, but squashes values between -1 and 1. Often preferred over Sigmoid in hidden layers because it is zero-centered.
*   **Softmax:** Used almost exclusively in the final output layer of a multi-class classification problem (including predicting the next word in an LLM). It converts a vector of raw scores (logits) into a probability distribution, where all output values sum up to exactly 1.
*   **GELU (Gaussian Error Linear Unit):** A smoother version of ReLU. It is the primary activation function used in modern Transformer models like GPT and BERT.

## 3. Network Architecture

Neurons are organized into layers to form a complete Neural Network.

*   **Input Layer:** The first layer that receives the raw data (e.g., pixel values of an image, or token embeddings of a text).
*   **Hidden Layers:** The layers between the input and output. A network with multiple hidden layers is called a "Deep" Neural Network. These layers learn hierarchical representations of the data.
*   **Output Layer:** The final layer that produces the model's prediction.

When information flows strictly from the input layer to the output layer without looping back, it is called a **Feedforward Neural Network**.
