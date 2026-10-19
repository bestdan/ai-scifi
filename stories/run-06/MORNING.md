# Morning report: run-06

Read this after `final.md` and after the debrief's first section. It
discusses how the story was made.

## The run

- **The pipeline:** a brief, 30 idea cards from ten lenses, an audit, five
  premises, the bible, the outline, a five-part draft with per-part lens
  checks, three review rounds, polish, and the gate on `final.md`.
- **Gates:** every gate after the brief was decided by proxy and logged in
  `STATUS.md` with reasons and a runner-up. A consultant (fable) was asked
  at stage 3 and at the loop cap.
- **Length:** `final.md` is about 32,200 words, inside the brief's
  30,000–40,000.

## The comprehension gate across rounds

| Row | Draft 1 | Draft 2 | Draft 3 | final.md |
|---|---|---|---|---|
| Premise | partial | partial | partial | partial |
| Stakes | partial | partial | partial | got it |
| Why | partial | got it | got it | got it |
| Twist | partial | got it | got it | got it |
| Ending | got it | partial | partial | got it |
| Reach | partial | partial | partial | partial |
| Terms | missed | missed | got it | missed |

- **The loop cap.** It fired after round 2, and round 3 ran under a
  logged stop rule.
- **Premise and Reach never closed.** Each time, the cold reader's summary
  omitted one clause of a multi-clause fact, such as "must refuse unless
  the record proves incapacity" or the clause-by-clause shift of
  sovereignty. That is run-05's pattern. The debrief should test whether
  your read matches.
- **Terms failed on different words each round,** six words in all.

## Candidate process changes

- **Keep the cold reader away from the Drafter's notes.** In round 1 the
  First Reader's view of `draft-N.md` included the Drafter's notes, which
  quote the ledger lines. From round 2 the reader got a copy with them
  stripped. Make that the default in `07-review.md`: write
  `reviews/draft-N/story-only.md` and point the reader at it.
- **Check a draft's terms against the Glossary.** Mandazi entered the
  draft without a Glossary entry, so `terms.md` missed it, and the final
  reader guessed it. A pre-review check could flag any non-English word
  not in the Glossary.
- **Per-part lens checks were cheap and caught real problems early,**
  among them the wise-clerk drift in Part 3 and the unmotivated save in
  Part 1. Keep them for long-form runs.
- **A killed drafter.** The session was interrupted mid-revision, and the
  drafter's context was lost with it. Draft 2 survived on disk, complete.
  A fresh drafter held the voice for draft 3 from `continuity.md`. That
  file's voice notes were the thing that made a handover possible.
- **Token use.** It wasn't logged per stage, so this is a rough tally
  from the subagent reports: about 5 million subagent tokens, plus the
  orchestrator's own turns. The review rounds were the biggest cost:
  about 0.9 million each for a full panel at this length. Logging per
  stage in `STATUS.md` would make the next estimate a measurement.
