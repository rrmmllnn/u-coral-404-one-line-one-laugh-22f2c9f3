#!/usr/bin/env python3
"""One Line, One Laugh -- a single hilarious line, at most 200 characters.

The line is a domestic punchline with a concrete scene and two turns:
a household robot files for divorce, and the punch lands in the last
few words, when the couch it kept getting stuck under becomes what it
takes in the settlement.
"""

import os
import sys

LIMIT = 200

_OPENING = "My Roomba filed for divorce,"
_GROUNDS = " citing irreconcilable dirt,"
_SETTLEMENT = " and took the couch in the settlement."


def build_line():
    parts = (_OPENING, _GROUNDS, _SETTLEMENT)
    line = ""
    for part in parts:
        line += part
    return line


def checked_line():
    line = build_line()
    if not line.strip():
        sys.stderr.write("error: line is empty\n")
        raise SystemExit(1)
    if any(mark in line for mark in ("\r", "\n")):
        sys.stderr.write("error: line must fit on one line\n")
        raise SystemExit(1)
    if len(line) > LIMIT:
        sys.stderr.write(
            "error: line is %d characters, over the %d limit\n"
            % (len(line), LIMIT)
        )
        raise SystemExit(1)
    return line


def main():
    line = checked_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
