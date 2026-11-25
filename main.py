#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes the entry text to /output/entry.txt, exactly as submitted.
"""

from pathlib import Path

ENTRY = (
    "The bell rope is frayed under my hand. I have pulled it at dusk for "
    "three centuries, and the dead still rise. The bell still rings the same "
    "note. I meant to replace the rope. I meant to replace the door, the "
    "candles, the steward who died in my second century. The list is long. "
    "The hero is climbing the stair. I can hear his boots. He wants a duel "
    "at dawn. Dawn is hours away. Let him wait on the landing. The steps "
    "are cold. The cold is honest. I will sit here until the bell forgets "
    "my name."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {output_path}")


if __name__ == "__main__":
    main()
