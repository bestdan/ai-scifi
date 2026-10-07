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

1. **Required items.** Before dispatching the line editor, collect the
   line-level notes from the last review round into a numbered list, and add
   it to the line editor's prompt as "Required items".
2. **Spot-check suggestions.** Apply or decline each one. Log each decline,
   with its reason, in `STATUS.md`. Then run `dli check`.
3. **Optional EPUB.** For reading on a device, run
   `python3 scripts/make_epub.py stories/<slug>/final.md stories/<slug>/<title>.epub`.

**Gate:** the human signs off. After that, the story branch can land (see
`AGENTS.md`).

## For the agent (`line-editor`)

**Read:**
- `stories/<slug>/drafts/draft-N.md`
- the last round's reviews in `stories/<slug>/reviews/draft-N/`
- the Glossary and Characters sections of `stories/<slug>/04-bible.md`

**Task:**
- Do the six jobs in your persona file.
- Handle every "Required item" in the prompt.
- Cut 3% to 6% of the words, taken from slack rather than texture.
- Change no structure. A structural problem goes back to stage 8, so report
  it rather than fixing it.
- `just lint stories/<slug>/final.md` must pass.

**Write:**
- `stories/<slug>/final.md`: the title and story text only, with no notes.
- `stories/<slug>/reviews/polish-changelog.md`: the categories of change,
  with counts; how each required item was handled; the judgement calls for
  the human; and the final word count.

**Reply:** the word count, and the last three lines of the story.

## For the agent (`lens-critic`, spot-check)

**Read:**
- `stories/<slug>/reviews/polish-changelog.md`
- `stories/<slug>/final.md`

**Task:** a spot-check only, since the structure is frozen.

| Lens | Checks |
|---|---|
| Asimov | Clarity. Did the polish introduce any contradiction in the logic, the arithmetic or the rulings? |
| Rajaniemi | Density and texture. Is anything still explained that context would carry? Are the invented terms consistent with the bible's glossary? Is there a familiar detail that one word could make stranger? |

Give at most 5 suggestions, each written as `current text → exact
replacement`. If something is fine, say so; don't invent work. Keep it under
300 words.

**Write:** `stories/<slug>/reviews/polish-<lens>.md`

**Reply:** your suggestions as `current → replacement` pairs, or "none".
