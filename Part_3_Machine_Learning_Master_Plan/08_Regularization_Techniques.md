# 8. Regularization Techniques

Deep neural networks are powerful partly because they can fit extremely complex patterns.
That same flexibility creates a danger:

- the model may memorize the training set instead of learning general rules

Regularization is the set of techniques used to reduce overfitting and improve generalization.

---

## 8.1 What Overfitting Looks Like

Overfitting happens when:

- training performance keeps improving
- validation performance stops improving or gets worse

In other words, the model becomes very good at the data it has already seen but weaker at handling new data.

This is one of the central failure modes in machine learning.

---

## 8.2 Dropout

Dropout randomly disables a fraction of neurons during training.

For example:

- one forward pass may use one subset of neurons
- the next pass may use a slightly different subset

### Why it works

This prevents the network from relying too heavily on one narrow pathway.
It encourages the model to spread information more robustly across many features.

### Important note

Dropout is typically active during training and disabled during inference.

---

## 8.3 L2 Regularization and Weight Decay

L2 regularization adds a penalty for large weights.
This encourages the model to keep parameter magnitudes under control.

Weight decay is a closely related practical form used with optimizers such as AdamW.

### Why it matters

Very large weights can make the model sharp, brittle, and more likely to overfit.
Keeping weights more restrained often improves stability and generalization.

---

## 8.4 Early Stopping

Early stopping monitors validation performance during training.

If validation stops improving for a sustained period, training is halted.

### Why it works

Training loss almost always keeps dropping eventually.
That alone does not mean the model is improving in a useful way.

Early stopping protects you from continuing into the memorization regime after the model has already learned the useful structure available in the data.

---

## 8.5 Data Augmentation

Data augmentation increases the effective diversity of the training set without collecting entirely new samples.

In vision, this can include:

- flipping
- cropping
- rotating
- color changes

In text, augmentation is more delicate, but some tasks may use controlled paraphrasing, noise injection, or retrieval-grounded variation.

### Why it works

It teaches the model that small superficial variations should not change the core meaning or label.

---

## 8.6 Label Smoothing

Label smoothing slightly softens the target distribution instead of treating the correct class as absolute certainty.

This can help reduce overconfidence and sometimes improve calibration.

It is especially useful in some classification settings.

---

## 8.7 Normalization and Generalization

Normalization methods such as batch normalization, layer normalization, or RMSNorm are not purely regularizers in the classic sense, but they often improve training stability and indirectly help generalization.

They make optimization easier by keeping internal activations in healthier numeric ranges.

---

## 8.8 Regularization in LLMs

Large language models use some regularization ideas differently from older small models.

Examples:

- dropout may be used more carefully than in classic vision pipelines
- weight decay remains important
- data quality and deduplication act like powerful forms of regularization
- early stopping and checkpoint selection still matter

For LLMs, regularization is not only about the architecture.
It is also about the dataset and the training recipe.

---

## 8.9 Practical Mental Model

Regularization does not make the model weaker.
It makes the learning process more disciplined.

The goal is not to stop the network from learning.
The goal is to stop it from learning the wrong thing too aggressively.
