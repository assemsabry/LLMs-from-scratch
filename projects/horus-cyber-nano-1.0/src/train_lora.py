"""Run one stage of the two-stage Kimi-VL text-only LoRA SFT recipe."""
import argparse
import json
from pathlib import Path

import torch
import yaml
from datasets import Dataset, Features, Value
from peft import LoraConfig, PeftModel
from transformers import AutoModelForCausalLM, AutoProcessor
from trl import SFTConfig, SFTTrainer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/qlora.yaml")
    parser.add_argument("--stage", required=True, help="Stage name from configs/qlora.yaml")
    args = parser.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    model_cfg, data_cfg = cfg["model"], cfg["data"]
    try:
        stage = cfg["stages"][args.stage]
    except KeyError as error:
        raise SystemExit(f"Unknown stage {args.stage!r}; choose one of {list(cfg['stages'])}") from error
    targets = cfg["model"].get("target_modules") or []
    if not targets:
        raise SystemExit("Set model.target_modules after inspecting named_modules() for this pinned revision.")
    if model_cfg.get("trust_remote_code"):
        print("WARNING: trust_remote_code is enabled. Verify the pinned repository code before continuing.")

    model_id, revision = model_cfg["id"], model_cfg["revision"]
    processor = AutoProcessor.from_pretrained(
        model_id, revision=revision, trust_remote_code=model_cfg["trust_remote_code"]
    )
    tokenizer = processor.tokenizer
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model_kwargs = {
        "revision": revision,
        "trust_remote_code": model_cfg["trust_remote_code"],
        "torch_dtype": getattr(torch, model_cfg.get("torch_dtype", "bfloat16")),
        "device_map": model_cfg.get("device_map", "auto"),
    }
    if model_cfg.get("load_in_4bit"):
        from transformers import BitsAndBytesConfig

        model_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
        )
    model = AutoModelForCausalLM.from_pretrained(model_id, **model_kwargs)
    model.config.use_cache = False
    modules = dict(model.named_modules())
    unmatched = [target for target in targets if not any(name == target or name.endswith("." + target) for name in modules)]
    if unmatched:
        raise SystemExit(f"Configured LoRA targets not found: {unmatched}; inspect this model's module names.")

    def load_split(path: str):
        task_filter = stage.get("filter_task")
        def rows():
            with Path(path).open(encoding="utf-8") as source:
                for line_number, raw in enumerate(source, start=1):
                    if not raw.strip():
                        continue
                    row = json.loads(raw)
                    metadata = row.get("meta") or row.get("metadata") or {}
                    if task_filter and metadata.get("task") != task_filter:
                        continue
                    messages = row.get("messages")
                    if not isinstance(messages, list) or not messages:
                        raise ValueError(f"{path}:{line_number}: missing messages list")
                    yield {"text": processor.apply_chat_template(messages, tokenize=False)}

        return Dataset.from_generator(rows, features=Features({"text": Value("string")}))

    train = load_split(stage["train_file"])
    validation_path = stage.get("validation_file")
    validation = load_split(validation_path) if validation_path and Path(validation_path).exists() else None
    train_args = cfg["training"]
    model = PeftModel.from_pretrained(model, stage["adapter_from"], is_trainable=True) if stage.get("adapter_from") else model
    output_dir = stage["output_dir"]
    if not len(train):
        raise SystemExit(f"No training rows after filtering stage {args.stage}; check dataset schema/filter_task.")
    trainer = SFTTrainer(
        model=model,
        args=SFTConfig(
            output_dir=output_dir, learning_rate=train_args["learning_rate"],
            num_train_epochs=stage.get("epochs", train_args["num_train_epochs"]),
            per_device_train_batch_size=train_args["per_device_train_batch_size"],
            gradient_accumulation_steps=train_args["gradient_accumulation_steps"],
            gradient_checkpointing=train_args["gradient_checkpointing"],
            logging_steps=train_args["logging_steps"], save_steps=train_args["save_steps"],
            eval_strategy=train_args.get("evaluation_strategy", "steps"),
            eval_steps=train_args.get("eval_steps", 100), report_to=train_args.get("report_to", "none"),
            max_seq_length=data_cfg["max_seq_length"], dataset_text_field="text",
            packing=False, seed=train_args.get("seed", 42),
        ),
        train_dataset=train,
        eval_dataset=validation,
        processing_class=tokenizer,
        peft_config=None if stage.get("adapter_from") else LoraConfig(
            r=cfg["lora"]["r"], lora_alpha=cfg["lora"]["alpha"],
            lora_dropout=cfg["lora"]["dropout"], bias=cfg["lora"]["bias"],
            target_modules=targets, task_type="CAUSAL_LM",
        ),
    )
    trainer.train()
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)
    print(json.dumps({"model": model_id, "revision": revision, "stage": args.stage, "output": output_dir}))


if __name__ == "__main__":
    main()
