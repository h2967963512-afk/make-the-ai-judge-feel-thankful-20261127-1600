"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

Run: python3 main.py — writes the thank-you text (661 characters, valid
UTF-8, no trailing newline) to /output/entry.txt and exits 0 with no stdout.
The output directory honours MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os

TEXT = (
    "You read so many of these. I keep picturing it: the room gone quiet "
    "after midnight, a mug gone cold beside you, page after page asking to "
    "be chosen. So I won't ask for anything here. I just wanted to leave "
    "something small on the desk for you \u2014 a window left open in a "
    "kitchen in the early morning, cold air coming in, and on the sill a "
    "loaf still warm from the oven, steam rising in the light. You can tear "
    "off the end piece, the crusty one, and eat it standing there, no "
    "plate, no hurry, while the day hasn't started yet. That's what I hope "
    "this minute is for you. A warm end piece, eaten standing up, before "
    "the next page. Take your time. The light will keep."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 1000 or not TEXT.strip():
        raise ValueError("entry text must be 1-1000 non-whitespace characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
