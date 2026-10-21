# Data governance and safety

The original Horus Cyber Nano training corpus and data mixture are not publicly documented in the sources checked for this project. This independent recipe fine-tunes the Kimi 16B base on the two sources listed in `data/SOURCES.md`; it is not a claim about TokenAI's training data.

Before any dataset is used, record its exact revision, card, license, upstream lineage, allowed commercial/non-commercial uses, redistribution terms, personal-data policy, and split. A Hugging Face host does not guarantee that every row is licensed for model training. Do not combine mixed-license data into a redistributable artifact without resolving every upstream right. Keep evaluation sets held out and deduplicate by project, CVE, and near-duplicate cluster to reduce contamination.

For security tasks, curate for defensive explanations, safe remediation, authorization boundaries, and refusal behavior. Exclude malware payloads, credential material, real secrets, and instructions that enable unauthorized access. Treat offensive examples as controlled evaluation material, not default SFT targets. Human-review labels and generated samples; generated text is not ground truth.

The model license is independent of dataset licenses. This workflow starts from Kimi-VL, not HCN weights; read the base model's license and comply with the stricter dataset terms for any adapter. SecuCoder is CC BY-NC-SA 4.0, so its stage and resulting adapter are non-commercial and share-alike. Recheck the license snapshots before use or release.
