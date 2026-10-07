# Stage 8: Revise

**Dispatch:** the same `drafter` that wrote draft 1. Resume it with
SendMessage if its context is still available. Otherwise dispatch a new
`drafter` with this prompt:

`Stage: process/stages/08-revise.md. Story: stories/<slug>. Next draft: N+1.`

Don't pass `model:`.

## For the orchestrator

1. Before dispatching, write `stories/<slug>/06-revision-plan.md` with:
   - **Scores:** a table, plus the mean for each lens.
   - **Consensus:** notes two or more lenses raised. These get fixed.
   - **Adopted single-lens notes.**
   - **Conflicts:** each one resolved with a recommendation for the human.
   - **Declined:** each note not taken, with the reason.

   Rewrite the file each round. Git history keeps the earlier rounds.
2. Number every item, so the drafter can report against each one.

**Gate:** the human approves the plan. Stages 7 and 8 repeat until the human
calls the draft structurally done, usually after 2 or 3 rounds.

## For the agent

**Read:**
- `stories/<slug>/06-revision-plan.md`. It is binding.
- the reviews in `stories/<slug>/reviews/draft-N/` that the plan cites
- `stories/<slug>/drafts/draft-N.md`

**Task:**
- Write draft N+1 from the plan.
- Keep the voice, and protect everything the reviews and the plan say to
  protect.
- Leave `draft-N.md` untouched.
- Run `just lint` on the new draft, and fix every error and budget overrun.

After the story, add a `## Drafter's notes` section with:
- the word count of the story text alone;
- one line per numbered plan item, saying how it was handled;
- anything declined, and why.

**Write:** `stories/<slug>/drafts/draft-(N+1).md`

**Reply:** the word count, and the story's new last three lines.
