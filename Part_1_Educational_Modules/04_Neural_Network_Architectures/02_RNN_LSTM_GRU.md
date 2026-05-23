# Neural Network Architectures: RNN, LSTM, and GRU

While Convolutional Neural Networks (CNNs) excel at processing spatial data like images, they struggle with data where the **order** of inputs matters. 

Consider a sentence: "I grew up in France, so I speak fluent ___". To predict the word "French," a network must remember the word "France" that appeared earlier in the sequence. Standard FNNs and CNNs have no memory of previous inputs.

---

## 1. Recurrent Neural Networks (RNN)

Recurrent Neural Networks (RNNs) were the first major architecture designed specifically for sequential data (text, time series, audio).

*   **The Concept of "Memory":** Unlike a standard feedforward network where data goes strictly from input to output, an RNN has loops. The output of the hidden layer at time step `t` is fed back into the network as an input alongside the new data for time step `t+1`.
*   **Hidden State:** This looping mechanism creates an internal "Hidden State." The hidden state acts as the network's memory, capturing information about what has been calculated so far.
*   **The Mathematics:** At each time step, the new hidden state is calculated using the current input and the previous hidden state: 
    `h_new = f(W_input * x_current + W_hidden * h_previous + bias)`
*   **Use Cases:** Text generation, speech recognition, stock market prediction.

### The Problem: Vanishing Gradients

While mathematically elegant, standard RNNs failed in practice on long sequences. If the sequence is 100 words long, the network must perform backpropagation through 100 time steps. Because the gradients are repeatedly multiplied by the same weight matrices, they tend to exponentially shrink toward zero (Vanishing Gradients) or explode toward infinity (Exploding Gradients). 

When gradients vanish, the network stops learning. As a result, standard RNNs have very "short-term memory" and completely forget information from the beginning of a long sentence.

## 2. Long Short-Term Memory (LSTM)

To solve the vanishing gradient problem and allow networks to remember long-term dependencies, LSTMs were invented in 1997. They remained the undisputed king of NLP (Natural Language Processing) until the invention of the Transformer in 2017.

### The Memory Cell
Instead of a simple hidden state, LSTMs introduce a complex "Cell State" that acts like a conveyor belt running straight down the entire chain. Information can flow along it relatively unchanged, solving the vanishing gradient problem.

### The Gates
LSTMs control what information gets added to or removed from this conveyor belt using complex mathematical structures called "Gates." Each gate contains a Sigmoid neural network layer (which outputs values between 0 and 1, acting as a valve) and a pointwise multiplication operation.

1.  **Forget Gate:** Decides what information we should throw away from the previous cell state. (e.g., If the subject changes from singular to plural, forget the singular conjugation rules).
2.  **Input Gate:** Decides what new information from the current input we should store in the cell state.
3.  **Output Gate:** Decides what parts of the cell state we should output as the new hidden state for the next step.

Because of this gating mechanism, LSTMs can maintain memory over thousands of time steps.

## 3. Gated Recurrent Units (GRU)

The GRU is a slightly newer (2014) and simplified variation of the LSTM.

*   **Simplification:** GRUs combine the Forget and Input gates into a single "Update Gate." They also merge the cell state and hidden state into one single vector.
*   **Performance:** Because they have fewer gates and parameters, GRUs are mathematically simpler and computationally faster to train than LSTMs. 
*   **Trade-off:** LSTMs are generally strictly more powerful and capable of remembering slightly longer sequences, but on many tasks, GRUs achieve nearly identical performance in less time. 

### Why did we move past LSTMs?
Despite their brilliance, LSTMs and GRUs have a fatal flaw for the modern era: **Sequential Processing**. You must process word 1 before word 2, and word 2 before word 3. This means they cannot be easily parallelized on modern GPUs. This bottleneck prevented them from being scaled up to the massive sizes of modern LLMs, paving the way for the Transformer.
