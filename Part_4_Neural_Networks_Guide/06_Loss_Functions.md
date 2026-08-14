# 6. Loss Functions

A neural network learns by making mistakes and then correcting them.
The loss function is the component that measures how wrong the model currently is.

Without a loss function, the optimizer has no clear direction.
The model would produce outputs, but it would not know what "better" means.

---

## 6.1 What a Loss Function Does

The loss function compares:

- the model prediction
- the true target

It then returns a numeric value that represents the error.

Lower loss means the prediction is closer to the desired behavior.
Training tries to reduce this value over time.

---

## 6.2 Why the Choice of Loss Matters

Different tasks require different definitions of error.

For example:

- predicting a house price is not the same as predicting a class label
- predicting the next word in a sentence is not the same as predicting a binary yes or no decision

If the loss does not match the task, the model may optimize for the wrong behavior even if the code runs correctly.

---

## 6.3 Mean Squared Error (MSE)

MSE is common for regression tasks where the target is a continuous number.

Examples:

- price prediction
- temperature forecasting
- score estimation

### Intuition

Take the difference between prediction and target, square it, and average across examples.

Why squaring matters:

- larger mistakes are punished more heavily
- positive and negative errors do not cancel each other out

This makes MSE useful when large errors are especially undesirable.

---

## 6.4 Cross Entropy

Cross entropy is one of the most important loss functions in modern deep learning.

It is used heavily for:

- classification
- token prediction
- language modeling

### Intuition

The model outputs probabilities across possible classes.
Cross entropy punishes the model when it assigns low probability to the correct class.

So if the correct answer is present but the model is not confident in it, the loss still becomes large.

This is why cross entropy works so well for classification and next-token prediction.

---

## 6.5 KL Divergence

KL divergence compares one probability distribution to another.

It is often used when the target itself is not a single label but a distribution.

Common situations:

- distillation
- variational methods
- distribution matching

### Intuition

It measures how different the model's belief distribution is from a reference distribution.

---

## 6.6 Loss in LLM Training

In language models, the usual pretraining objective is next-token prediction.

That means:

- the model reads previous tokens
- it predicts a probability distribution over the next token
- cross entropy measures how much probability it assigned to the true next token

This happens for huge numbers of tokens across massive corpora.

So a simple loss function, repeated at huge scale, becomes the engine behind modern LLM capability.

---

## 6.7 Training Loss vs Real-World Quality

A lower loss is usually good, but it is not the full story.

A model can improve its training loss while still having practical problems such as:

- hallucinations
- poor instruction following
- weak reasoning
- safety failures

That is why loss is necessary but not sufficient.
It must be combined with broader evaluation.

---

## 6.8 Practical Mental Model

The loss function defines the target behavior in mathematical form.

You can think of it as the translation layer between:

- the human goal
- the optimization process

If that translation is poor, the model learns the wrong lesson.
If it is well chosen, the model has a meaningful objective to improve against.
