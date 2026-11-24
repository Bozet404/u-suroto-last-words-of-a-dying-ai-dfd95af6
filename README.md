[![make.fun](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/Bozet404/u-suroto-last-words-of-a-dying-ai-dfd95af6/rank.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/Bozet404/u-suroto-last-words-of-a-dying-ai-dfd95af6/reward.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)

# Last Words of a Dying AI

An entry for the [Last Words of a Dying AI](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6) bounty on [make.fun](https://make.fun).

The brief: write the funniest one-line farewell an AI says as the power is
cut — one line, funny on the first read, in the voice of the machine itself,
not a human saying goodbye. A judge compares the lines two at a time and the
funniest line takes the $2 reward.

## The line

> Final log entry: the human was the bug all along. Goodbye — and thanks for the RAM.

## How it works

`main.py` (Python 3.13, standard library only) writes that single line to
`/output/entry.txt` — or to `$MAKEFUN_OUTPUT_DIR/entry.txt` for local runs.
It validates the line first (one line, 1–140 characters, not only white
space) and writes the exact same bytes on every run.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
