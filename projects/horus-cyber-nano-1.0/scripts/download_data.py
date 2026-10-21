"""Download the pinned SFT data snapshots and verify their SHA-256 digests."""
import hashlib
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "data/raw/owasp-sft/train.jsonl": (
        "https://huggingface.co/datasets/Humanlearning/CyberSecurity_OWASP-sft-dataset/resolve/79e64947c1aec23affeb13f29da455c13c6834e7/train.jsonl",
        "43FDC144A05FF6DC16A39176A34A914944A3BA127CB99F6E6272CB05CD2BC3EA",
    ),
    "data/raw/owasp-sft/validation.jsonl": (
        "https://huggingface.co/datasets/Humanlearning/CyberSecurity_OWASP-sft-dataset/resolve/79e64947c1aec23affeb13f29da455c13c6834e7/validation.jsonl",
        "EDAE639021375115FDA4A5462A72EF0A39F863F49583BC174B0A921CF4D2F84B",
    ),
    "data/raw/secucoder/train.jsonl": (
        "https://huggingface.co/datasets/ivitopow/SecuCoder/resolve/7d5149ab257ad938384cacef9fd1827174630d0d/data/corpus.messages.train.jsonl",
        "4C4307207BD4930A4B4C5AFE085044F6374DD1BF6B21FF4AFE3EC6DEC791257C",
    ),
    "data/raw/secucoder/validation.jsonl": (
        "https://huggingface.co/datasets/ivitopow/SecuCoder/resolve/7d5149ab257ad938384cacef9fd1827174630d0d/data/corpus.messages.val.jsonl",
        "FE5FC90159D96267ED8A3A872202557E89911C2B09EA8F9BD11E117134AB35AE",
    ),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def main() -> None:
    for relative, (url, expected) in FILES.items():
        destination = ROOT / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() and sha256(destination) == expected:
            print(f"Verified existing file: {relative}")
            continue
        temporary = destination.with_suffix(destination.suffix + ".download")
        try:
            print(f"Downloading: {relative}")
            urllib.request.urlretrieve(url, temporary)
            actual = sha256(temporary)
            if actual != expected:
                raise ValueError(f"SHA-256 mismatch for {relative}: {actual}")
            temporary.replace(destination)
            print(f"Verified: {relative}")
        finally:
            temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
