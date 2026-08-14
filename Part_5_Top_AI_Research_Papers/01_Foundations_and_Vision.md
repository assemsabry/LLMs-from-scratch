# Top AI Research Papers (Part 1 / 50)

This is the first segment of the Top 50 AI Research Papers Roadmap, covering papers 1 through 20. It spans the core foundations of modern deep learning, the computer vision revolution, and the inception of generative AI.

---

## 1. Attention Is All You Need (2017)
*   **Link:** [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)
*   **Overview:** The paper that introduced the Transformer architecture and changed the direction of modern AI.
*   **Key Ideas:**
    *   self-attention
    *   multi-head attention
    *   positional encoding
*   **Impact:** Foundation of GPT, BERT, LLaMA, Claude, and Gemini.

## 2. Deep Residual Learning (ResNet) (2015)
*   **Link:** [https://arxiv.org/abs/1512.03385](https://arxiv.org/abs/1512.03385)
*   **Overview:** Introduced residual connections.
*   **Key Math:** `y = F(x) + x`
*   **Why Important:** Enabled training of much deeper neural networks.

## 3. ImageNet Classification with Deep CNN (AlexNet) (2012)
*   **Link:** [https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html)
*   **Overview:** The first major deep learning breakthrough in vision.
*   **Key Ideas:**
    *   ReLU activation
    *   GPU training
    *   data augmentation

## 4. BERT (2018)
*   **Link:** [https://arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805)
*   **Overview:** Introduced bidirectional transformer pretraining.
*   **Key Innovation:** Masked Language Modeling.
*   **Impact:** Revolutionized NLP understanding tasks.

## 5. GPT (Generative Pretrained Transformer) (2018)
*   **Link:** [https://openai.com/research/language-unsupervised](https://openai.com/research/language-unsupervised)
*   **Overview:** Early foundation of modern generative AI.
*   **Introduced:** Unsupervised pretraining plus fine-tuning.
*   **Impact:** Became the base pattern for future GPT models.

## 6. GPT-2 (2019)
*   **Link:** [https://openai.com/research/better-language-models](https://openai.com/research/better-language-models)
*   **Overview:** Demonstrated the raw power of scaling language models.
*   **Showed:**
    *   scaling improves performance dramatically
    *   zero-shot behavior can emerge from scale

## 7. GPT-3 (2020)
*   **Link:** [https://arxiv.org/abs/2005.14165](https://arxiv.org/abs/2005.14165)
*   **Overview:** Pushed language model scale to 175B parameters.
*   **Key Concept:** Few-shot learning.
*   **Insight:** Scale can unlock broad general capabilities.

## 8. Adam Optimizer (2014)
*   **Link:** [https://arxiv.org/abs/1412.6980](https://arxiv.org/abs/1412.6980)
*   **Overview:** One of the most widely used optimizers in deep learning.
*   **Contribution:** Adaptive learning rates per parameter.

## 9. Batch Normalization (2015)
*   **Link:** [https://arxiv.org/abs/1502.03167](https://arxiv.org/abs/1502.03167)
*   **Solved:** Training instability and difficult optimization in deep networks.
*   **Result:** Faster training and often better accuracy.

## 10. Dropout (2014)
*   **Link:** [https://www.jmlr.org/papers/v15/srivastava14a.html](https://www.jmlr.org/papers/v15/srivastava14a.html)
*   **Overview:** Prevents overfitting by randomly dropping neurons during training.

## 11. U-Net (2015)
*   **Link:** [https://arxiv.org/abs/1505.04597](https://arxiv.org/abs/1505.04597)
*   **Architecture:** Encoder-decoder with skip connections.
*   **Used In:** Medical imaging and image segmentation.

## 12. GANs (Generative Adversarial Networks) (2014)
*   **Link:** [https://arxiv.org/abs/1406.2661](https://arxiv.org/abs/1406.2661)
*   **Overview:** Two networks competing against each other: generator vs discriminator.
*   **Importance:** One of the key early breakthroughs in deep generative modeling.

## 13. Variational Autoencoders (VAE) (2013)
*   **Link:** [https://arxiv.org/abs/1312.6114](https://arxiv.org/abs/1312.6114)
*   **Overview:** Generative probabilistic model.
*   **Key Idea:** Learn a structured latent space distribution.

## 14. Word2Vec (2013)
*   **Link:** [https://arxiv.org/abs/1301.3781](https://arxiv.org/abs/1301.3781)
*   **Overview:** Introduced practical word embeddings.
*   **Famous Example:** `king - man + woman ~= queen`

## 15. Seq2Seq Models (2014)
*   **Link:** [https://arxiv.org/abs/1409.3215](https://arxiv.org/abs/1409.3215)
*   **Architecture:** Encoder to decoder
*   **Used For:** Translation and text generation.

## 16. Transformer-XL (2019)
*   **Link:** [https://arxiv.org/abs/1901.02860](https://arxiv.org/abs/1901.02860)
*   **Key Idea:** Recurrence inside transformer-style modeling.
*   **Improves:** Long-context memory.

## 17. Vision Transformer (ViT) (2020)
*   **Link:** [https://arxiv.org/abs/2010.11929](https://arxiv.org/abs/2010.11929)
*   **Overview:** Applied transformers to image understanding.
*   **Key Idea:** Split images into patches, then process like tokens.

## 18. CLIP (2021)
*   **Link:** [https://arxiv.org/abs/2103.00020](https://arxiv.org/abs/2103.00020)
*   **Connects:** Text and images.
*   **Used In:** DALL-E-style systems and image retrieval.

## 19. Diffusion Models (DDPM) (2020)
*   **Link:** [https://arxiv.org/abs/2006.11239](https://arxiv.org/abs/2006.11239)
*   **Overview:** One of the core modern image generation methods.
*   **Idea:** Learn to reverse a noise process.

## 20. Score-Based Generative Models (2021)
*   **Link:** [https://arxiv.org/abs/2011.13456](https://arxiv.org/abs/2011.13456)
*   **Overview:** Alternative diffusion-style formulation using score matching.

---

## Why This Part Matters

This part covers the foundational papers that made later LLM, multimodal, and generative systems possible.

Without understanding these ideas, later papers on alignment, scaling, and agents feel disconnected.

## Summary of Part 1

This part covered the bedrock of the modern AI revolution:
*   **Core Foundations:** CNNs, optimization, and regularization
*   **NLP Revolution:** Word2Vec, Seq2Seq, the Transformer, BERT, and the GPT series
*   **Generative AI:** GANs, VAEs, and diffusion models
*   **Modern AI Core:** Vision models like CLIP and ViT
