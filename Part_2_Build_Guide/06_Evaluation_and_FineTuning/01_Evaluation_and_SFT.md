# Evaluation and Fine-Tuning

After pretraining, you have a "Base Model." A base model is not an assistant. If you prompt it with "What is the capital of France?", it might complete the text by generating "What is the capital of Germany?". It only knows how to predict the next word on the internet.

To turn a Base Model into an Assistant (like ChatGPT), you must perform Supervised Fine-Tuning (SFT) and Alignment.

---

## 13.1 Pre-Training Evaluation

Before fine-tuning, you must evaluate if the pretraining actually worked.
*   **Perplexity:** The primary mathematical metric. It measures how "surprised" the model is by real text. A lower perplexity means the model accurately predicts language.
*   **Zero-Shot Benchmarks:** You test the base model on standardized academic tests (like MMLU, GSM8K, or HumanEval). You do this to see if the model has naturally absorbed factual knowledge, math, and coding abilities during pretraining.

## 14.1 Supervised Fine-Tuning (SFT)

To teach the model to act as an assistant, you train it on a highly curated dataset of instructions and responses.

*   **The Dataset:** Instead of raw web text, the data is formatted carefully:
    `Prompt: Write a python script to reverse a string. Response: [Python Code]`
*   **The Process:** It is exactly the same as the pretraining loop (next-token prediction with Cross-Entropy Loss), but you ONLY calculate the loss on the *Response* portion. You do not punish the model for failing to predict the *Prompt*.
*   **Data Quality over Quantity:** Unlike pretraining which requires trillions of tokens, SFT requires only 10,000 to 100,000 extremely high-quality examples. A human should review every single SFT example.

## 14.2 Parameter-Efficient Fine-Tuning (PEFT) / LoRA

If you want to fine-tune a massive 7B parameter model, you usually need the same massive GPU cluster used for pretraining. This is too expensive.

**LoRA (Low-Rank Adaptation)** is the industry solution.
Instead of updating all 7 Billion parameters, you freeze the original base model entirely. You then inject tiny, mathematically simplified "adapter" matrices into the Transformer blocks. You only train these tiny adapters.
*   **Result:** You can fine-tune a 7B model on a single consumer GPU (like an RTX 3090) in a few hours, achieving 99% of the quality of full fine-tuning.

## 14.3 Alignment (RLHF / DPO)

Even after SFT, the model might give technically correct but dangerous or unhelpful answers. You must "align" it to human preferences.

*   **RLHF (Reinforcement Learning from Human Feedback):** You train a secondary "Reward Model" based on human ratings (e.g., Human A rated this response 5 stars, this one 1 star). You then use Reinforcement Learning (PPO algorithm) to update the LLM to maximize the Reward Model's score.
*   **DPO (Direct Preference Optimization):** The modern, simpler alternative to RLHF. Instead of building a complex Reward Model, you directly modify the Loss Function in the training loop. You feed the model pairs of responses (one Good, one Bad) and the math directly forces the model to increase the probability of the Good response and decrease the probability of the Bad response.
