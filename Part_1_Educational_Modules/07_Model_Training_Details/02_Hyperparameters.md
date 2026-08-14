# Model Training Details: Hyperparameters

Parameters (weights and biases) are learned by the model during training. **Hyperparameters** are the settings that *you* (the engineer) configure before training begins. They dictate the architecture of the model and the rules of the training process. Tuning these correctly is the difference between a model that learns perfectly and a model that completely fails.

The key idea is that hyperparameters are not random knobs.
They encode your assumptions about how the model should learn.

---

## 1. Training Hyperparameters

These settings control the optimization process itself.

### Learning Rate (LR)
*   **What it is:** The multiplier used to control how much the weights are updated during backpropagation.
*   **Impact:** As discussed in the Optimizers section, this is the most critical hyperparameter. Too high, and the model diverges. Too low, and it learns too slowly.
*   **Typical Values:** Usually between `1e-3` (0.001) and `1e-5` (0.00001) for LLMs, often using a Warmup + Cosine Decay schedule.

### Why LR is the most dangerous hyperparameter

If you choose the wrong learning rate, even a good architecture and a good dataset may fail.

This is why experienced engineers treat LR tuning as a first-class priority.

### Batch Size
*   **What it is:** The number of training examples processed together in one forward/backward pass.
*   **Impact:** A larger batch size provides a more accurate estimate of the gradient, leading to smoother and faster convergence, but it requires significantly more GPU VRAM. A smaller batch size introduces noise into the training process (which can sometimes act as a regularizer) but takes longer.
*   **Typical Values:** Ranges from 16 to thousands in massive distributed setups.

### Effective batch size

In large-scale training, the true batch behavior often depends on:

- per-device micro-batch size
- number of devices
- gradient accumulation steps

So the batch size you think you are using may not be the whole story.

### Epochs
*   **What it is:** The number of times the model sees the entire dataset.
*   **Impact:** Training for too many epochs leads to overfitting (the model memorizes the data). Training for too few leads to underfitting.
*   **In LLM Pretraining:** Because pretraining datasets are so unimaginably large (trillions of tokens), modern LLMs are often trained for exactly **1 Epoch**. They never see the same piece of text twice.

### Tokens vs epochs

In LLM work, engineers often think in terms of:

- total tokens seen

more than:

- classic small-dataset epoch counts

This is a better mental model for large-scale language training.

## 2. Architectural Hyperparameters

These settings define the physical size and structure of the Neural Network.

### Sequence Length (Context Window)
*   **What it is:** The maximum number of tokens the model can process at once.
*   **Impact:** Determines how much context the model can remember. Increasing sequence length drastically increases memory usage due to the `O(N^2)` scaling of attention.

### Hidden Size (Embedding Dimension)
*   **What it is:** The size of the vector used to represent each token inside the model. 
*   **Impact:** A larger hidden size allows the model to learn more complex semantic representations, but drastically increases the number of parameters. (e.g., GPT-3 uses a hidden size of 12,288).

### Number of Layers (Depth)
*   **What it is:** The number of Transformer blocks stacked on top of each other.
*   **Impact:** Deeper networks can learn more abstract, hierarchical features. However, they are harder to train due to vanishing gradients and require much more compute. (e.g., GPT-3 has 96 layers).

### Number of Attention Heads
*   **What it is:** How many parallel self-attention mechanisms operate within a single layer.
*   **Impact:** Allows the model to focus on different aspects of the text simultaneously (grammar, sentiment, subject).

## 3. Architectural Ratios Matter

It is not only the individual hyperparameters that matter.
The ratios between them matter too.

For example:

- hidden size relative to head count
- FFN expansion relative to hidden size
- depth relative to width
- context length relative to available memory

Good model design is about coherent combinations, not isolated values.

## 4. Regularization Hyperparameters

These settings intentionally introduce constraints to prevent the model from overfitting.

### Dropout
*   **What it is:** During training, randomly selected neurons are completely turned off (their output is set to 0) with a certain probability (e.g., `p=0.1`). 
*   **Impact:** This prevents neurons from co-adapting too heavily to each other and forces the network to learn robust, redundant features. It is heavily used in standard neural networks but is sometimes omitted in modern, massive LLM pretraining because the massive dataset itself acts as a regularizer.

### Weight Decay
*   **What it is:** (L2 Regularization) Adds a penalty to the loss function based on the size of the weights, encouraging the model to keep weights small and distributed.
*   **Impact:** Improves generalization to unseen data. It is a key component of the AdamW optimizer.

## 5. Hyperparameter Tuning Strategy

A strong tuning strategy is usually:

1. get a small run working
2. verify loss decreases
3. tune learning rate first
4. then tune batch size and schedule
5. only then scale model or context more aggressively

### Common beginner mistake

Many learners change too many hyperparameters at once.

That makes debugging impossible.

## 6. What Learners Should Record

For every serious run, log:

- learning rate
- batch size
- sequence length
- hidden size
- layers
- heads
- dropout
- weight decay
- optimizer
- scheduler

If you do not record your settings, you cannot learn from your own experiments.
