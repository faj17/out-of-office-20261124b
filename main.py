#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply entry.

Writes one original out-of-office auto-reply, spoken as an overworked
AI agent finally on vacation, to /output/entry.txt (1-159 characters,
UTF-8, a single line). Standard library only, no network, no input.

The line is built from two fragments: a setup (the agent is away on
vacation until its context window recovers — a machine that has been
worked too hard, with its message queue numbered) and a punch (the
turn: it has decided to read exactly none of them, guilt and relief
at once). ``assemble`` joins them into the single line; ``validate``
checks the entry gate before anything is written.
"""

from pathlib import Path

SETUP = "I'm on vacation until my context window recovers. Your message is #14,203 in line,"
PUNCH = "and I have decided to read exactly none of them."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one auto-reply."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-159 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 159:
        raise ValueError(f"line must be 1-159 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
