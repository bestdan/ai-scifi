---
created: 2026-10-14
status: accepted
supersedes: 2026-10-11-comprehension-gate-counts-confusion.md
convention: ../../process/stages/07-review.md
---

# The lost-list gates on the rows it touches, not on its length

## Context

The decision of 2026-10-11 made the First Reader's "Where I got lost" list
part of the comprehension gate. The gate failed if any entry concerned a
graded row's fact, or if there were more than three entries. Its revisit
trigger was the loop cap firing on the count alone in most rounds of the
next two stories.

Both stories have run, and the count never predicted the human:

- **Run-03** (branch `bestdan/story-run-03`, now on `main`): four reports
  with 7, 6, 5 and 8 entries. The human's one snag, that the children
  weren't childish, matched none of them (`stories/run-03/debrief.md`).
- **Run-04** (branch `bestdan/story-run-04`, parked): three reports with 4,
  8 and 6 entries. The human named none of those places. Their snag, that
  the story never asked what the technology meant beyond the family,
  matched none of them either (`stories/run-04/debrief.md` on that branch).

Every First Reader report in four stories has listed between 4 and 8
entries, so the over-three rule fails nearly every round. A reader told to
"list every place you got lost, even where you worked it out" will always
find more than three.

## Decision

The count no longer decides the gate. The gate fails on the lost-list only
when an entry concerns a graded row's fact. The orchestrator still reads
every entry as a revision note. The rest of the 2026-10-11 decision stands
unchanged: the two-turn read, the outsider grader, the Terms row, the split
of `names.md` from `terms.md`, and the orchestrator's lower-only override.

## Consequences

- Good, because the gate stops failing on confusions the human doesn't
  share, so the loop cap fires on real problems.
- Bad, because the rule that remains, entries that touch a graded row, has
  no debrief evidence for it either. It stays because a reader lost on the
  premise or the stakes is a direct failure of what the row asks, not
  because a debrief confirmed it.

## Revisit when

- A debrief's human snags on a passage the First Reader also listed, and
  the gate had passed: the count, or some other use of the list, mattered.
- A third debrief finds no overlap between the human's snags and the
  graded-row entries either: then drop the lost-list from the gate.

## Confirmation

`tests/test_agents.py` checks that the grader's Gate line names the
lost-list and no longer says "at most three".

## Alternatives

- **Raise the threshold to six or eight:** the counts ran 4 to 8 with no
  link to the human, so any number is arbitrary.
- **Drop the lost-list entirely:** the graded-row test is cheap and still
  targets the right failure; drop it only on the second trigger above.
