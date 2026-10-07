---
title: justfile, pre-commit shim, and the branch-per-story flow in AGENTS.md
priority: high
size: 3
status: new
created: 2026-10-06
source_branch: bestdan/story-tooling
parent: story_tooling
is_blocked_by: story_tooling_task_1
related_files:
  - justfile
  - scripts/hooks/pre-commit
  - AGENTS.md
  - /home/dan/src/dotfiles/git/hooks/pre-commit
  - /home/dan/src/dotfiles/git/hooks/_delegate
expires: 2026-12-06
tags: [tooling, git]
---

Part of [[story_tooling_plan]].

## Context

The global hooks (`~/src/dotfiles/git/hooks/pre-commit` and `_delegate`) run
a repo-local hook only if `$(git rev-parse --git-common-dir)/hooks/<name>` is
a regular executable file. That path resolves to the main checkout's `.git/`
from any worktree. The global pre-commit blocks `main` before it delegates.
`dli check` auto-detects a `just check` recipe.

Read the design section "2. A branch per story" for the shim's rationale. A
symlink into a worktree dangles after the worktree is torn down, and the
delegate then skips the hook without saying so.

## Task

1. Create a `justfile` with these recipes:
   - `check`: run every test, with `python3 -m unittest discover -s tests`; run `lint_prose.py` on every
     `stories/*/final.md`; run the shared `dev-docs-layout.py` checker. Resolve the plugin root with
     `"$HOME/src/dotfiles/agents/agent-guidance-dir.sh"`. That's the
     resolver the dotfiles convention names. As a fallback, use
     `jq -r '.plugins["agent-guidance@agent-guidance"][0].installPath'
     ~/.claude/plugins/installed_plugins.json`. If neither resolves, fail;
     don't skip.
   - `lint *FILES`: run the linter strictly on the files given.
   - `install-hooks`: write the shim (step 3) to the common git dir's
     `hooks/pre-commit` and `chmod +x` it. The common git dir is the main checkout's `.git/hooks/`,
     which the review didn't write-probe. If the sandbox denies the write,
     run it unsandboxed.
2. Write `scripts/hooks/pre-commit`. It lints staged `stories/*/final.md`
   files, read with `git diff --cached --name-only --diff-filter=ACM`, and exits
   non-zero on failure. Spell out `python3`; don't rely on any alias.
3. Write the shim. It's a short `sh` script that runs
   `"$(git rev-parse --show-toplevel)/scripts/hooks/pre-commit"` if that file
   exists, and otherwise prints a one-line warning and exits 0. The hook
   script calls `python3` explicitly, with no aliases. Run
   `just install-hooks`.
4. Add to `AGENTS.md`, under "Ground rules", two lines on the branch-per-story
   flow:
   - **Start:** `EnterWorktree` with `name: story-<slug>`.
   - **Sessions and landing:** plain commits; `ExitWorktree` at the end of each
     session; land by `git merge --ff-only` from the main checkout once the
     human signs off; rebase if `main` has moved. Note that `ExitWorktree`
     needs an unsandboxed run once `.claude/agents/` is tracked (see task 3).

   Point at the global worktree rules rather than restating them.

## Acceptance Criteria

- **Code-enforced:**
  - `dli check` (that is, `just check`) passes on this branch.
  - Stage a deliberately banned phrase in `stories/zz-scratch/final.md`.
    `git commit` is refused by the local hook, which lints the staged index
    version (`git show :<path>`) rather than the working file. Delete the
    scratch story afterwards.
  - With only a draft staged, `git commit` succeeds.
- **User-run:**
  - `just install-hooks` is idempotent: running it twice leaves a single shim.
