# The process

Nine stages take a story from brief to final manuscript. Each stage produces
one artifact on disk in `stories/<slug>/` and ends at a **gate**, where the
human chooses what goes forward. The orchestrator (the main agent session)
runs the stages, dispatches the persona agents and keeps `STATUS.md` current.

Two principles hold the stages together:

- **The novum comes first.** Darko Suvin's term for the new thing a story
  turns on: an invention, a law, a kind of mind, a social form. A story with a
  weak novum can't be rescued by good prose. So the first three stages search
  for one, test it and harden it, before any characters exist.
- **Pohl's traffic jam.** Frederik Pohl's line is that good SF predicts the
  traffic jam, not the automobile. We judge a novum by the consequences it
  forces, two or three steps out, and the story lives in those consequences.

## Story directory

```
stories/<slug>/
  STATUS.md            stage, gate decisions, open questions
  00-brief.md          constraints for this story
  01-ideas/<lens>.md   idea cards, one file per lens
  02-audit.md          Cartographer's prior-art map and scores
  03-synthesis.md      the chosen novum, its collisions, the premise
  04-bible.md          world, consequences, characters
  05-outline.md        structure and scene list
  drafts/draft-N.md    full drafts
  reviews/draft-N/<lens>.md   critiques of draft N
  06-revision-plan.md  triaged notes for the next draft
  final.md             the polished manuscript
```

## Stage 0: Brief

**Who:** the human and the orchestrator.
**Output:** `00-brief.md` (template: `templates/brief.md`).

Set the target length, the Futurity floor (see `rubric.md`), tone, anything
off-limits, and any seed obsession the human brings, even a single word. The
brief also lists any changes to the default panels below.

**Gate:** the human approves the brief.

## Stage 1: Ideate

**Who:** every author lens, as parallel agents.
**Output:** `01-ideas/<lens>.md`, with **3 idea cards** per lens
(template: `templates/idea-card.md`).

Each lens generates ideas from its own preoccupations, using the "Ideation
mode" section of its persona file. A card holds a novum, its first- and
second-order consequences, the story it might make, and the lens's own
guess at the closest prior art. Lenses don't see each other's cards, which
keeps them from converging.

There's no gate here; the cards go straight to audit.

## Stage 2: Audit

**Who:** the Cartographer.
**Output:** `02-audit.md`.

The Cartographer reads every card and does three things:

1. **Maps each card to its nearest prior art** in published SF, by title and
   author, and says how close the match is.
2. **Scores each card** on the rubric in `rubric.md`.
3. **Flags collisions:** pairs or triples of cards from different lenses that
   could combine into something none of them is alone.

Cards whose closest prior art is a direct match get marked **charted**. They
can still feed a collision but can't be the core novum by themselves.

**Gate:** the human reads the audit and shortlists 3 to 5 cards or collisions.

## Stage 3: Synthesize

**Who:** the orchestrator drafts; the Vinge, Chiang and Banks lenses plus the
Cartographer critique.
**Output:** `03-synthesis.md`.

For each shortlisted option, write a one-paragraph **premise**: the novum,
who it happens to, and what they are forced to choose. Combine where the
audit found collisions. The critique round asks three questions of each
premise. Is it uncharted (the Cartographer)? Is it pointed far enough into
the future (Vinge)? Does the idea itself carry the emotional weight, rather
than a plot attached to it (Chiang)?

**Gate:** the human picks **one** premise. Record the runners-up in
`STATUS.md`; they're seed stock for the next story.

## Stage 4: Build

**Who:** the orchestrator drafts; the Watts, Egan, Le Guin and Lem lenses
stress-test in parallel.
**Output:** `04-bible.md` (template: `templates/story-bible.md`).

The bible covers:

- **The novum, rigorously.** How it works, and what it costs.
- **The consequence ladder.** First-, second- and third-order effects (the
  traffic jam and what comes after it).
- **The society it produces.** Its institutions, language, economics, taboos.
- **The minds involved.** Which of them are human, posthuman or alien, and
  how each one perceives.
- **Characters.** What each one wants, what they're wrong about, and what the
  novum does to them in particular.
- **POV and voice.** Who tells the story, in what tense and register, and why
  this teller.

The stress test pulls in four directions. Watts and Egan check the science
and the logic. Le Guin checks whether the society reads as lived-in rather
than as scenery. Lem checks whether the alien parts are actually alien.

**Gate:** the human approves the bible.

## Stage 5: Structure

**Who:** the orchestrator drafts; the Asimov, Chiang and Banks lenses critique.
**Output:** `05-outline.md` (template: `templates/outline.md`).

The outline sets the shape, which may be non-linear or tied to the novum the
way the form of "Story of Your Life" is tied to its idea. It then lists the
scenes, each with its purpose, its turn and the information it reveals. It
plans where each fact about the novum surfaces: as dramatized discovery, not
exposition, and late rather than early when in doubt. It names the ending's
final image and what it costs the protagonist.

**Gate:** the human approves the outline.

## Stage 6: Draft

**Who:** a single drafting agent.
**Output:** `drafts/draft-1.md`.

The drafter reads the brief, the synthesis, the bible, the outline and
`style-guide.md`, then writes the whole story in one voice. That voice is set
in the bible and must not imitate any persona's author. The drafter may depart
from the outline, but notes every departure in a short section at the end of
the draft.

## Stage 7: Review

**Who:** the panel in parallel, 4 to 6 lenses by default plus the First Reader.
**Output:** `reviews/draft-N/<lens>.md` (template: `templates/critique.md`).

Each lens reviews from its own angle. The First Reader always takes part: it
is a smart reader with no investment in the genre, and it reports where it got
lost, bored or moved. The default panel is Asimov, Watts, Le Guin, Chiang and
the Cartographer, and the brief can swap lenses in or out.

## Stage 8: Revise

**Who:** the orchestrator triages; the same drafting agent revises.
**Output:** `06-revision-plan.md`, then `drafts/draft-N+1.md`.

The orchestrator merges the critiques into one plan, grouped as follows:

- **Consensus:** two or more lenses flagged it. Fix it.
- **Conflicts:** lenses pulled in opposite directions. These go to the human
  with a recommendation.
- **Declined:** notes deliberately not taken, each with the reason.

**Gate:** the human approves the plan. Stages 7 and 8 repeat until the human
calls the draft structurally done, usually after 2 or 3 rounds.

## Stage 9: Polish

**Who:** the Line Editor, with the Asimov lens (clarity) and the Rajaniemi
lens (density) pulling against each other.
**Output:** `final.md`.

The polish works sentence by sentence. It applies the style guide's banned
list mechanically, then reads for rhythm, then checks every invented term:
is it consistent, and is it introduced at the right moment? Nothing
structural changes here. A structural problem found at this stage sends the
story back to stage 8.

**Gate:** the human signs off.

## Default panels

| Stage | Lenses |
|---|---|
| 1 Ideate | Asimov, Banks, Watts, Egan, Chiang, Le Guin, Lem, Vinge, Rajaniemi |
| 2 Audit | Cartographer |
| 3 Synthesize | Vinge, Chiang, Banks, Cartographer |
| 4 Build | Watts, Egan, Le Guin, Lem |
| 5 Structure | Asimov, Chiang, Banks |
| 7 Review | Asimov, Watts, Le Guin, Chiang, Cartographer, First Reader |
| 9 Polish | Line Editor, Asimov, Rajaniemi |

## Lengths

| Form | Words |
|---|---|
| Short story | 3,000 – 7,500 |
| Novelette | 7,500 – 17,500 |
| Novella | 17,500 – 40,000 |
