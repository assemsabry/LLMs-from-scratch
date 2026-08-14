# 1. Key Terminology

A quick reference glossary for the most critical AI terminology.

---

*   **Token:** The fundamental unit of data processed by an LLM. It is not necessarily a full word; it can be a word fragment, a single character, or a piece of code.
*   **Parameter:** A trainable weight or bias inside the neural network. A "7B" model has 7 billion parameters, representing the mathematical connections between its neurons.
*   **Embedding:** A dense vector (a list of numbers) that represents the semantic meaning of a token or concept in a high-dimensional mathematical space.
*   **Attention:** The core mechanism of the Transformer architecture. It allows the model to look at every other word in a sentence and assign a "relevance score" to determine context.
*   **Layer:** A discrete block of mathematical transformations. Data enters the bottom layer, is transformed sequentially through dozens of hidden layers, and exits the top layer.
*   **Hidden State:** The intermediate mathematical representation of the data as it flows through the internal layers of the network.
*   **Logits:** The raw, unnormalized scores output by the final layer of the neural network before they are converted into probabilities (using a Softmax function).
*   **Inference:** The act of running a fully trained model to generate predictions or text. This is fundamentally different from *Training*, which is the act of modifying the model's weights.
*   **Epoch:** In training, one complete pass through the entire dataset.
*   **Batch Size:** The number of data samples the GPU processes simultaneously before pausing to update the model's weights.
*   **Context Window:** The maximum number of tokens the model can process at once.
*   **Tokenizer:** The algorithm that converts raw text into token IDs the model can process.
*   **Embedding:** The learned vector representation of a token inside the model.
*   **Perplexity:** A core language-modeling metric that measures how surprised a model is by real text. Lower is better.
*   **Cross-Entropy Loss:** The main loss used in GPT-style next-token prediction training.
*   **Fine-Tuning:** Additional training applied after pretraining to adapt a model to a desired behavior or domain.
*   **SFT (Supervised Fine-Tuning):** Fine-tuning on curated instruction and response pairs.
*   **RLHF:** Reinforcement Learning from Human Feedback. A method for aligning model behavior with human preferences.
*   **DPO:** Direct Preference Optimization. A simpler preference-optimization method often used instead of full RLHF pipelines.
*   **LoRA:** Low-Rank Adaptation. A parameter-efficient fine-tuning method that trains small adapter matrices instead of all model weights.
*   **Quantization:** Compressing model weights to lower precision, such as 8-bit or 4-bit, to improve deployment efficiency.
*   **KV Cache:** Stored attention keys and values reused during autoregressive generation to reduce repeated computation.
*   **RAG:** Retrieval-Augmented Generation. A system pattern that retrieves external documents and injects them into the prompt before answering.
*   **Agent:** An LLM-based system that can use tools and act across multiple steps to complete tasks.
*   **Inference Engine:** Optimized serving software such as vLLM or llama.cpp that runs the model efficiently for users.
