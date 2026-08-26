#!/usr/bin/env python3
"""Find Continue button bounds in uiautomator dump and print tap coords."""
import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
t = path.read_text(encoding="utf-8", errors="ignore")

# text before or after bounds
patterns = [
    re.compile(
        r'text="([^"]*)"[^>]*bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"'
    ),
    re.compile(
        r'bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"[^>]*text="([^"]*)"'
    ),
]

found = []
for pat in patterns:
    for m in pat.finditer(t):
        groups = m.groups()
        if pat.pattern.startswith("text"):
            text, x1, y1, x2, y2 = groups
        else:
            x1, y1, x2, y2, text = groups
        if text:
            found.append((text, int(x1), int(y1), int(x2), int(y2)))

for text, x1, y1, x2, y2 in found:
    print(f"TEXT {text!r} bounds=[{x1},{y1}][{x2},{y2}]")

for key in ("Continue", "CONTINUE", "Sign in", "OK", "Accept", "Connect"):
    for text, x1, y1, x2, y2 in found:
        if key.lower() in text.lower():
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            print(f"TAP {cx} {cy}  # {text!r}")
            sys.exit(0)

print("NO_CONTINUE_FOUND")
sys.exit(2)
