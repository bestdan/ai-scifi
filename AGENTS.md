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

## Dispatching a persona agent

Use this prompt shape. The agent writes its own output file, so parallel
agents never collide.

```
You are working as the <Lens Name> editorial lens on a science-fiction story.

1. Read personas/<name>.md. It defines your preoccupations, the questions you
   ask and your blind spots. Work from that lens, and state your blind spots
   rather than pretending to cover them.
2. Read process/style-guide.md and process/rubric.md.
3. Read these story inputs: <list of files in stories/<slug>/>.
4. Task: <stage-specific task, from PROCESS.md>.
5. Write your output to stories/<slug>/<path>, using templates/<template>.md.

Don't claim to be the real author or quote them. Be specific: cite lines,
scenes or idea cards. Disagreeing with the other lenses is your job.
```
