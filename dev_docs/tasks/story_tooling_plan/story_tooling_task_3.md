---
title: Role-based agent definitions in .claude/agents/
priority: high
size: 3
status: new
created: 2026-10-06
source_branch: bestdan/story-tooling
parent: story_tooling
related_files:
  - .claude/agents/
  - personas/*.md
  - AGENTS.md
expires: 2026-12-06
is_blocked_by: story_tooling_task_1
tags: [tooling, agents]
---

Part of [[story_tooling_plan]].

## Context

The design section "3. Agent definitions and stage files" gives the six roles,
with each one's model and tools:

| Role | Model |
|---|---|
| `lens-ideator` | opus |
| `lens-critic` | sonnet |
| `cartographer` | opus |
| `drafter` | opus |
| `line-editor` | opus |
| `first-reader` | sonnet |

Frontmatter fields are `name`, `description`, `tools` and `model`. They match
the plugin agent file
`~/.claude/plugins/cache/workflow-skills/workflow-skills/2.78.0/agents/fact-reviewer.md`.

The lens arrives as the prompt's first line (`Lens: <name>`).

There are two risks to verify:

- **Sandbox.** `.claude/agents/` is in the sandbox's deny set; see
  `workflow-skills/2.78.0/scripts/worktree-remove.sh:79-80`. So writing it
  probably needs an unsandboxed call. Once it's tracked, every worktree holds
  protected paths, and a sandboxed `ExitWorktree` is refused and asks for an
  unsandboxed re-run.
- **Loading mid-session.** This session's project directory is the main
  checkout, which has no `.claude/agents/`. So the definitions probably won't
  load mid-session.

Task 1 must land first, because the definitions point at
`process/prose-rules.toml`.

## Task

1. Write the six definitions, one per role, at `.claude/agents/<role>.md`.
   - The body states the standing rules once: read the persona file, read the
     style guide (except `first-reader`), the no-impersonation rule, write only
     to the stage file's output path, and reply in the stage file's format.
   - The lens roles map `Lens: <name>` to `personas/<name>.md`.
   - The role personas (`cartographer`, `first-reader`, `line-editor`) read
     their own files.
   - `drafter` has no persona file and skips that rule.
   - Every role except `first-reader` also reads `process/prose-rules.toml`.
2. Remove the impersonation disclaimer sentence (it sits inside each file's
   opening paragraph) from each of the 9 author
   persona files, since it now lives in the definitions. Leave one line in
   `AGENTS.md` for agents running outside the definitions.
3. Verify loading. Try dispatching `lens-critic` in this session with a
   trivial task. If the harness doesn't know the type, run this from the
   worktree, unsandboxed:
   `claude -p --agent lens-critic --output-format json "Lens: asimov. Reply in one sentence: what is the Asimov lens's job?"`.
   Record the result in the commit message.

## Acceptance Criteria

- **Code-enforced:**
  - Each `.claude/agents/*.md` parses as YAML frontmatter and has `name`,
    `description`, `model` and `tools`.
  - `rg -U "isn't an\s+impersonation" personas/` returns nothing. The
    multiline flag matters, because the disclaimers in `asimov.md` and
    `lem.md` wrap across a line break.
- **User-run:**
  - The `claude -p` JSON's `modelUsage` names a sonnet model, and the reply
    is in role.
