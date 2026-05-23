# 2. The Neuron

The artificial neuron (or perceptron) is the fundamental building block of any neural network.

---

## 2.1 Components
A single neuron consists of the following elements:
*   **Inputs:** $x_1, x_2, ..., x_n$
*   **Weights:** $w_1, w_2, ..., w_n$
*   **Bias:** $b$

## 2.2 The Fundamental Equation
The neuron performs two distinct operations. 

First, it calculates the weighted sum of its inputs plus the bias:

$$z = \sum_{i=1}^{n} w_i x_i + b$$

Then, this linear result is passed through a non-linear activation function to produce the final output:

$$a = f(z)$$

## 2.3 The Goal
The primary objective of the neuron is to transform the inputs into a more useful representation that assists in making accurate predictions. By adjusting the weights ($w$) and bias ($b$), the neuron learns which inputs are the most important.
