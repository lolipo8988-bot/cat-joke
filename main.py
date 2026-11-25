#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the entry for 'The One-Line Cat Joke That Lands' to /output/entry.txt.

The competition asks for one single-line joke about cats, under 200
characters, nothing else in the entry. The gate checks that the file
is UTF-8 text of 1 to 200 characters and not only white space.

Revision note: the first version had the cat "knock the empty space",
which reads as a grammar slip rather than an action. The joke is now
built from its two beats -- the setup (the cup goes off the table, the
stare) and the turn (a slow paw at the empty space where the cup was)
-- and the turn's verb is "pawed at", a deliberate, visible cat action:
the cat was never after the coffee, it was making a point. No pun, no
stock cat cliche, and nothing after the punchline.

This program is deterministic: every run writes exactly the same
bytes, and it re-reads the file after writing to prove the bytes on
disk are the bytes intended.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

SETUP = (
    "My cat knocked my coffee off the table, stared me dead in the "
    "eyes, then slowly pawed at the empty space too"
)
TURN = "just to prove it wasn't about the coffee."


def build_entry() -> str:
    """Assemble the one-line joke from its setup and its turn."""
    return f"{SETUP} \u2014 {TURN}"


def render() -> str:
    """Return the entry text, checked against the gate's contract."""
    text = build_entry()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    assert "\n" not in text and text == text.strip() and text
    return text


def main() -> None:
    text = render()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.dirname(OUTPUT_PATH))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, encoding="utf-8", newline="") as f:
        assert f.read() == text, "written entry does not match the intended text"


if __name__ == "__main__":
    main()
