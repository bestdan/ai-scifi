---
created: 2026-10-19
status: accepted
convention: ../../process/stages/01-ideate.md
---

# Audit findings reach stage 1, and every lens starts somewhere different

## Context

Every stage 2 audit from calibration-01 to run-06 found the same
convergence, and every one said the next run should steer away from it.
Nothing carried the finding to stage 1, so the next run converged again:

- Water settings: about 12 cards a run in run-02, run-03 and run-06. Run-03's
  audit: "Banning it in the synthesis didn't reach stage 1. It needs to be
  in the lens prompt."
- An office that certifies, explains or adjudicates the novum: 7, 6, 8, 5
  and 10 cards across five runs.
- A functionary who finds something hidden and must decide whether to
  disclose it: about 20 of 30 protagonists in run-06.
- The name Ines in run-02, run-03, run-04 and run-06.
- The Futurity scale's own words played back as the cards' reasons
  (calibration-01, and again in calibration-02, whose audit noted the fix
  "hasn't been applied").
- Each lens repeating its own last card (6 of 9 lenses, calibration-02):
  each persona's "In ideation" section held one recipe.

The lenses are one model in ten costumes, so blind ideation doesn't give
independent draws. Run-03's audit: "blind to each other, but not blind to
the model". Shared inputs make it worse: run-05's dossier put 31 of 33
cards on its own list of angles.

Stage 3 compounded it by playing safe. Run-04 picked a narrowed card over
the most novel premise, and the human found the story "not philosophically
provocative". Run-05 picked a collision and pushed it further, and the
human scored it 9/10. Two runs is thin, but the reader profile says the
same: this reader credits ambition.

## Decision

- **`process/attractors.md`** records every cluster an audit judged an
  attractor, with the runs that hit it. Ideators read it and stay off it;
  the Cartographer updates it at every audit. Recurring names also get a
  warn-only lint rule.
- **`scripts/assign_ideation.py`** gives each lens a different entry point
  (least-used first, from three per persona), a different reader-profile
  pull, and a random stimulus from `process/stimuli.toml`. It's code because
  a model asked to choose at random chooses its favourites.
- **Each lens names its obvious card and doesn't write it.** The audit
  clusters these lines to see the brief's most literal answer.
- **Ideators don't rate Futurity.** The Cartographer does.
- **Stage 3 prefers the more ambitious premise** among those that serve the
  seed, and a Decision that narrows a premise names what was cut and why.

## Consequences

- Good, because the audit's best data now changes the next run instead of
  only describing it.
- Good, because diversity comes from different inputs, which the model can't
  undo by converging, rather than from personas alone, which it can.
- Bad, because the attractor list grows and narrows the field each run. If
  it outgrows the territory the seeds need, entries will need retiring.
- Bad, because `attractors.md` is updated on the story branch, so a run's
  findings reach main only when its story lands. A parked story's findings
  stay on its branch.
- Bad, because a random stimulus can be a poor fit for a seed. The card may
  travel far from it, and says where it went.

## Revisit when

- An audit finds a hard attractor hit again although it was in the file:
  the ideators are ignoring it, and it needs to be in the prompt itself.
- Two consecutive audits find the stimuli and entry points didn't spread the
  cards.
- The human finds an ambitious premise unreadable at debrief, as in
  calibration-01, and the comprehension gate didn't catch it.

## Confirmation

`tests/test_process.py` checks that stage 1 runs the assignment script, that
every stage 1 lens's persona lists at least three entry points, and that the
script's draw is spread and reproducible.

## Alternatives

- **Run some lenses on other models.** Real independence, but more cost and
  dependent on which models are available. Kept in reserve if the cheap
  fixes don't spread the cards.
- **A second ideation round** that develops the audit's collisions and
  pushes before stage 3. The Cartographer's collisions already win most
  runs; deferred until this change's effect is known.
