---
created: 2026-11-20
status: proposed
---

# Run-08 takeaways: an early tone check, a gate that stops failing on recall, and an external drafter

Run-08 landed with the human picking every graded row correctly, but the
brief's tone ("funny and wry") didn't come through, and nothing in the
pipeline could have told us, because no stage owns the brief's tone. The
gate failed on every read, which fired the loop cap and spent a third
revision round, while the human, who reads days later, got every row the
cold reader was partial on. Part of that failure was the orchestrator
listing real words (californium, "Actuarial") as terms, which the rubric
already excludes. This design proposes five changes: a tone check on an
opening sample before the full draft, two corrections to how the gate
counts, a debrief asked one question at a time, and a written protocol for
drafting with a model outside Claude Code.

## What is true today

Evidence is from `stories/run-08/` unless a path says otherwise.

- **The brief's tone has no owner after stage 0.** `templates/brief.md`
  carries a Tone field and the bible restates it as a Register. No stage
  file, lens question or rubric axis checks a draft against it: `rg -i
  tone process/stages` finds only the tone charter and Banks's stage 3
  question "Where does the humour live?". Banks is not on the draft panel.
- **The signal was there and went nowhere.** At stage 5 Banks noted "Wit
  thins" (`05-outline.md`). On draft 1 Chiang wrote "By Day 117 the
  register is long additive catalogues" and "The wry teller disappears"
  (`reviews/draft-1/chiang.md`). Neither note maps to a graded row, so the
  revision plans, which are built around the gate, never carried them.
- **The human, at the debrief:** "The tone didn't come across as funny or
  wry." On when to catch it: "early enough on to catch issues rather than
  at the end when it's already written" (`debrief.md`).
- **The gate under-predicts the human on dramatised rows, for the third
  run.** The cold reader on `final.md` was partial on Premise, Stakes,
  Twist, Ending and Reach. The human picked all five correctly. Each is
  carried in a scene (the moot, Day 117, Day 118, the coda). Run-05 and
  run-06 showed the same, and `process/stages/07-review.md` already says
  so in "Dramatised, not stated". But the pass rule still requires every
  row to be "got it", so the note changes how the orchestrator reads a
  failure, not whether the gate fails.
- **A partial is often one omitted clause.** Draft 2's Stakes and Ending
  partials each "omit one clause" (STATUS, Gate failures). On `final.md`,
  Twist omits "teaching by touch" while its explicit line was unchanged
  since it passed on draft 3.
- **Terms failed on real words the rubric excludes.** `process/rubric.md`:
  "Real units and scientific words, such as kelvin or astronomical unit,
  are not terms." Yet draft 2's Terms row was "missed" on "californium"
  and "Actuarial", from outside knowledge
  (`reviews/draft-2/comprehension.md`). They were graded because the
  orchestrator put them in `terms.md` under "Used by the draft, not in the
  Glossary". Stage 7 step 2 says that list is for "coined, foreign or
  slang" words, but nothing stops a real one going in, and the grader has
  no way to tell.
- **The loop cap cost a round.** Draft 2 failed on Stakes and Ending
  (partial) and Terms. Round 3 was spent under the loop cap, and its
  success test failed partly on reader variance: "Premise and Reach fell
  to partial, though round 3 changed no text they rest on" (STATUS).
- **A gloss didn't make the Desk clear.** Polish glossed it at first use as
  "my dispatcher at sector headquarters" (`reviews/polish-changelog.md`).
  The final reader still couldn't tell "whether the Desk is a person", and
  the human answered "No idea". The bible defines it as "a voice with a
  six-hour lag"; the page never shows it as either.
- **The debrief check is written as one block.** `10-debrief.md` step 3:
  "show the whole check at once". The human asked instead for one question
  at a time through the question dialog. That dialog takes at most four
  options, so each question carried three of its options plus "Can't say".
- **Drafting with Gemini needed workarounds nobody wrote down.** Stages 6,
  8 and 9 ran on Gemini 4 Argon through the `agy` CLI on the human's
  subscription (STATUS header). Gemini can't count its own words: it
  reported 6,812 for a 10,985-word draft. Per-section counts and
  replacement-paragraph patches held the length. Without tool access the
  orchestrator inlined every input. The human has since added `agy`
  permission grants (`command(just lint)`, `write_file(stories/)`,
  `command(wc -w)`), and a test confirmed Gemini can now write, count and
  lint for itself without the bypass flag.

## Proposal

1. **A tone sample at the start of stage 6.** Before writing the whole
   draft, the drafter writes the opening section (about 800 words, or the
   first scene) to `drafts/sample.md`. A fresh `first-reader` reads only
   the sample and answers one question: "Describe the tone in three words,
   and quote the line that sets it." A fresh `lens-critic`, using the lens
   the brief's tone names (Banks for comic, by default), compares the
   answer and the sample with the brief's Tone. If the tone misses, the
   drafter rewrites the sample once before going on. The check is logged in
   STATUS like any gate. The full draft is then written from the accepted
   sample, so the voice is set before 7,000 words are built on it.
2. **The first reader reports tone at stage 7.** The first reader's report
   gains one question: "What tone did the story have?" The orchestrator
   sets that answer beside the brief's Tone in the revision plan. It
   doesn't fail the gate (tone isn't comprehension), but a miss goes into
   the plan as an item, so a note like "the wry teller disappears" has a
   home.
3. **A partial on a dramatised row passes the gate.** A row graded
   "partial" counts as passing when all three hold: the bible's "Shown in"
   scene dramatises it in the draft; the grader says the answer omits a
   part rather than getting one wrong; and no lost-list entry concerns that
   row. A row that is only stated still needs "got it". The partial stays
   in the revision plan as a note.
4. **`terms.md` holds coined, foreign and slang words only.** Real words,
   scientific or institutional (californium, "actuarial"), never go in,
   even when a reader might not know them. The grader is told the same, so
   an answer saying "I knew it from outside" can't fail the row on a real
   word. A real word a reader didn't know is a lost-list or prose note.
5. **An institution that speaks only through messages is shown, not
   glossed.** For a Glossary term that is an office, a role or a channel,
   the bible's "Clear at first use by" line names what it does on the page
   at first use (the Desk replies, with its lag), not an appositive. The
   line editor may not fix such a term with a gloss alone.
6. **The debrief check is asked one question at a time.** `10-debrief.md`
   step 3 changes from "show the whole check at once" to: ask each row in
   the question dialog, one per call, with three options plus "Can't say"
   (four is the dialog's limit), so each row keeps its right answer and
   its two strongest wrong ones. Who's who is asked per name, and Terms as
   multi-select groups. The written check stays in `debrief.md` as the
   record.
7. **A convention for drafting with an external model.** A new
   `dev_docs/external-drafter.md` records how to run the one drafter on a
   model outside Claude Code, using Gemini through `agy` as the worked
   case: how to sign in on a subscription, one resumed conversation for
   the whole story, the permission grants that let it write, count and
   lint, the orchestrator measuring every word count, per-section counts
   for length rounds, and replacement-paragraph patches for revisions and
   polish. The "one drafter" rule is unchanged.

## Decisions

### The tone check runs on a sample, before the full draft

The check runs on the opening section before the rest is written. The
alternative, a tone axis on the full draft at stage 7, was rejected: that
is where run-08 already had the signal (Chiang on draft 1) and couldn't use
it, because by then a voice change is a rewrite and the gate's rows
crowd it out. The human asked for the check early for this reason. The
cost is one short reader and one lens per story, and at most one extra
sample.

### Tone is judged by a cold reader's words, with a lens comparing

A cold reader names the tone, and a lens compares that with the brief. A
lens alone was rejected because lenses read the bible's Register first and
see the tone they were told to expect. Asking the human was rejected
because in proxy mode the human reads blind, and an opening sample shows
the premise.

### A partial on a dramatised row passes

The gate counts a partial as passing when the row is dramatised in a scene,
the answer omits rather than errs, and no lost-list entry concerns the row.
Keeping "every row got it" was rejected on three runs of evidence: on rows
carried in scenes, the human picked correctly where the reader was
partial. The rule stays strict where the gate is right: rows the page only
states still need "got it", since those are where the reader over-predicts
the human (run-06).

### Real words are never terms

Only coined, foreign and slang words go in `terms.md`. Listing every
unfamiliar word was rejected because the rubric already excludes real
words, and including them made Terms fail on draft 2 for a reader who knew
the words already.

### The debrief is asked one question at a time

Each question goes in its own dialog call. The written block was rejected
at the human's request: six multi-paragraph questions plus a matching
table is too much to answer at once. The four-option limit drops one
wrong option per question. The one kept is the most specific misreading,
which keeps the test that the stage 10 rules care about.

### External drafting gets a convention, not a stage change

The `agy` mechanics go in a `dev_docs/` convention. Writing them into
`06-draft.md` was rejected because they are tooling, and the stage file
should hold for any drafter. Stage 6 gains one line pointing to the
convention when the brief names an external model.

## Not decided here

- Which lens judges which tone. Banks for comic is the default proposed;
  a mapping for other tones (elegiac, cold) is left to the first run that
  needs one.
- Whether a missed tone at stage 7 should ever fail the gate. Proposed
  here as a plan item only.
- Whether Gemini's prose density, rather than the premise's load, caused
  the human's "small turns of phrase" friction. One run can't separate
  them; the next external-model run should compare.
- Whether the brief should name the drafter model as a field.

## Graduation

- Decision records:
  - a tone sample is checked before the full draft;
  - a partial on a dramatised row passes the gate;
  - real words are never terms;
  - the debrief is asked one question at a time;
  - drafting with an external model follows a convention.
- Conventions:
  - `process/stages/06-draft.md` (the tone sample; the external-model
    pointer);
  - `process/stages/07-review.md` (the tone question, the pass rule, the
    `terms.md` rule);
  - `process/stages/10-debrief.md` (one question at a time);
  - `process/rubric.md` (the Terms note, the tone line);
  - `process/style-guide.md` and `templates/story-bible.md` (institutions
    shown, not glossed);
  - `.claude/agents/comprehension-grader.md` (real words);
  - `dev_docs/external-drafter.md` (new).
