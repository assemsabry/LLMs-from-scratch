# 7. Optimizers

Once gradients are computed, the model still needs a rule for how to use them.
That rule is the optimizer.

An optimizer is the algorithm that converts gradient information into actual parameter updates.
In other words, it decides how the model learns from its mistakes.

---

## 7.1 Why Optimizers Matter

Even if you have:

- a strong dataset
- a correct architecture
- a good loss function

training can still fail if optimization is poor.

The optimizer strongly affects:

- convergence speed
- stability
- final model quality
- sensitivity to hyperparameters

This is why optimization is not a minor detail.
It is a central part of successful training.

---

## 7.2 The Basic Idea

After backpropagation, every trainable parameter has a gradient.
That gradient indicates how the loss would change if the parameter changed slightly.

The optimizer uses that information to update the weights in a direction that should reduce the loss.

At a simple level:

- positive gradient means the parameter may need to move downward
- negative gradient means the parameter may need to move upward

The exact update rule depends on the optimizer.

---

## 7.3 SGD

Stochastic Gradient Descent is the classic baseline optimizer.

### Core idea

Take the gradient and move the weights a small step in the direction that reduces the loss.

Why it matters:

- it is conceptually simple
- it teaches the foundation of optimization
- many advanced optimizers build on similar intuition

### Limitation

Plain SGD can be noisy and slower to tune well, especially in deep modern architectures.

---

## 7.4 Momentum

Momentum improves on plain SGD by accumulating directional information from previous steps.

### Intuition

Instead of reacting only to the current gradient, the optimizer keeps some memory of where useful progress has already been happening.

This can help:

- smooth noisy updates
- accelerate learning along stable directions
- reduce oscillation

Momentum is one of the first major practical improvements to basic gradient descent.

---

## 7.5 Adam

Adam stands for Adaptive Moment Estimation.
It is one of the most widely used optimizers in deep learning.

### Why Adam became popular

Adam adapts the effective update size for each parameter individually.
That makes it easier to use across many architectures without extremely delicate tuning.

Benefits:

- strong default behavior
- faster practical convergence in many settings
- works well for deep and complex models

This is why Adam became a common default for many research and production pipelines.

---

## 7.6 AdamW

AdamW is a refinement of Adam that handles weight decay more cleanly.

This matters because regularization and parameter updates interact in subtle ways.
AdamW separates those effects better than classic Adam.

That is one reason AdamW became especially important in:

- transformers
- LLM training
- modern large-scale fine-tuning

In many contemporary deep learning systems, AdamW is the most practical default choice.

---

## 7.7 The Optimizer Is Not Working Alone

An optimizer interacts with several other pieces:

- learning rate
- batch size
- gradient clipping
- normalization strategy
- weight decay
- schedule and warmup

So when training fails, the optimizer itself may not be the only issue.
It may be the optimizer plus the surrounding training recipe.

---

## 7.8 Choosing an Optimizer

A practical starting point is:

- learn with SGD first for intuition
- use Adam for general deep learning experiments
- use AdamW for transformers and LLM-focused systems

The best optimizer depends on the architecture, data, and scale, but this rule is a solid educational starting point.

---

## 7.9 Practical Mental Model

If gradients tell you what direction is downhill, the optimizer tells you how to walk downhill.

It decides:

- how big each step should be
- how noisy updates should be handled
- how history should influence the next step

That makes the optimizer one of the main reasons a model either learns efficiently or struggles for millions of steps.
