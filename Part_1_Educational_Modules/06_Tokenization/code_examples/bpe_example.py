from transformers import GPT2Tokenizer

def demonstrate_bpe():
    """
    Demonstrates how Byte Pair Encoding (BPE) works in practice
    using the pre-trained GPT-2 tokenizer.
    
    Prerequisites: pip install transformers
    """
    print("--- Tokenization Example: BPE ---")
    
    # Load the standard GPT-2 tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    
    # Example 1: Standard words vs. Subwords
    # "playing" is a common word, but how does the tokenizer see it?
    # Let's try a made up word: "unbelievablyfast"
    text = "The player is playing unbelievablyfast."
    
    print(f"\nOriginal Text: '{text}'")
    
    # Tokenize the text (convert strings to token IDs)
    token_ids = tokenizer.encode(text)
    print(f"Token IDs: {token_ids}")
    
    # Let's see exactly how the text was split into subwords
    # We decode each ID back to text individually
    tokens = [tokenizer.decode([token_id]) for token_id in token_ids]
    
    print("\nHow BPE split the sentence:")
    for i, token in enumerate(tokens):
        print(f"Token {i}: '{token}' (ID: {token_ids[i]})")
        
    # Notice how "unbelievablyfast" is broken down into known subword chunks.
    # The tokenizer might break it into something like ["un", "believ", "ably", "fast"]
    
    # Example 2: Vocabulary Size
    vocab_size = tokenizer.vocab_size
    print(f"\nTotal Vocabulary Size of GPT-2: {vocab_size} tokens")
    
    # Example 3: Handling unknown characters
    # If we feed it completely gibberish characters or emojis it hasn't seen heavily
    weird_text = "Hello 🚀 xyz"
    weird_tokens = tokenizer.encode(weird_text)
    print(f"\nWeird Text: '{weird_text}'")
    print("Split result:")
    for token_id in weird_tokens:
        print(f"'{tokenizer.decode([token_id])}'")

if __name__ == "__main__":
    demonstrate_bpe()
