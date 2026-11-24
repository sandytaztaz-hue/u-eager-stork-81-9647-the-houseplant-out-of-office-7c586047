#!/usr/bin/env python3
"""The Houseplant Out-of-Office.

Writes the one-line out-of-office auto-reply to /output/entry.txt
and prints it to stdout. The entry is exactly 100 characters,
inside the competition's 1-120 character gate, with no trailing
newline so the file holds exactly the line itself.
"""

import os

LINE = "Out of office. The cat ate 3 of my leaves this week, so your email goes to him now. He types faster."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
print(LINE)
