---
created: 2026-10-11
status: proposed
---

# Make stories legible to a human reader, and gate on it

Two stories have now reached the human, and the human couldn't say what
either was about. The comprehension gate added after calibration-01 didn't
catch run-02: a cold model reader recovered meaning the human couldn't, and
the gate counts only that reader's answers, not its reported confusion. This
design changes three things:

- **The gate measures confusion as well as recall.** A long lost-list fails
  it, and so does a term the reader understood only from outside the story.
- **The style guide stops licensing opacity.** It replaces "leave invented
  terms undefined" with a rule that every term earns its place and is clear
  from the page.
- **Synthesis and the bible must make the premise plain.** A premise has to
  survive a two-sentence pitch to a non-SF reader, and the world's
  mechanism has to be shown, not only read out.

## What is true today

**The human missed every graded row on run-02.** "Strike Note" is a 5,943-word
story on the branch `bestdan/story-run-02`; its debrief is
`stories/run-02/debrief.md` on that branch. Asked the seven comprehension
questions, the human answered "I don't know / I'm not sure" to questions 2
to 7, and to question 1:

> I kind of don't know. It's vaguely a coming of age story, that part I got.
> However, the mechanism and the importance of the netting is unclear. [...]
> And the nature of the decision the main character has to made was unclear.

On the same `final.md`, the grader gave the cold reader "got it" on Why and
Who's who and "partial" on Premise, Stakes and Ending
(`reviews/final/comprehension.md`). This is the revisit trigger of
[the comprehension-gate decision](../decisions/2026-10-06-comprehension-gate.md):
"the reader and grader passed a row that the human missed".

**The reader had no inside information.** The `first-reader` agent reads
only `personas/first-reader.md` and the draft (`.claude/agents/first-reader.md`),
and the persona says nothing about any story. The grader sees only the
ledger rows, `names.md` and the answers. The gap is on the model's side:

- **It knows the languages the story doesn't explain.** The story uses
  untranslated Portuguese throughout: *uai* 7 times, *brabo* 6, *agarrada*
  6, plus *Pregar*, *cata-vento*, *Entrega*, *Irmandade* and *sino de mão*.
  A model reads them from its own knowledge.
- **It reads at full attention.** The story states its mechanism once, in a
  legal text read aloud in the clinic scene (`final.md` lines 101 and 105,
  about 240 words). The cold reader absorbed it and called it "homework".
  The human didn't absorb it.
- **It performs being a reader.** Its report says of one scene "I thought
  about it for days", an experience it didn't have. Its Felt signals are
  performed too.

**The reader reported the human's snags, and the gate ignored them.** Under
"Where I got lost", `reviews/final/first-reader.md` has seven entries,
among them the clinic reading, one entry listing five terms (*Pregar*,
*agarrada*, *cata-vento*, *brabo*, *bricked*), the 22 September fountain
paragraph and the 28 September decision paragraph. It says "the opening
pages were work". The gate in `process/stages/07-review.md` reads only
`comprehension.md`, so none of this counted.

**The grader's names list is a glossary.** Stage 7 has the orchestrator
write `names.md` with "each named character and invented term, with its
role". The grader therefore knows what *firma*, *the nets* and *agarrado*
mean whether or not the page said so.

**The style guide asks for this opacity.** `process/style-guide.md`
positive rule 3 says "Leave invented terms undefined while context carries
them", and rule 2 says characters "don't explain it to each other". The
drafter followed both. The human's verdict on the result:

> The use of novel words/terms without benefit was particularly high. [...]
> You need to spend more time making clear what's happening and why, and
> not trying to use fancy language.

> Jargon can be cool when it serves a purpose and is clear what it conveys.
> When it's just random words to indicate local slang, less so.

The human's example: "two labs answered and one not yet, which would,
obviously, ceiling, the whole thing ceiling." The human got the sentence
except "ceiling". The friends use it 7 times, and "bricked" 5 times, as
slang the story never explains. Neither is in the bible's Glossary
(`04-bible.md`), so no stage was checking them.

**The premise didn't survive the human's first questions.**

> To be honest, I don't care about Davi. Why the heck are they making bells?
> Why would that benefit from intelligence boosting? What's the tension?

The synthesis gate (`process/stages/03-synthesize.md`) checks novelty,
futurity and load, but never asks whether the premise can be stated plainly
to someone outside the genre. On atmosphere, the human found "very little
contextual world-building to give bones to the vibes". On prose: "good, but
exclusive to the casual reader".

## Proposal

### 1. The gate counts confusion, not only recall (stage 7)

- **The lost-list is graded.** The grader also reads the "Where I got lost"
  section of `first-reader.md`. The gate fails if any lost entry concerns a
  graded ledger row's fact, or if there are more than three entries in all.
  Three is a starting threshold. No report so far has come under it: run-02's
  four rounds listed 8, 7, 6 and 7 entries, and calibration-01's two rounds
  listed 7 and 7. So this rule would have failed every round of both
  stories, which matches the human's read: no story to date has held the
  human's immersion. The ledger-row rule is the hard fail; the count is the
  part to tune from the next debriefs.
- **A turn-2 question on terms.** The reader is asked an eighth question:
  "Which words or terms didn't you know from the story itself, and where did
  you get their meaning, if you got it?" Any term the reader understood
  only from outside knowledge (another language, a trade's jargon, prior
  reading), or got wrong, fails a new **Terms** row. Terms is a gate row,
  unlike Who's who, which stays a score. The debrief template asks the
  human the same question.
- **`names.md` lists characters only.** Invented terms move to a separate
  `terms.md`, which the grader uses only to grade the Terms row, so the
  terms' meanings don't leak into grading the other rows.
- **The reader reports only this read.** Add to the persona's rules: report
  what happened while reading, and claim no experience you didn't have
  ("I thought about it for days" is out). The persona's prompt "The question
  I'd still be thinking about the next day" asks for exactly that, so it
  becomes "The question you're left with at the end, if there is one".

### 2. Jargon has to pay for itself (style guide, stages 4, 6 and 9)

Replace positive rule 3 ("Trust the reader, then pay them") with:

> **Every term earns its place, and the page makes it clear.** A coined or
> foreign word stays only when it does a job the plain word can't: it names
> something the reader's world has no word for, or its strangeness is the
> point. Its meaning is clear from the page at its first use, to a reader
> who doesn't speak the language. Slang and dialect for local colour alone
> don't qualify; use the plain word.

Add "ceiling, the whole thing ceiling" to rule 10's examples, as the
counterpart of the calibration-01 line the human couldn't follow. Rule 2
("Live the novum, don't lecture it") stays, with a second sentence: living
the novum is not a reason to leave its mechanism unstated.

The style guide's **Invented terms** section changes to match:

- **The apposition ban stays.** A term is made clear by its role and its
  use on the page, not by a dictionary-style gloss (", a device that…").
- **The coinage bullet is qualified.** Compounding, clipping, borrowing and
  slang remain the ways to coin a term, but only for a term that passes the
  Job test. Slang that is there only for local colour gets the plain word.

The bible's Glossary gains two columns, **Job** (what the plain word
couldn't do) and **Clear at first use by** (the line that makes it clear).
A term with no job is cut at stage 4. The line editor's jobs in
`personas/line-editor.md` gain one: replace any term the glossary doesn't
justify with the plain word.

### 3. The premise can be said plainly (stage 3)

Each premise in `03-synthesis.md` gains a **Plain pitch**: two sentences to
a smart reader outside the genre, saying why this world does this, why it
matters to this person's life or trade, and what they are torn between. The
gate rejects a premise whose plain pitch doesn't hold up, or whose novum
doesn't bear directly on what the protagonist does all day. The Banks lens
already asks "Is it enjoyable to inhabit?"; the Chiang lens gains "Would a
reader care about this person in the first page, and why?"

### 4. The world reaches the page (stages 4 to 6)

Each graded payoff-ledger row is made clear twice: once **stated**, in
plain words, and once **shown**, as a consequence in a scene. A statement
can't be a quoted document of more than about 150 words, which is the form
run-02's mechanism took. The bible gains a short **What the reader needs
about the world** list: the three to five facts of daily life the premise
rests on, each placed in the first third by the outline.

## Decisions

### Confusion is a gate input, not only recall

**Chosen:** the lost-list and a Terms row can fail the gate. **Rejected:**
keeping the gate to the five recall rows and making them stricter. The cold
reader's recall beat the human's on every row, so stricter grading of
recall still measures the model. Its confusion report is the signal that
matched the human, and the gate threw it away.

### The reader stays on sonnet

**Chosen:** keep the model, change what it is asked. **Rejected:** a weaker
model as a stand-in for a casual human reader. The comprehension-gate
record rejected opus as too strong; a weaker model might predict the human
better. It is worth a test, but it is a change to the reader rather than to
what the gate measures, so it isn't decided here.

### Terms must pay, rather than a term budget

**Chosen:** every term needs a job and a first-use line. **Rejected:** a
numeric cap on invented terms, enforced by lint. The human's rule is about
purpose, not count ("Jargon can be cool when it serves a purpose"), and a
lint can't tell a coined word from an ordinary one without a per-story
list.

### The pitch test sits at synthesis

**Chosen:** a plain pitch on each premise at stage 3. **Rejected:** catching
an unclear premise at stage 7. By stage 7 the story is drafted. Run-02's
"why bells?" problem was set when the premise was chosen at stage 3, and
four review rounds didn't raise it.

## Not decided here

- **The reader model.** Whether a weaker model, or two readers of different
  strength, predicts the human better.
- **The lost-list threshold.** Three is a guess; the next two debriefs
  should set it. If stories keep reaching the loop cap on the count alone,
  change the threshold or the persona's "Where I got lost" prompt, not the
  rule. Counting only entries the reader never resolved is ruled out: most
  of run-02's entries say the reader worked the meaning out from context,
  so that rule would have passed a story the human couldn't follow.
- **A lint rule for terms.** A per-story `terms.toml` the lint could check
  first uses against is possible, but waits on whether the judgement rules
  above are enough.
- **What happens to run-02.** It stays unmerged as a record. Whether to
  rewrite it under the new rules is a separate call.

## Graduation

- **Decision records:**
  - one superseding the comprehension-gate record, for confusion as a gate
    input and the Terms row;
  - one for the "terms must pay" rule replacing "trust the reader";
  - one for the plain-pitch test at synthesis.
- **Conventions:**
  - `process/stages/07-review.md`: the eighth question, `terms.md`, and the
    new gate rule.
  - `.claude/agents/first-reader.md`, `personas/first-reader.md` and
    `.claude/agents/comprehension-grader.md`: the reader and grader changes,
    including a Gate line that names Terms and the lost-list rule.
  - `process/style-guide.md`: rules 2, 3 and 10, and the Invented terms
    section.
  - `templates/story-bible.md`: the Glossary columns and the world list.
  - `process/stages/03-synthesize.md`: the plain pitch.
  - `process/stages/04-build.md`, `05-structure.md` and `06-draft.md`: the
    stated-and-shown rule; `04-build.md` also cuts any glossary term with
    no Job.
  - `personas/line-editor.md`: the plain-word job.
  - `templates/debrief.md` and `process/rubric.md`: the Terms row.
  - `tests/test_agents.py` and `tests/test_process.py`: the eighth
    question, the grader's Gate line naming Terms and the lost-list rule,
    stage 7 writing `names.md` and `terms.md`, and the Terms row in the
    debrief template and rubric.
