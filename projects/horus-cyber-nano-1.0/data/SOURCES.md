# Downloaded training files

These files were downloaded into `data/raw/` from the immutable Hugging Face revisions below. SHA-256 values let you verify the local copies. The `.gitignore` keeps raw data out of source control; each source license and its limits still apply.

| Local file | Source / revision | Split | License | Bytes | SHA-256 |
|---|---|---|---|---:|---|
| `raw/owasp-sft/train.jsonl` | [Humanlearning/CyberSecurity_OWASP-sft-dataset](https://huggingface.co/datasets/Humanlearning/CyberSecurity_OWASP-sft-dataset/resolve/79e64947c1aec23affeb13f29da455c13c6834e7/train.jsonl) | train | Apache-2.0 | 22331840 | `43FDC144A05FF6DC16A39176A34A914944A3BA127CB99F6E6272CB05CD2BC3EA` |
| `raw/owasp-sft/validation.jsonl` | same source and revision | validation | Apache-2.0 | 4479872 | `EDAE639021375115FDA4A5462A72EF0A39F863F49583BC174B0A921CF4D2F84B` |
| `raw/secucoder/train.jsonl` | [ivitopow/SecuCoder](https://huggingface.co/datasets/ivitopow/SecuCoder/resolve/7d5149ab257ad938384cacef9fd1827174630d0d/data/corpus.messages.train.jsonl) | train | CC BY-NC-SA 4.0 | 22236797 | `4C4307207BD4930A4B4C5AFE085044F6374DD1BF6B21FF4AFE3EC6DEC791257C` |
| `raw/secucoder/validation.jsonl` | [ivitopow/SecuCoder](https://huggingface.co/datasets/ivitopow/SecuCoder/resolve/7d5149ab257ad938384cacef9fd1827174630d0d/data/corpus.messages.val.jsonl) | validation | CC BY-NC-SA 4.0 | 1033712 | `FE5FC90159D96267ED8A3A872202557E89911C2B09EA8F9BD11E117134AB35AE` |

The SecuCoder license is non-commercial/share-alike. Stage 2 and any adapter trained from it must be treated accordingly; do not use this stage for commercial training. Stage 1 uses the OWASP data alone. The downloaded OWASP rows are defensive, local AppSec interaction traces; audit content before any further use. Both sources are chat/SFT data, not raw language-model pretraining corpora.

The datasets were opened in Edge and their cards, splits, file trees, and licenses were inspected. SecEval is listed as evaluation-only in `benchmarks/README.md`; no benchmark test split is used for training.

The OWASP Hugging Face page currently reports a viewer `CastError` on heterogeneous nested fields. The source JSONL files open/download correctly; `src/train_lora.py` reads them line by line and keeps only the message text so schema inference over nested metadata is not required.
