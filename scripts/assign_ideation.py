"""Give each stage 1 lens a different place to start from.

Every lens is the same generating model, so lenses that read the same brief
converge (process/attractors.md). This draws, for each lens on the stage 1
panel:

- an entry point from its persona's "In ideation" list, preferring the ones
  it has used least in earlier runs;
- a pull from process/reader-profile.md, spread so no pull goes to a second
  lens before every pull has one;
- a stimulus: two items from two different lists in process/stimuli.toml.

The draw is done in code because a model asked to pick at random picks its
favourites. It writes stories/<slug>/01-ideas/assignments.md.

    python3 scripts/assign_ideation.py stories/<slug> [--seed N] [--lenses a,b]
"""

import argparse
import random
import re
import sys
import tomllib
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ROW = re.compile(r"^\| (?P<lens>[a-z-]+) \| (?P<entry>\d+)\. ")


def lens_names(spec: str) -> list[str]:
    """'Asimov, Le Guin' -> ['asimov', 'le-guin'], the persona file stems."""
    return [name.strip().lower().replace(" ", "-") for name in spec.split(",")]


def stage1_panel() -> list[str]:
    text = (REPO / "process" / "PROCESS.md").read_text()
    m = re.search(r"^\| 1 Ideate \| (.+?) \|$", text, re.M)
    if not m:
        sys.exit("assign_ideation: no stage 1 row in process/PROCESS.md")
    return lens_names(m.group(1))


def numbered_items(path: Path, heading: str) -> list[str]:
    """The bold labels of a section's numbered list: `1. **Label.** ...`."""
    text = path.read_text()
    section = re.search(rf"^## {heading}\n(.*?)(?:^## |\Z)", text, re.S | re.M)
    name = path.relative_to(REPO)
    if not section:
        sys.exit(f"assign_ideation: {name} has no '{heading}' section")
    found = re.findall(r"^\d+\. \*\*(.+?)\*\*", section.group(1), re.M)
    if not found:
        sys.exit(f"assign_ideation: {name}'s '{heading}' section lists nothing")
    return [f.rstrip(".") for f in found]


def pulls() -> list[str]:
    return numbered_items(REPO / "process" / "reader-profile.md", "What pulls")


def entry_points(lens: str) -> list[str]:
    return numbered_items(REPO / "personas" / f"{lens}.md", "In ideation")


def format_row(lens: str, entry: str, pull: str, stimulus: str) -> str:
    """One table row; past_entries() reads it back with ROW."""
    return f"| {lens} | {entry} | {pull} | {stimulus} |"


def past_entries(skip: Path) -> Counter:
    """How often each lens has used each entry point in earlier runs.

    Only runs in this checkout count: a story lands on main after the human
    signs off, so parked and in-flight stories on other branches are unseen.
    """
    used = Counter()
    for path in (REPO / "stories").glob("*/01-ideas/assignments.md"):
        if path.resolve() == skip.resolve():
            continue
        for line in path.read_text().splitlines():
            m = ROW.match(line)
            if m:
                used[(m["lens"], int(m["entry"]))] += 1
    return used


def assign(lenses, rng, used):
    stimuli = tomllib.loads((REPO / "process" / "stimuli.toml").read_text())
    pool = pulls()
    order = []
    rows = []
    seen = set()
    for lens in lenses:
        entries = entry_points(lens)
        least = min(used[(lens, i)] for i in range(1, len(entries) + 1))
        choices = [i for i in range(1, len(entries) + 1) if used[(lens, i)] == least]
        entry = rng.choice(choices)
        if not order:
            order = rng.sample(pool, len(pool))
        pull = order.pop()
        # No item goes to two lenses in one run.
        a, b = rng.sample(sorted(stimuli), 2)
        x = rng.choice([s for s in stimuli[a] if s not in seen])
        y = rng.choice([s for s in stimuli[b] if s not in seen])
        seen.update((x, y))
        stimulus = f"{x} × {y}"
        rows.append((lens, f"{entry}. {entries[entry - 1]}", pull, stimulus))
    return rows


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("story", type=Path, help="the story directory, stories/<slug>")
    ap.add_argument("--seed", type=int,
                    help="seed the draw; it reproduces only against the same earlier runs")
    ap.add_argument("--lenses", help="comma-separated lenses, if the brief changes the panel")
    ap.add_argument("--force", action="store_true", help="overwrite an existing file")
    args = ap.parse_args()

    out = args.story / "01-ideas" / "assignments.md"
    if out.exists() and not args.force:
        sys.exit(f"assign_ideation: {out} exists; pass --force to redraw")
    seed = args.seed if args.seed is not None else random.randrange(10**6)
    lenses = lens_names(args.lenses) if args.lenses else stage1_panel()
    rows = assign(lenses, random.Random(seed), past_entries(out))

    lines = [
        "# Stage 1 assignments",
        "",
        f"Drawn by `scripts/assign_ideation.py` with seed {seed}. Each lens writes",
        "its cards from its entry point, aims at least one card at its pull, and",
        "starts from its stimulus. A card may travel far from the stimulus, and",
        "says where it went.",
        "",
        "| Lens | Entry point | Pull | Stimulus |",
        "|---|---|---|---|",
        *(format_row(*row) for row in rows),
        "",
    ]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines))
    print(f"wrote {out} (seed {seed})")


if __name__ == "__main__":
    main()
