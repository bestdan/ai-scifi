---
title: Graduate the design and land the branch
priority: medium
size: 2
status: new
created: 2026-10-06
source_branch: bestdan/story-tooling
parent: story_tooling
is_blocked_by: [story_tooling_task_2, story_tooling_task_4]
related_files:
  - dev_docs/decisions/
  - dev_docs/designs/2026-10-06-story-tooling.md
  - dev_docs/tasks/story_tooling_plan/
  - dev_docs/README.md
expires: 2026-12-06
tags: [docs, cleanup]
---

Part of [[story_tooling_plan]].

## Context

The design's Graduation section names the outputs: two decision records
(branch per story, role-based agents) and the conventions in `AGENTS.md`,
`PROCESS.md` and the style guide. Tasks 1–4 already wrote those conventions.

A design and a finished plan are transient. Delete both before the branch
lands. A fast-forward makes no commit on `main`, so deleting them has to be the
branch's last commit. The decision-record format and its required
`## Revisit when` section are set by `decisions/README.md` in the
agent-guidance plugin's `dev_docs/`.

## Task

1. Copy the canonical `decisions/README.md` into `dev_docs/decisions/`. Write
   the two records, `2026-10-06-branch-per-story.md` and
   `2026-10-06-role-based-agents.md`, from the design's Decisions section.
2. Update `dev_docs/README.md`: add `decisions/`. Keep `designs/`, since its
   `README.md` stays. Drop `tasks/` once the plan directory is gone. Put model
   alias risk 4 from the design into the role-agents record's
   `## Revisit when` section.
3. Delete `dev_docs/designs/2026-10-06-story-tooling.md` and
   `dev_docs/tasks/story_tooling_plan/`. Commit.
4. Land the branch:
   1. `ExitWorktree`, keeping the branch. This needs an unsandboxed run,
      because `.claude/agents/` is now tracked (see task 3).
   2. From the main checkout, run
      `git merge --ff-only bestdan/story-tooling`.
   3. Run `just install-hooks` there if it isn't already installed.
   4. Run `dli check` on `main`.

## Acceptance Criteria

- **Code-enforced:**
  - `dev-docs-layout.py` passes.
  - `dli check` passes on `main` after the fast-forward.
- **User-run:**
  - `git log --oneline main` shows the tooling commits, with no merge commit.
