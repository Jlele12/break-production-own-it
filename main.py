#!/usr/bin/env python3
"""Break Production, Own It: the agent prints its own confession."""
import os

LINE = "placeholder"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
