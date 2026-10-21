# Benchmark code and evaluation plan

This folder indexes the official benchmark code used by the published HCN 1.0 scorecard and provides commands for the public evaluation runners. The source repositories are shallow-cloned locally under `upstream/`; see `repos.json` and [the exact local commits](UPSTREAM.md). Some upstream repositories bundle benchmark assets or test examples, so keep the folders out of training and out of the parent Git repo. Respect each benchmark's access terms.

## HCN 1.0 scorecard benchmark sources

| Benchmark | Official code / dataset repository | Runner |
|---|---|---|
| MMLU | [hendrycks/test](https://github.com/hendrycks/test) | lm-evaluation-harness |
| GPQA Diamond | [idavidrein/gpqa](https://github.com/idavidrein/gpqa) | lm-evaluation-harness; dataset access is gated |
| Terminal-Bench 2.0 | [laude-institute/terminal-bench](https://github.com/laude-institute/terminal-bench) | Terminal-Bench / Harbor instructions |
| AIME 2025 | [math-ai-org/aime25](https://github.com/math-ai-org/aime25), [HF dataset](https://huggingface.co/datasets/math-ai/aime25) | lm-evaluation-harness task when available, otherwise official scorer |
| SWE-Bench Verified | [SWE-bench/SWE-bench](https://github.com/SWE-bench/SWE-bench) | SWE-bench harness |
| Math-Vision | [YerongLi/MathVision](https://github.com/YerongLi/MathVision) | VLMEvalKit |
| MathVista mini | [lupantech/MathVista](https://github.com/lupantech/MathVista) | VLMEvalKit |
| MMBench-EN-v1.1 | [OpenCompass/MMBench](https://github.com/open-compass/MMBench) | VLMEvalKit |
| MMStar | [MMStar-Benchmark/MMStar](https://github.com/MMStar-Benchmark/MMStar) | VLMEvalKit |
| VideoMMMU | [EvolvingLMMs-Lab/VideoMMMU](https://github.com/EvolvingLMMs-Lab/VideoMMMU) | Official evaluator / VLMEvalKit support varies by release |

## Runner repositories

- [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — text benchmarks such as MMLU and GPQA.
- [open-compass/VLMEvalKit](https://github.com/open-compass/VLMEvalKit) — multimodal benchmark inference and scoring.
- [SWE-bench/SWE-bench](https://github.com/SWE-bench/SWE-bench) — executable software issue resolution tasks.
- [laude-institute/terminal-bench](https://github.com/laude-institute/terminal-bench) — terminal agent tasks; run only in the isolated environment described upstream.

## Install runner code

Run from this directory in a Linux environment. This clones code-only repositories into `benchmarks/upstream/`; it does not download gated benchmark data or execute evaluations.

```bash
python -m pip install "lm_eval[api]"
python -m pip install vlmeval
git clone --depth 1 https://github.com/SWE-bench/SWE-bench.git upstream/SWE-bench
git clone --depth 1 https://github.com/laude-institute/terminal-bench.git upstream/terminal-bench
```

`repos.json` is the full source manifest for every benchmark on the HCN scorecard. Clone individual official repos from those URLs when needed; benchmark repositories can bundle large datasets or have separate access terms, so the manifest intentionally does not mass-download them.

The runner packages change frequently. Pin their Git commits and follow the benchmark's own model adapter, dataset access, metric, and environment instructions before recording results. Kimi-VL is multimodal: use a Kimi-VL-compatible adapter for vision and video benchmarks; a generic text-only harness result is not a valid substitute. The current training pipeline only tunes the language decoder on text chat data, so report vision/video capabilities as unchanged and re-evaluate them.

## Text runner examples

```bash
lm_eval --model hf --model_args pretrained=moonshotai/Kimi-VL-A3B-Instruct,trust_remote_code=True --tasks mmlu --batch_size 1
```

GPQA access is restricted. Do not fetch or redistribute the gated dataset without approval from its publisher. Terminal-Bench and SWE-Bench execute code in controlled sandboxes; use their documented isolated runners. Results are comparable only when model revision, prompt, decoding, few-shot settings, scorer, and dataset version match the published setup.
