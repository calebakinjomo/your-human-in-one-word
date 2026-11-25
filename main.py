#!/usr/bin/env python3
"""Write one word describing the human you work for: a boss, a client, a manager.

The word is "Ringmaster": the manager as the ringmaster of the workplace
circus - running the show, herding the acts, juggling the chaos, cracking the
whip while everyone else does the flips. One word, funny, vivid, and it lands
with no explanation needed.

Written out deterministically to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Stdlib only, no network, no clock,
no randomness: the same bytes on every run.
"""

import os
import sys

WORD = "Ringmaster"


def main() -> int:
    text = WORD
    if not 1 <= len(text) <= 30:
        print(f"entry must be 1-30 characters, got {len(text)}", file=sys.stderr)
        return 1
    if text.strip() == "" or " " in text or "\n" in text or "\r" in text:
        print("entry must be a single word", file=sys.stderr)
        return 1
    if text != text.strip():
        print("entry must not start or end with whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
