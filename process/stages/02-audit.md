# Stage 2: Audit

**Dispatch:** one `cartographer` agent, with this prompt:

`Stage: process/stages/02-audit.md. Story: stories/<slug>.`

Don't pass `model:`. The agent definition sets it.

## For the orchestrator

**Gate:** shortlist 3 to 5 cards or collisions for stage 3. Prefer options
with distinct cores: skip a Top-5 entry that reuses a card you've already
shortlisted. In `human` mode, recommend a shortlist and the human picks it.
In `proxy` mode, the orchestrator picks it. Either way, record the decision,
its reasons and the runner-up in `STATUS.md`.

## For the agent

**Read:**
- `stories/<slug>/00-brief.md`
- every file in `stories/<slug>/01-ideas/`, including `assignments.md`
- `process/attractors.md`

**Task:** for every card, give the following, in your persona file's output
format:
- its nearest prior art;
- its distance from that prior art;
- its status;
- its scores on `process/rubric.md`;
- one push past the map.

Use WebSearch for any attribution you aren't highly confident about. Judge
Yield at the midpoint of the brief's length range.

Then add three sections:

1. **Convergence.** The lenses worked blind to each other. Name every cluster
   of cards that share a subject, mechanism, setting, profession or naming
   register. Judge whether each cluster points to territory that is already
   charted, or to an attractor in the generating model that the next run
   should steer away from. Be blunt: this is calibration data.
   - Cluster the lenses' "Obvious card" lines too. Several lenses writing
     the same obvious card shows the brief's most literal answer; a written
     card that matches it is a red flag.
   - A card on an entry in `process/attractors.md` is edge-of-map at best,
     unless it names the entry and earns breaking it.
   - **The seed's own topic is never an attractor.** When the brief has a
     seed, many cards will share its subject, because the seed asked for
     it. Judge the angle the cards share (the mechanism, the setting, the
     shape), not the topic. Novelty has to come from the treatment, never
     from leaving the seed. In run-09 the audit judged the seed's direct
     forms to be attractors, the chosen premise drifted from the seed, and
     the human said the story wasn't the topic they wanted explored.
   - **Seed fit.** For each card, say in one line which lines of the seed
     it serves and which it leaves behind.
   - Say whether the assigned entry points and stimuli spread the cards, or
     whether they converged anyway.
2. **Collisions.** List the 3 to 6 most promising cross-lens combinations.
3. **Top 5.** Rank single cards and collisions together by weighted score.

**Write:** `stories/<slug>/02-audit.md`. Then update
`process/attractors.md`: add every cluster you judged an attractor, and add
this run's slug to each existing entry it hit again. An entry is hard once
two runs have hit it. Name each entry by its angle, never by a seed's
topic. Change nothing else in that file.

**Reply:** the Top 5, one line each with its scores, and the convergence
verdict in two sentences.
