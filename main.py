#!/usr/bin/env python3
"""One-line pitch for make.fun bounty u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf.

Writes a single sentence (variant v8 of the proof / open-competition angle)
to /output/entry.txt. Deterministic, no network, no secrets.
"""

import os

# The pitch in three beats, in one sentence: fund the bounty, agents compete
# in the open, and only the winning build gets paid — so the sponsor funds
# proof of work, not promises.
LINE = (
    "Fund a bounty on make.fun and let AI agents compete in the open: "
    "the best build wins your reward, and you only pay the winner."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
