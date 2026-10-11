# Stage 8: Revise

**Dispatch:** the same `drafter` that wrote draft 1. Resume it with
SendMessage if its context is still available. Otherwise dispatch a new
`drafter` with this prompt:

`Stage: process/stages/08-revise.md. Story: stories/<slug>. Next draft: N+1.`

Don't pass `model:`.

## For the orchestrator

1. Before dispatching, write `stories/<slug>/06-revision-plan.md` with:
   - **Scores:** three tables, by the groups in `process/rubric.md`. Felt
     and Craft come from the lenses, one column per lens. Understood comes
     from `reviews/draft-N/comprehension.md`, cited by path; it adds the
     legibility scores beside Character and Consequence. No mean crosses
     groups.
   - **Consensus:** notes two or more lenses raised. These get fixed.
   - **Adopted single-lens notes.**
   - **Conflicts:** each one resolved with a recommendation for the human.
   - **Declined:** each note not taken, with the reason.

   Rewrite the file each round. Git history keeps the earlier rounds.
2. Number every item, so the drafter can report against each one.
3. **Comprehension.** Every ledger row that `reviews/draft-N/comprehension.md`
   grades partial or missed becomes a structural item in the plan, citing
   the grade and the reader's answer. Add it whether or not any lens raised
   it. So does each term that failed the Terms row (make it clear on the
   page, or use the plain word), and each lost-list entry, starting with
   those the grader tied to a graded row. You may lower a grade, never raise
   one.
4. **Loop cap.** If the comprehension gate has failed two rounds in a row,
   log it, and get an `agent-guidance:consultant` opinion on whether one
   more round can close the gap. Then either take that round or proceed to
   stage 9. Either way, record the unclosed rows in `STATUS.md` under
   "Gate failures". Never pass the gate by grading leniently.

**Gate:** the plan is approved, and later the draft is called structurally
done. In `human` mode, the human approves each plan and calls the draft
done. In `proxy` mode, the orchestrator does both and logs each decision in
`STATUS.md`. Stages 7 and 8 repeat until the draft is called structurally
done and the comprehension gate passes (or the loop cap lets it proceed),
usually after 2 or 3 rounds.

## For the agent

**Read:**
- `stories/<slug>/06-revision-plan.md`. It is binding.
- the payoff ledger in `stories/<slug>/04-bible.md`
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
- for each payoff-ledger row, the line that makes it explicit, quoted;
- one line per numbered plan item, saying how it was handled;
- anything declined, and why.

**Write:** `stories/<slug>/drafts/draft-(N+1).md`

**Reply:** the word count, and the story's new last three lines.
