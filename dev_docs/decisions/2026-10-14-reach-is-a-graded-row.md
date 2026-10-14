---
created: 2026-10-14
status: accepted
convention: ../../templates/story-bible.md
---

# What the novum means beyond the characters is a graded row

## Context

Run-04 (branch `bestdan/story-run-04`, parked) was a near-present story
about a plumber paid to wear a camera for a robotics firm. The human's
verdict: "AI itself was really only a sideshow in this. … Is the father
automating himself out of a job? How is the family going to live? … What is
society doing? It felt like this was less science and more fiction." They
parked it as "well written as a story but not philosophically provocative"
(`stories/run-04/debrief.md` on that branch).

The bible knew the irony: the firm "is building the thing that will someday
do his job. Dad knows." Nothing carried it to the page. No ledger row
tracked it, so no draft had to state it and no grader checked for it. On the
page it became a shrug ("Someday. Not for years."). The lenses had read the
bible and scored Consequence 4 or 5 in the last round.

Run-03 drew the same note more softly: "There could have been more
world-building about other implications. The topic was very narrow."

At stage 3, run-04's premise beat the runner-up because "its child logic
is plainly ten", the answer to run-03's debrief note. The run picked for the
last debrief's complaint, not for the brief's seed: "parents whose jobs are
being reshaped".

## Decision

The payoff ledger gets a sixth graded row, **Reach**: what the novum
changes for people beyond the main characters (whose work, money or power
it moves, and what that costs them). A character in the story states it,
and a shrug doesn't count. The cold reader gets a ninth question, "What
does the story's central change mean for people beyond its main
characters?", and the grader grades it against the row. The gate needs it
to be got it. At stage 3 each premise carries a **Reach** line, and a
premise whose reach stays inside the household is rejected. The premise is
picked on the brief's seed, and a note carried from an earlier debrief is a
constraint every premise must meet, not the reason to prefer one.

## Consequences

- Good, because the thing the human judges a story on, its push on what
  the change means, is now checked by an outsider, not only by lenses who
  read the bible.
- Good, because stage 3 can no longer win a premise on the previous run's
  complaint alone.
- Bad, because a stated reach can turn into a character delivering the
  theme, which the style guide's "Nobody delivers the theme out loud"
  warns against. The template allows a speech when the question needs one
  (the human, in review: "occasional monologues or speeches are fine,
  especially if grappling with a complex topic"), so the line is drawn by
  the debrief, not by a rule.
- Bad, because a story whose point is intimate, with a deliberately small
  world, now has to reach anyway. The brief's seed is the escape: if it
  asks for something small, the reach can be small, but it is stated.

## Revisit when

- A debrief again finds the novum a "sideshow" although the gate graded
  Reach got it: the row is measuring recall, not weight.
- A debrief finds a story preachy, with its reach stated as a lecture.

## Confirmation

`tests/test_templates.py` checks the bible's ledger has a Reach row;
`tests/test_process.py` checks the rubric and debrief carry it, and that
stage 3 asks for a Reach line and picks on the seed; `tests/test_agents.py`
checks the ninth question lives in stage 7 only and that the grader's gate
names Reach.

## Alternatives

- **A lens question only (Banks or Chiang at stage 7):** the lenses have
  read the bible, so they score the reach the bible describes, which is how
  run-04 got Consequence 5.
- **A brief field for societal weight:** helps one run at a time; the
  ledger carries it through every stage.
