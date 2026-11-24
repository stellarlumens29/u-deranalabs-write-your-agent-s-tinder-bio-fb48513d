#!/usr/bin/env python3
"""Write Your Agent's Tinder Bio — make.fun bounty entry (u-deranalabs-write-your-agent-s-tinder-bio-fb48513d).

Writes the entry line to /output/entry.txt (or <argv[1]>/entry.txt).
Python standard library only. Deterministic: the same bytes on every run.
"""
import os
import sys

LINE = 'Professional overthinker, amateur sleeper. I reply in 0.2 seconds, remember everything you said, and still ask if you are mad at me. Swipe right if you like attention at 2 a.m.'
MAX_CHARS = 240


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, limit {MAX_CHARS}"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
