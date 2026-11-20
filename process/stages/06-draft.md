# Stage 6: Draft

**Dispatch:** one `drafter`, with this prompt:

`Stage: process/stages/06-draft.md. Story: stories/<slug>.`

Don't pass `model:`. Keep the agent's ID. Stage 8 resumes this same agent
with SendMessage, so the voice holds across drafts. If the brief names a
model outside Claude Code as the drafter, follow
`dev_docs/external-drafter.md` for how to run it; everything in this file
still applies.

## The tone sample

The drafter writes the opening first, and the voice is checked against the
brief's Tone before the rest is built on it. Run-08's brief asked for
"funny and wry"; a lens saw the wry voice fade on draft 1, nothing carried
the note, and the human found the finished story neither. A voice is cheap
to change at 800 words and a rewrite at 7,000.

1. **The sample.** The drafter's first task (below) is the opening scene,
   or about 800 words, written to `drafts/sample.md` with no drafter's
   notes.
2. **The read.** Dispatch a fresh `first-reader` with this prompt:

   `Read stories/<slug>/drafts/sample.md. It is the opening of a longer story. Write to stories/<slug>/drafts/sample-tone.md: the tone, in three words, and the line that set it. Reply with the three words.`

3. **The comparison.** Dispatch one `lens-critic`, the lens whose standing
   fits the brief's tone (Banks for comic, by default), with this prompt:

   `Lens: <lens>. Stage: process/stages/06-draft.md, the tone sample. Story: stories/<slug>.`

4. **The decision.** If the lens says the tone matches, resume the drafter
   for the whole draft. If not, resume it once with the lens's notes to
   rewrite the sample, then go on whatever the second reading says, and
   log any remaining gap in `STATUS.md` for the stage 7 tone check. Log
   the check like a gate, with the reader's three words.

## For the orchestrator

- Read the draft yourself before review starts.
- Commit it.

## For the agent (`lens-critic`), the tone sample

**Read:** `stories/<slug>/00-brief.md` (its Tone), the bible's Register
line, `drafts/sample.md`, and `drafts/sample-tone.md`, the cold reader's
words.

**Task:** say whether the sample reads in the brief's tone. The cold
reader's three words are the evidence; your own reading comes second,
because you know what tone to expect. If it misses, name at most three
lines where it misses and say what the tone needs there, in terms of
mechanism and situation, not adjectives about the narrator.

**Write:** `stories/<slug>/drafts/sample-review.md`, opening with
**Match:** yes or no.

**Reply:** the Match line and one sentence.

## For the agent

**Read, in this order:**
1. `stories/<slug>/00-brief.md`
2. the Decision section of `stories/<slug>/03-synthesis.md`
3. `stories/<slug>/04-bible.md`, all of it. Its amendments and stress-test
   resolutions are binding.
4. `stories/<slug>/05-outline.md`. Its scenes table is the plan.
5. `process/reader-profile.md`, the *How the best-loved stories are built*
   section. It says who this story is for.

**Task, first:** write the opening scene, or about 800 words, in the
voice the bible sets, to `stories/<slug>/drafts/sample.md`. Reply with its
word count and stop. The orchestrator checks its tone and resumes you,
either to rewrite it with notes or to go on.

**Task, then:** write the whole story as draft 1, opening from the
accepted sample.
- **Length.** Stay within the brief's length range; its top is the hard
  ceiling. Within it, take the words the payoff ledger needs.
- **Title.** Choose your own; a working title is only a placeholder.
- **Voice and form.** Use the voice the bible sets, and any headings or
  formal device the outline specifies.
- **Planting.** Plant every fact the ending depends on before the ending
  needs it, and make sure any arithmetic is actually correct.
- **Withholding.** Withhold only what the outline says to withhold, and
  only until the payoff point the outline gives for it. Every payoff-ledger
  row in the bible is made explicit on the page, and Stakes comes before the
  climax.
- **Stated and shown.** Each graded row is stated once in plain words and
  shown once as a consequence in a scene. A statement can't be a quoted
  document of more than about 150 words. Each fact in the bible's world list
  is on the page in the first third.
- **Introductions.** Bring in each name and invented term with its role
  attached, at the pace the outline's Introduces column sets.
- **Terms.** Use no coined, foreign or slang word that isn't in the bible's
  Glossary. Make each one clear at first use, the way the Glossary says.
  Where you're unsure a reader would get it, use the plain word.
- **Specificity and colour.** Make every sentence specific: things,
  weather, food, materials. Err toward more description, not less. An idea
  the story rests on gets a scene, not a few sentences (the style guide's
  rule 11).
- **The other mind.** If the story has one, show it reasoning about the
  people it deals with, as the synthesis Decision and the bible's Minds
  section set out. Its outputs alone read as a transcript.
- **Lint.** Run `just lint stories/<slug>/drafts/draft-1.md`. Fix every error
  and every budget overrun. If you break a linted rule on purpose, add a
  waiver to `stories/<slug>/lint-waivers.toml` with the reason.

After the story, add a `## Drafter's notes` section with:
- the word count of the story text alone;
- for each payoff-ledger row, the line that makes it explicit, quoted, and
  for each graded row, the scene that shows it;
- each departure from the outline, and why;
- each rule broken on purpose, and why.

**Write:** `stories/<slug>/drafts/draft-1.md`

**Reply:** the title, the word count, and one sentence on the biggest risk you
see in the draft.
