# Tokenization: Types and Concepts

Before a neural network can process text, the text must be translated into numbers. A neural network cannot read the string "Hello". It only understands mathematical vectors. 

Tokenization is the bridge between human language and machine computation. It is the process of breaking down a sequence of text into smaller, discrete units called "tokens", and mapping those tokens to integer IDs.

This sounds simple, but tokenization is one of the most underappreciated design choices in LLM engineering.

---

## 1. Types of Tokenization

There are three primary approaches to breaking down text.

### Word-Level Tokenization
This is the most intuitive approach: split the sentence by spaces and punctuation.
*   **Example:** "I am playing." -> `["I", "am", "playing", "."]`
*   **The Problem:** The vocabulary size explodes. You need a unique ID for "play", "plays", "played", "playing", "player", and every single misspelling of those words. If the model encounters a word not in its vocabulary (Out-Of-Vocabulary or OOV), it fails, usually defaulting to a generic `[UNK]` (Unknown) token.

### Character-Level Tokenization
Break the text down into individual letters and symbols.
*   **Example:** "Play" -> `["P", "l", "a", "y"]`
*   **The Problem:** The vocabulary is tiny (just the alphabet and some symbols, maybe 100-200 tokens total), which is great. However, individual characters hold very little semantic meaning. Furthermore, this drastically increases the sequence length. A 10-word sentence might become a 60-token sequence, making it incredibly expensive for a Transformer to process due to the quadratic scaling of Attention.

### Subword Tokenization (The Standard)
Subword tokenization strikes the perfect balance. Frequent words are kept as whole words, while rare words or misspellings are broken down into smaller, meaningful chunks.
*   **Example:** "playing" -> `["play", "##ing"]`
*   **Why it wins:** It keeps the vocabulary size manageable (usually 30,000 to 100,000 tokens) while never encountering an Out-Of-Vocabulary word, because in the absolute worst-case scenario, it can fall back to spelling a weird word character-by-character.

### Why subwords dominate modern LLMs

Subwords are the practical compromise between:

- huge vocabularies
- tiny character sets
- short sequence lengths
- good generalization to unseen text

They are one of the reasons transformer models can handle:

- normal prose
- code
- domain jargon
- rare names
- multilingual inputs

without requiring impossible vocabulary sizes.

## 2. Dominant Subword Algorithms

Almost all modern LLMs use one of these three statistical subword algorithms:

*   **BPE (Byte Pair Encoding):** Used by GPT-2, GPT-3, GPT-4, and LLaMA. It starts with a base vocabulary of individual characters. It then scans the training data, finds the most frequently adjacent pair of characters (e.g., "e" and "r" -> "er"), and merges them into a new single token. It repeats this merging process thousands of times until it reaches the desired vocabulary size.
*   **WordPiece:** Used primarily by Google's BERT. Similar to BPE, but instead of merging the most frequent pairs, it merges pairs that maximize the likelihood of the training data based on a language model.
*   **SentencePiece:** Unlike BPE and WordPiece, which usually require pre-tokenizing by spaces first, SentencePiece treats the entire input (including spaces) as a raw stream of characters. This is incredibly important for languages that do not use spaces to separate words, like Chinese or Japanese.

### Practical difference between BPE and SentencePiece

For many learners, BPE and SentencePiece can feel interchangeable.
They are related, but the engineering implications matter.

- **BPE-style systems** are common in GPT-style ecosystems.
- **SentencePiece** is often easier to use in multilingual settings or when raw-text handling matters.

This is one reason SentencePiece became popular for training custom tokenizers from scratch.

## 3. Important Concepts

When designing or choosing a tokenizer for a new LLM, several metrics matter:

*   **Vocabulary Size:** The total number of unique tokens the model knows. GPT-2 had a vocabulary of 50,257. GPT-4 has a vocabulary of around 100,000. LLaMA 3 increased its vocabulary to 128,000. A larger vocabulary means the model can represent complex words in fewer tokens, but it also increases the size of the embedding matrix, requiring more memory.
*   **Compression Ratio:** A measure of efficiency. How many raw characters are represented by a single token on average? A highly efficient tokenizer for English might achieve ~4 characters per token (meaning a 100-token limit allows for ~400 characters of text). If a tokenizer is poorly trained for a specific language (e.g., Arabic in early GPT models), it might fall back to character-level tokenization, drastically reducing the effective context window for that language.
*   **Token Distribution:** Ensuring that the tokenizer represents numbers, code symbols, and whitespace efficiently. For example, if a tokenizer splits the number "10500" into `["10", "500"]` it might struggle with mathematical reasoning compared to a tokenizer that splits every digit individually `["1", "0", "5", "0", "0"]`.

## 4. Why Tokenization Affects Cost

Tokenization directly changes how expensive your system is.

If your tokenizer is inefficient, the same document may require:

- more tokens
- more attention computation
- more memory
- more inference time
- more API cost

This means a better tokenizer can improve:

- quality
- speed
- cost

all at once.

## 5. Why Tokenization Affects Quality

A tokenizer does not understand meaning by itself, but it strongly shapes what the model can learn efficiently.

Bad tokenization can hurt:

- rare-word understanding
- code quality
- number handling
- multilingual performance
- domain adaptation

For example, if medical terms or cybersecurity terms are split in awkward ways, the model has to work harder to learn them.

## 6. Languages, Scripts, and Domain-Specific Data

One tokenizer does not serve all data equally well.

Important differences show up across:

- English vs Arabic
- prose vs code
- math-heavy text
- social-media text
- biomedical or legal terminology

This is why many modern model builders think carefully about:

- multilingual coverage
- code efficiency
- digit handling
- whitespace behavior
- Unicode normalization

## 7. What Learners Should Test When Training a Tokenizer

Do not judge a tokenizer only by vocabulary size.

You should test:

1. How many tokens common sentences require
2. How well it handles code
3. How it splits numbers
4. How it handles your target language
5. How it behaves on domain-specific terms
6. Whether important repeated phrases become efficient tokens

## 8. Final Takeaway

Tokenization is not a boring preprocessing step.

It is part of the model's interface to the world.

A strong tokenizer helps the model see text in a more efficient, learnable, and affordable way.
