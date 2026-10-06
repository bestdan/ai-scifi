---
created: 2026-10-06
status: proposed
---

# Story-run tooling: prose lint, a branch per story, and role-based agents

A story run currently relies on the orchestrator doing three things by hand,
every time:

- checking prose against the style guide's banned list;
- committing past a global hook that blocks `main`;
- writing every subagent prompt, model choice included.

This design replaces each of them with something on disk:

1. **A prose linter** (`scripts/lint_prose.py`). It reads its rules from a data
   file, honours per-story waivers, and is wired into `just check` and a
   repo-local pre-commit hook.
2. **A branch per story.** Each story is written on `bestdan/story-<slug>` in
   its own worktree, so the global hook passes and the local lint hook runs. A
   finished story lands on `main` by fast-forward.
3. **Agent definitions by role** in `.claude/agents/`, with the model fixed in
   frontmatter, plus **stage files** in `process/stages/` that hold each stage's
   task text. A dispatch is then a role, a lens, and a pointer to a stage file.

This covers findings 1–3 of the mechanical `/retro` run on 2026-10-06 against
the calibration-01 session. That retro was given in conversation and isn't
saved to a file. Its numbering differs from the process retro in
`stories/calibration-01/MORNING.md`.

## What is true today

| Retro finding | Observation | Cost |
|---|---|---|
| 1 | The drafter reported 3 "zinger" paragraph closers in draft 2. The Cartographer listed about 8 (`stories/calibration-01/reviews/draft-2/cartographer.md`). The drafter reported "the way" as fixed, but it still appeared 7 times. | Reviewer lenses grepped by hand in both rounds, and the self-report couldn't be trusted. |
| 1 | The repo has no check command, no pre-commit hook and no CI, so `dli check` finds nothing to run. | No guardrail at all. |
| 2 | `~/src/dotfiles/git/hooks/pre-commit` exits on `main` before delegating to a repo-local hook. All 15 story commits used `--no-verify`. | A local hook would be skipped on every commit. |
| 3 | There were 36 hand-written subagent prompts. Each repeated the persona path, the reading list, the impersonation disclaimer, the output path and the reply format, at about 250–400 output tokens apiece. | Orchestrator tokens, and drift between prompts. |
| 3 | The model policy ("frugal with subagents, generous with creative work") existed only as a `model:` argument the orchestrator chose on each call. | Unenforced, and invisible to a new session. |

Against the proposed rules, as estimated by the design review,
`stories/calibration-01/final.md` currently has:

- 0 em-dashes;
- 3 "the way" similes, plus one literal use ("On the way to the surgery");
- 1 real contrast shape ("That's not argument. That's a heron.");
- 0 banned phrases, names or ships.

## Proposal

### 1. The prose linter

**Rules as data.** The *regexable* entries in the style guide's banned list
move into `process/prose-rules.toml`. That file becomes their single source of
truth, and the style guide links to it. These entries are fixed phrases,
banned names, banned ship names, and the counted patterns listed below. The
rest stays as prose in the style guide, because no regex can judge it: reflex
triplets, sense lists, and the Characters and Plots sections. Python 3.12's
`tomllib` reads the TOML, so the linter has no dependencies.

**Rules** each have an id, a pattern, and a severity:

| Rule | Severity | Definition |
|---|---|---|
| banned phrase | error | Case-insensitive phrase match ("a testament to", …). |
| banned name or ship | error | A whole-word, case-sensitive match, so "Nova" doesn't fire inside "Novak". |
| em-dash pileup | budget | No more than 2 em-dashes in any sliding 300-word window. |
| "the way" simile | budget, 3 per story | Excludes literal uses: "on/by/all the way", "the way to", "the way back/home". |
| contrast shape | budget, 1 per story | Matches "It wasn't/wasn't/isn't/was not X. It was Y." and "That's not X. That's Y." Two adjacent sentences, where the second repeats the first's subject and verb without the negation. "had not done the sum. She had wanted the seat." is a negative fixture: it must not match. |
| zinger closer | budget, tuned | The last sentence or clause of a narration paragraph is short (at most N words, set in the TOML) *and* closes a paragraph of at least 2 sentences. Dialogue paragraphs are skipped. |

A budget rule reports every hit as a warning, and fails only when the count
goes over its budget.

**Tuning the zinger rule.** Two fixtures fix N and the budget:

- **Recall:** the Cartographer's draft-2 closer list. The linter must flag at
  least 6 of those 8 lines in `drafts/draft-2.md`.
- **Precision:** `final.md`, which reviewers accepted. It must pass within the
  budget.

If no value of N satisfies both, the rule ships at warn severity with no
budget, and the commit says so.

**What the linter skips:**

- Markdown headings.
- The literal scene-break line `<p align="center">·</p>`.
- Everything after a `## Drafter's notes` heading.

**Waivers.** The style guide allows any rule to be broken on purpose. A story
records a deliberate break in `stories/<slug>/lint-waivers.toml`, which lists
rule ids, each with a reason. The linter reads the file and reports waived
hits as `waived`. The bible's "Rules deliberately broken" section points to
the waiver file rather than restating it. Waivers also stop an old story from
failing forever when a new rule is added.

**Output.** One line per finding:
`path:line: [error|warn|waived] rule-id: "matched text"`. Then a summary of
each budget's use. The linter exits 1 on any error or any budget overrun. The
`--warn-only` flag always exits 0.

**Where it runs:**

| Where | What | Mode |
|---|---|---|
| `just check` | every `stories/*/final.md`, plus `tests/test_lint_prose.py` | strict |
| `just lint <file>` | any file | strict |
| pre-commit hook | staged `stories/*/final.md` only | strict |
| the drafter, before hand-back | its own draft | strict, and it fixes overruns before review |

Drafts aren't linted at commit time. A draft that breaks the rules is a
legitimate artifact in the story's history, and linting it would only add
noise.

**Tests.** `tests/test_lint_prose.py` uses stdlib `unittest`. It has a
positive and a negative fixture for each rule, the recall and precision
fixtures above, and tests for the waiver and skip behaviour.

### 2. A branch per story

The worktree mechanics follow the global `CLAUDE_ONLY.md` rules (`EnterWorktree`
with `name`, worktrees under `$HOME/src/worktrees/<repo>/`), and this design
doesn't restate them. What's specific to this repo:

- **Start.** `EnterWorktree` with `name: story-<slug>`. That creates the branch
  `bestdan/story-<slug>` from local `main`.
- **Commit.** Plain `git commit`. The global hook passes because the branch
  isn't `main`. `--no-verify` is no longer part of the process.
- **Hook install.** `just install-hooks` writes a small **shim** to
  `.git/hooks/pre-commit`. It's a copied file, not a symlink, because a symlink
  into a worktree dangles once that worktree is torn down, and the global
  `_delegate` would then skip the hook silently. The shim resolves
  `"$(git rev-parse --show-toplevel)/scripts/hooks/pre-commit"` at run time,
  calls `python3` explicitly (no aliases), and prints a one-line warning if the
  script is missing. Global hooks resolve local hooks through
  `--git-common-dir`, so one install covers every worktree.
- **Resume across sessions.** At the end of each session, commit everything,
  then `ExitWorktree`. That removes the worktree and keeps the branch, because
  with no remote the PR lookup fails and `branch-remove.sh` keeps the branch.
  The next session's `EnterWorktree` with the same `name` re-attaches the
  existing branch, with no path prompt. `STATUS.md` on the branch carries the
  story's state between sessions.
- **Land, after the human signs off.**
  1. `ExitWorktree`, because a worktree-isolated session can't run git
     against the main checkout.
  2. From the main checkout, run `git merge --ff-only bestdan/story-<slug>`.
     A fast-forward creates no commit, so neither pre-commit nor
     pre-merge-commit fires. The `post-merge` and `reference-transaction`
     delegates do fire, but they find no local hook and can't block anyway.
  3. If `main` has moved, because a tooling branch or another story landed
     first, the fast-forward is refused. Re-enter the story worktree, run
     `git rebase main`, exit, and fast-forward again.
- **Tooling changes**, such as this one, follow the same flow on their own
  `bestdan/<name>` branches.

### 3. Agent definitions and stage files

Agent definitions are **per role**. The lens is named in the prompt's first
line (`Lens: watts`). That's prompt text, not a harness argument mechanism,
and the definition's body tells the agent to read the persona file it names.

| Definition | Model | Tools | Used for |
|---|---|---|---|
| `lens-ideator` | opus | Read, Write, Glob, Grep | stage 1 |
| `lens-critic` | sonnet | Read, Write, Glob, Grep, WebSearch | stages 3, 4, 5, 7 and 9, and Cartographer critiques |
| `cartographer` | opus | Read, Write, Glob, Grep, WebSearch, WebFetch | stage 2 audit |
| `drafter` | opus | Read, Write, Edit, Glob, Grep, Bash | stages 6 and 8. It needs Bash for `just lint` and `wc` |
| `line-editor` | opus | Read, Write, Edit, Glob, Grep, Bash | stage 9 |
| `first-reader` | sonnet | Read, Write | stage 7 |

Each definition's body states the standing rules once:

- read the persona file;
- read `process/style-guide.md`, except for `first-reader`, whose persona
  rules out craft vocabulary and which must not see the banned list;
- never claim to be, quote, or imitate the author;
- write only to the output path the stage file names;
- reply in the stage file's format.

The impersonation disclaimer then moves out of the 9 persona files and into
these definitions. One line in `AGENTS.md` covers agents that run outside the
definitions.

`personas/` stays the content. The definitions are thin pointers to it, so a
harness without `.claude/agents` support (Codex) can still use the personas.

**Stage files.** `process/stages/NN-<name>.md` holds each dispatching stage
(1–9). Each file gives:

- the role and the default lenses;
- the inputs;
- the task text;
- the output path and template;
- the reply format.

`PROCESS.md` keeps the overview and the gates and links to each stage file.
The task text moves out of `PROCESS.md`, so it exists in one place.
`PROCESS.md`'s story layout gains the paths calibration-01 invented mid-run
(`0N-critique/`, `reviews/polish-*.md`, `MORNING.md`, `*.epub`,
`lint-waivers.toml`). The stage files refer to that layout instead of
restating it.

A dispatch then looks like this:

```
Agent(subagent_type: "lens-critic",
      prompt: "Lens: watts. Stage: process/stages/07-review.md.
               Story: stories/calibration-02. Round: draft-2.")
```

The call passes no `model:`. The stage files say this explicitly, so any
`model:` that does appear reads as a deliberate deviation.

## Decisions

### A branch per story, not a main-branch opt-out

Each story runs on `bestdan/story-<slug>` in its own worktree and lands by
fast-forward.

**Rejected:** adding a per-repo opt-out to the global hook
(`hooks.allowMainCommits`). That would also let the local hook run, but it
needs a dotfiles change, and it leaves stories on `main` with no isolation
between concurrent runs. A branch per story matches the existing worktree
convention and needs no change outside this repo.

### Agent definitions per role, with the lens in the prompt

**Rejected:** one definition per lens. Every lens needs two models (opus to
ideate, sonnet to critique), so that would mean either duplicate definitions or
a `model:` override on every call. The override is the in-head policy this
design removes.

**Also rejected:** moving persona content into the definitions. That would
lock the personas to one harness.

## Not decided here

- **Out of scope** from the same retro:
  - the story-facts ledger;
  - separate drafter's-notes files;
  - `scripts/status.py`;
  - keeping the banned list away from the drafter. Moving rules into the TOML
    makes that possible, but this design doesn't decide it.
- **Open risks, each verified during implementation:**
  1. **Do project agent definitions load mid-session?** If they don't, the
     definitions can't be exercised in the session that creates them. Test
     them with a `claude -p` run instead.
  2. **Are writes under the repo's `.claude/` sandbox-denied?** (See the
     `sandbox-escapes` skill.) If so, escape only for writing those files.
  3. **The zinger rule may not reach both fixtures at any N.** That case has
     a fallback, described in the proposal.
  4. **Model aliases.** `opus` and `sonnet` resolve to the harness's current
     mapping. That's intended, but recheck it when the harness changes.

## Graduation

- **Decision records** under `dev_docs/decisions/`: one for the branch per
  story, one for role-based agents.
- **Conventions:**
  - `AGENTS.md`: the branch-per-story flow in two lines, plus pointers to
    `.claude/agents/` and `process/stages/`.
  - `process/PROCESS.md`: the story layout, plus links to the stage files.
  - `process/style-guide.md`: a link to `prose-rules.toml` and the waiver file.
- **Delete this design** as the last commit on `bestdan/story-tooling`, before
  it lands. A fast-forward makes no commit on `main`, so the deletion can't
  happen there.
