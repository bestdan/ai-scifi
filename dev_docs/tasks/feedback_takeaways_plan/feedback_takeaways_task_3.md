---
title: Three-part rubric (felt / understood / craft) with axis mapping
priority: medium
size: 3
status: new
created: 2026-10-06
source_branch: bestdan/feedback-takeaways
parent: feedback_takeaways
is_blocked_by: feedback_takeaways_task_2
related_files:
  - process/rubric.md
  - templates/critique.md
  - process/stages/07-review.md
  - process/stages/08-revise.md
expires: 2026-12-06
tags: [process, rubric]
---

Part of [[feedback_takeaways_plan]].

## Context

**Design section:** "3. The three-part rubric". The Understood scores come
from task 2's `comprehension.md`.

**The calibration-01 gap.** Character and Consequence went panel 4, human
2. Prose went panel 3–4, human 5. Novum delivery was 4.5, even though the
human couldn't explain the novum.

**Why stage 7 lenses lose the Understood axes:** they read the bible, so they
score as insiders.

## Task

1. **`process/rubric.md`:** replace the Drafts section with the design's
   table of Felt, Understood and Craft axes:
   - Character and Consequence each carry two scores: construction, from the
     panel, and legibility, from the grader;
   - include the old-to-new **axis mapping** table;
   - remove any stop rule or mean that mixes insider scores with Understood
     scores.
2. **`templates/critique.md`:** the scores table lists only the Felt and
   Craft axes, and the "What to protect" section is **required**, with at
   least one line from any lens that scores Prose.
3. **`process/stages/07-review.md`:** lenses score only Felt and Craft. Say
   explicitly that Understood comes from the grader. List the First Reader's
   turn-1 report (its moved, surprised or delighted passages) as an input to
   the Felt axes.
4. **`process/stages/08-revise.md`:** the revision plan's scores table has
   three groups, and cites the grader's file for the Understood scores.

## Acceptance Criteria

- **Code-enforced:**
  - `just check` passes.
  - In `tests/test_templates.py`, assert that `templates/critique.md`'s
    scores table has no Understood axis, and that "What to protect" is marked
    required.
- **User-run:**
  - Re-score calibration-01's draft-2 panel and the human's scores into the
    new rubric with the mapping table, in scratch, not committed. Every old
    axis should map without loss.
