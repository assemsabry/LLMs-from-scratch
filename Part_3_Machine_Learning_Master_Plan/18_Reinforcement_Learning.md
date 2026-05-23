# 18. Reinforcement Learning

Reinforcement Learning (RL) is how we teach models complex decision-making and alignment, rather than just simple prediction.

---

## 18.1 The RL Framework
*   **Agent:** The AI model taking actions.
*   **Environment:** The world the agent interacts with.
*   **Action:** A move the agent makes (e.g., generating a word, moving a chess piece).
*   **State:** The current situation.
*   **Reward:** A numerical score given after an action (+1 for good, -1 for bad).

## 18.2 Q-Learning
A foundational algorithm where the agent builds a "Q-Table"—a cheat sheet mapping every possible state to the best possible action based on expected future rewards.

## 18.3 Deep Reinforcement Learning
When the environment is too complex for a simple table (like a video game or a language model), a Neural Network replaces the table to approximate the best actions.

## 18.4 RLHF (Reinforcement Learning from Human Feedback)
The algorithm that created ChatGPT.
1.  Humans rank AI responses from best to worst.
2.  A separate "Reward Model" is trained to mimic the human rankings.
3.  The main LLM generates responses, the Reward Model scores them, and an RL algorithm (like **PPO - Proximal Policy Optimization**) updates the LLM to generate higher-scoring responses over time.
