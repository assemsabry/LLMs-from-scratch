import torch
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

app = FastAPI(title="LLM API", description="A REST API for serving our fine-tuned LLM")

# Configuration
BASE_MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
ADAPTER_PATH = "./finetuned_lora_adapters" # Path to the LoRA adapters from our training script

# Global variables for lazy loading
tokenizer = None
model = None

class GenerationRequest(BaseModel):
    prompt: str
    max_tokens: int = 100
    temperature: float = 0.7

@app.on_event("startup")
def load_model():
    """
    Loads the base model and merges it with the LoRA adapters on API startup.
    """
    global tokenizer, model
    print(f"Loading Base Model: {BASE_MODEL_NAME}...")
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_NAME)
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL_NAME, 
        torch_dtype=torch.float16, 
        device_map="auto"
    )
    
    try:
        # Load the PEFT/LoRA model
        print(f"Loading LoRA adapters from {ADAPTER_PATH}...")
        model = PeftModel.from_pretrained(base_model, ADAPTER_PATH)
        # Merge the LoRA weights into the base model weights for faster inference
        model = model.merge_and_unload()
    except Exception as e:
        print(f"Warning: Could not load LoRA adapters. Running base model only. Error: {e}")
        model = base_model
        
    model.eval()
    print("Model loaded successfully!")

@app.post("/generate")
async def generate_text(req: GenerationRequest):
    """
    Endpoint to generate text from a prompt.
    """
    inputs = tokenizer(req.prompt, return_tensors="pt").to(model.device)
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=req.max_tokens,
            temperature=req.temperature,
            do_sample=True if req.temperature > 0 else False
        )
        
    # Decode the output
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Remove the prompt from the generated text
    response_text = generated_text[len(req.prompt):].strip()
    
    return {
        "prompt": req.prompt,
        "response": response_text
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
