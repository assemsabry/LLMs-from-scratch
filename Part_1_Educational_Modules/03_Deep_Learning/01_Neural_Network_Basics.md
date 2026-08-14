# Deep Learning: Neural Network Basics

Deep Learning is a specialized subfield of Machine Learning based on Artificial Neural Networks (ANNs). It is the technology behind modern AI breakthroughs like Large Language Models, self-driving cars, and advanced image generation.

---

## 1. The Artificial Neuron

The fundamental building block of a neural network is the artificial neuron, also called a node or perceptron.

A single neuron takes multiple numerical inputs, processes them, and produces a single numerical output.

### The Mathematics of a Neuron

The operation of a neuron consists of two distinct mathematical steps: Summation and Activation.

**Step 1: Summation (Linear Transformation)**  
Every input connected to a neuron has a corresponding weight. The neuron multiplies each input by its weight, sums them, and then adds a bias term.

`z = (w1 * x1) + (w2 * x2) + ... + (wn * xn) + b`

*   **Weights:** Determine the importance of a given input.
*   **Bias:** Shifts the activation behavior and allows the neuron to respond even when inputs are near zero.

**Step 2: Activation Function (Non-linear Transformation)**  
The result of the summation is only linear. If you stack only linear operations, the whole network collapses into a bigger linear function.

So we apply a non-linear activation:

`a = f(z)`

### Why non-linearity matters

Without non-linearity, depth would not buy you much.
With non-linearity, stacked layers can represent:

- curves
- interactions
- hierarchies
- abstract concepts

## 2. Activation Functions

Different activation functions serve different purposes depending on where they are placed in the network.

*   **ReLU:** `f(z) = max(0, z)`. Cheap to compute and widely used.
*   **Sigmoid:** Squashes output between 0 and 1. Mostly used for binary outputs today.
*   **Tanh:** Squashes values between -1 and 1.
*   **Softmax:** Converts logits into a probability distribution over classes.
*   **GELU:** A smoother activation used heavily in modern transformer models.

### Practical intuition

Activation functions shape how information flows and how gradients behave.

That means they affect:

- trainability
- stability
- expressiveness
- convergence speed

## 3. Network Architecture

Neurons are organized into layers to form a complete neural network.

*   **Input Layer:** Receives the raw data.
*   **Hidden Layers:** Intermediate layers that learn increasingly useful internal representations.
*   **Output Layer:** Produces the final prediction.

When information flows strictly from the input layer to the output layer without looping back, it is called a **Feedforward Neural Network**.

### Why depth helps

Depth allows the model to build representations stage by stage.

For example:

- early layers may detect simple patterns
- middle layers combine them into richer structures
- later layers form higher-level abstractions

This hierarchical learning is one reason deep learning became so powerful.

## 4. Why These Basics Matter for LLMs

Large Language Models may feel far away from simple neural networks, but they are still built on the same foundations:

- linear transformations
- activations
- stacked layers
- learned parameters

Transformers are more advanced, but they are still deep neural networks.

## 5. Final Takeaway

If you understand neurons, activations, and layered computation, you already understand the base language of deep learning.

Everything larger, including LLMs, is built on top of these same ideas.
