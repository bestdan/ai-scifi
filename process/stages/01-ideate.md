# Stage 1: Ideate

**Dispatch:** `lens-ideator`, once per lens on the stage 1 panel, all in one
message so they run in parallel. Use this prompt:

`Lens: <lens>. Stage: process/stages/01-ideate.md. Story: stories/<slug>.`

Don't pass `model:`. The agent definition sets it.

## For the orchestrator

- Before dispatching, run `python3 scripts/assign_ideation.py
  stories/<slug>`, adding `--lenses` if the brief changes the panel. It
  writes `01-ideas/assignments.md`, which gives every lens a different entry
  point, reader pull and stimulus. Don't pick these yourself: a model asked
  to choose at random chooses its favourites.
- Wait until every lens has reported, then commit the idea cards.
- Stage 1 has no gate. The cards go straight to the stage 2 audit.

## For the agent

**Read:**
- `stories/<slug>/00-brief.md`. It sets the number of cards (3 unless the
  brief says otherwise), the length range, the Futurity floor and any seed.
- your row of `stories/<slug>/01-ideas/assignments.md`: your entry point,
  your pull and your stimulus.
- `process/attractors.md`, all of it. It is the ground earlier runs kept
  landing on.
- `process/reader-profile.md`, the *What pulls* and *What disappoints*
  sections.

**Task:**
- **Discard the obvious card first.** Before writing anything, write down
  the card you'd write first: the most literal answer to the brief and its
  seed. Put it in the file's "Obvious card" line, then don't write it.
  Several lenses will have the same first thought, and only the second one
  is yours.
- Write exactly the brief's number of idea cards, from your assigned entry
  point. Aim at least one card at your assigned pull, and start from your
  stimulus. A card may travel far from the stimulus; say where it went.
- Stay off every entry in `process/attractors.md`. A card that breaks one
  says which, and why the story needs it.
- Every card is meant to clear the brief's Futurity floor and honours the
  tone charter. Don't rate your own Futurity, and don't borrow the rubric's
  wording to describe it: the Cartographer scores it.
- Before you write a card, name the nearest published story to it. If that
  story is a close match, discard the card and go further.
- At short lengths, the novum must be dramatizable with a small cast in a
  few scenes. Every extra novum or twist a card needs costs words; stage 3
  counts them against the brief's range.

**Write:** `stories/<slug>/01-ideas/<lens>.md`, using
`templates/idea-card.md`. State your lens's blind spots at the top.

**Reply:** each card's title and a one-line statement of its novum. Nothing
else.
