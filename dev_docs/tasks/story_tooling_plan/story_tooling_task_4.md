---
title: Stage files and a PROCESS.md refactor
priority: medium
size: 5
status: new
created: 2026-10-06
source_branch: bestdan/story-tooling
parent: story_tooling
is_blocked_by: [story_tooling_task_2, story_tooling_task_3]
related_files:
  - process/PROCESS.md
  - process/stages/
  - AGENTS.md
  - stories/calibration-01/
  - personas/line-editor.md
expires: 2026-12-06
tags: [tooling, process]
---

Part of [[story_tooling_plan]].

## Context

In calibration-01, every stage's task text was written into a fresh prompt,
36 times in all. Much of that text overlapped with `PROCESS.md`'s stage
sections. The actual prompts are recoverable from this session's transcript,
or can be reconstructed from the artifacts each stage produced under
`stories/calibration-01/`.

The design puts task text in `process/stages/NN-<name>.md` and keeps
`PROCESS.md` as the overview: who works at each stage, what it produces, the
gate, and the default panels. The story layout gains the paths calibration-01
invented mid-run:
- `03-critique/`, `04-critique/` and `05-critique/`;
- `reviews/polish-*.md` and `reviews/polish-changelog.md`;
- `MORNING.md`;
- `*.epub`;
- `lint-waivers.toml`.

## Task

1. Write `process/stages/01-ideate.md` through `09-polish.md`. Each file holds:
   - the role and the default lenses;
   - the inputs;
   - the task text, carrying over the stage-specific questions that worked in
     calibration-01;
   - the output path;
   - the template;
   - the reply format;
   - the line "dispatch without `model:`".

   The drafter's stage file (06) requires it to run `just lint` on its draft
   before hand-back. Stage 8 (revise) covers both the orchestrator's triage and
   the drafter's revision. Note that the drafter is resumed with SendMessage
   when its earlier context is still available.
2. Refactor `process/PROCESS.md` so each stage section keeps who, output and
   gate plus a link to its stage file. Move the task prose out. Update the
   story layout. Point stage 9 at `just lint` and `prose-rules.toml` rather than "every
   item in `process/style-guide.md`". Do the same in
   `personas/line-editor.md:8-9`.
3. Update the dispatch section of `AGENTS.md`. Replace the prompt template
   with the role, lens and stage form from the design.

## Acceptance Criteria

- **Code-enforced:**
  - `just check` still passes.
  - Every stage file that `PROCESS.md` links to exists. A
    `test_process_links` check in `tests/` asserts this.
- **User-run:**
  - Read `PROCESS.md` cold. Each stage should be clear in under a minute,
    with no task text duplicated between `PROCESS.md` and the stage files.
