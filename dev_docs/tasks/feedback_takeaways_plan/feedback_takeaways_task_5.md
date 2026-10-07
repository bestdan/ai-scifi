---
title: Length follows load — range in the brief, load line, range-aware stages
priority: medium
size: 3
status: new
created: 2026-10-06
source_branch: bestdan/feedback-takeaways
parent: feedback_takeaways
is_blocked_by: [feedback_takeaways_task_1, feedback_takeaways_task_4]
related_files:
  - templates/brief.md
  - process/stages/01-ideate.md
  - process/stages/02-audit.md
  - process/stages/03-synthesize.md
  - process/stages/06-draft.md
  - process/PROCESS.md
expires: 2026-12-06
tags: [process, length]
---

Part of [[feedback_takeaways_plan]].

## Context

**Design section:** "6. Length follows load".

**What happened in calibration-01:** the brief set 2,500 words, below
`PROCESS.md`'s 3,000-word floor. The premise carried two nova plus a twist.

**The heuristic:** 3,000 words plus about 1,500 for each novum or twist after
the first, which gives 6,000 for calibration-01. It rests on one data point,
so label it a heuristic wherever it appears.

**Ordering:** this task runs after two others.
- Task 1 also edits `06-draft.md`.
- Task 4 also edits `tests/test_process.py`.

## Task

1. **`templates/brief.md`:** replace the single length with a **length
   range**, and add a waiver line for going below the floor.
2. **`process/stages/01-ideate.md`:** say "the brief's length range", not
   "the target length". **`process/stages/02-audit.md`:** judge Yield at the
   range's midpoint.
3. **`process/stages/03-synthesize.md`:**
   - Each premise gets a **Load** line (nova and twist) and an **estimated
     minimum** from the heuristic.
   - The gate rejects or narrows any premise whose minimum is above the
     range's top.
4. **`process/stages/06-draft.md`:** the hard ceiling becomes the top of the
   range. Remove the "115% of the target" fallback.
5. **`process/PROCESS.md`:** the stage 0 note and the Lengths table say the
   brief gives a range, and that going below the floor needs a waiver line.

## Acceptance Criteria

- **Code-enforced:**
  - `just check` passes.
  - In `tests/test_process.py`, assert that no stage file still contains
    "target length" or "115%".
- **User-run:**
  - Apply the stage 3 load line to calibration-01's premise B. It should
    give 6,000 as the minimum.
