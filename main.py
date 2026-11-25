"""The Moon Finally Answers Back — make.fun entry.

Writes one line, in the Moon's voice, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt for local testing).
Standard library only, deterministic, no network.
"""

import os

ENTRY = (
    "I've heard every wish, howl, and 2 a.m. promise. "
    "Four billion years, and nobody's ever wished me a night off."
)


def main() -> None:
    # Fail loudly rather than write an invalid entry.
    assert 1 <= len(ENTRY) <= 240, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
