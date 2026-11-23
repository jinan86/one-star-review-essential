#!/usr/bin/env python3
"""One-star review of something essential: the elbow's funny bone.

Writes a single deadpan one-star review, at most 160 characters, of an
everyday essential everyone relies on, to /output/entry.txt.

The review is a fixed string. No randomness, no network, no clock, no
environment input: two runs produce byte-identical output.
"""

from pathlib import Path

REVIEW = (
    "One star. My elbow has a bone called funny, and in my whole "
    "life it has never once been funny."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(REVIEW, encoding="utf-8")


if __name__ == "__main__":
    main()
