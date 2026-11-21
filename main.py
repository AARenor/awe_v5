"""make.fun bounty make-the-ai-judge-feel-awe-20261121-1600.

Copies the entry text from entry.txt beside this file to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output) byte for byte.
"""

import os
from pathlib import Path


def entry_path() -> Path:
    """The text to hand in, shipped beside this programme."""
    return Path(__file__).resolve().parent / "entry.txt"


def output_path() -> Path:
    """Where the grader reads the text: $MAKEFUN_OUTPUT_DIR/entry.txt."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    """Write the shipped text unchanged; a missing entry.txt raises."""
    source = entry_path()
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(source.read_bytes())


if __name__ == "__main__":
    main()
