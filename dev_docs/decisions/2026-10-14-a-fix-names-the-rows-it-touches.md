---
created: 2026-10-14
status: accepted
convention: ../../process/stages/08-revise.md
---

# A revision fix names every ledger row its line serves

## Context

In run-02 (branch `bestdan/story-run-02`, not landed) a fix in one round
caused a miss in the next, twice (`stories/run-02/MORNING.md`):

- Round 2 fixed Premise by spelling out both branches of Davi's choice.
  The fix gave both the same picture, "at the board, beside her", and the
  round 2 reader merged them into one: "He stays open and works at the
  board beside his mother, and is set that way."
- Round 3 separated the branches by "no tablets", as the revision plan
  asked. Stakes then went partial: the reader lost what waiting would gain.

No lens caught either regression. The next cold reader did, so each one
cost a round, and run-02 was capped at three.

## Decision

When a stage 8 plan item rewrites a line the last drafter's notes quote for
a ledger row, the item names every row that line serves and says how each
still reads. Two things the reader must tell apart, such as the branches of
a choice, never share one picture. In `process/stages/08-revise.md`
step 3.

## Consequences

- Good, because the orchestrator writing the plan, who has the ledger and
  the drafter's notes, sees what a fix touches before the drafter acts on
  it.
- Good, because "never share one picture" names run-02's actual failure in
  a form a plan can check.
- Bad, because it rests on the drafter's notes quoting each row's lines. A
  line that carries a row without being quoted is still unguarded.
- Bad, because the cold reader stays the only real test. This rule only
  makes a regression less likely; the next round still has to catch it.

## Revisit when

- A debrief or a round's grade again shows a fix breaking a row the plan
  named and said was safe: naming rows isn't enough, and the round needs a
  check, for example a lens told which rows the last plan touched.

## Confirmation

Nothing beyond review: the rule is in stage 8's orchestrator steps.

## Alternatives

- **Have a lens re-check the touched rows each round:** heavier, and in
  run-02 the lenses already read each draft and caught neither regression:
  four read draft 2, and Asimov read draft 3.
