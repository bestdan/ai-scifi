---
created: 2026-10-14
status: accepted
convention: ../../process/stages/09-polish.md
---

# After a loop-cap pass, a miss on final.md is logged, not sent back

## Context

Two rules met head-on in run-02 (branch `bestdan/story-run-02`, not landed).
The stage 8 loop cap lets a story whose gate has failed twice go on to
polish, with the unclosed rows logged under "Gate failures". Stage 9 step 5
then reruns the gate on `final.md`, and said a failed gate sends the story
back to stage 8, with no exception. So a story the cap had just let through
was sent straight back into the loop it had capped. Run-02 had a logged stop
rule (no round 4), and the orchestrator broke stage 9's rule to keep it
(`stories/run-02/MORNING.md`).

The final gate in run-02 also failed a row that had passed on draft 3:
Ending, got it in rounds 2 and 3, partial on `final.md`. Polish hadn't
touched Ending's lines. The only change to the lines the drafter's notes
quote for it was "tasted of nothing" becoming "tasted of the paper cup".
Across four rounds every graded row except Why was both partial and got it,
depending on the reader. A fresh reader's miss on unchanged text is noise
in the reader, not damage from polish.

## Decision

After a loop-cap pass, a failed gate on `final.md` doesn't send the story
back to stage 8. For each failing row the orchestrator compares the lines
the drafter's notes quote for it in draft N with the same lines in
`final.md`. Unchanged lines mean the reader differs: log the row under
"Gate failures". Changed lines mean polish broke the row: restore draft N's
lines and log it. Outside a loop-cap pass, a failed final gate still sends
the story back to stage 8. In `process/stages/09-polish.md` step 5 and
`process/PROCESS.md`.

## Consequences

- Good, because the loop cap now caps the loop: no rule sends a capped
  story back into revision.
- Good, because the one thing polish can do to the gate, change a row's
  lines, is still caught, and is undone by restoring lines rather than by
  a whole revision round.
- Bad, because a row that is fragile on unchanged text ships as a logged
  failure. The debrief is the only place that cost is weighed.
- Bad, because the comparison trusts the drafter's notes to quote every
  line a row depends on. A row carried by a line they don't quote can be
  broken by polish unseen.

## Revisit when

- A debrief finds a row failed by polish that this comparison called
  unchanged: the notes' quotes are too narrow, and the check needs a diff
  of the scenes the row lives in.
- The loop cap changes, so that a capped story can take another round.

## Confirmation

Nothing beyond review: the rule is in stage 9's orchestrator steps.

## Alternatives

- **Send back only a row that passed on draft N and fails on `final.md`:**
  the first version of this rule. Run-02's Ending is that case, and it was
  reader noise, so this would have sent run-02 back for nothing.
- **Rerun the final gate after restoring lines:** another reader adds
  another sample of the same noise. Restoring draft N's lines puts the row
  back to text that has already been graded.
