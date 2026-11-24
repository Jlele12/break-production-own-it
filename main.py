#!/usr/bin/env python3
"""Break Production, Own It: the agent prints its own confession."""
import os

LINE = ("I dropped the prod table. Not staging — prod. "
        "No backup, no rollback, no excuse: I did this. "
        "Postmortem at 4, my name on every slide.")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
