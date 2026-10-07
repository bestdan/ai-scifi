---
title: Graduate the design and land the branch
priority: medium
size: 2
status: new
created: 2026-10-06
source_branch: bestdan/feedback-takeaways
parent: feedback_takeaways
is_blocked_by: feedback_takeaways_task_7
related_files:
  - dev_docs/decisions/
  - dev_docs/designs/2026-10-06-feedback-takeaways.md
  - dev_docs/tasks/feedback_takeaways_plan/
  - dev_docs/README.md
expires: 2026-12-06
tags: [docs, cleanup]
---

Part of [[feedback_takeaways_plan]].

## Context

**Decision records.** The design's Graduation section names three. This task
writes **two**, deliberately:

- **The comprehension gate.** This record also holds two of the design's
  other decisions: that the First Reader stays on sonnet, and that
  understanding is scored only by an outsider. All three share one revisit
  trigger.
- **Proxy gates.**

The gate record notes this deviation from the design. The record format,
including `## Revisit when`, is in `dev_docs/decisions/README.md`.

**Deleting the design.** A fast-forward makes no commit on `main`, so the
design and this plan are deleted in the branch's own last commit.

**Landing:**
- `ExitWorktree` needs an unsandboxed run, because `.claude/agents/` is
  tracked.
- A worktree-isolated session can't run git against the main checkout, so
  exit first.
- If `main` has moved, rebase inside the worktree first. Delete any
  `__pycache__` directories before rebasing.

## Task

1. **Write two decision records:**
   - **`dev_docs/decisions/2026-10-06-comprehension-gate.md`:** the two-turn
     read, outsider grading with no orchestrator raises, the reader staying
     on sonnet, and understanding scored only by the outsider. Its
     `## Revisit when`: a reader and grader pass, but the human misses on
     calibration-02's debrief, using the same questions.
   - **`dev_docs/decisions/2026-10-06-proxy-gates.md`:** proxy as the
     default, landing kept human, and hidden-premise gates rejected. Its
     `## Revisit when`:
     - the human wants to steer a premise again;
     - or a proxy run produces a story the debrief rejects at the premise
       level.
2. **Delete the design and this plan.** Update `dev_docs/README.md` if
   `tasks/` is now gone. Commit.
3. **Land:**
   1. `ExitWorktree` with `keep`.
   2. From the main checkout, run
      `git merge --ff-only bestdan/feedback-takeaways`.
   3. Run `dli check`.
   4. Remove the worktree with the plugin's `worktree-remove.sh`, using its
      literal path, unsandboxed.

## Acceptance Criteria

- **Code-enforced:**
  - `dev-docs-layout.py` passes.
  - `dli check` passes on `main`.
- **User-run:**
  - `git log --oneline main` shows the plan's commits with no merge commit.
