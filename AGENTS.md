# Agent instructions — ai-scifi

You are running a fiction-writing pipeline, not a codebase. The process in
`process/PROCESS.md` is the contract; read it before doing any story work.

## Ground rules

- **Every story's state is on disk.** `stories/<slug>/STATUS.md` records the
  current stage, every gate decision and why it went that way, and any open
  questions. Read it first when you resume a story, and update it at every
  gate. Don't rely on conversation memory carrying across sessions.
- **A story is written on its own branch.** Use `EnterWorktree` with
  `name: story-<slug>`, which gives the branch `bestdan/story-<slug>`. The
  global worktree rules cover the rest. Commit normally: the repo's
  pre-commit hook lints any staged `final.md`. `ExitWorktree` at the end of
  each session. Once `.claude/agents/` is tracked this needs an unsandboxed
  run, and the next session's `EnterWorktree` with the same name re-attaches.
- **A story lands only after the human signs off.** From the main checkout,
  run `git merge --ff-only bestdan/story-<slug>`. If `main` has moved, rebase
  the story branch first. `dli check` runs the tests, the prose lint on every
  `final.md`, and the dev_docs layout check. `just lint <file>` lints one
  draft.
- **The human decides at every gate.** Lay out the options and give your
  recommendation, then stop. Don't advance a story past a gate on your own.
- **A persona is a lens, not an impersonation.** When you dispatch a persona
  agent, it reads its `personas/<name>.md` file and works in that role. It
  never claims to be the author, never invents quotes, and never imitates the
  author's prose voice when drafting.
- **One drafter per story.** Ideation and critique run in parallel across
  persona agents. Drafting doesn't: one agent writes the whole draft, so the
  voice holds together. Revisions go through the same agent or through the
  orchestrator.
- **Novelty is the point.** Every idea goes past the Cartographer
  (`personas/cartographer.md`) before synthesis. "It's been done" is the most
  common failure and the costliest to discover late.
- **Follow the tone charter in `process/style-guide.md`.** Stories are for
  enjoyment. Use no stock post-apocalypse or tech dystopia, and no darkness
  as a default. Violence and loss are fine, and so is a hard ending, but a
  bleak world has to be the uncharted novum itself. The opposite failure,
  frictionless utopia, is out too. Every persona works under this charter,
  including the ones whose instincts run bleak (Watts, Lem).
- **The style guide is binding.** `process/style-guide.md` lists the habits of
  machine-written fiction. Every drafting agent and every editing agent reads
  it.

## Dispatching an agent

Agents are dispatched by **role**. Each role is defined in `.claude/agents/`:
`lens-ideator`, `lens-critic`, `cartographer`, `drafter`, `line-editor` and
`first-reader`. The definition fixes the model and the tools, and it holds the
standing rules. **Pass no `model:`.** The task text is in each stage's file
in `process/stages/`, and `process/PROCESS.md` says which role and which
lenses each stage dispatches.

```
Agent(subagent_type: "lens-critic",
      prompt: "Lens: watts. Stage: process/stages/07-review.md.
               Story: stories/<slug>. Draft: 2.")
```

The definitions load from the directory a session **starts** in, so any
session started from the main checkout has them. A session that moves into a
worktree with `EnterWorktree` keeps its launch directory's agent set. If a
type isn't found, run `claude -p --agent <role> …` from a checkout that holds
the definitions.
