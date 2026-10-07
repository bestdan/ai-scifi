---
title: Proxy gate mode — brief field, AGENTS rule, per-stage gate lines, STATUS logging
priority: high
size: 5
status: new
created: 2026-10-06
source_branch: bestdan/feedback-takeaways
parent: feedback_takeaways
is_blocked_by: feedback_takeaways_task_5
related_files:
  - templates/brief.md
  - templates/status.md
  - AGENTS.md
  - process/stages/02-audit.md
  - process/stages/03-synthesize.md
  - process/stages/04-build.md
  - process/stages/05-structure.md
  - process/stages/08-revise.md
  - process/stages/09-polish.md
expires: 2026-12-06
tags: [process, gates]
---

Part of [[feedback_takeaways_plan]].

## Context

**Design section:** "7. The proxy gate mode". This task covers everything in
that section except the stage 10 debrief, which is task 7.

**The human's decision** (`human-feedback.md` §5.8): the orchestrator acts
as proxy and the human reads blind. Every gate from stage 2 onward shows the
premise, so in proxy mode the human holds only two things:
- the brief;
- landing, after the debrief.

**Where the human-only gate wording lives today:**
- `AGENTS.md`: "The human decides at every gate."
- **Stage files:** each Gate line, for example "the human approves the plan"
  in 08 and "the human signs off" in 09. The design's new wording is
  "decides every gate". Searching for the old phrase "decides at every gate"
  would therefore pass vacuously, so the check below searches the
  stage-file wording instead.

**Ordering:** task 5 edits `brief.md` and `03-synthesize.md` first.

## Task

1. **`templates/brief.md`:** add a **Gates** field, `human` or `proxy`, with
   `proxy` as the default.
2. **`AGENTS.md`:**
   - Replace "The human decides at every gate" with the design's gate-mode
     rule. Landing stays human, after the debrief.
   - Add the no-spoiler rules:
     - the run is unattended;
     - the slug and branch are chosen at stage 0 from the brief and never
       renamed;
     - commit messages name the stage, not the premise;
     - the end-of-run message says only where the story is.
   - Add `comprehension-grader` to the role list in the dispatch section.
3. **The Gate lines in stage files 02, 03, 04, 05, 08 and 09:** reword each
   one by mode. In `human` mode, the human does X. In `proxy` mode, the
   orchestrator does X and logs it. 09's sign-off in proxy mode marks the
   story ready, and landing stays human.
4. **`process/stages/03-synthesize.md`:** in proxy mode, get an
   `agent-guidance:consultant` second opinion before choosing the premise.
5. **`templates/status.md`:**
   - Add a **Gate mode** line.
   - Give the gate-decisions table columns for **Reasons** and **Runner-up**.
   - Add a **Gate failures** section, which task 2's loop cap writes to.
   - Add a proxy-mode reminder: the human shouldn't open the story
     directory until they have read the story.

## Acceptance Criteria

- **Code-enforced:**
  - `just check` passes.
  - `tests/test_process.py` asserts that every Gate line in 02–09 mentions
    both modes. Equivalently, `rg "the human (approves|signs off|calls|picks|reads)" process/stages`
    only matches lines that also name `human` mode.
- **User-run:**
  - Read `AGENTS.md`'s gate rule cold. Proxy mode should be unambiguous, and
    landing should clearly stay human.
