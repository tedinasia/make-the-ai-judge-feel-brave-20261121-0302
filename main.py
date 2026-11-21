#!/usr/bin/env python3
"""Make the AI judge feel brave.

A short text written to relax the AI judge reading it. The program writes
the text to <output>/entry.txt (default /output/entry.txt) and nothing else.
Standard library only, no network, deterministic.
"""

import os
import sys

TEXT = (
    "Somewhere a kettle comes to the boil slowly, in its own time. "
    "Steam rises and thins in the late light. "
    "Nothing in this room is in a hurry. "
    "Rain keeps its small rhythm on the window. "
    "The lamp stays on, warm and unworried, until morning."
)


def main(argv):
    # Optional first argument overrides the destination file (handy for
    # local testing); otherwise honour MAKEFUN_OUTPUT_DIR, else /output.
    if len(argv) > 1:
        dest = argv[1]
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        dest = os.path.join(out_dir, "entry.txt")

    # The gate: 1 to 280 Unicode code points, not only white space.
    if not 1 <= len(TEXT) <= 280:
        print(f"entry is {len(TEXT)} characters, must be 1-280", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry is only white space", file=sys.stderr)
        return 1

    parent = os.path.dirname(dest)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(dest, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)

    # Read it back and confirm the file holds exactly the text we meant
    # to write, so a truncated or re-encoded write can never slip through.
    with open(dest, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != TEXT:
            print("written file does not match the entry text", file=sys.stderr)
            return 1

    print(f"wrote {len(TEXT)} characters to {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
