# Stage 7: Review

**Dispatch:** in parallel, send both of these. Don't pass `model:`.

- `lens-critic`, once per lens on the stage 7 panel, with this prompt:

  `Lens: <lens>. Stage: process/stages/07-review.md. Story: stories/<slug>. Draft: N.`

- A **fresh** `first-reader` every round, never a resumed one, with this
  prompt:

  `Read stories/<slug>/drafts/draft-N.md and write your report to stories/<slug>/reviews/draft-N/first-reader.md. Reply with your two-sentence "what I think the story is about" and whether you'd have kept reading past page 2.`

  The `first-reader` doesn't read this file. Its definition and that prompt
  are its whole brief.

## For the orchestrator

- **Round 1** uses the full default panel.
- **Later rounds** can run leaner: the lenses that scored lowest or raised
  structural notes, plus a fresh First Reader.

## For the agent (`lens-critic`)

**Read:**
- `stories/<slug>/drafts/draft-N.md`, in full. Stop at `## Drafter's notes`
  when reading as story; the notes are context only.
- whatever context your lens needs: the bible, the outline, or the synthesis
  Decision.
- **from round 2 on:** your own critique of the previous draft, in
  `stories/<slug>/reviews/draft-(N-1)/<lens>.md`, and
  `stories/<slug>/06-revision-plan.md`, which records how your notes were
  triaged.

**Task:**
- Review the draft from your persona's "In critique" angle. Quote exact
  lines.
- Score it against the Drafts table in `process/rubric.md`, and only on the
  axes where your lens has standing. Mark the rest "—".
- Name **the one thing**: the change that matters most from your lens.
- Classify every note as **structural** or **line-level**.
- Don't redo the linter's job. `just lint` reports the mechanical hits, so
  cite its output if it matters to you.
- The Cartographer also judges drift toward the nearest prior art, and flags
  stock beats.

Keep it under 600 words in round 1, and under 450 after that.

**Write:** `stories/<slug>/reviews/draft-N/<lens>.md`, using
`templates/critique.md`.

**Reply:** your scores row, the one thing, and one line saying whether any
structural problem remains.
