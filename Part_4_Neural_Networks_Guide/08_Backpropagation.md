# 8. Backpropagation (The Mathematical Foundation)

Backpropagation is how the network actually learns from its mistakes.

---

## The Concept

Once the Loss Function calculates the error, backpropagation uses calculus (specifically the Chain Rule) to calculate the gradient of the loss with respect to every single weight in the network.

## The Weight Update Equation

The weights are then updated using gradient descent to minimize the loss:

$$w = w - \eta \frac{\partial L}{\partial w}$$

Where:
*   **$w$** = The current weight
*   **$\eta$** = The learning rate (how big of a step to take)
*   **$\frac{\partial L}{\partial w}$** = The gradient of the Loss with respect to the weight
