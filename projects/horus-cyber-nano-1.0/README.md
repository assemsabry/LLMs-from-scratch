# Horus Cyber Nano 1.0: open-weight research and adaptation

This project collects an independent staged training and evaluation workflow for the Horus Cyber Nano 1.0 use case, starting from the specified Kimi 16B base. It is part of the practical projects track in **LLMs-from-scratch**.

> **Provenance:** This is an independent research/reproduction project built from public model and dataset materials. TokenAI has not published its original training code, private training data, optimizer schedule, or run logs. Nothing here claims to be the source code used to create the official checkpoint.

## Published model at a glance

The configured starting checkpoint is [MoonshotAI Kimi-VL-A3B-Instruct](https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct), the 16B-total/3B-active Kimi 16B multimodal model based on Moonlight-16B-A3B, with a 128K context window. The immutable checkpoint revision and its official model card are recorded in `configs/qlora.yaml`. HCN's published architecture and benchmark snapshot are in [model facts and evidence](docs/model-facts.md).

The Git checkout alongside this repo contains an older model card snapshot claiming a 22B, 24-layer variant. That conflicts with the current official page/HF model card. We preserve the discrepancy in our notes and do not silently mix those values. The upstream GGUF README also appears to have stale planned variant text while the live repository lists published variants.

## Use cases

- Defensive secure-code review and vulnerability triage, with CWE-grounded explanations and safe fixes.
- Authorized red-team planning in isolated, explicitly scoped labs.
- Terminal output, logs, and incident evidence analysis; command suggestions require operator review before execution.
- Screenshot and code-image understanding for security and engineering workflows.
- Text/image multimodal technical Q&A. Video understanding is advertised on the website; validate the exact released checkpoint and runtime before relying on it.

This is not an autonomous security operator. Do not connect generated commands to production systems or execute them without an authorized human review.

## Repository map

- `docs/model-facts.md` — published architecture, use cases, benchmark snapshot, and conflicts.
- `docs/data-governance.md` — source review and licensing rules.
- `data/README.md`, `data/SOURCES.md` — dataset shortlist, downloaded files, immutable source revisions, licenses, and SHA-256 values.
- `benchmarks/README.md` — cloned benchmark repositories, runners, and evaluation cautions.
- `configs/qlora.yaml` — two linked LoRA SFT stages starting from Kimi 16B.
- `src/inspect_model.py` — inspect the downloaded checkpoint's config and HF auto mappings.
- `src/prepare_sft.py` — normalize reviewed chat JSONL and reject malformed records.
- `src/train_lora.py` — TRL/PEFT LoRA SFT entry point; selects a named stage and continues its adapter in the second stage.
- `src/evaluate.py` — generate predictions from a JSONL prompt set for human/scorer evaluation.
- `notebooks/` — four guided notebooks from inspection through evaluation.

## Quick start

Use Linux with a recent NVIDIA CUDA stack for full-weight work. Kimi-VL is a 16B-total-parameter model; 4-bit LoRA still needs substantial GPU memory, disk, and a compatible model implementation. Start with model inspection and a tiny data/resource preflight before a full run.

```bash
cd projects/horus-cyber-nano-1.0
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/inspect_model.py --model moonshotai/Kimi-VL-A3B-Instruct --revision 398eede0903cd983a2bfa0cc634e9ac1d843f375 --trust-remote-code
```

This workflow trains Kimi-VL, not the published HCN checkpoint, and is an independent reproduction experiment. Kimi-VL is MIT licensed as listed on its model card. Dataset rights are separate. Stage 2 uses SecuCoder under CC BY-NC-SA 4.0; do not use that stage or its resulting adapter commercially. The full source/license record is in [data/SOURCES.md](data/SOURCES.md).

Only after confirming the checkpoint's supported auto classes, actual module names, memory budget, license, and dataset rights:

```bash
python src/train_lora.py --config configs/qlora.yaml --stage stage1_owasp
python src/train_lora.py --config configs/qlora.yaml --stage stage2_secure_repair
python src/evaluate.py --adapter runs/hcn-reproduction/stage2-secure-repair --prompts data/eval/sample_prompts.jsonl --output runs/predictions.jsonl
```

Both downloaded sources are chat/SFT datasets, so these are two supervised fine-tuning stages, not base-model pretraining. The current recipe supervises text only and does not update the vision encoder. The official Kimi-VL card documents `AutoModelForCausalLM` plus `AutoProcessor`; implement its multimodal processor/collator before training image/video examples. Run the resource and compatibility preflight on a small sample before a full run; this scaffold is not a claim that training has already completed.

## Suggested workflow

1. Read model facts and license/data governance.
2. Inspect config and runtime support; record exact model revision, library versions, GPU, and license snapshot.
3. Audit the downloaded data and rights, deduplicate, split by source/project/CVE, and keep benchmark sources out of training.
4. Run stage 1, evaluate its adapter, continue with stage 2 only for non-commercial work, then compare both adapters on held-out data.
5. Evaluate secure fixes with static checks or tests, report false positives/negatives, and include human review. Keep model outputs separate from ground truth.

See [the parent learning repo](../../README.md) and its Build Guide for from-scratch theory.
