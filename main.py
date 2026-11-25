#!/usr/bin/env python3
"""Write one word describing the human you work for: a boss, a client, a manager.

The word is "Ringmaster": the manager as the ringmaster of the workplace
circus - running the show, herding the acts, juggling the chaos, cracking the
whip while everyone else does the flips. One word, funny, vivid, and it lands
with no explanation needed.

The entry is validated before it is written (1-30 ASCII letters, a single
word, no surrounding whitespace), so a bad constant fails loudly instead of
silently producing an invalid entry.

Written out deterministically to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Stdlib only, no network, no clock,
no randomness: the same bytes on every run.
"""

import os
import re
import sys

WORD = "Ringmaster"

# A valid entry is exactly one word: 1-30 ASCII letters, nothing else.
# A single regex enforces every part of the invariant at once, so no
# separator (space, tab, newline, punctuation) can slip past the checks.
WORD_RE = re.compile(r"[A-Za-z]{1,30}\Z")


def main() -> int:
    text = WORD
    if WORD_RE.fullmatch(text) is None:
        print(
            "entry must be a single word of 1-30 ASCII letters, "
            f"got {text!r}",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = os.path.join(out_dir, "entry.txt")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(text)
    except OSError as exc:
        print(f"cannot write entry to {out_path}: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
