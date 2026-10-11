---
created: 2026-10-06
status: superseded
superseded_by: 2026-10-11-comprehension-gate-counts-confusion.md
convention: ../../process/stages/07-review.md
---

# Comprehension is graded by an outsider, from a two-turn cold read

## Context

Calibration-01's story, "Raking Light", scored 5/5 for prose from the
human, who still couldn't say what it was about, what was at stake, or what
the twist was. The signals were there before polish. The draft-1 First
Reader said the twist's key line "lost me", and the draft-2 reader raised
the twist only as an open question. The orchestrator, who wrote the bible,
read both reports as passes. The lens panel had also read the bible, and
scored Character and Consequence 4 where the human gave 2.
(`stories/calibration-01/human-feedback.md`, sections 1, 2 and 5.)

Anyone who has read the bible knows what the story means to say, and grades
the page as though it said it.

## Decision

A fresh sonnet First Reader reads the draft and writes its experience report.
It is then resumed for a second turn with seven fixed comprehension
questions, which appear only in `process/stages/07-review.md` so they can't
prime the read. A separate `comprehension-grader`, also on sonnet, sees only
the payoff ledger's five graded rows, a names list and the answers, never
the bible or the draft. It grades each row got it, partial or missed, and
"got it" needs the causal link in the reader's own words. Polish starts only
when every row is got it, and the gate runs again on `final.md`. The
orchestrator may lower a grade but never raise one. The Understood axes of
the rubric are scored by the grader alone; the lenses score only Felt and
Craft.

This one record holds three of the design's choices: the two-turn read with
outsider grading, the reader staying on sonnet, and understanding scored
only by the outsider. The design listed them separately. They share one
piece of evidence and one revisit trigger, so they are kept together here.

## Consequences

- Good, because the only judge of whether the page explains the story is an
  agent that has nothing but the page's effect to go on.
- Good, because a failed row turns into a structural revision item
  automatically, rather than relying on someone to notice it.
- Good, because the human's debrief asks the same seven questions, so each
  story measures whether the gate predicts the human.
- Bad, because the no-reread rule in turn 2 can't be enforced: the reader
  has the Read tool. It is an honour rule.
- Bad, because a sonnet reader already read calibration-01 more strongly
  than the human did, so a pass is weak evidence on its own. The strict
  "causal link" standard is the counterweight, not a cure.
- Bad, because each review round costs a second turn and a grader dispatch,
  and the gate runs once more after polish.

## Revisit when

- On a calibration debrief, the reader and grader passed a row that the
  human missed, answering the same questions. That means the reader model
  or the grading standard doesn't predict the human.
- The loop cap fires on most stories, which would mean the gate is
  unpassable rather than strict.

## Confirmation

`tests/test_agents.py` holds the grader on sonnet without Bash, and checks
that the seven questions are in stage 7 and absent from both First Reader
files. `tests/test_process.py` checks that the debrief asks the same
questions. `tests/test_templates.py` checks that the bible template carries
the ledger's graded rows. Grading strictness rests on the grader definition
alone.

## Alternatives

- **The questions in the reader's first prompt:** they prime the read.
- **The orchestrator grades:** it wrote the ledger, and in calibration-01
  it read a confused reader as a pass.
- **A second cold reader for comprehension:** a second full read, when one
  reader can give both the report and the answers.
- **An opus reader:** it would read even more strongly than the human,
  widening the gap the gate is meant to close.
- **Lenses do a cold read before opening the bible:** a lens that knows the
  bible is coming still reads as an insider.
