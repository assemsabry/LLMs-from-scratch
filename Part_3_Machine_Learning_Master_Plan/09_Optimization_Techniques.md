# 9. Optimization Techniques

Even a strong model architecture can fail if optimization is unstable.
Optimization techniques are the practical tools that keep training numerically healthy and make learning efficient.

This is where many real training runs succeed or collapse.

---

## 9.1 Why Optimization Matters

During training, the optimizer repeatedly changes millions or billions of parameters.
If those updates are poorly controlled, you may get:

- divergence
- exploding gradients
- vanishing learning progress
- NaN losses
- unstable validation behavior

Optimization techniques exist to prevent those outcomes and improve convergence.

---

## 9.2 Gradient Clipping

Sometimes a batch produces extremely large gradients.
If the optimizer applies them directly, the parameter update can be destructive.

Gradient clipping limits the size of the gradient vector before the optimizer step.

### Why it helps

- prevents catastrophic updates
- stabilizes difficult training runs
- is especially useful in recurrent or large-scale training setups

Gradient clipping does not fix every training issue, but it often prevents one bad batch from ruining the run.

---

## 9.3 Learning Rate Schedules

The learning rate is one of the most important hyperparameters in deep learning.

If it is too high:

- training becomes unstable

If it is too low:

- learning becomes painfully slow
- the model may get stuck in weak solutions

So modern training usually uses a schedule instead of a single fixed value.

### Warmup

Warmup starts the learning rate very low and increases it gradually over the first training steps.

Why this matters:

- early model weights are random
- large updates at the beginning can destabilize training

Warmup gives the optimizer time to enter a healthier region of parameter space.

### Decay schedules

After warmup, the learning rate is often reduced over time.
Common approaches include:

- cosine decay
- linear decay
- step decay

This allows:

- larger exploratory updates early
- smaller refinements later

---

## 9.4 Momentum and Adaptive Optimizers

Optimization is not only about the learning rate.
It is also about how gradients are accumulated and interpreted over time.

### Momentum

Momentum helps updates move consistently in useful directions instead of reacting too aggressively to noisy local fluctuations.

### Adam and AdamW

Adaptive optimizers such as Adam estimate per-parameter update scales.
AdamW improves on Adam by handling weight decay more cleanly.

These optimizers became standard in many transformer and LLM training setups because they are robust and practical.

---

## 9.5 Normalization Layers

Normalization methods help keep activations in stable numeric ranges.

Examples:

- batch normalization
- layer normalization
- RMSNorm

In modern transformers, layer normalization and RMSNorm are more common than batch normalization.

These methods help optimization by making the internal signal flow more stable across deep networks.

---

## 9.6 Mixed Precision and Numerical Stability

Modern training often uses lower precision arithmetic to reduce memory and increase throughput.

Examples:

- FP16
- BF16

This speeds up training, but it also introduces numeric concerns.
So large-scale systems often use:

- loss scaling
- precision-aware kernels
- gradient checks

Optimization and systems engineering become tightly connected here.

---

## 9.7 Monitoring During Optimization

You should not treat training as a black box.

Useful signals to monitor include:

- gradient norm
- learning rate
- training loss
- validation loss
- activation statistics
- optimizer step stability

Monitoring helps distinguish:

- bad data
- bad hyperparameters
- true model limitations

---

## 9.8 Practical Mental Model

Optimization is controlled learning.

The model is not just changing.
It is being guided through a very large error landscape.

Good optimization techniques make those steps:

- stable
- efficient
- recoverable

That is why optimization is often the difference between a model that should work in theory and a model that actually trains in practice.
