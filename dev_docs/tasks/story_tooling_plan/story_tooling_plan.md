---
type: epic
title: Story-run tooling (prose lint, a branch per story, role-based agents)
status: active
created: 2026-10-06
---

# Story-run tooling

**Goal:** implement [the story-tooling design](../../designs/2026-10-06-story-tooling.md)
so the next story run gets three things from the repo instead of from the
orchestrator: prose-rule checks, commits that the hook system lets through,
and subagent dispatch with the model fixed per role.

**Scope and non-goals:**
- **In:**
  - the prose linter, its rule data, waivers and tests;
  - `just check`, `just lint` and `just install-hooks`, plus the pre-commit
    shim;
  - six role agent definitions;
  - stage files, and the `PROCESS.md` refactor that goes with them;
  - documenting the branch-per-story flow;
  - graduating the design.
- **Not in:**
  - the story-facts ledger;
  - separate drafter's-notes files;
  - `scripts/status.py`;
  - keeping the banned list from the drafter;
  - CI. The repo has no remote.
  - Documenting the autonomous overnight mode, where the orchestrator stands
    in for the human at gates. Calibration-01 used it, but it conflicts with
    `AGENTS.md`'s gate rule and needs a design of its own.

**Before task 1:** commit this plan to the branch, so an agent picking it up
from a fresh worktree can see it.

**Approach:** the order is linter → wiring → agents → stage files →
graduation. The linter comes first because `just check` and the hook need
something to run. Agent definitions come before stage files because each
stage file names the role it dispatches. Each task is one commit on
`bestdan/story-tooling`. The repo has no remote, so there are no PRs. The
branch lands on `main` by fast-forward after the last task.

## Tasks

1. [[story_tooling_task_1]]: the prose linter (`prose-rules.toml`,
   `lint_prose.py`, waivers, tests), tuned against calibration-01.
2. [[story_tooling_task_2]]: the `justfile` and pre-commit shim, plus the
   branch-per-story flow in `AGENTS.md`.
3. [[story_tooling_task_3]]: six role agent definitions in `.claude/agents/`,
   with the disclaimer moved out of the persona files.
4. [[story_tooling_task_4]]: stage files in `process/stages/`, and a
   `PROCESS.md` refactor covering the overview, the layout and the links.
5. [[story_tooling_task_5]]: graduation. Write the decision records and
   conventions, delete the design and this plan, then land.

## Decided

- **The shared `dev-docs-layout.py` checker runs in `just check`.** The
  human approved this on 2026-10-06. Task 2 resolves the plugin root and fails
  if it can't.
