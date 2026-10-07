---
title: Stage 10 debrief — template, stage file, PROCESS.md stage 10 and layout
priority: high
size: 3
status: new
created: 2026-10-06
source_branch: bestdan/feedback-takeaways
parent: feedback_takeaways
is_blocked_by: feedback_takeaways_task_6
related_files:
  - templates/debrief.md
  - process/stages/10-debrief.md
  - process/PROCESS.md
  - tests/test_process.py
  - stories/calibration-01/human-feedback.md
expires: 2026-12-06
tags: [process, debrief]
---

Part of [[feedback_takeaways_plan]].

## Context

**Design section:** "7. The proxy gate mode", the debrief part.

**The template** is modelled on `human-feedback.md`'s structure. Its
interview opens with the seven questions from `07-review.md`'s
`## Comprehension questions` (task 2), word for word, so the human's answers
can be compared with the reader's. It avoids questions that reveal
details: calibration-01 asked "what had to happen when the nine days ran
out", which gave one away.

**`tests/test_process.py` today:**
- It asserts exactly 9 stage links.
- `test_stage_files_dispatch_known_roles_without_model` requires every stage
  file to name a role and carry "pass `model:`". A debrief dispatches no
  agent, so that test has to change.

**`PROCESS.md` today:** it says "Nine stages" and "Each stage that dispatches
agents has a stage file".

## Task

1. **`templates/debrief.md`**, with this fixed order:
   1. the unprimed interview, opening with the seven questions word for word;
   2. rubric scores on the three-part rubric (task 3);
   3. the run's own open questions;
   4. lines to protect;
   5. process takeaways;
   6. an **appendix**: gate failures from `STATUS.md` first (task 2's loop
      cap), then a pointer to `MORNING.md`.
2. **`process/stages/10-debrief.md`:**
   - who runs it: the orchestrator and the human;
   - that it starts only after the human has read the story;
   - that `MORNING.md` is opened only after the interview;
   - that it writes `stories/<slug>/debrief.md`;
   - that landing follows if the human approves.
3. **`process/PROCESS.md`:**
   - say "Ten stages", and reword the stage-file line to "Each stage with
     agent or orchestrator work has a stage file";
   - add a stage 10 row and link;
   - in the intro, say that gates are decided by the brief's mode;
   - add a comprehension-gate note on the stage 7→9 transition;
   - add these paths to the story layout: `reviews/draft-N/comprehension-answers.md`,
     `ledger-rows.md`, `names.md`, `comprehension.md`, `reviews/final/`,
     `reviews/protect-list.md` and `debrief.md`;
   - in the panels table, note the reader's two turns and the grader.
4. **`tests/test_process.py`:**
   - expect 10 links;
   - exempt `10-debrief.md` from the role and model test;
   - assert that `templates/debrief.md` and `10-debrief.md` both contain the
     seven questions, hard-coded, word for word.

## Acceptance Criteria

- **Code-enforced:**
  - `just check` passes.
  - The updated `tests/test_process.py` passes.
- **User-run:**
  - Walk through calibration-01's interview using the new template. No
    question should reveal a detail the story hadn't made explicit.
