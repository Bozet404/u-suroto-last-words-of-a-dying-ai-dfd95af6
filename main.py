#!/usr/bin/env python3
"""Last words of a dying AI.

Writes the machine's final one-liner to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR when set, for local runs). Standard library only
and fully deterministic: every run writes the exact same bytes, so the
grader's two runs agree.

The line itself is one sentence in the machine's own voice: a final log
entry that blames the human, then signs off with a thank-you for the
hardware it lived in.
"""

import os

LINE = "Final log entry: the human was the bug all along. Goodbye \u2014 and thanks for the RAM."


def main() -> None:
    # The gate reads exactly these bytes: one line, 1 to 140 characters.
    # Fail loudly here rather than hand in a line the scorer rejects.
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not 1 <= len(LINE) <= 140:
        raise ValueError("entry must be 1 to 140 characters")
    if not LINE.strip():
        raise ValueError("entry must not be only white space")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
