---
title: Prose linter with rule data, waivers and tests
priority: high
size: 5
status: new
created: 2026-10-06
source_branch: bestdan/story-tooling
parent: story_tooling
related_files:
  - process/style-guide.md
  - process/prose-rules.toml
  - scripts/lint_prose.py
  - tests/test_lint_prose.py
  - stories/calibration-01/final.md
  - stories/calibration-01/drafts/draft-2.md
  - stories/calibration-01/reviews/draft-2/cartographer.md
  - templates/story-bible.md
expires: 2026-12-06
tags: [tooling, lint]
---

Part of [[story_tooling_plan]].

## Context

The style guide's banned list (`process/style-guide.md`, "The banned list") is
currently enforced only by agents reading it. In calibration-01, the drafter's
self-report was wrong: it reported 3 zinger closers where the Cartographer
found about 8. The design section "1. The prose linter" in
`dev_docs/designs/2026-10-06-story-tooling.md` specifies the rules, the
severities, the output format and the waiver file. Follow it exactly.

Gotchas the design review found:
- "On the way to the surgery" (`final.md:35`) is a literal use and must not
  count as a simile.
- "had not done the sum. She had wanted the seat." (`final.md:91`) must not
  match the contrast rule.
- The zinger rule has to find *trailing short clauses inside long paragraphs*,
  not short standalone paragraphs. A standalone-paragraph version finds 0
  of the Cartographer's 8 in draft 2.
- Python is 3.12, so `tomllib` is in the stdlib. Add no dependencies.
- A **dialogue paragraph** is one that *starts* with a quotation mark. A
  narration paragraph that contains a quote still counts as narration, so it
  is checked.
- **Measured** by the plan review with a comma-split approximation:
  - The 8 Cartographer closers are 3, 5, 5, 7, 8, 8, 9 and 12 words long.
    Flagging 6 of 8 needs N≈8, or N=9 if the line-85 paragraph doesn't count
    as narration.
  - At N=8 the closer counts are about 18 in `final.md`, 21 in draft 2 and 25
    in draft 1, which leaves a thin margin.
  - So the fallback, warn-only with no budget, is a likely outcome and an
    acceptable one.

## Task

1. Create `process/prose-rules.toml` holding:
   - the regexable entries from the style guide's banned list: the phrases,
     the names and the ships;
   - the budget rules: em-dashes in a sliding window, "the way" with its
     literal exclusions, the contrast shape, and the zinger closer;
   - the zinger rule's N and budget.

   Give every rule an `id`, a `severity` and a pattern (or the parameters that
   stand in for one).
2. Edit `process/style-guide.md`. Remove the entries that moved and link to
   `prose-rules.toml` in their place. Change the guide's last banned-list line
   ("The bible or the outline has to name…") to point at
   `lint-waivers.toml`. In `templates/story-bible.md`, make "Rules
   deliberately broken" point at the story's `lint-waivers.toml` for linted
   rules. Keep the prose-only entries (triplets,
   sense lists, the Characters and Plots sections), the positive rules and the
   tone charter. Mention `stories/<slug>/lint-waivers.toml` as the way to break
   a rule on purpose.
3. Write `scripts/lint_prose.py`.
   - **Command line:** `lint_prose.py [--warn-only] FILE...`.
   - **Skip:** headings, the literal `<p align="center">·</p>` line, and
     everything after `## Drafter's notes`.
   - **Waivers:** load `lint-waivers.toml` from the story directory, which is
     the file's parent, or its grandparent for `drafts/*.md`.
   - **Output:** lines of the form
     `path:line: [error|warn|waived] rule-id: "text"`, then a summary of each
     budget's use.
   - **Exit:** 1 on any error or budget overrun, unless `--warn-only` is set.
4. Write `tests/test_lint_prose.py` using `unittest`. It needs:
   - a positive and a negative fixture for each rule;
   - the two literal-use and contrast negatives above;
   - a test for waivers and one for the skip regions;
   - a **recall** test: at least 6 of the 8 closer lines the Cartographer lists
     in `reviews/draft-2/cartographer.md` are flagged in `drafts/draft-2.md`;
   - a **precision** test: `final.md` passes in strict mode.
5. Tune N and the budget for the zinger rule until both the recall and the
   precision tests pass. If no N passes both, set the rule's severity to warn
   with no budget, and say so in the commit message. If `final.md` fails any
   other rule, decide whether the hit is a real miss (fix the story text) or a
   mis-tuned rule (retune it), and record which in the commit message.

## Acceptance Criteria

- **Code-enforced:**
  - `python3 -m unittest tests/test_lint_prose.py` passes.
  - `python3 scripts/lint_prose.py stories/calibration-01/final.md` exits 0.
  - **If the zinger rule has a budget:** the budget is at least
    count(`final.md`) and less than count(draft 1), and
    `lint_prose.py stories/calibration-01/drafts/draft-1.md` exits 1 with a
    zinger-budget overrun.
  - **If the rule fell back to warn-only:** the same command still lists at
    least 6 of the 8 Cartographer closers as warnings. The commit message says
    which branch was taken and gives the measured counts.
- **User-run:**
  - Skim the linter's output on draft 2 and confirm the flagged closers look
    like the ones the Cartographer meant.
