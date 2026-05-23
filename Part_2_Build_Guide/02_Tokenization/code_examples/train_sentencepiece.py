import os

def generate_dummy_data(file_path: str):
    """Generates a small dummy text file to train the tokenizer on."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("This is a simple example to train a BPE tokenizer.\n")
        f.write("SentencePiece is highly recommended for building LLMs from scratch.\n")
        f.write("It merges characters into subwords based on frequency.\n")
        f.write("Artificial Intelligence and machine learning are fascinating fields.\n")
        f.write("A BPE tokenizer will learn common suffixes like 'ing' and 'tion'.\n")

def demonstrate_sentencepiece_training():
    """
    Demonstrates training a SentencePiece tokenizer and using it to encode text.
    Prerequisites: pip install sentencepiece
    """
    print("--- SentencePiece Tokenizer Training Demonstration ---")
    
    try:
        import sentencepiece as spm
        
        data_file = "dummy_dataset.txt"
        model_prefix = "custom_bpe"
        
        # 1. Create dummy data
        generate_dummy_data(data_file)
        
        # 2. Train the Tokenizer
        print("\nTraining SentencePiece Tokenizer...")
        # Note: In reality, you would use a much larger vocab_size (e.g., 32000)
        # and point to a massive dataset. We use 100 here just for the tiny dummy text.
        spm.SentencePieceTrainer.train(
            input=data_file,
            model_prefix=model_prefix,
            vocab_size=100,
            model_type='bpe',
            pad_id=0,
            unk_id=1,
            bos_id=2,
            eos_id=3,
            pad_piece='<pad>',
            unk_piece='<unk>',
            bos_piece='<bos>',
            eos_piece='<eos>'
        )
        print(f"Training complete. Saved '{model_prefix}.model' and '{model_prefix}.vocab'")
        
        # 3. Load and test the trained tokenizer
        print("\nLoading Tokenizer...")
        sp = spm.SentencePieceProcessor(model_file=f"{model_prefix}.model")
        
        sample_text = "SentencePiece is fascinating."
        
        # 4. Encode: Text to IDs
        encoded_ids = sp.encode(sample_text)
        print(f"\nOriginal Text: '{sample_text}'")
        print(f"Encoded IDs:   {encoded_ids}")
        
        # 5. Decode: IDs back to Text
        decoded_text = sp.decode(encoded_ids)
        print(f"Decoded Text:  '{decoded_text}'")
        
        # 6. View the subword pieces
        pieces = sp.encode(sample_text, out_type=str)
        print(f"Subword pieces: {pieces}")
        print("(Note: The ' ' character represents a space in SentencePiece)")
        
        # Cleanup dummy files
        os.remove(data_file)
        os.remove(f"{model_prefix}.model")
        os.remove(f"{model_prefix}.vocab")
        
    except ImportError:
        print("Please install sentencepiece to run this script:")
        print("pip install sentencepiece")

if __name__ == "__main__":
    demonstrate_sentencepiece_training()
