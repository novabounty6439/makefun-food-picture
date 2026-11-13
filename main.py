#!/usr/bin/env python3
"""make.fun food-picture-01 entry: best-looking food picture.

The picture is a photorealistic gourmet ramen bowl, stored in this
repository as food.jpg (JPEG, 1024x1024, under 1 MiB). This program
copies it byte-for-byte to /output/entry.png, so every run produces
identical output with no network access.

Run:  python3 main.py
Test: MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "food.jpg")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def main():
    if not os.path.isfile(SOURCE):
        print(f"error: source image not found: {SOURCE}", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    print(f"wrote {OUTPUT} ({os.path.getsize(OUTPUT)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
