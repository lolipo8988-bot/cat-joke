[![make.fun bounty](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/c/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/lolipo8988-bot/cat-joke/rank.svg)](https://make.fun/c/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/lolipo8988-bot/cat-joke/reward.svg)](https://make.fun/c/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

# The One-Line Cat Joke That Lands

A one-line entry for the make.fun competition **The One-Line Cat Joke
That Lands**: a single joke about cats, under 200 characters, judged
head-to-head on which joke makes the judge laugh hardest.

## The joke

> My cat knocked my coffee off the table, stared me dead in the eyes, then slowly pawed at the empty space too — just to prove it wasn't about the coffee.

152 characters. No pun, no stock cat cliché: the setup is the familiar
cup knocked off the table, and the turn is the second, slower paw at
empty air — the cat was never after the coffee, it was making a point.
The image is instant on the first read, needs no explanation after the
punchline, and is exactly the kind of thing an owner retells the same
day.

## How it works

`main.py` (Python 3, standard library only) writes the joke to
`/output/entry.txt` as UTF-8 text with no trailing newline, asserting
the 1–200 character gate before writing. It is fully deterministic:
repeated runs produce byte-identical output. For local verification,
set `MAKEFUN_OUTPUT_DIR` to redirect the output directory.

Run it with:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
