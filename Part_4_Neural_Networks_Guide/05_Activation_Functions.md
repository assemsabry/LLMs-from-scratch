# 5. Activation Functions

Activation functions are what give neural networks nonlinear expressive power.
Without them, even a very deep network would behave like a much simpler linear system.

This makes activations one of the most important hidden ingredients in deep learning.

---

## 5.1 Why Nonlinearity Is Necessary

Suppose every layer only applies a linear transformation.
Then stacking many layers still collapses into one overall linear transformation.

That means the model would struggle with complex decision boundaries and rich pattern learning.

Activation functions solve this by introducing nonlinearity after the weighted sum.
That allows the network to model much more complicated relationships.

---

## 5.2 ReLU

ReLU stands for Rectified Linear Unit.
It is one of the most common hidden-layer activations in deep learning.

### Intuition

ReLU keeps positive values and zeroes out negative ones.

Why it became popular:

- simple
- fast
- effective in deep networks

ReLU helped make large-scale deep learning more practical because it is computationally cheap and tends to avoid some of the saturation issues of older activations.

### Limitation

If a neuron stays in the negative region too often, it may stop contributing meaningfully.
This is sometimes called the "dying ReLU" issue.

---

## 5.3 Sigmoid

Sigmoid maps values into the range between `0` and `1`.

### Why it is useful

This makes it natural for:

- probabilities
- binary classification outputs
- gating mechanisms in some recurrent models

### Limitation

Sigmoid can saturate at the extremes, which weakens gradients.
That makes optimization harder in deep hidden layers.

So sigmoid is important, but it is no longer the default hidden-layer activation in most modern deep models.

---

## 5.4 Tanh

Tanh maps values into the range between `-1` and `1`.

Compared with sigmoid, tanh is zero-centered, which can sometimes make optimization behavior better.

It was historically common in recurrent networks and older deep learning systems.

### Limitation

Like sigmoid, tanh can still saturate and shrink gradients in some regimes.

---

## 5.5 Softmax

Softmax is usually used in output layers for multi-class classification.

### What it does

It converts raw scores, often called logits, into a probability distribution whose values sum to `1`.

This allows the model to express relative confidence across many possible classes.

Softmax is especially important in:

- image classification
- text classification
- language modeling over vocabularies

---

## 5.6 Modern Activations in Large Models

As deep learning evolved, newer activations became important in large-scale systems.

Examples:

- GELU
- SwiGLU

These are especially common in transformers because smoother nonlinear behavior can improve optimization and representation quality at scale.

This is a good example of how even small design choices can matter a lot in frontier systems.

---

## 5.7 Choosing the Right Activation

A useful starting rule is:

- ReLU for many standard hidden layers
- sigmoid for binary output probabilities
- tanh when zero-centered bounded outputs are useful
- softmax for multi-class output distributions

In modern transformer systems, you should also expect GELU-family activations to appear frequently.

---

## 5.8 Practical Mental Model

Weights and biases decide how signals are combined.
Activation functions decide how those combined signals are reshaped before moving forward.

That reshaping is what lets networks move beyond straight-line behavior and learn the rich nonlinear structure that makes modern AI possible.
