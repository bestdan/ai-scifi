---
created: 2026-10-06
status: proposed
---

# Story-run tooling: prose lint, a branch per story, and role-based agents

This design covers retro findings 1–3 from the calibration-01 session.

A story run currently depends on the orchestrator getting three things right
by hand, every time:

- checking prose against the style guide's banned list;
- committing past a global hook that blocks commits on `main`;
- writing every subagent prompt from scratch, model choice included.

This design replaces each of those with something on disk:

1. **A prose linter**, `scripts/lint_prose.py`, which reads its rules from a
   data file and is wired into `just check` and a repo-local pre-commit hook.
2. **A branch per story.** Each story is written on `bestdan/<slug>` in its own
   worktree, so the global hook passes and the local lint hook actually runs.
   The branch is fast-forwarded into `main` when the story is signed off.
3. **Role-based agent definitions** in `.claude/agents/`, with the model fixed
   in each definition's frontmatter, and **stage files** in `process/stages/`
   that hold each stage's task text. A dispatch becomes a role, a lens and a
   stage file.

## What is true today

| # | Observation | Cost |
|---|---|---|
| 1 | The drafter reported 3 short "zinger" paragraph closers in draft 2; the Cartographer counted about 8. "the way" was reported fixed and still appeared about 7 times. | Two reviewer lenses spent part of every review grepping by hand, and the self-report could not be trusted. |
| 1 | The repo has no check command, no pre-commit hook and no CI. `dli check` finds nothing to run. | No guardrail at all. |
| 2 | The global hook `~/src/dotfiles/git/hooks/pre-commit` exits on `main` *before* it delegates to a repo-local hook. All 15 story commits used `--no-verify`. | Any local hook added for finding 1 would be skipped on every commit. |
| 3 | There were 36 hand-written subagent prompts. Each repeated the persona path, the reading list, the impersonation disclaimer, the output path and the reply format, at roughly 250–400 output tokens apiece. | Orchestrator output tokens, and drift between prompts. |
| 3 | "Be frugal with sub-agent models, generous with creative ones" lived only in the orchestrator's head, as a `model:` argument on each call. | The policy is unenforced, and a new session doesn't know it. |

## Proposal

### 1. The prose linter

**Rules as data.** The banned list moves out of `process/style-guide.md` into
`process/prose-rules.toml`, which becomes the single source of truth. The style
guide keeps the positive rules and the tone charter, and points to the TOML for
the mechanical list. Python 3.12's `tomllib` reads it, so the linter has no
dependencies.

Every rule carries a **severity**:

- **error:** a hit fails the lint. Examples are banned phrases ("a testament
  to", "the silence was deafening"), banned default names (Elara, Kael, Voss,
  …) and banned ship names.
- **warn:** a hit is reported but doesn't fail on its own. Rules at this level
  are counted against a budget, and they fail only when the count goes over
  it. That covers:
  - em-dashes (at most 2 per 300 words);
  - "the way …" similes (at most 3 per story);
  - the "It wasn't X. It was Y." and "not X. Y." contrast shapes (at most 1
    per story);
  - short closing paragraphs (at most 3 per story; see below).

A **short closing paragraph** is a paragraph of 8 or fewer words that ends a
run of narration: it follows a narration paragraph and isn't dialogue. Those
thresholds are a heuristic, and the TOML sets them. The linter reports every
hit with `file:line`, so a human can judge each one.

**Input.** The linter takes Markdown story files. It ignores headings, the
centered scene-break line, and anything after a `## Drafter's notes` heading,
so draft files that still carry their notes lint correctly.

**Output.** One line per hit, in the form
`path:line: [error|warn] rule-id: "matched text"`, followed by a per-rule budget
summary. It exits 0 when it's clean and 1 when it finds any error or any budget
overrun. `--warn-only` reports everything and always exits 0.

**Which files get linted:**

| Where | Files | Mode |
|---|---|---|
| `just check` | every `stories/*/final.md`, plus the linter's own tests and an EPUB smoke test | strict |
| `just lint <file>` | any file you name | strict |
| pre-commit hook | staged `stories/*/final.md` strict; staged `stories/*/drafts/*.md` with `--warn-only` | mixed |
| the drafter, before hand-back | its own draft | strict, so overruns get fixed before review |

Drafts aren't blocked at commit time, on purpose. A draft that breaks the
rules is a legitimate artifact in the history: draft 1 is what the reviewers
reviewed. Only `final.md` is held to the rules.

**Tests.** `tests/test_lint_prose.py`, using stdlib `unittest`, has one fixture
per rule plus the notes-section and heading exclusions. `just check` runs it.

**Existing story.** `stories/calibration-01/final.md` must pass strict mode as
it stands, or with fixes that the implementation commits alongside the
linter. Any rule that would fail this already-reviewed story is either a
genuine miss, and gets fixed, or a mis-tuned threshold, and gets retuned. The
implementation commit records which.

### 2. Branch per story

- **Starting a story.** The orchestrator calls `EnterWorktree` with
  `name: story-<slug>`. That gives a worktree at
  `$HOME/src/worktrees/ai-scifi/story-<slug>` on the branch
  `bestdan/story-<slug>`, started from local `main`.
- **Commits.** Commits within a story are plain `git commit`. The global hook
  passes because the branch isn't `main`, and the repo-local
  `.git/hooks/pre-commit` runs the lint. **`--no-verify` is no longer part of
  the process.**
- **Installing the hook.** A hook file under `.git/hooks/` isn't versioned, so
  the repo carries `scripts/hooks/pre-commit`, and a `just install-hooks` recipe
  symlinks it into place. The global `pre-commit` and `_delegate` scripts
  resolve local hooks through `git rev-parse --git-common-dir`, so a single
  install covers every worktree.
- **Landing a story.** At sign-off, run `git merge --ff-only bestdan/story-<slug>`
  from the main checkout. A fast-forward creates no commit, so no hook blocks
  it. The repo has no remote, so there are no PRs. This step happens only once
  the human has signed off.
- **Tearing down.** Use `ExitWorktree`. The plugin's teardown gates branch
  deletion on PR evidence, and there are no PRs here, so it will keep the
  branch. That's acceptable: a landed story branch is a fully merged ref, so
  keeping it costs nothing. Whether the teardown works cleanly in a repo with
  no remote needs to be verified (see Risks).
- **Tooling and process changes** (like this one) use their own
  `bestdan/<name>` branches in the same way.

`AGENTS.md` changes to say this in two lines. The current text says nothing
about branches, and the calibration-01 session committed to `main` only
because the human authorized it.

### 3. Agent definitions and stage files

**Roles, not lenses.** Model policy follows the *role* an agent plays, not the
lens it wears. In calibration-01 the Watts lens ran on opus for ideation and on
sonnet for critique. One definition per lens would need two models per lens.
So the definitions are per role, and each one takes the lens as an argument.

| Agent definition | Model | Used for |
|---|---|---|
| `lens-ideator` | opus | stage 1 idea cards |
| `lens-critic` | sonnet | stages 3, 4 and 5 critiques; stage 7 reviews; stage 9 spot-checks |
| `cartographer` | opus | stage 2 audit (needs broad prior-art recall and web search) |
| `drafter` | opus | stage 6 drafts and stage 8 revisions |
| `line-editor` | opus | stage 9 polish |
| `first-reader` | sonnet | stage 7 |

The Cartographer critiquing at stages 3 and 7 runs as `lens-critic` with
`lens: cartographer`, because that work is critique, not audit.

**Each definition's body holds the standing rules,** written once:

- read `personas/<lens>.md` (for the lens roles) or the role's own persona
  file;
- read `process/style-guide.md`;
- never claim to be the author, quote the author, or imitate the author's
  voice;
- write output only to the path the stage file names;
- reply with the short summary the stage file asks for.

The impersonation disclaimer leaves the 8 persona files and lives only here,
plus one line in `AGENTS.md` for agents that run outside these definitions.

**Persona files stay in `personas/`.** They are the content, and harnesses
without `.claude/agents` support (Codex) can still read them. The definitions
are thin wrappers that point at them.

**Stage files** go in `process/stages/NN-<name>.md`, one per stage that
dispatches agents: 1, 2, 3, 4, 5, 6, 7, 8 and 9. Each one holds:

- the role to dispatch, and the lenses (default panel, overridable by the
  brief);
- the inputs to read;
- the task text, including the stage-specific questions now written out in
  each prompt;
- the output path and template;
- the reply format.

`PROCESS.md` keeps the overview (who, output and gate for each stage) and
links to each stage file. The task text moves out of `PROCESS.md`'s stage
sections into the stage files, so each meaning lives in one place.

**A dispatch then looks like:**

```
Agent(subagent_type: "lens-critic",
      prompt: "Lens: watts. Stage: process/stages/07-review.md.
               Story: stories/calibration-02. Round: draft-2.")
```

The orchestrator passes no `model:`. The definition sets it. The stage files
say this explicitly, so a passed `model:` stands out as a deviation.

**Story directory layout.** The layout in `PROCESS.md` gains the paths that
calibration-01 invented mid-run: `03-critique/`, `04-critique/`,
`05-critique/`, `reviews/polish-*.md`, `MORNING.md` and `*.epub`. The stage
files refer to it rather than restating paths. (Strictly this is finding 5,
but the stage files can't name output paths without it.)

## Decisions

### A branch per story, not a main-branch opt-out

Each story runs on `bestdan/story-<slug>` in its own worktree, and lands by
fast-forward. **Rejected:** a per-repo opt-out in the global hook
(`hooks.allowMainCommits`). It needs a dotfiles change, and it keeps stories
on `main`, so concurrent story runs have no isolation from each other. The
branch-per-story approach matches the existing worktree convention, and it is
the only option under which the local lint hook runs.

### Agent definitions per role, not per lens

Model policy attaches to the role (ideator, critic, drafter, and so on), and
the lens is an argument. **Rejected:** one definition per lens (`watts.md`,
and so on). Every lens needs two models, opus for ideation and sonnet for
critique, which means either duplicate definitions or a `model:` override on
every call. The override is exactly the in-head policy this design removes.

### Persona content stays in `personas/`

The definitions are thin wrappers that point at the persona files.
**Rejected:** moving persona content into `.claude/agents/`. That would remove
one indirection, but it would lock the personas to Claude Code. A Codex run
could no longer read them, and each lens would be split across a
harness-specific file.

### The banned list becomes data

`process/prose-rules.toml` is the single source of truth, and both the linter
and the style guide refer to it. **Rejected:** keeping the list in the style
guide's prose and hard-coding the same patterns in the linter. That puts one
meaning in two places, and they would drift.

### Strict lint on `final.md` only

Commits lint `final.md` strictly and drafts at warn level. **Rejected:**
linting drafts strictly at commit. That would block committing a reviewable
draft, and the review loop exists precisely to fix such drafts. A rule-breaking
draft 1 is a legitimate artifact in the history.

## Not decided here

Four retro findings are **out of scope**:

- 4, the story-facts ledger;
- 6, separate drafter's-notes files;
- 7, `scripts/status.py`;
- 8, keeping the banned list away from the drafter.

Finding 8 is partly addressed as a side effect, because the banned list moves
into the TOML. Whether the drafter should still read it is left for a
follow-up.

These risks are open, and each gets verified during implementation:

1. **When agent definitions load.** Claude Code may only read `.claude/agents/`
   at session start. If so, the definitions can't be used in the session that
   creates them. **Verify during implementation;** if it's true, test the
   definitions with a `claude -p` run.
2. **Whether `.claude/agents/` can be written from a sandboxed session.**
   Writes inside the repo's `.claude/` directory are a known sandbox-denied
   path for repos that version their agent config (see the `sandbox-escapes`
   skill). The worktree is inside the sandbox's write allowlist, but
   `.claude/**` may be denied anyway. **Verify; if it's denied, the escape is
   needed only for this one commit.**
3. **ExitWorktree in a repo with no remote.** The teardown's PR-evidence gate
   has nothing to look up. It should keep the branch and remove the worktree,
   but this needs to be verified on this branch's teardown.
4. **The short-closer heuristic.** It will have false positives, such as a
   short line of dialogue or a deliberate one-line beat. That's acceptable at
   warn severity with a budget, because the budget allows 3. Retune it against
   calibration-01's two drafts.
5. **Model aliases.** `opus` and `sonnet` in frontmatter resolve to whatever
   the harness maps them to. That's the behaviour we want, but the
   definitions' models should be checked when the harness changes.

## Graduation

- **Decision records, under `dev_docs/decisions/`:**
  - a branch per story;
  - agent definitions per role;
  - prose rules as data.
- **Conventions:**
  - `AGENTS.md`: two lines on the branch-per-story workflow, plus a pointer
    to `.claude/agents/` and `process/stages/`;
  - `process/PROCESS.md`: the story layout and links to the stage files;
  - `process/style-guide.md`: a pointer to `prose-rules.toml`.
- **Delete this design** in the commit that lands the change on `main`. The
  repo has no remote, so there's no PR.
