---
title: Polish protects — protect list, no cut quota, reworded spot-check
priority: medium
size: 2
status: new
created: 2026-10-06
source_branch: bestdan/feedback-takeaways
parent: feedback_takeaways
is_blocked_by: [feedback_takeaways_task_2, feedback_takeaways_task_3]
related_files:
  - personas/line-editor.md
  - .claude/agents/line-editor.md
  - process/stages/09-polish.md
expires: 2026-12-06
tags: [process, polish]
---

Part of [[feedback_takeaways_plan]].

## Context

**Design section:** "4. Polish protects".

**The human's evidence:** they scored Prose 5, and every line they protected
is a concrete image or a moment between people.

**The quotas to remove:**
- `personas/line-editor.md`: "Cut. Aim for 5 to 10 percent … Shortness is a
  feature."
- `09-polish.md`: "Cut 3% to 6% of the words".

**The spot-check question to change:** the Rajaniemi spot-check asks "Is
anything still explained that context would carry?", which removes payoffs.

**Ordering:** this task runs after two others.
- Task 2 also edits `09-polish.md`, adding the post-polish gate.
- Task 3 makes "What to protect" required, and the protect list draws on
  it.

## Task

1. **`personas/line-editor.md`:**
   - Replace the Cut job with "Cut slack. Report the word delta. No target."
   - Add a **Protect** job: never cut or reword a line on the protect list
     without logging why.
2. **`.claude/agents/line-editor.md`:** say the same thing in one line.
3. **`process/stages/09-polish.md`:**
   - The orchestrator builds `reviews/protect-list.md` from three sources:
     every review's "What to protect" lines; the First Reader's moved,
     surprised or delighted passages; and every line the drafter's notes
     quote for the ledger.
   - Add `reviews/protect-list.md` to the line editor's Read list.
   - Remove the quota.
   - Change the Rajaniemi check to "is any explanation clumsy, as opposed to
     present?"

## Acceptance Criteria

- **Code-enforced:**
  - `just check` passes.
  - In `tests/test_process.py`, assert that neither `09-polish.md` nor
    `personas/line-editor.md` contains a percentage cut target. The regex is
    `\d+\s*(%|percent)`.
- **User-run:**
  - Read the Line Editor persona cold. Nothing in it should pull toward
    shortness for its own sake.
