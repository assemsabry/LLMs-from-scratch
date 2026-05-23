import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_text():
    """
    Demonstrates how to load a pre-trained Large Language Model (GPT-2)
    and use it to generate text auto-regressively.
    
    Prerequisites: pip install transformers torch
    """
    print("--- LLM Text Generation Example ---")
    print("Loading GPT-2 model and tokenizer (this may take a moment to download)...")
    
    # 1. Load the Tokenizer
    # The tokenizer converts raw text strings into the integer token IDs the model expects.
    model_name = "gpt2" # We use standard GPT-2 as it is small enough to run quickly on a CPU
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    
    # 2. Load the Model
    # We load the weights of the pre-trained causal language model.
    model = GPT2LMHeadModel.from_pretrained(model_name)
    
    # Set model to evaluation mode (disables dropout layers, etc.)
    model.eval()

    # 3. Define the Prompt
    prompt_text = "The future of artificial intelligence is"
    print(f"\nPrompt: '{prompt_text}'")
    
    # 4. Tokenize the input
    # return_tensors="pt" tells the tokenizer to return PyTorch tensors instead of standard Python lists.
    input_ids = tokenizer.encode(prompt_text, return_tensors="pt")
    
    print("\nGenerating text...")
    
    # 5. Generate Output
    # The generate() function handles the auto-regressive loop (predicting token by token).
    with torch.no_grad(): # Disable gradient calculation for faster inference
        output_ids = model.generate(
            input_ids,
            max_length=50,          # Maximum total tokens (prompt + generated)
            num_return_sequences=1, # Generate just one response
            no_repeat_ngram_size=2, # Prevent the model from repeating the same 2-word phrases
            do_sample=True,         # Enable probabilistic sampling rather than just picking the mathematically most likely word (Greedy decoding)
            temperature=0.7,        # Controls randomness. Higher (1.0) = more creative, Lower (0.1) = more predictable.
            top_k=50,               # Limits sampling pool to the top 50 most likely next tokens
            pad_token_id=tokenizer.eos_token_id # Supress padding warnings
        )
    
    # 6. Decode the Output
    # Convert the resulting integer token IDs back into readable English text.
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    print("\n--- Final Generated Output ---")
    print(generated_text)

if __name__ == "__main__":
    generate_text()
