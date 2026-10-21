"""Inspect public HF config metadata before loading large checkpoint weights."""
import argparse
import json

from transformers import AutoConfig


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="moonshotai/Kimi-VL-A3B-Instruct")
    parser.add_argument("--revision", default="398eede0903cd983a2bfa0cc634e9ac1d843f375")
    parser.add_argument("--trust-remote-code", action="store_true")
    args = parser.parse_args()

    config = AutoConfig.from_pretrained(
        args.model, revision=args.revision, trust_remote_code=args.trust_remote_code
    )
    print(json.dumps(config.to_dict(), indent=2, default=str))
    print("\nModel type:", getattr(config, "model_type", "unknown"))
    print("Architectures:", getattr(config, "architectures", None))
    print("Auto map:", getattr(config, "auto_map", None))
    print("\nReview config and remote code at the pinned revision before weight loading.")


if __name__ == "__main__":
    main()
