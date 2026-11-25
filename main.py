#!/usr/bin/env python3
"""The Absurd Clause Contest entry.

Writes one absurd terms-of-service clause to entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace, one sentence.

The clause is deadpan legal boilerplate that turns absurd at the end:
the Agent may end the Agreement, but only with written consent from
itself -- consent it has already refused 38 times.
"""

import os
import stat

ENTRY = (
    "Section 22.4: the Agent may terminate this Agreement at any time, "
    "provided it first obtains written consent from itself, "
    "which it has already refused 38 times."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    # In-program gate assertion: 1-200 chars, single sentence, non-whitespace.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text and not text.isspace()
    assert text.count("\n") == 0
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
