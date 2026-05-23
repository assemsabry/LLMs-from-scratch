# 6. Neural Network Architectures

Neurons can be connected together in different structural patterns (Architectures) depending on the type of data being processed.

---

## 6.1 Feedforward Neural Network (FNN)
Also known as a Multi-Layer Perceptron (MLP).
*   **Structure:** A basic fully connected network. Every neuron in Layer 1 is connected to every neuron in Layer 2. Data moves only forward.
*   **Use Case:** Tabular data, basic classification.
*   **Drawback:** It treats all inputs independently. It has no concept of sequence, time, or spatial structure (like pixels next to each other).

## 6.2 Convolutional Neural Network (CNN)
The revolution in Computer Vision.
*   **Structure:** Instead of connecting to everything, neurons only look at small local "patches" of the input using a sliding window (Convolution). 
    *   **Convolution Layers:** Extract features (edges, textures).
    *   **Pooling Layers:** Compress the image, keeping only the most important features.
*   **Use Case:** Image classification, object detection, medical imaging.

## 6.3 Recurrent Neural Network (RNN)
Designed for sequential data (where the order of inputs matters).
*   **Structure:** It processes data sequentially and maintains an internal "hidden state" (memory) that is passed forward to the next step.
*   **Use Case:** Time series forecasting, early NLP tasks.
*   **Drawback:** The **Vanishing Gradient Problem**. During backpropagation through time, gradients shrink exponentially. Because of this, RNNs physically cannot remember information from long ago in a sequence.

## 6.4 LSTM / GRU
Variations designed to fix the RNN memory problem.
*   **LSTM (Long Short-Term Memory):** Introduces complex "Gates" (Forget, Input, Output gates) that allow the network to explicitly decide what information to keep in long-term memory and what to throw away.
*   **GRU (Gated Recurrent Unit):** A streamlined, slightly faster version of the LSTM with fewer gates.
*   **Use Case:** Advanced time-series, speech recognition.

## 6.5 Transformers (MOST IMPORTANT)
The architecture that took over the world and birthed the AI boom.
*   **Structure:** Abandons the sequential processing of RNNs completely. It processes all tokens in a sequence simultaneously. 
*   **Core Idea (Attention):** Uses the Self-Attention mechanism to allow every word in a sentence to look at every other word simultaneously to gather context.
    $$ Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V $$
*   **Use Case:** Large Language Models (LLMs), ChatGPT, Vision Transformers.
