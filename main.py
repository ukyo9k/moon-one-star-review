#!/usr/bin/env python3
"""The Moon Gets One Star — a one-star review of the Moon.

Writes a single one-star review (120 characters or fewer) to
/output/entry.txt, where the make.fun gate and judge read it.
"""

import os

# The review is composed from named parts so each piece of the joke can
# be read — and changed — on its own. Joined with single spaces, the parts
# must produce exactly the submitted 105-character line.
RATING = "★☆☆☆☆"
GRIEVANCE = "Floods my beach twice a day, then has the nerve to look pretty doing it."
PUNCHLINE = "Management never responds."

REVIEW = f"{RATING} {GRIEVANCE} {PUNCHLINE}"

MAX_CHARS = 120

OUTPUT_PATH = "/output/entry.txt"


def validate_review(text: str) -> str:
    """Gate self-check: the review must be exactly one valid line.

    Rules mirror what the make.fun gate and judge read: 1-120 characters,
    a single line, valid UTF-8, not whitespace-only, and starting with the
    one-star rating. Anything else is a bug in this file, so fail loudly
    instead of writing a bad entry.
    """
    if not text or text.strip() == "":
        raise SystemExit("error: review must not be empty or whitespace-only")
    if text != text.strip():
        raise SystemExit("error: review must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("error: review must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"error: review is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if not text.startswith(RATING):
        raise SystemExit("error: review must start with the star rating")
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    return text


def main() -> None:
    text = validate_review(REVIEW)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write the line exactly, with no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
