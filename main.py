#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one line of honest, funny error copy to /output/entry.txt:
the database crashed mid-save, the changes were swallowed, a backup
copy was kept, and the user is told to hit retry.
"""

import os

ENTRY = "The database crashed mid-save and swallowed your last changes. We kept a backup copy \u2014 hit retry and we'll pretend this never happened."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
