# Stage 1: Ideate

**Dispatch:** `lens-ideator`, once per lens on the stage 1 panel, all in one
message so they run in parallel. Use this prompt:

`Lens: <lens>. Stage: process/stages/01-ideate.md. Story: stories/<slug>.`

Don't pass `model:`. The agent definition sets it.

## For the orchestrator

- Wait until every lens has reported, then commit the idea cards.
- Stage 1 has no gate. The cards go straight to the stage 2 audit.

## For the agent

**Read:**
- `stories/<slug>/00-brief.md`. It sets the number of cards (3 unless the
  brief says otherwise), the target length, the Futurity floor and any seed.

**Task:**
- Write exactly the brief's number of idea cards, working from the "In
  ideation" section of your persona.
- Every card meets the brief's Futurity floor and honours the tone charter.
- Before you write a card, name the nearest published story to it. If that
  story is a close match, discard the card and go further.
- At short lengths, the novum must be dramatizable with a small cast in a
  few scenes.

**Write:** `stories/<slug>/01-ideas/<lens>.md`, using
`templates/idea-card.md`. State your lens's blind spots at the top.

**Reply:** each card's title and a one-line statement of its novum. Nothing
else.
