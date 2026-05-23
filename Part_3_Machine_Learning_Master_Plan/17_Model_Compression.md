# 17. Model Compression

Once a model is trained, it is often too large to run on edge devices, phones, or cheap servers. Compression makes inference fast and cheap.

---

## 17.1 Quantization
The most important compression technique.
*   **The Concept:** Neural network weights are normally stored as high-precision 32-bit floats. Quantization converts them down to 16-bit, 8-bit, or even 4-bit integers.
*   **The Result:** A model shrinks to 1/4th of its size and runs much faster, with minimal loss in "smartness". Methods like GGUF and AWQ dominate this space.

## 17.2 Pruning
*   **The Concept:** After training, you mathematically analyze the network to find weights that are very close to zero or neurons that rarely fire. You permanently delete them.
*   **The Result:** A physically smaller, sparser network that processes data faster.

## 17.3 Knowledge Distillation
*   **The Concept:** You use a massive, slow, expensive "Teacher" model (like GPT-4) to generate high-quality data. You then train a tiny, fast "Student" model (like an 8B parameter model) to mimic the Teacher.
*   **The Result:** The student model cannot do everything the teacher can, but it becomes exceptionally good at specific tasks while remaining tiny and fast.
