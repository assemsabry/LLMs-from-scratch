# Foundation 1: Mathematics for AI

To truly understand how AI, Machine Learning, and Deep Learning algorithms work under the hood, a solid grasp of specific mathematical concepts is absolutely essential. This section covers the core pillars of mathematics required for AI Engineering: Linear Algebra, Calculus, and Probability & Statistics.

---

## 1. Linear Algebra

Linear Algebra is the mathematical language of data. Neural networks operate on data stored in high-dimensional structures, and linear algebra provides the rules for manipulating these structures efficiently.

### Vectors, Matrices, and Tensors

*   **Scalar:** A single number (e.g., 5, -2.3). It has magnitude but no direction. In a neural network, a single weight or bias is a scalar.
*   **Vector:** A one-dimensional array of numbers. You can think of it as a point in space or a directed line segment. A vector has both magnitude and direction. In ML, a single data sample (like a row in a spreadsheet) is often represented as a feature vector.
*   **Matrix:** A two-dimensional array of numbers, consisting of rows and columns. A dataset containing multiple samples is typically represented as a matrix. The weights connecting one layer of a neural network to the next form a weight matrix.
*   **Tensor:** The generalization of scalars, vectors, and matrices to higher dimensions. 
    *   A 0-dimensional tensor is a scalar.
    *   A 1-dimensional tensor is a vector.
    *   A 2-dimensional tensor is a matrix.
    *   A 3-dimensional tensor can represent an image (height, width, color channels).
    *   A 4-dimensional tensor can represent a batch of images.

### Eigenvalues and Eigenvectors

When a linear transformation (represented by a square matrix) is applied to a vector, the vector generally changes both its direction and magnitude. However, for a given matrix, there are special vectors that only change in magnitude (they are stretched or shrunk) but not in direction.

*   **Eigenvector:** A non-zero vector that changes at most by a scalar factor when a linear transformation is applied to it.
*   **Eigenvalue:** The scalar factor by which the eigenvector is scaled.

Mathematically, for a square matrix `A`, an eigenvector `v`, and an eigenvalue `lambda`:
`A * v = lambda * v`

**Why is this important in AI?**
Eigenvalues and eigenvectors are fundamental to Principal Component Analysis (PCA), a technique used for dimensionality reduction. PCA finds the directions (eigenvectors) along which the data varies the most, and the magnitude of this variance is given by the corresponding eigenvalues. They are also crucial in understanding the stability of Recurrent Neural Networks (RNNs) and graph-based models.

---

## 2. Calculus

Calculus helps us understand how things change. In Machine Learning, we want to change our model's parameters (weights and biases) to minimize the error (loss) of its predictions.

### Derivatives

The derivative of a function measures the sensitivity to change of the function value (output value) with respect to a change in its argument (input value). Geometrically, the derivative is the slope of the tangent line to the graph of the function at that point.

If you have a loss function `L(w)`, the derivative `dL/dw` tells you how much the loss `L` will change if you change the weight `w` by a tiny amount.

### Partial Derivatives

In deep learning, functions almost always depend on multiple variables (millions or billions of weights). A partial derivative is the derivative of a function with respect to one of those variables, holding the others constant.

If a loss function `L` depends on weights `w1` and `w2`, the partial derivative of `L` with respect to `w1` (written as `partial L / partial w1`) tells us how the loss changes as we vary `w1`, assuming `w2` remains fixed. The collection of all partial derivatives of a function forms a vector called the **Gradient**. Optimization algorithms like Gradient Descent use the gradient to find the direction of steepest descent to minimize the loss.

### The Chain Rule

The Chain Rule is arguably the most important calculus concept in deep learning. It is a formula to compute the derivative of a composite function.

If you have a function `f(g(x))`, the chain rule states:
`d/dx [f(g(x))] = f'(g(x)) * g'(x)`

**Why is this critical?**
A neural network is essentially a massive composite function: `Output = Layer3(Layer2(Layer1(Input)))`. To update the weights in `Layer1`, we need to know how a change in `Layer1`'s weights affects the final `Output` (and thereby the Loss). The Chain Rule allows us to compute these derivatives backward from the output layer to the input layer. This process is called **Backpropagation**, the engine that powers neural network training.

---

## 3. Probability and Statistics

Since real-world data is noisy and models make predictions with varying degrees of certainty, probability and statistics provide the framework for reasoning under uncertainty.

### Distributions

A probability distribution describes how the probabilities are distributed over the values of a random variable.
*   **Normal (Gaussian) Distribution:** The famous "bell curve." It is defined by its mean (center) and standard deviation (spread). Many processes in nature follow this distribution. In ML, weight initialization techniques often sample from a normal distribution, and many models assume the errors are normally distributed.
*   **Bernoulli Distribution:** A discrete probability distribution of a random variable which takes the value 1 with probability `p` and the value 0 with probability `q = 1-p`. This is foundational for binary classification problems.
*   **Uniform Distribution:** All outcomes are equally likely. Often used for initial random guesses.

### Expectation and Variance

*   **Expectation (Mean):** The long-run average value of repetitions of the experiment it represents. It is the "center of mass" of a distribution.
*   **Variance:** A measure of how far a set of numbers is spread out from their average value. High variance indicates the data points are very spread out. Standard deviation is the square root of the variance. In ML, we often talk about the "Bias-Variance Tradeoff," where variance refers to how much the model's predictions fluctuate based on the specific training data it saw.

### Bayesian Inference

Bayesian probability is an interpretation of the concept of probability, in which probability is seen not as a frequency of occurrence, but as a degree of belief or certainty.

**Bayes' Theorem** provides a mathematical rule for updating our beliefs in light of new evidence.
`P(A|B) = [P(B|A) * P(A)] / P(B)`

*   **P(A): Prior.** Our initial belief about hypothesis A before seeing the data.
*   **P(B|A): Likelihood.** The probability of observing the data B given that hypothesis A is true.
*   **P(A|B): Posterior.** Our updated belief about hypothesis A after seeing the data B.
*   **P(B): Evidence.** The total probability of observing the data B.

Bayesian inference is the foundation of many ML algorithms, including Naive Bayes classifiers, Bayesian Neural Networks, and generative models like Variational Autoencoders (VAEs), where we wish to infer latent variables from observed data.
