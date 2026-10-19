# Stage 5: Structure

**Dispatch:** `lens-critic`, once per lens on the stage 5 panel (by default
Asimov, Chiang and Banks), in parallel. Use this prompt:

`Lens: <lens>. Stage: process/stages/05-structure.md. Story: stories/<slug>.`

Don't pass `model:`.

## For the orchestrator

1. Before dispatching, write `stories/<slug>/05-outline.md` from
   `templates/outline.md`. It covers:
   - **The shape.** This can be non-linear, or tied to the novum the way the
     form of "Story of Your Life" is tied to its idea.
   - **The scenes.** Each with its purpose, its turn, and what it reveals.
   - **The information plan.** Facts surface as dramatized discovery, and
     late rather than early when in doubt. Every payoff-ledger row gets a
     "Made explicit by" scene, and Stakes comes before the climax. Each
     graded row also gets a "Shown by" scene. Each fact in the bible's world
     list surfaces in the first third.
   - **Introductions.** The scene table's Introduces column lists each new
     name and term. Keep the opening scene's list short.
   - **The opening.** Open in a scene a human body could stand in, with
     things to see, hear and touch. When the novum lives far from human
     scale (a wall, a mind, a vacuum), start where it touches people, and
     bring the strange layer in through that frame or in a flashback. An
     opening that defines the world before the reader has a place to stand
     costs the reader at page 2.
   - **The ending.** Its final image, and what it costs.
2. If the story hinges on a fair-play clue, add a calendar or arithmetic
   section that plants every input before the payoff scene.
3. Resolve every must-fix note into the outline, and log how each was
   resolved in its "Stage 5 lens notes" section.

**Gate:** the outline is approved. In `human` mode, the human approves it.
In `proxy` mode, the orchestrator approves it and logs the decision and its
reasons in `STATUS.md`.

## For the agent

**Read:**
- `stories/<slug>/00-brief.md`
- `stories/<slug>/04-bible.md`, amendments included
- `stories/<slug>/05-outline.md`

**Task:** critique the outline from your lens.

| Lens | Questions |
|---|---|
| Asimov | Can a reader state the rules by the midpoint? Is every clue planted early and fairly, and could an attentive reader beat the protagonist to it? Is anyone required to be stupid? Does any scene fail to turn? Is the information plan in the right order? Is the length realistic for the scene count? Is every payoff-ledger row made explicit, with Stakes before the climax? Is each graded row both stated and shown? Are the world-list facts all in the first third? |
| Chiang | Does the climax grow out of the idea? Which scene is unnecessary? Is the cost paid on the page rather than stated? Does the ending deepen the question rather than answer it? Is there a light formal device that would make the form enact the idea? Does any scene introduce more names than it anchors? |
| Banks | Is the scale felt at least once, concretely? Where does the wit live, and is there enough of it? Would reordering the scenes hit harder? Is it enjoyable to inhabit? Who is missing from the view? |
| other | Your persona's "In critique" questions. |

Give at most 5 notes. Tag each one [must-fix], [should] or [could], and
give each a concrete fix. Keep the whole critique under 450 words.

**Write:** `stories/<slug>/05-critique/<lens>.md`

**Reply:** your must-fix notes, one line each.
