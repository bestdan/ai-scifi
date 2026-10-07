---
created: 2026-10-06
status: accepted
convention: ../../AGENTS.md
---

# Each story is written on its own branch and lands by fast-forward

## Context

The user's global pre-commit hook (`~/src/dotfiles/git/hooks/pre-commit`)
refuses commits on `main` before it delegates to any repo-local hook. The
calibration-01 story was written on `main` because the human authorised it,
so all 15 of its commits used `--no-verify`. A local prose-lint hook would
therefore never have run. Story runs also span several sessions, and they
may overlap with tooling work.

## Decision

Every story is written on `bestdan/story-<slug>` in its own worktree, which
`EnterWorktree` creates with `name: story-<slug>`. Commits are plain. At the
end of each session, `ExitWorktree` removes the worktree and keeps the
branch. The next session's `EnterWorktree` with the same name re-attaches the
branch. After the human signs off, the branch lands with
`git merge --ff-only` from the main checkout, rebased first if `main` has
moved. Tooling changes follow the same flow on their own `bestdan/<name>`
branches.

## Consequences

- Good, because the repo's pre-commit hook runs on every story commit. The
  hook strictly lints any staged `final.md`.
- Good, because concurrent story runs and tooling branches can't collide in
  one working tree.
- Good, because it needs no change to the user's dotfiles.
- Bad, because landing is a manual step from the main checkout. A
  worktree-isolated session can't run git against the main checkout.
- Bad, because once `.claude/agents/` is tracked, `ExitWorktree` needs an
  unsandboxed run: the sandbox protects that path.

## Revisit when

- The repo gains a remote, and PR-based merging becomes possible.
- The global hook gains a per-repo opt-out, and story isolation stops
  mattering.

## Confirmation

The global hook refuses commits on `main`, and the repo's pre-commit hook
(`scripts/hooks/pre-commit`, installed by `just install-hooks`) lints on every
other branch.

## Alternatives

- **A per-repo opt-out in the global hook:** it needs a dotfiles change, and
  it leaves concurrent story runs on `main` with nothing isolating them.
