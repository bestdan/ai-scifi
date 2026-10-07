# Stage 7: Review

**Dispatch, in this order.** Don't pass `model:`.

1. A **fresh** `first-reader` every round, never a resumed one, with this
   prompt:

   `Read stories/<slug>/drafts/draft-N.md and write your report to stories/<slug>/reviews/draft-N/first-reader.md. Reply with who you cared about and whether you'd have kept reading past page 2.`

   The `first-reader` doesn't read this file. Its definition and that prompt
   are its whole brief. Keep its agent ID for the comprehension gate.
2. Once its report is written, in parallel:
   - `lens-critic`, once per lens on the stage 7 panel, with this prompt:

     `Lens: <lens>. Stage: process/stages/07-review.md. Story: stories/<slug>. Draft: N.`

   - the comprehension gate below.

## Comprehension questions

1. What is this story about, in two sentences?
2. What does the protagonist stand to gain or lose, and what happens if they fail?
3. Why did the people or powers who set this situation up do it that way?
4. What did you learn late that changed how you saw the earlier part, if anything?
5. What happened at the end, and why?
6. Who is each named character, in one line each?
7. What are you still unsure about?

These questions appear nowhere else the reader can see. Asked before the
read, they would steer it.

## The comprehension gate

All of its files go in `stories/<slug>/reviews/draft-N/`.

1. **Turn 2.** Once `first-reader.md` is written, resume the same
   `first-reader` with SendMessage:

   `Answer these from memory, without rereading. Write your answers, numbered, to stories/<slug>/reviews/draft-N/comprehension-answers.md.`

   followed by the seven questions above, word for word.
2. **The grader's inputs.** Write two files from `04-bible.md`:
   - `ledger-rows.md`: only the Row and The fact columns of the payoff
     ledger's five graded rows. No scenes, no explicit lines.
   - `names.md`: each named character and invented term, with its role in
     one line, from the bible's Characters and Glossary sections.
3. **Grading.** Dispatch a fresh `comprehension-grader` with this prompt:

   `Ledger: stories/<slug>/reviews/draft-N/ledger-rows.md. Names: stories/<slug>/reviews/draft-N/names.md. Answers: stories/<slug>/reviews/draft-N/comprehension-answers.md. Write: stories/<slug>/reviews/draft-N/comprehension.md.`

The gate passes when every graded row is "got it" (or N/A for a story with
no twist). Stage 8 acts on a fail; stage 9 can't start without a pass.

## For the orchestrator

- **Round 1** uses the full default panel.
- **Later rounds** can run leaner: the lenses that scored lowest or raised
  structural notes, plus a fresh First Reader and the comprehension gate.
  The gate runs every round.
- **You don't grade comprehension.** You wrote the ledger, so you read the
  answers as an insider would. You may lower one of the grader's grades, with
  a reason, but never raise one.

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
- Score it against the Drafts table in `process/rubric.md`: the Felt and
  Craft axes only, and only where your lens has standing. Mark the rest "—".
  You've read the bible, so you don't score the Understood axes; the
  comprehension grader does. For the Felt axes, read
  `stories/<slug>/reviews/draft-N/first-reader.md`, and weigh where the
  cold reader was moved, surprised or delighted.
- Fill in "What to protect". It's required, and a lens that scores Prose
  quotes at least one line.
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
