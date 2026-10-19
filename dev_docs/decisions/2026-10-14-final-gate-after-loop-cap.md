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
Ending, got it in rounds 2 and 3, partial on `final.md`. Every passage the
drafter's notes quote for Ending is word for word the same in `final.md`.
Polish changed the sentence after one of them, "tasted of nothing" becoming
"tasted of the paper cup", in a spot-check; drafts hold a paragraph per
line, so a line-by-line comparison would have counted that as a change.
Across the three draft gates and the final gate, Stakes was partial on
drafts 1 and 3 and on `final.md` and got it on draft 2; Ending was partial
on draft 1 and `final.md` and got it on drafts 2 and 3; Why and Who's who
were got every time, and Premise was partial every time. A fresh reader's miss
on unchanged text is noise in the reader, not damage from polish.

Premise is the opposite case. It failed on draft 3, so the loop cap let it
through, and polish's required item 1 rewrote its quoted line on purpose:
"her trade at a child's speed, eight bells of it" became "his mother's
trade at a child's speed, … a year of bells, eight of them". Changed text
on a row that was already failing is a fix, not damage.

## Decision

After a loop-cap pass, a failed gate on `final.md` doesn't send the story
back to stage 8. For each failing row the orchestrator compares the text
the drafter's notes quote for it in draft N with the same text in
`final.md`. A row that passed on draft N and whose text changed was broken
by polish: restore draft N's text and log it. Every other failing row is
logged under "Gate failures": unchanged text means the reader differs, and
a row that failed on draft N may have been rewritten on purpose. The
Terms row follows the same rule for each failing term, and a lost-list
entry that touches a graded row follows its row. Outside a loop-cap pass,
a failed final gate still sends the story back to stage 8. In
`process/stages/09-polish.md` step 5 and `process/PROCESS.md`.

## Consequences

- Good, because the loop cap now caps the loop: no rule sends a capped
  story back into revision.
- Good, because the one thing polish can do to the gate, change a row's
  quoted text, is still caught, and is undone by restoring that text
  rather than by a whole revision round. Comparing quoted text rather than
  whole lines leaves the rest of each paragraph's polish alone.
- Bad, because a row that is fragile on unchanged text ships as a logged
  failure. The debrief is the only place that cost is weighed.
- Bad, because the comparison trusts the drafter's notes to quote every
  line a row depends on. A row carried by a line they don't quote can be
  broken by polish unseen.
- Bad, because a row that already failed on draft N is only logged, even
  if polish changed its quoted text outside a required item and made it
  worse; only the debrief sees that.

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
- **Rerun the final gate after restoring text:** another reader adds
  another sample of the same noise. Restoring draft N's text puts the row
  back to text that has already been graded.
- **Restore every row whose quoted text changed:** would have undone
  run-02's required item 1, the Premise fix aimed at that same row.
- **Compare whole file lines:** a draft line is a paragraph, so any polish
  near a quoted passage would count as a change and be reverted, as
  run-02's "paper cup" edit would have been.
