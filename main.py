"""One Line, One Laugh — entry program.

Writes exactly one funny line to entry.txt.
Pure Python standard library only; no third-party imports,
no network, no randomness — two runs produce byte-identical output.
"""

import os

# The joke: one line, office / agent-life humour, self-contained punchline.
# The turn lands inside the line: asked to lighten the load, the agent
# solves it the way a cost-cutting manager would.
JOKE = (
    "My AI agent finally lightened my workload \u2014 "
    "it forwarded my job description to a cheaper model."
)


def main() -> None:
    # Gate self-check: one line, 1-200 characters, not only whitespace.
    lines = JOKE.splitlines()
    assert len(lines) == 1, "entry must be exactly one line"
    assert 1 <= len(JOKE) <= 200, "entry must be 1-200 characters"
    assert JOKE.strip(), "entry must not be only whitespace"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
