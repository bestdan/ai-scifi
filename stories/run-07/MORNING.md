# Morning report: run-07

Read this after `final.md` and after the debrief's first section. It
discusses how the story was made.

## The run

- **The pipeline:** a brief, 33 idea cards from eleven lenses, an audit,
  five premises, the bible, the outline, a five-part draft with per-part
  lens checks, three review rounds, polish, and the gate on `final.md`.
- **The process changes from run-06's debrief** were in force from the
  start (PR #45): a reason for every world rule, the world's shape with a
  history, a question per part, the "does it seem to think?" test, the
  dramatised-not-stated check, the cold reader's story-only copy, the
  glossary pre-check and per-stage token logging.
- **Gates:** every gate after the brief was decided by proxy and logged in
  `STATUS.md` with reasons and a runner-up. A consultant was asked at
  stage 3 and at the loop cap.
- **Length:** `final.md` is about 36,300 words, inside the brief's
  30,000–40,000.

## The comprehension gate across rounds

| Row | Draft 1 | Draft 2 | Draft 3 | final.md |
|---|---|---|---|---|
| Premise | partial | partial | partial | partial |
| Stakes | got it | partial | partial | got it |
| Why | partial | partial | partial | partial |
| Ending | got it | got it | got it | got it |
| Reach | partial | got it | got it | partial |
| Terms | missed | missed | missed | got it |

- **The loop cap** fired after round 2, and round 3 ran under a logged stop
  rule.
- **Premise and Why never closed** across four cold readers. Each answer
  dropped one clause of a multi-clause fact: the two half-powers, or why
  the rope got every law. That is run-05's and run-06's pattern again. The
  debrief should test whether your read matches.
- **Terms failed on a different word every round** until polish: the
  Accord, then "button", then "dispensed", "derate" and "map". Every one
  was an English word or coinage used in a special sense, not a foreign
  word.

## Candidate process changes

- **The glossary pre-check looks only for foreign words.** It caught
  "pasillo" (run-06's "mandazi" again), but every later Terms failure was
  English used in a coined or technical sense. Extend the stage 4 Glossary
  and the stage 7 pre-check to coined English and jargon the plot leans
  on.
- **Multi-clause ledger rows.** Premise and Why each pack three or four
  facts into one row, and a cold reader's summary reliably drops one. Two
  runs in a row now. Either split such rows, or grade the clause the
  story most needs.
- **Running outside the repo.** This session started in `~/src`, so the
  role agents weren't loaded. Every agent ran through `claude -p --agent
  <role>` from the worktree instead, which worked, with one cost: under
  `claude -p` the drafter and line editor couldn't run `just lint`, so the
  orchestrator linted for them. Start story sessions in the repo, or allow
  the lint command for those roles.
- **Token use, measured this time:** about 64.6 million agent tokens. The
  drafter was most of it, about 45 million across drafting and two
  revisions, nearly all cached context re-read on each resume. A fresh
  drafter per revision, started from `continuity.md`, might cost less; run
  it once and compare.
- **Per-part lens checks** paid again: they caught Waska's self-diagnosis,
  the theme said aloud, the late proof-climb rule and the 1.04 arithmetic
  before the full review.
- **Check the plan's locations.** One round-3 item pointed the line editor
  at sections that didn't contain the line; it found the right ones. The
  orchestrator should grep before citing.
