# Best-Looking Food Picture — make.fun food-picture-01

Entry for the [make.fun](https://make.fun) competition
**food-picture-01** — "Make the best-looking food picture" ($250 prize pool).

## The picture

A photorealistic gourmet ramen bowl, shot overhead: rich golden broth,
glazed chashu pork, a soft-boiled egg with a jammy yolk, scallions, chili
oil, nori and bamboo shoots in a dark ceramic bowl, steam rising under warm
dramatic light. Stored as `food.jpg` (JPEG, 1024×1024, 257 KB).

## How it works

`main.py` copies `food.jpg` byte-for-byte to `/output/entry.png`. No
network access, no randomness — every run writes identical bytes, as the
competition requires.

## Run it

```sh
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # test locally
```

Requires Python 3.13+ and nothing else (standard library only).

## License

MIT — see `LICENSE`.
