# Drafting with a model outside Claude Code

How to run a story's one drafter on a model Claude Code can't dispatch as
an agent. The worked case is Gemini through Google's Antigravity CLI
(`agy`), as run-08 used it for stages 6, 8 and 9. The stage files still
govern what the drafter does; this file covers only how to run it.

## The rules that don't change

- **One drafter per story.** Use one resumed conversation for every
  drafting turn: the draft, every revision round, and the polish if the
  human gives it to the same model. Record its conversation ID in
  `STATUS.md`.
- **Every other role stays a Claude agent:** the lenses, the first readers
  and the grader. The comprehension gate, the lint and `dli check` run as
  usual.
- **The orchestrator measures.** Never take the model's own word count,
  word for word or section by section. Run-08's Gemini reported 6,812
  words for a 10,985-word draft and 6,758 for 8,142.

## Gemini through `agy`

### Sign-in on the subscription

`agy` uses the human's Google account (Google AI Pro), not an API key, so
usage comes out of the subscription. An AI Studio API key is a different
route that bills separately, and `agy` ignores it; don't store one.

- Sign in by running `agy` interactively and following its OAuth link. The
  code it asks for expires in about a minute, so the human must paste it
  straight back. An interactive session has no timeout; a one-shot login
  command does.
- On a headless host the human opens the link on another device and
  pastes the code into the session that is waiting for it.

### The call

```
agy -p "<prompt>" --model gemini-4-argon-high --conversation <id> \
    --output-format json --print-timeout <ms> < /dev/null
```

- `--conversation` resumes the story's conversation; omit it only on the
  first call and record the ID it returns.
- `--output-format json` returns the reply in `response` and the token
  counts in `usage`. Log `usage` in `STATUS.md`'s token table.
- Run it unsandboxed, with stdin from `/dev/null`.
- Never pass `--dangerously-skip-permissions`. Auto mode refuses it, and
  the grants below make it unnecessary.

### Permission grants

`agy` keeps its rules in `~/.gemini/config/projects/default-cli-project.json`,
its global default project, so they apply in every worktree. Its format is
`action(target)`, with the actions `command`, `read_file`, `write_file` and
`mcp`. Claude Code's `Bash(...)` form is refused as an unknown action.
The grants this pipeline needs:

```
command(just lint)
command(wc -w)
write_file(stories/)
```

`write_file(stories/)` is relative to wherever `agy` starts, so it also
lets any `agy` session write to a `stories/` folder in any repo.

With these grants Gemini writes its draft file, counts it and lints it
itself, so the prompt names files to read and write rather than inlining
them.

### Without the grants

Run-08's first stages ran with no tool access. The orchestrator inlined
every input in the prompt, and Gemini returned the draft between
`<<<DRAFT` and `DRAFT>>>` markers. The orchestrator wrote the file, counted
it and linted it. That route still works if the grants are missing.

## Holding the length

- **For a length round,** give the model the measured count of every
  section and the target for each. A total alone wasn't enough: the
  first length round, given only a total, missed it.
- **For a revision or a polish,** ask for replacement paragraphs only, each
  between markers naming the paragraph it replaces (`<<<L[n]` … `L[n]>>>`,
  where `n` is a line number in the current draft). The orchestrator
  splices them in and measures. In run-08 a whole new draft took the
  story from 6,255 words to 7,236; the replacement-paragraph round took
  it to 7,223.
