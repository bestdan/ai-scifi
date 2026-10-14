---
created: 2026-10-11
status: superseded
supersedes: 2026-10-06-comprehension-gate.md
superseded_by: 2026-10-14-lost-list-gates-on-rows-not-count.md
convention: ../../process/stages/07-review.md
---

# The comprehension gate counts the reader's confusion, not only its recall

## Context

The gate of 2026-10-06 had a fresh sonnet First Reader read the draft, then
answer seven fixed questions in a second turn, and an outsider
`comprehension-grader` grade those answers against the payoff ledger's five
graded rows. Polish waited for every row to be "got it".

On run-02 ("Strike Note", branch `bestdan/story-run-02`) the human missed
every graded row. The grader had given the cold reader "got it" on Why and
Who's who and "partial" on the rest (`stories/run-02/debrief.md`). That was
this gate's revisit trigger. The reader had no inside information: it read
only its persona file and the draft. It beat the human for reasons on the
model's side:

- It decoded the story's untranslated Portuguese from its own knowledge.
- It read a 240-word legal text at full attention, which the human didn't.
- Its "Where I got lost" list named the human's snags: seven entries,
  including the legal reading and five unexplained terms. The gate didn't
  read that list.
- The grader's `names.md` defined every invented term, so it knew meanings
  the page may not have given.

Every First Reader report so far has listed 6 to 8 lost entries: run-02's
four rounds 8, 7, 6 and 7, calibration-01's two rounds 7 and 7.

## Decision

The two-turn read, the outsider grader on sonnet, the fixed questions kept
out of the reader's files, and the orchestrator's lower-only override all
stand. Three inputs are added to the gate.

- **The lost-list.** The grader reads the report's "Where I got lost"
  section. The gate fails if any entry concerns a graded row's fact, or if
  there are more than three entries.
- **A Terms row.** An eighth question asks which words or terms the reader
  didn't know from the story itself, and where it got their meaning. A term
  understood only from outside knowledge, got wrong or never got fails the
  row, and Terms decides the gate. Who's who stays a score.
- **Names and terms are split.** `names.md` lists characters only, and a
  separate `terms.md` is used only for the Terms row.

The reader also reports only what happened during the read and claims no
experience it didn't have.

## Consequences

- Good, because the signal that matched the human, the reader's confusion,
  now decides the gate, where before it was thrown away.
- Good, because a term the model decoded from its own languages no longer
  passes as clear.
- Bad, because the three-entry threshold would have failed every round of
  both stories so far, so the loop cap may fire often until the drafts
  change.
- Bad, because whether a lost entry "concerns" a graded row is the grader's
  judgement.

## Revisit when

- The loop cap fires on the lost-list count alone in most rounds of the
  next two stories: change the threshold or the persona's "Where I got
  lost" prompt, not the rule.
- A debrief again finds the human missing a row the gate passed. The next
  thing to try is a weaker reader model, or two readers of different
  strength.

## Confirmation

`tests/test_agents.py` checks the eight questions are in stage 7 and absent
from the reader's files, that the grader's Gate line names Terms and the
lost-list rule, that stage 7 writes `names.md` and `terms.md` separately,
and that the persona drops the "next day" prompt. `tests/test_process.py`
checks that the debrief template and the rubric carry a Terms row.

## Alternatives

- **Stricter grading of the five recall rows:** the model's recall beat the
  human's on every row, so stricter recall still measures the model.
- **Counting only lost entries the reader never resolved:** most of run-02's
  entries say the reader worked the meaning out, so that rule would have
  passed a story the human couldn't follow.
- **A weaker reader model:** worth a test, but it changes the reader, not
  what the gate measures.
