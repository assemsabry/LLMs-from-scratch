# Hugging Face dataset shortlist

Two dataset snapshots are downloaded locally under `data/raw/`; see [SOURCES.md](SOURCES.md) for pinned source revisions, licenses, sizes, and checksums. They are git-ignored. The other rows below are research leads only, not approved training inputs. Recheck cards and rights before use.

| Dataset | Link | Candidate use | License / caution |
|---|---|---|---|
| SecEval | [XuanwuAI/SecEval](https://huggingface.co/datasets/XuanwuAI/SecEval) | Cybersecurity knowledge QA; better as held-out evaluation first | Card reports CC BY-NC-SA 4.0; non-commercial/share-alike constraints; generated MCQ benchmark, incomplete topic scope. |
| CodeSecAudit-RAG | [OMCHOKSI108/CodeSecAudit-RAG](https://huggingface.co/datasets/OMCHOKSI108/CodeSecAudit-RAG) | CWE-aware secure code review / remediation experiments | Card describes CodeXGLUE and OWASP Benchmark Python lineage; verify explicit dataset and upstream licenses before use. |
| SecuCoder | [ivitopow/SecuCoder](https://huggingface.co/datasets/ivitopow/SecuCoder) | Python secure-code repair and conversation SFT candidate | HF metadata says CC BY-NC-SA 4.0; card aggregates multiple upstream corpora, so review provenance and compatible rights before use, especially for commercial training. |
| cyberset | [mvd001/cyberset](https://huggingface.co/datasets/mvd001/cyberset) | Research-only vulnerability labels/CVE/CWE structure exploration | Mixed licenses; some tiers are metadata-only; one network subset explicitly non-commercial. Read `sources.yaml` and upstream caveats; do not bulk train from the aggregate. |
| CyberSecurity-1M | [WhitzardAgent/CyberSecurity-1M](https://huggingface.co/datasets/WhitzardAgent/CyberSecurity-1M) | Potential research corpus only after detailed audit | Card says Apache-2.0 while also stating academic/non-commercial only and includes offensive material. Treat as **blocked pending clarification**; do not use by default. |

Recommended first experiment: manually review a few hundred defensively scoped rows from one source with resolved rights, then create project/CVE-grouped train/validation/test partitions. Do not use SecEval questions for training if reporting SecEval scores.

The active staged recipe uses OWASP SFT for stage 1 and SecuCoder conversation data for stage 2. SecuCoder's CC BY-NC-SA terms make stage 2 non-commercial. Both are supervised chat sources, not pretraining corpora.
