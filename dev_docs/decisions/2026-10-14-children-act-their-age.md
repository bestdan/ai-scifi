---
created: 2026-10-14
status: accepted
convention: ../../templates/story-bible.md
---

# The bible says what each young character can't do yet

## Context

Run-02 and run-03 both drew the note that their children read as competent
adults. From run-03's debrief: "The one part that seemed odd is the lack of
... childishness of the children. They should still be immature?" No review
in that run mentioned it, because the bible gave the children adult minds
and nothing asked what stayed fifteen.

Run-04's brief carried the note by hand: "This child thinks, wants,
misreads and feels like a ten-year-old. Stage 4's bible says what the child
doesn't yet understand." Run-04's human called its characters "meaningful
and relatable" and raised no note about the child's age
(`stories/run-04/debrief.md` on branch `bestdan/story-run-04`).

## Decision

The story bible's character entry gets a field for any character under 18:
what they can't do or don't understand yet, whatever the novum gives them.
The stage 4 Le Guin lens asks whether the children act their age. The note
no longer needs carrying in each brief.

## Consequences

- Good, because the fix that worked in run-04 by hand now runs every time.
- Bad, because one run is thin evidence that the bible field, not the
  premise, made the difference.

## Revisit when

- A debrief again finds a child reading as an adult although the bible
  filled the field.

## Confirmation

Nothing beyond review: the field is in `templates/story-bible.md` and the
question in `process/stages/04-build.md`.
