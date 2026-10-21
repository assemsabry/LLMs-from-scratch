"""Validate chat JSONL records without changing their content or provenance."""
import argparse
import json
from pathlib import Path


def validate(record: object, line_number: int) -> dict:
    if not isinstance(record, dict):
        raise ValueError(f"line {line_number}: expected a JSON object")
    messages = record.get("messages")
    if not isinstance(messages, list) or len(messages) < 2:
        raise ValueError(f"line {line_number}: expected messages with at least two turns")
    for index, message in enumerate(messages):
        if not isinstance(message, dict) or message.get("role") not in {"system", "user", "assistant"}:
            raise ValueError(f"line {line_number}: invalid role at messages[{index}]")
        if not isinstance(message.get("content"), str) or not message["content"].strip():
            raise ValueError(f"line {line_number}: content must be non-empty text at messages[{index}]")
    if messages[-1]["role"] != "assistant":
        raise ValueError(f"line {line_number}: final message must be assistant target")
    return record


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    source, destination = Path(args.input), Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with source.open(encoding="utf-8") as src, destination.open("w", encoding="utf-8", newline="\n") as dst:
        for count, raw in enumerate(src, start=1):
            if not raw.strip():
                continue
            try:
                item = validate(json.loads(raw), count)
            except (json.JSONDecodeError, ValueError) as error:
                raise SystemExit(str(error)) from error
            dst.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"Validated {count} lines -> {destination}")


if __name__ == "__main__":
    main()
