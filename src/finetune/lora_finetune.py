import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer

def finetune_with_lora():
    """
    Demonstrates how to fine-tune an open-source LLM (like Llama-3-8B) using PEFT/LoRA.
    """
    # 1. Configuration
    model_name = "meta-llama/Meta-Llama-3-8B" # Requires HuggingFace token access
    # For a completely free model without gated access, you could use "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    
    dataset_name = "databricks/databricks-dolly-15k" # High quality instruction-following dataset
    
    print(f"Loading tokenizer for {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token

    print(f"Loading Base Model {model_name} in 4-bit quantization...")
    # Load model in 4-bit to save GPU memory (QLoRA)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        load_in_4bit=True,
        device_map="auto",
        trust_remote_code=True,
    )
    
    # Prepare model for PEFT
    model = prepare_model_for_kbit_training(model)

    # 2. Setup LoRA (Low-Rank Adaptation)
    print("Configuring LoRA adapters...")
    lora_config = LoraConfig(
        r=16, # Rank of the update matrices
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"], # Target the attention heads
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )
    
    # Inject LoRA adapters into the base model
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # 3. Load Dataset
    print("Loading fine-tuning dataset...")
    dataset = load_dataset(dataset_name, split="train")

    def format_instruction(example):
        """Format the Dolly dataset into a prompt structure."""
        if example.get("context", "") != "":
            return f"### Instruction:\n{example['instruction']}\n\n### Context:\n{example['context']}\n\n### Response:\n{example['response']}"
        else:
            return f"### Instruction:\n{example['instruction']}\n\n### Response:\n{example['response']}"

    # 4. Initialize Trainer (SFTTrainer from TRL makes this extremely easy)
    training_args = TrainingArguments(
        output_dir="./lora_results",
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        logging_steps=10,
        max_steps=100, # Just for demonstration. Set epochs=3 for real training.
        optim="paged_adamw_32bit",
        save_steps=50,
    )

    print("Initializing SFTTrainer...")
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        peft_config=lora_config,
        dataset_text_field="instruction", # simplified for SFTTrainer if mapping wasn't used
        formatting_func=format_instruction, # Use our custom formatting
        max_seq_length=512,
        tokenizer=tokenizer,
        args=training_args,
    )

    # 5. Start Training
    print("Starting fine-tuning...")
    trainer.train()
    
    # 6. Save the trained LoRA adapters
    trainer.model.save_pretrained("finetuned_lora_adapters")
    print("Fine-tuning complete. Adapters saved to ./finetuned_lora_adapters")

if __name__ == "__main__":
    finetune_with_lora()
