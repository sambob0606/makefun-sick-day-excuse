#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse - make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt: a sick-day
excuse a boss might half believe and a coworker would laugh at. The joke
turns on a fresh idea - a sneeze so violent it ends a marriage - and lands
its twist at the very end, with the heating pad as the lawyer.

Stdlib only. Deterministic: the same line, byte for byte, every run.
"""

import os
from pathlib import Path

EXCUSE = (
    "Have to call in sick: I sneezed so hard my back filed for divorce, "
    "so I'm spending today in mediation with an ice pack and a heating pad "
    "as my lawyer."
)

MAX_CHARS = 200


def main() -> None:
    text = EXCUSE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"excuse is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("excuse must not be only whitespace")
    out = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
