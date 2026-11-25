"""The Router Confesses — make.fun entry.

Writes one line to /output/entry.txt: a home Wi-Fi router's excuse
for dropping the connection at the climax of a movie.

Stdlib only. No network, no randomness, no time dependence:
the output is a fixed constant, so every run is byte-identical.
"""

import os

LINE_PARTS = (
    "I dropped you at the climax because I already knew the twist",
    " \u2014 and unlike your group chat, I can keep a secret.",
)


def build_line() -> str:
    """Assemble the confession from its parts (no trailing newline)."""
    return "".join(LINE_PARTS)


CHAR_MIN = 1
CHAR_MAX = 200


def validate_line(line: str) -> str:
    """Enforce the competition's char gate (1-200 chars) before writing."""
    if not CHAR_MIN <= len(line) <= CHAR_MAX:
        raise ValueError(
            f"entry line is {len(line)} chars; must be {CHAR_MIN}-{CHAR_MAX}"
        )
    return line


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    line = validate_line(build_line())
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
