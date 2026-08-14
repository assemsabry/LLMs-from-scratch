# 16. Parameter-Efficient Fine-Tuning (PEFT)

Full fine-tuning updates every parameter in the model.
For large language models, that quickly becomes expensive in memory, compute, and storage.

Parameter-Efficient Fine-Tuning, usually called PEFT, solves this by updating only a small subset of trainable components while leaving the main pretrained model mostly or fully frozen.

This is one of the most important ideas in practical modern LLM engineering.

---

## 16.1 Why PEFT Matters

Without PEFT, adapting large models becomes difficult because you may need:

- large GPU memory
- expensive optimizer states
- full checkpoint storage for each task version
- long training cycles

PEFT reduces those costs dramatically.

Benefits include:

- cheaper adaptation
- faster experiments
- easier multi-task specialization
- smaller artifacts to store and share

---

## 16.2 LoRA

LoRA stands for Low-Rank Adaptation.
It is one of the most widely used PEFT methods.

### Core idea

Instead of updating a huge weight matrix directly, LoRA adds a small trainable low-rank update to that matrix.

In practice:

- the base model weights are frozen
- small additional matrices are inserted into selected layers
- only those small matrices are trained

This means you get task adaptation without paying the full cost of retraining the entire model.

### Why it works

Many useful task-specific updates can be represented as a low-rank change rather than a full dense rewrite of all parameters.

This makes LoRA surprisingly powerful relative to its small footprint.

---

## 16.3 QLoRA

QLoRA extends LoRA by combining it with quantization.

### Main idea

- keep the frozen base model in low precision, often 4-bit
- train LoRA adapters in higher precision

This lowers memory usage even further and makes fine-tuning large models possible on much cheaper hardware than full fine-tuning would require.

QLoRA became especially important because it made serious LLM adaptation accessible to smaller teams and individual builders.

---

## 16.4 Adapters

Adapters are another PEFT approach.
Instead of low-rank updates inside existing layers, they insert small trainable modules between parts of the network.

The base model remains frozen while the adapter layers learn task-specific behavior.

Advantages:

- modularity
- easy task swapping
- smaller training footprint than full fine-tuning

Tradeoff:

- some approaches can add more runtime overhead than LoRA-style methods

---

## 16.5 Prefix Tuning and Prompt Tuning

These approaches train continuous task-specific vectors instead of changing most model weights.

### Prefix tuning

Prefix tuning adds trainable virtual tokens or key-value style prefixes that guide the model's behavior across layers.

### Prompt tuning

Prompt tuning learns a soft prompt representation that steers the model toward a task without modifying the core model heavily.

These methods are lightweight, but their effectiveness can vary more by task and model scale.

---

## 16.6 When To Use PEFT

PEFT is especially useful when:

- you want to specialize a foundation model cheaply
- you need many domain variants of the same base model
- you have limited hardware
- you want to preserve the base model while testing many task heads

Examples:

- medical assistant variant
- legal summarization variant
- Arabic instruction-tuned variant
- support chatbot variant

---

## 16.7 PEFT vs Full Fine-Tuning

### Full fine-tuning

- maximum flexibility
- highest compute and storage cost
- useful when the task shift is very large

### PEFT

- much cheaper
- easier to iterate
- often enough for many practical use cases

For many real-world teams, PEFT is the default starting point and full fine-tuning is only used if PEFT clearly underperforms.

---

## 16.8 Practical Mental Model

Think of the pretrained model as a large library of capabilities.
PEFT does not rebuild the library.
It learns a compact way to access and redirect those capabilities for a specific job.

That is why PEFT is one of the key reasons modern LLM development became much more accessible.
