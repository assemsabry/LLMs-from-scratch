# Model facts and evidence

Checked against public sources on 2026-10-21. These are published claims, not independently reproduced measurements.

## Identity and intended work

Horus Cyber Nano 1.0 is published by TokenAI as an open-weights cybersecurity-focused multimodal model. Officially listed workflows: secure code review; vulnerability analysis and remediation; authorized red-team task reasoning; terminal/tool workflow support; and screenshot/code-image understanding. The web page also mentions video understanding. Treat outputs as suggestions requiring an authorized security professional's review.

## Current official architecture snapshot

| Property | Published value | Source |
|---|---|---|
| Parameters / tensors | 16B; BF16 and F32 | [official model page](https://tokenai.llc/models/horus-cyber-nano1.0) |
| Modalities | text + image input, text output | [HF model card](https://huggingface.co/tokenaii/Horus-Cyber-Nano-1.0) |
| Language decoder | causal MoE; 27 layers; hidden 2,048; 16 attention heads; 16 KV heads | [official model page](https://tokenai.llc/models/horus-cyber-nano1.0) |
| MoE | 64 routed + 2 shared experts; 6 routed active/token; every layer; expert parallel size 1 | [official model page](https://tokenai.llc/models/horus-cyber-nano1.0) |
| Vision | 27 layers; hidden 1,152; 16 heads; patch size 14 | [official model page](https://tokenai.llc/models/horus-cyber-nano1.0) |
| Image limit | 3.2 million total pixels/image | [official model page](https://tokenai.llc/models/horus-cyber-nano1.0) |
| Other decoder settings | SiLU; RoPE theta 800,000 | [official model page](https://tokenai.llc/models/horus-cyber-nano1.0) |
| License | TokenAI Custom License | [license](https://huggingface.co/tokenaii/Horus-Cyber-Nano-1.0/blob/main/LICENSE) |

HF identifies the model as `kimi_vl`, `image-text-to-text`, and custom code; its quick start uses Transformers with `trust_remote_code=True`, and also documents vLLM/SGLang. Treat custom model code as executable code: pin a reviewed revision and inspect it before enabling remote code.

## Public evaluation snapshot

Official page figures: MMLU 82.0%, GPQA Diamond 45.2%, Terminal-Bench 2.0 46.2%, AIME 2025 76.4%, SWE-Bench Verified 61.7%; MATH-Vision 56.9%, MathVista MINI 80.1%, MMBench-EN-v1.1 84.4%, MMStar 70.4%, VideoMMMU 65.2%. These are reported by TokenAI; this project has not reproduced them. The page notes evaluation protocol differences may affect comparisons.

The official GGUF card estimates combined RAM+VRAM requirements: F16 59.71 GiB, Q8_0 32.18 GiB, Q6_K 27.24 GiB, Q5_K_M 23.11 GiB, Q4_K_M 20.84 GiB. These are inference estimates, not SFT requirements.

## Conflicting/stale public metadata

The local sibling `Horus-Cyber-Nano-1.0/README.md` describes 22B parameters, 24 layers, hidden size 2,880, 32 experts/4 active, and 131,072 context. That snapshot conflicts with the current official model page (16B, 27 layers, hidden 2,048, 64+2 experts/6 routed active). The current page and current HF model card link are used as the working baseline; always inspect the actual downloaded `config.json` and revision before configuring a run. The public page does not currently establish the full original training recipe, pretraining corpus, or verified reproduction protocol.
