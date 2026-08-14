# 4. Types of Neural Networks

Different types of data require different structural configurations of layers and neurons.

---

## 4.1 Feedforward Neural Network (FNN)

*   **The Idea:** Data moves only forward. There is no memory of past inputs.
*   **Structure:**
    *   Input layer
    *   Hidden layers (fully connected)
    *   Output layer
*   **Usage:** Classification, Regression, Tabular data.

### Why FNNs matter

FNNs are the simplest deep learning architecture and the best place to understand:

- linear layers
- activations
- forward passes
- backpropagation

They are still useful today for:

- tabular problems
- embeddings plus MLP heads
- smaller structured tasks

### PyTorch Code
```python
import torch
import torch.nn as nn

class FNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(10, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )

    def forward(self, x):
        return self.model(x)
```

## 4.2 Convolutional Neural Network (CNN)

*   **The Idea:** Designed to extract features from images.
*   **Structure:**
    *   Convolution Layer
    *   Activation (ReLU)
    *   Pooling Layer
    *   Fully Connected Layer
*   **The Math (Convolution):**
    $$(I * K)(i,j) = \sum_{m}\sum_{n} I(i+m, j+n)K(m,n)$$
*   **Usage:** Image classification, Object detection, Computer vision.

### Why CNNs were so important

CNNs solved a major problem in vision:

- images are high-dimensional
- nearby pixels matter more than distant ones
- repeating patterns appear in many locations

By using local filters and weight sharing, CNNs became both powerful and efficient.

### PyTorch Code
```python
class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(16, 32, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.fc = nn.Sequential(
            nn.Linear(32*6*6, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)
```

## 4.3 Recurrent Neural Network (RNN)

*   **The Idea:** Designed to handle sequential data by maintaining an internal memory.
*   **The Math:**
    $$h_t = \tanh(W_h h_{t-1} + W_x x_t)$$
*   **Usage:** NLP, Time series, Speech processing.
*   **The Problem:** Suffers heavily from the vanishing gradient problem.

### Why RNNs still matter conceptually

Even though transformers replaced RNNs in many language tasks, RNNs are still important to study because they teach:

- sequential state updates
- temporal dependence
- why long-range memory is difficult

Understanding their limitations helps you appreciate why transformers were such a breakthrough.

### PyTorch Code
```python
class RNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.rnn = nn.RNN(input_size=10, hidden_size=20, batch_first=True)
        self.fc = nn.Linear(20, 1)

    def forward(self, x):
        out, _ = self.rnn(x)
        return self.fc(out[:, -1, :])
```

## 4.4 LSTM (Long Short-Term Memory)

*   **The Idea:** An improvement over standard RNNs designed specifically to preserve long-term memory and solve the vanishing gradient problem.
*   **Usage:** NLP, Speech, Forecasting.

### Why LSTMs mattered historically

Before transformers, LSTMs were one of the main solutions for real sequential learning.
They remain useful in:

- smaller sequence problems
- constrained real-time systems
- educational understanding of gated memory

### PyTorch Code
```python
class LSTMModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(input_size=10, hidden_size=64, batch_first=True)
        self.fc = nn.Linear(64, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])
```

## 4.5 GRU (Gated Recurrent Unit)

*   **The Idea:** A lighter, faster version of the LSTM that performs similarly but uses fewer parameters.
*   **Usage:** NLP, Real-time systems.

### GRU intuition

GRUs keep much of the practical benefit of LSTMs while simplifying the gating structure.
They are often chosen when you want a strong recurrent baseline without maximum complexity.

## 4.6 Transformer Networks

*   **The Core Idea:** Relies entirely on the Attention mechanism instead of recurrence (RNNs).
*   **The Most Important Equation:**
    $$Attention(Q,K,V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
*   **Usage:** Large Language Models (LLMs), ChatGPT-style models, Vision Transformers.

### Why transformers dominate now

Transformers became dominant because they combine:

- parallel training
- strong long-range context handling
- scalability
- flexibility across text, code, images, audio, and video

## 4.7 Final Comparison

The key lesson is not that one architecture is always best.

It is that architectures are responses to data structure:

- FNNs for fixed feature vectors
- CNNs for spatial patterns
- RNNs and LSTMs for temporal sequence state
- Transformers for scalable context modeling

### PyTorch Code (Abbreviated)
```python
class SimpleTransformer(nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = nn.MultiheadAttention(embed_dim=64, num_heads=4)
        self.fc = nn.Linear(64, 1)

    def forward(self, x):
        x, _ = self.attn(x, x, x)
        return self.fc(x.mean(dim=0))
```
