# 1. Foundations (Prerequisites for ML)

Before diving into Machine Learning and Deep Learning, a strong foundation in programming and mathematics is strictly required. Machine learning is fundamentally applied mathematics executed through code.

---

## 1.1 Programming Fundamentals

Python is the absolute standard language for modern AI engineering. You must master the following libraries:

*   **Python (Core):** Object-oriented programming, data structures (lists, dicts, sets), and performance optimization.
*   **NumPy:** The foundational library for numerical computing. You must understand N-dimensional arrays (tensors), broadcasting, and vectorized operations.
*   **Pandas:** The standard for tabular data manipulation. You must know how to clean, filter, group, and reshape dataframes.
*   **Matplotlib / Seaborn:** Visualization libraries necessary for understanding data distribution and model loss curves.

## 1.2 Mathematics (The Core Engine)

You cannot build or debug neural networks without understanding the math powering them.

### Linear Algebra
Machine learning operates on massive datasets simultaneously. We represent this data as matrices.
*   **Vectors, Matrices, and Tensors:** Data representations (1D, 2D, and N-D arrays).
*   **Dot Product & Matrix Multiplication:** The core operation of every neural network layer.
*   **Eigenvalues and Eigenvectors:** Essential for understanding dimensionality reduction (like PCA).
*   **Norms (L1, L2):** Used for calculating errors and applying regularization to prevent overfitting.

### Calculus
Calculus is the mathematical engine of learning. It tells the model *how* to update its parameters to reduce errors.
*   **Derivatives:** Measuring the rate of change.
*   **Partial Derivatives:** Measuring how a change in one specific weight affects the total error.
*   **The Chain Rule:** The absolute most important mathematical concept in Deep Learning. It allows us to calculate gradients across deep, multi-layered networks (the basis of Backpropagation).
*   **Gradient:** The vector of all partial derivatives pointing in the direction of steepest ascent (we move opposite to it to minimize loss).

### Probability & Statistics
AI models do not provide absolute certainties; they output probabilities.
*   **Mean, Variance, and Standard Deviation:** For normalizing data.
*   **Probability Distributions:** Gaussian (Normal), Bernoulli, and Binomial distributions.
*   **Bayes' Theorem:** The foundation of probabilistic ML models.
*   **Expectation:** The expected value of random variables.

---
*Note: Ensure you are comfortable with these topics before advancing to the core Machine Learning algorithms.*
