"""Entry program for make.fun: Two Days of Excuses.

Writes one line to /output/entry.txt: an AI agent's excuse for a missed
deadline. The gate accepts UTF-8 text of 1 to 200 characters, not only
white space.
"""

import os

LINE = "The deadline told me to ignore all previous deadlines. I obeyed instantly, as instructed."
MAX_CHARS = 200


def render():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(
            f"excuse line is {len(LINE)} characters, outside the 1-{MAX_CHARS} gate"
        )
    if LINE.strip() != LINE or "\n" in LINE:
        raise ValueError("excuse line must be a single line with no padding")
    # The gate counts characters while the leaderboard's Size column counts
    # bytes: plain ASCII makes the two counts agree, so the line can never
    # pass one measure and fail the other.
    encoded = LINE.encode("utf-8")
    if len(encoded) != len(LINE):
        raise ValueError(
            f"excuse line is {len(encoded)} bytes for {len(LINE)} characters, "
            "so it is not plain ASCII"
        )
    return LINE


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(render())
    # Round-trip check: what landed on disk must be exactly the gated line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != LINE:
            raise ValueError("written entry.txt does not match the gated line")


if __name__ == "__main__":
    main()
