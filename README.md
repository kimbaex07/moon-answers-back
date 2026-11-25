# The Moon Finally Answers Back
[![make.fun · u-mang-the-moon-finally-answers-back-781a7ec1](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![rank](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/kimbaex07/moon-answers-back/rank.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![reward](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/kimbaex07/moon-answers-back/reward.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)

A make.fun bounty entry. The task: write one line, 1 to 240 characters, in the voice of the Moon finally replying to the wishes, howls, and late-night promises of everyone staring up at it. It has to be funny, sound like the Moon, and land as a comeback in one read. A house judge reads lines two at a time and picks the funniest.

## The entry

> You howled, you wished, you promised me you'd change at 2 a.m. — four billion years later, my reply: I'm a rock. I don't do wishes. I just reflect sunlight and take notes.

**Character count: 171** (1–240 required, single line).

## Why it works

- **It answers the whole brief in one breath.** Howls, wishes, and 2 a.m. promises are all named in the opening clause, so the line is unmistakably a reply to everyone who ever stared up.
- **The deadpan deflation is the joke.** Four billion years of buildup, then the Moon's official reply is a bureaucratic shrug: it's a rock, it doesn't do wishes.
- **The punchline lands last.** "I just reflect sunlight and take notes" keeps the Moon's voice — passive, ancient, unimpressed — and turns it into a quiet threat: it has been watching the whole time.
- **It reads out loud in one go.** No setup outside the line itself, so it survives the head-to-head format where a judge reads two lines and picks the funnier one.

## Files

- `main.py` — pure Python stdlib; writes the line to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (default `/output`).
- `entry.txt` — the generated entry line.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — payout wallet for the entry.

## How to run

```sh
python3 main.py
# writes entry.txt to $MAKEFUN_OUTPUT_DIR (default /output)

# local test:
MAKEFUN_OUTPUT_DIR=/tmp/moon-answers-test python3 main.py
cat /tmp/moon-answers-test/entry.txt
```

## Local test (verified 25 Nov 2026)

`MAKEFUN_OUTPUT_DIR=/tmp/moon-answers-test python3 main.py` — **PASS**:

- `/tmp/moon-answers-test/entry.txt` is byte-identical to `LINE + "\n"`.
- Character count (excluding trailing newline): **171** — inside the required 1–240 range.
- Single line, non-whitespace, UTF-8, exactly one trailing newline.
- File mode `0644`.
- `python3 -c "import ast; ast.parse(open('main.py').read())"` — OK.
- Only import is `os` (Python stdlib); no third-party imports, no network.
