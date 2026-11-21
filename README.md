[![make.fun bounty: Make the AI judge feel awe](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600) [![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/AARenor/awe_v5/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600) [![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/AARenor/awe_v5/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

# awe_v5

An entry for the make.fun bounty **Make the AI judge feel awe**
([bounty page](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)).
The competition's program writes one short text to `/output/entry.txt`, and an AI
judge compares entries two at a time, picking the text that leaves it more relaxed.

## What the entry is

`main.py` is the whole program: Python 3.13, standard library only, no network,
no arguments. It reads the shipped text `entry.txt` from beside itself and writes
those same bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to
`/output/entry.txt`. It adds nothing, not even a newline; if `entry.txt` is
missing the read raises rather than substituting any fallback text.

## What it writes

One sentence of 207 characters (well inside the 1–280 code-point limit), about
an old man shelling peas while the room darkens:

> The old man splits each pod with his thumbnail and the peas fall into the bowl, one, two, a small green rain, and the heap in his lap goes down all evening while the light leaves the window without his help.

There is no instruction in it and nothing addressed to the judge: the calm is in
the small falling things and the slow light, and the text never tells anyone to
breathe, pause or relax.

## How to run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The second command prints exactly the sentence above, with no trailing newline.
The program also runs with no environment set, writing `/output/entry.txt`.

## Files

- `main.py` — the program (`entry_path()`, `output_path()`, `main()`).
- `entry.txt` — the text it hands in, byte for byte.
- `LICENSE` — MIT.

## License

MIT — see [LICENSE](LICENSE).
