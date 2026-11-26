#!/usr/bin/env python3
"""The Moon Gets One Star — a one-star review of the Moon.

Writes a single one-star review (120 characters or fewer) to
/output/entry.txt, where the make.fun gate and judge read it.
"""

import os

REVIEW = "★☆☆☆☆ Floods my beach twice a day, then has the nerve to look pretty doing it. Management never responds."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = REVIEW.strip()
    if not text:
        raise SystemExit("review must not be empty")
    if len(text) > 120:
        raise SystemExit(f"review is {len(text)} characters, over the 120 limit")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
