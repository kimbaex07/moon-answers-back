"""Entry for make.fun bounty: The Moon Finally Answers Back.

Writes the Moon's one-line reply to entry.txt inside the output
directory given by MAKEFUN_OUTPUT_DIR (default /output).

Pure Python standard library only. Deterministic, no network.
"""

import os

LINE = "You howled, you wished, you promised me you'd change at 2 a.m. — four billion years later, my reply: I'm a rock. I don't do wishes. I just reflect sunlight and take notes."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
