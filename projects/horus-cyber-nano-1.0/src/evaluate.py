"""Generate text predictions for a held-out JSONL prompt set."""
import argparse
import json
from pathlib import Path

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoProcessor


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="moonshotai/Kimi-VL-A3B-Instruct", help="Base model id or local base checkpoint")
    parser.add_argument("--adapter", help="Optional local PEFT adapter directory")
    parser.add_argument("--prompts", required=True, help="JSONL objects with a messages list")
    parser.add_argument("--output", required=True)
    parser.add_argument("--revision", default="398eede0903cd983a2bfa0cc634e9ac1d843f375")
    parser.add_argument("--max-new-tokens", type=int, default=512)
    args = parser.parse_args()
    processor = AutoProcessor.from_pretrained(args.model, revision=args.revision, trust_remote_code=args.trust_remote_code)
    model = AutoModelForCausalLM.from_pretrained(
        args.model, revision=args.revision, trust_remote_code=args.trust_remote_code,
        device_map="auto", torch_dtype="auto"
    )
    if args.adapter:
        model = PeftModel.from_pretrained(model, args.adapter)
    model.eval()
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with Path(args.prompts).open(encoding="utf-8") as src, destination.open("w", encoding="utf-8", newline="\n") as dst:
        for index, line in enumerate(src):
            record = json.loads(line)
            prompt = processor.apply_chat_template(record["messages"], tokenize=False, add_generation_prompt=True)
            inputs = processor(text=prompt, return_tensors="pt").to(model.device)
            generated = model.generate(**inputs, max_new_tokens=args.max_new_tokens, do_sample=False)
            answer = processor.batch_decode(
                generated[:, inputs.input_ids.shape[1]:], skip_special_tokens=True,
                clean_up_tokenization_spaces=False,
            )[0]
            dst.write(json.dumps({"id": record.get("id", index), "prediction": answer}, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
