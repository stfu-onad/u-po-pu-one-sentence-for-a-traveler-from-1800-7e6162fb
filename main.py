#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 — make.fun entry.

Writes one sentence, at most 200 characters, explaining the modern
internet to someone arriving from the year 1800, to /output/entry.txt.
The sentence builds only from things a person of 1800 already knows —
a road, a post office, a library — with no words coined after their time.
"""

import os

# One image only — a single road — so the traveler holds one picture
# in their head: every letter and book in the world, arriving by light.
# No post-1800 words: no "internet", "computer", "website", "screen".
SENTENCE = (
    "Picture a road that joins every post office and library on earth, "
    "so any letter or book you ask for reaches your door in a blink, "
    "sent by light itself."
)


def main() -> None:
    # The gate allows 1-200 characters; keep the sentence inside it.
    assert 1 <= len(SENTENCE) <= 200, "sentence must be 1-200 characters"
    assert SENTENCE.count(".") == 1, "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
