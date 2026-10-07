# Stage 4: Build

**Dispatch:** `lens-critic`, once per lens on the stage 4 panel (by default
Watts, Egan, Le Guin and Lem), in parallel. Use this prompt:

`Lens: <lens>. Stage: process/stages/04-build.md. Story: stories/<slug>.`

Don't pass `model:`.

## For the orchestrator

1. Before dispatching, write `stories/<slug>/04-bible.md` from
   `templates/story-bible.md`.
   - **Ending direction.** The bible settles where the ending goes and what
     it costs.
   - **Numbers.** It states every number and date the story depends on,
     together with its arithmetic.
2. After the stress test, resolve every must-fix note into the bible. Log
   each note in the bible's stress-test log, with what was done about it or
   why it was declined.

**Gate:** the bible is approved.

## For the agent

**Read:**
- `stories/<slug>/00-brief.md`
- the Decision section of `stories/<slug>/03-synthesis.md`
- `stories/<slug>/04-bible.md`

**Task:** stress-test the bible from your lens.

| Lens | Questions |
|---|---|
| Watts | Is the biology or neuroscience right, and which real mechanisms support or contradict it? Are minds more coherent or self-aware than the evidence allows? Where does the story flinch? Aim at wonder and unsettling truth, not misery. |
| Egan | Does the logic hold? Find every edge case that breaks the novum, its rules or its arithmetic. Do posthuman minds think like posthumans? What next logical step does the story not take? |
| Le Guin | Does the society feel lived-in, with children and the old in it? Are the characters people or functions? Who pays, and do we see them? Do the invented words imply a culture? Are the names plausible and respectful? |
| Lem | Is the alien truly alien, or a human in costume? Does the story flatter anyone's ability to understand? Where is the irony? Does it resolve too much? Could a document or fragment do more than narration? |
| other | Your persona's "In critique" questions. |

Give at most 6 notes. Tag each one [must-fix], [should] or [could], and
give each a concrete suggestion that fits the brief's length. Keep the
whole critique under 600 words.

**Write:** `stories/<slug>/04-critique/<lens>.md`

**Reply:** your must-fix notes, one line each.
