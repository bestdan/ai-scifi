---
type: epic
title: Feedback takeaways (payoffs, comprehension gate, proxy gates)
status: active
created: 2026-10-06
---

# Feedback takeaways

**Goal:** implement
[the feedback-takeaways design](../../designs/2026-10-06-feedback-takeaways.md),
so the next story is legible to a blind reader. It covers:

- making every inference pay off on the page;
- an outsider-graded comprehension gate that stops polish;
- a rubric that separates what a reader felt from what they understood;
- a polish stage that protects good lines;
- length set by how much the premise has to carry;
- a proxy-gate mode for blind reading.

**Scope:**
- **In:** everything in the design's Proposal and Graduation sections.
- **Not in:**
  - revising Raking Light;
  - the story-facts ledger, drafter's-notes files and `status.py`, unless
    task 1 folds the facts ledger into the payoff ledger;
  - a name-density lint, which the design dropped;
  - any change to `stories/calibration-01/`.

**Before task 1:** commit this plan to the branch, so an agent picking it up
from a fresh worktree can see it.

**Approach:**
- **Order.** Writing rules and templates come first (task 1), because the
  gate grades against the ledger they define. Then the gate (task 2), which
  defines the grader's outputs. Then the rubric that consumes those outputs
  (task 3). Then polish, length and proxy mode, which edit the remaining
  stage files.
- **Shared files.** Tasks that edit the same stage file are chained, so no
  two touch one file in parallel.
- **Landing.** Each task is one commit on `bestdan/feedback-takeaways`. The
  branch lands by fast-forward after task 8.

## Tasks

The chain runs 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8. Task 5 also depends on task 1.
The order is close to linear because most tasks edit shared stage files and
tests.

1. [[feedback_takeaways_task_1]]: the payoff ledger and the writing rules
   (style guide, bible and outline templates, stages 04, 05, 06 and 08).
2. [[feedback_takeaways_task_2]]: the comprehension gate. A two-turn First
   Reader, whose questions appear only in 07, and a new
   `comprehension-grader` that also scores who's who. Wired into 07–09, with
   a loop cap.
3. [[feedback_takeaways_task_3]]: the three-part rubric and axis mapping,
   the critique template, and stage 07 scoring.
4. [[feedback_takeaways_task_4]]: polish protects. A protect list, no cut
   quota, and a reworded spot-check.
5. [[feedback_takeaways_task_5]]: length follows load. A length range, a
   load line, and range-aware stages 01, 02, 03 and 06.
6. [[feedback_takeaways_task_6]]: proxy gate mode. The brief field, the
   `AGENTS.md` rule, gate lines by mode in 02–09, and `STATUS.md` logging.
7. [[feedback_takeaways_task_7]]: the stage 10 debrief. Its template and
   stage file, plus stage 10 and the new layout paths in `PROCESS.md`.
8. [[feedback_takeaways_task_8]]: graduation. Two decision records, delete
   the design and this plan, then land.

## Decided

- **Stakes are made explicit before the climax**, not just by the end. The
  human confirmed this on 2026-10-06.
