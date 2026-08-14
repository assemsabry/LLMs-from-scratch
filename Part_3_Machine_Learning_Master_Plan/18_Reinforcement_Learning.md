# 18. Reinforcement Learning

Reinforcement Learning (RL) is the framework used when an AI system must learn through interaction, rewards, and long-term consequences rather than only direct labeled supervision.

---

## 18.1 The RL Framework

The standard RL setup has several core parts:

*   **Agent:** The AI system taking actions
*   **Environment:** The world or simulator the agent interacts with
*   **Action:** A move the agent makes
*   **State:** The current situation the agent observes
*   **Reward:** A numerical signal indicating how good or bad the action was

### Why RL is different

In supervised learning, the correct answer is usually given directly.

In RL, the system often has to discover good behavior indirectly by maximizing cumulative reward over time.

That makes RL harder because:

- rewards may be delayed
- actions may affect future states
- exploration matters

## 18.2 Q-Learning

Q-Learning is a foundational RL algorithm.

The idea is to estimate:

- how good a specific action is in a specific state

This is stored in a value often called `Q(state, action)`.

In simple environments, the agent can build a Q-table that acts like a cheat sheet for choosing high-value actions.

### Why it matters

Q-Learning gives learners a concrete way to understand RL before moving to neural-network-based methods.

## 18.3 Deep Reinforcement Learning

When the environment becomes too large or complex for a table, a neural network is used to approximate the value or policy.

This leads to Deep Reinforcement Learning.

Examples include:

- game-playing systems
- robotic control
- policy learning in high-dimensional spaces

### Why deep RL is difficult

It combines the instability of RL with the instability of deep learning.

That means engineers must deal with:

- noisy rewards
- unstable optimization
- exploration problems
- sample inefficiency

## 18.4 RLHF (Reinforcement Learning from Human Feedback)

One of the most important modern uses of RL in language models is RLHF.

The simplified pipeline is:

1. humans rank model responses from better to worse
2. a reward model is trained to imitate those preferences
3. the main LLM is updated to produce responses that score higher under that reward model

### Why RLHF matters

RLHF helped transform raw language models into more useful assistants by teaching:

- helpfulness
- safer behavior
- better instruction following
- more aligned response style

## 18.5 Modern Note

By August 13, 2026, many AI systems still draw on RL ideas, but practical alignment pipelines often also use:

- DPO
- preference optimization
- policy tuning
- tool-use evaluation

So RL remains important, but it is now part of a broader alignment and systems toolkit.

## 18.6 Final Takeaway

Reinforcement Learning is the framework you use when success depends on sequences of actions and long-term consequences.

It is especially important for:

- robotics
- games
- control systems
- alignment
- agentic AI
