# Stage 9: Polish

**Dispatch, in this order:**

1. One `line-editor`, with this prompt:

   `Stage: process/stages/09-polish.md. Story: stories/<slug>. Draft: N.`

   N is the last draft.
2. Once the line editor's output is in, the spot-checks: `lens-critic`, once
   per lens (by default Asimov and Rajaniemi), in parallel, with this prompt:

   `Lens: <lens>. Stage: process/stages/09-polish.md. Story: stories/<slug>. Part: spot-check.`

Don't pass `model:`.

## For the orchestrator

1. **Before polish.** The stage 7 comprehension gate must have passed on
   draft N, in `reviews/draft-N/comprehension.md`. The one exception is a failure the
   stage 8 loop cap let through, logged under "Gate failures" in
   `STATUS.md`. Otherwise go back to stage 8.
2. **Required items.** Before dispatching the line editor, collect the
   line-level notes from the last review round into a numbered list, and add
   it to the line editor's prompt as "Required items".
3. **The protect list.** Also before dispatching, write
   `stories/<slug>/reviews/protect-list.md`: every line quoted under "What
   to protect" in the last round's reviews, every passage the First Reader
   was moved, surprised or delighted by, and every line the drafter's notes
   quote for a payoff-ledger row. Quote each one, and say where it came
   from.
4. **Spot-check suggestions.** Apply or decline each one. Log each decline,
   with its reason, in `STATUS.md`. Then run `dli check`.
5. **After polish, the gate again.** Run the stage 7 comprehension gate on
   `final.md`, with a fresh `first-reader` and a fresh
   `comprehension-grader`, and write every file to `reviews/final/` instead
   of `reviews/draft-N/`. A failed gate sends the story back to stage 8,
   except after a loop-cap pass (step 1). Then compare, for each failing
   row, the lines the drafter's notes quote for it in draft N with the same
   lines in `final.md`:
   - **Unchanged:** the reader differs, not the text. Log the row under
     "Gate failures" in `STATUS.md`, and go on.
   - **Changed in polish:** restore draft N's lines, log it, and go on.
     Polish may not break a row, and undoing that is a line fix, not a
     stage 8 round.
6. **Optional EPUB.** For reading on a device, run
   `python3 scripts/make_epub.py stories/<slug>/final.md stories/<slug>/<title>.epub`.
   `just kindle <slug>` builds the EPUB if it is missing or older than
   `final.md`, then emails it to the owner's Kindle. It needs an unsandboxed
   run, and uses the `ai-scifi` 1Password profile unless `OP_SA_PROFILE` is
   already set.

**Gate:** sign-off. In `human` mode, the human signs off. In `proxy` mode,
the orchestrator marks the story ready, logs it in `STATUS.md`, and tells
the human only that the story is ready and where. In both modes the branch
lands only on the human's word, after the debrief (see `AGENTS.md`).

## For the agent (`line-editor`)

**Read:**
- `stories/<slug>/drafts/draft-N.md`
- the last round's reviews in `stories/<slug>/reviews/draft-N/`
- the Glossary and Characters sections of `stories/<slug>/04-bible.md`
- `stories/<slug>/reviews/protect-list.md`

**Task:**
- Do the seven jobs in your persona file.
- Handle every "Required item" in the prompt.
- Cut slack, not texture. There's no target.
- Leave every line on the protect list alone, unless you log why it had to
  change.
- Change no structure. A structural problem goes back to stage 8, so report
  it rather than fixing it.
- `just lint stories/<slug>/final.md` must pass.

**Write:**
- `stories/<slug>/final.md`: the title and story text only, with no notes.
- `stories/<slug>/reviews/polish-changelog.md`: the categories of change,
  with counts; how each required item was handled; any protected line that
  changed, and why; the judgement calls for the human; and the word count
  before and after.

**Reply:** the word count, and the last three lines of the story.

## For the agent (`lens-critic`, spot-check)

**Read:**
- `stories/<slug>/reviews/polish-changelog.md`
- `stories/<slug>/final.md`

**Task:** a spot-check only, since the structure is frozen.

| Lens | Checks |
|---|---|
| Asimov | Clarity. Did the polish introduce any contradiction in the logic, the arithmetic or the rulings? |
| Rajaniemi | Density and texture. Is any explanation clumsy, as opposed to present? (A payoff-ledger line must stay explicit; only its phrasing is in question.) Are the invented terms consistent with the bible's glossary? Is there a familiar detail that one word could make stranger? |

Give at most 5 suggestions, each written as `current text → exact
replacement`. If something is fine, say so; don't invent work. Keep it under
300 words.

**Write:** `stories/<slug>/reviews/polish-<lens>.md`

**Reply:** your suggestions as `current → replacement` pairs, or "none".
