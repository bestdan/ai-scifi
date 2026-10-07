---
created: 2026-10-06
status: accepted
convention: ../../process/PROCESS.md
---

# Agents are defined per role, with the model fixed in each definition

## Context

calibration-01 dispatched 36 subagents. Each one got a hand-written prompt
that repeated the persona path, the reading list, the impersonation
disclaimer, the output path and the reply format. The model policy (opus for
creative work, sonnet for critique) lived only in the orchestrator's choice of
`model:` on each call. The same lens ran on opus for ideation and on sonnet
for critique.

## Decision

`.claude/agents/` defines six roles: `lens-ideator`, `cartographer`, `drafter`
and `line-editor` on opus, and `lens-critic` and `first-reader` on sonnet.
Each definition fixes its role's model and tools and states the standing
rules once. The lens is named in the prompt's first line (`Lens: <name>`). The
persona content stays in `personas/`. Each stage's task text lives in
`process/stages/`. A dispatch names the role, the lens and the stage file,
and passes no `model:`.

## Consequences

- Good, because the model policy is on disk, and `tests/test_agents.py`
  checks it.
- Good, because a dispatch is a few lines rather than a few hundred tokens,
  so prompts can't drift apart.
- Good, because harnesses without agent definitions (Codex) can still read
  the personas.
- Bad, because the definitions load only in a session started from a
  checkout that holds them. Entering a worktree mid-session doesn't load
  them. That was verified 2026-10-06, and the fallback is
  `claude -p --agent <role>`.
- Bad, because "the lens as an argument" is only a prompt convention. No
  harness mechanism enforces it.

## Revisit when

- The harness changes what the `opus` and `sonnet` aliases resolve to. That
  is intended, but each role's model should be re-checked against the
  creative/critique split.
- The harness supports parameterised agent definitions. The lens could then
  become a real argument.
- A role needs two models in practice. That would argue for splitting the
  role, not for overriding `model:` per call.

## Confirmation

`tests/test_agents.py` pins the role set, the frontmatter fields and each
role's model. `tests/test_process.py` checks that every stage file names a
known role and carries the no-`model:` line.

## Alternatives

- **One definition per lens:** every lens needs two models, which means
  either duplicate definitions or a `model:` override on every call.
- **Moving the persona content into the definitions:** it locks the personas
  to one harness.
