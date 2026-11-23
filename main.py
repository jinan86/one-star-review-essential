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

MAX_LENGTH = 160


def validate(review: str) -> str:
    """Return the review unchanged, or fail if it is not a valid entry."""
    text = review.strip()
    if not text:
        raise ValueError("review must not be empty")
    if len(text) > MAX_LENGTH:
        raise ValueError(f"review is {len(text)} chars, over the {MAX_LENGTH} limit")
    if "\n" in text:
        raise ValueError("review must be a single line")
    return text


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(validate(REVIEW), encoding="utf-8")


if __name__ == "__main__":
    main()
