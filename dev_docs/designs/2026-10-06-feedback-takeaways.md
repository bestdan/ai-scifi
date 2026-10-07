---
created: 2026-10-06
status: proposed
---

# Make stories legible to a blind reader: payoffs, an outsider-graded comprehension gate, proxy gates

Calibration-01 ended with a story whose prose the human scored 5/5 and
whose point the human couldn't state. Asked what the story was about, what
was at stake and what the twist was, the human had "no real idea." Every
answer was in the story bible, which the process wrote and then kept off the
page on purpose. The cold readers did signal trouble. The draft-1 First
Reader said the twist's key line "lost me", and the draft-2 reader asked
"Did the Parties choose the term on purpose…? Pell wouldn't say, and neither
would the story." But the orchestrator, who wrote the bible, read those
reports as passes. The lens panel had read the bible too, and it scored the
draft as though the answers had landed. The human also wants to read the next
story blind.

This design makes five changes:

1. **Every inference pays off explicitly.** The process carries this through
   a payoff ledger.
2. **Polish needs a comprehension gate.** A cold reader answers fixed
   questions in a second turn, and a separate grader who sees only the ledger
   and the answers grades each one.
3. **The rubric splits into felt, understood and craft.** The outsider
   scores everything that depends on understanding.
4. **Polish protects lines as well as cutting them.**
5. **A proxy gate mode lets the human read blind.** The human keeps the brief
   and the decision to land the story.

It covers the eight takeaways in section 5 of
`stories/calibration-01/human-feedback.md`. That file holds the evidence.

## What is true today

**What the human reported** (`human-feedback.md`):

- **Takeaway 1.** All four of the human's "why" questions are answered in
  `04-bible.md`:
  - why the agreement exists;
  - what is at stake;
  - where the metamorphosis comes from;
  - how integral it is.

  The bible marks those answers "never explained" and "explained only through
  the treaty text and the clerk". Given the answers, the human found the
  premise "definitely a lot better and more interesting."
- **The human's rule** is that inference is fine, "but it definitely needs to
  pay off. … safest if the author always makes it explicit eventually."
- **Takeaways 5 and 7.** The human scored Consequence 2 and Character 2,
  against the panel's 4s; Prose 5, against 3–4; and Novum delivery 4.5,
  despite being unable to explain the novum. On the ending: "Didn't
  understand it, but felt the loss." The round-2 lens prompts told the lenses
  to read the bible "for context".
- **Takeaway 2.** The brief set 2,500 words, below `PROCESS.md`'s 3,000-word
  floor. The story carried two nova (the turn, and the posthuman escrow), two
  polities and a twist.
- **Takeaway 3.** The opening scene, "Nine", is 503 words and introduces
  Pell, Mrs. Okonjo, Oyelaran, Bisi, the Standing Revision, the Disputed
  Volume, the Parties, the Keeper and § 14. The first "Eight" adds about six
  more names in 296 words. The novum's own terms, "the turn", "keeper" and
  "seat", are lowercase.
- **Takeaway 6.** Every line the human protected is a concrete physical
  image or a moment between people. Two of them are "the way…" similes. The
  one line the human couldn't follow is an abstract, stacked construction.
- **Takeaway 8.** The human decided: the orchestrator acts as proxy at the
  gates, and the human reads only the finished story.

**What the cold readers reported** (`reviews/draft-*/first-reader.md`):

- **The premise.** Both readers already state it, and `personas/first-reader.md`
  counts a mismatch with the synthesis as a finding. Their premises were
  passable.
- **The twist.** On draft 1, the reader said of "They had built the term
  around the latest she could possibly be": "lost me … I didn't see why that
  mattered." On draft 2, the reader raised the twist only as an open
  question.
- **How it was read.** `MORNING.md` reported "neither reader mentioned the
  reveal". That's a misreading by the orchestrator, the same insider-grading
  failure the human's scores show in the panel.

**The rules that encode the problem today:**

| File | Rule |
|---|---|
| `process/style-guide.md`, rules 2–3 | "Live the novum, don't explain it"; exposition only "where a character in the scene has a reason to explain"; "leave invented terms undefined when context carries them". |
| `process/style-guide.md`, Invented terms | "never next to a gloss in apposition". |
| `templates/story-bible.md` | No place to record when a withheld fact becomes explicit. |
| `templates/outline.md` | The information plan has no "made explicit by" column. |
| `process/stages/07-review.md` | Lenses read the bible, then score every axis, including the ones that depend on understanding. |
| `process/rubric.md` | The draft axes mix feeling and understanding (Novum delivery, Consequence, Ending). |
| `personas/line-editor.md`, `process/stages/09-polish.md` | "Cut 5 to 10 percent … Shortness is a feature" and "Cut 3% to 6%". Nothing protects a line. |
| `process/stages/09-polish.md`, Rajaniemi spot-check | "Is anything still explained that context would carry?" |
| `process/stages/02-audit.md`, `06-draft.md` | Both assume a single target length: "Yield at the brief's target length", and a 115% ceiling. |
| `AGENTS.md`, `PROCESS.md` | "The human decides at every gate. … Don't advance a story past a gate on your own." |

`process/stages/06-draft.md` already says to "withhold only … until the
payoff point the outline gives". There is nothing yet to define that payoff
point.

## Proposal

### 1. The payoff ledger (takeaway 1)

**The rule.** This one goes in the style guide, in the human's own terms:

> **Inference pays off.** The reader may be asked to work things out, and
> working them out is part of the pleasure. But every load-bearing fact
> (the novum's mechanism, the stakes, the twist, and why the people with
> power did what they did) is made explicit on the page eventually, so a
> reader who didn't work it out still gets the payoff.

**The bible.** `templates/story-bible.md` gains a **Payoff ledger** table:

| Row | The fact | Hinted at (scene) | Made explicit in (scene) | The explicit line or event |
|---|---|---|---|---|

The ledger's **graded rows** are fixed. Every story has them:

- **Premise:** what the story is about.
- **Stakes:** what the protagonist can win or lose.
- **Why:** why the people or powers who set things up did it.
- **Twist:** if the story has one.
- **Ending:** what happens, and why.

Further rows, one per mechanism the plot turns on, are **traced** rows. They
aren't graded, but they must have an explicit line.

"Never explained" is not a valid ledger entry. Every row is made explicit by
the final scene.

**Stakes before the climax.** The **Stakes** row is made explicit *before
the climax*, not just by the end. The human confirmed this on 2026-10-06. It
follows from the human's scores: Consequence 2, and an ending whose loss was
felt but not understood.

**The outline** gains a **Made explicit by** column in its information plan,
keyed to the ledger rows. The drafter's notes quote the explicit line for
every row.

### 2. The comprehension gate (takeaways 4, 5 and 7)

**The cold read takes two turns.** That way the questions can't prime it.

1. **Turn 1.** A fresh `first-reader` reads the draft once and writes its
   experience report, as now.
2. **Turn 2.** The orchestrator then resumes the same agent with SendMessage,
   carrying the **comprehension questions**:
   - What is this story about, in two sentences?
   - What does the protagonist stand to gain or lose, and what happens if
     they fail?
   - Why did the people or powers who set this situation up do it that way?
   - What did you learn late that changed how you saw the earlier part, if
     anything?
   - What happened at the end, and why?
   - Who is each named character, in one line each?
   - What are you still unsure about?

   It answers in a separate file, from memory.

The `first-reader` definition's line asking it to state the premise moves
out of its persona and into this second turn. Whether it rereads the draft
can't be enforced, because the agent has the Read tool. The no-reread rule is
an honour rule, and the design says so.

**A separate `comprehension-grader` grades the answers.** It is a new role,
on sonnet. It sees **only** the ledger's graded rows and the reader's answer
file. It never sees the bible, the outline or the draft.

- **Grades.** For each graded row, it gives **got it** (5), **partial** (3)
  or **missed** (1), with a quote from the answers and one sentence of reason.
- **The standard for "got it".** The reader states the causal link in its own
  words. Naming the terms isn't enough. The human's failure was having the
  terms "not put together".
- **The "unsure" answer** is reported verbatim as a finding.
- **The orchestrator** may lower a grade but never raise one.

**The gate.**
- **Before polish.** Stage 9 starts only when every graded row is *got it* on
  the latest draft. Any *partial* or *missed* row becomes an automatic
  structural note for stage 8.
- **After polish.** The gate runs again on `final.md`, with a fresh reader and
  grader, and writes to `reviews/final/`. A miss there sends the story back to
  stage 8.
- **Loop cap.** After two consecutive failed rounds, the orchestrator logs
  the failure, gets an `agent-guidance:consultant` opinion, and either takes
  one more round or proceeds. Either way it flags the gap at the top of the
  debrief appendix. A lenient grade must never be the way out.

**Where the grades go.** They are written to
`reviews/draft-N/comprehension.md`, or `reviews/final/comprehension.md` after
polish. The revision plan cites them.

### 3. The three-part rubric (takeaways 5 and 7)

`process/rubric.md`'s Drafts section becomes:

| Group | Axis | Scored by |
|---|---|---|
| **Felt** | Atmosphere: does the world feel like a place? | panel lenses, plus the First Reader's turn-1 report |
| **Felt** | Weight: does the ending carry emotional force? | panel lenses, plus the First Reader's turn-1 report |
| **Understood** | Premise, Stakes, Why, Twist, Ending | the grader, one per graded row |
| **Understood** | Who's who | the grader, from the who's-who answers |
| **Craft** | Structure | the panel |
| **Craft** | Character | the panel (construction), plus the grader's who's-who score (legibility) |
| **Craft** | Consequence | the panel (construction), plus the grader's Stakes and Why scores (legibility) |
| **Craft** | Prose | the panel |

Character and Consequence each carry **two scores**. The panel's score covers
how well they're built. The outsider's score covers whether a reader grasped
them. Calibration-01's gap (panel 4, human 2) was in the second.

**Mapping old axes to new,** so calibration-02's scores can be compared with
calibration-01's:

| Old axis | New axis |
|---|---|
| Novum delivery | Atmosphere, plus Understood: Premise |
| Consequence | Consequence (construction, plus legibility) |
| Character | Character (construction, plus legibility) |
| Structure | Structure |
| Prose | Prose |
| Ending | Weight, plus Understood: Ending |

**A counterweight in prose reviews** (takeaway 5). Every lens reviewing prose
names at least one line to protect. The critique template's "What to
protect" section becomes required.

### 4. Polish protects (takeaway 6)

- **The protect list.** `09-polish.md` builds one before the Line Editor
  runs. It's the union of three sources:
  - every review's "What to protect" lines;
  - the First Reader's moved, surprised or delighted passages;
  - every line quoted as a payoff-ledger line.

  The Line Editor doesn't cut or reword a protected line without logging why.
- **No cut quota.** "Cut 5 to 10 percent", "Shortness is a feature" and "Cut
  3% to 6%" go. The Line Editor cuts slack, and the change log reports the
  word delta.
- **Earned lyricism.** The style guide gains a rule that an ornate line
  earns its place when it's a concrete physical image or a moment between
  people.
  - The human's protected lines are the examples.
  - The abstract, stacked construction is the counter-example: "Twenty-two
    years of reading things that wanted a reaction from her…"
- **The Rajaniemi spot-check** changes from "is anything still explained that
  context would carry?" to "**is any explanation clumsy, as opposed to
  present?**" The spot-check stops removing payoffs.

### 5. Names arrive slowly (takeaway 3)

- **The introductions rule.** The style guide and the outline template gain
  it: every named character and invented term arrives with its role
  attached, and the opening scene introduces few of them.
- **The Invented terms rule is reworded.** It currently bans a gloss in
  apposition. The new wording allows the role in the same sentence and bans
  only a dictionary-style gloss.
- **The outline's scene table** gains an **Introduces** column, so stage 5
  can see the load in each scene.
- **The check** is the grader's **Who's who** score. A lint rule was
  considered and dropped. Capitalisation misses the novum's lowercase terms,
  and sentence-initial words swamp the count.

### 6. Length follows load (takeaway 2)

- **The brief** gives a **length range**. A brief below `PROCESS.md`'s
  3,000-word floor must name the reason in a waiver line.
- **Each premise** in `03-synthesis.md` gains a **Load** line: its nova plus
  its twist. Its **estimated minimum** is 3,000 words plus about 1,500 for
  each novum or twist after the first. That gives 6,000 for calibration-01.
  This is a heuristic with a single data point behind it, and calibration-02
  re-tests it.
- **The stage 3 gate** rejects or narrows any premise whose minimum is above
  the top of the range.
- **Range-aware stage files.** Stage 2 judges Yield at the range's midpoint.
  Stage 6's ceiling becomes the range's top.

### 7. The proxy gate mode (takeaway 8)

`templates/brief.md` gains a **Gates** field, which is either `human` or
`proxy`. The default is `proxy`, because the human has asked to read blind.

**In `proxy` mode:**

- **The run is unattended.** It's started from the brief and runs overnight
  or detached. The no-spoiler rule is only keepable if nobody watches the
  terminal.
- **The human's part.** The human writes the brief (stage 0) and decides
  whether the story **lands**, after the debrief. The proxy never lands a
  story.
- **The proxy's part.** The orchestrator decides every gate from stage 2
  through stage 9 and logs each decision, with its reasons and runner-up, in
  `STATUS.md`.
- **The stage 3 gate** gets an `agent-guidance:consultant` second opinion
  before the premise is chosen.
- **No spoilers** in anything the human sees before reading:
  - The slug and branch are chosen at stage 0, from the brief: for example
    `calibration-02`. They are never renamed after the premise.
  - Commit messages name the stage, not the premise.
  - The end-of-run message says only that the story is ready, and where.

**The debrief becomes stage 10,** with a stage file and a
`templates/debrief.md` modelled on `human-feedback.md`. Its order is fixed:

1. **An unprimed interview,** which opens with the First Reader's turn-2
   questions word for word. That makes the human's answers comparable with
   the reader's, which is the test of whether the gate predicts the human.
   It asks no question that reveals a detail, such as "what had to happen
   when the nine days ran out".
2. **Rubric scores,** on the three-part rubric.
3. **The run's own open questions.**
4. **Lines to protect.**
5. **Process takeaways.**

**`MORNING.md`** stays a separate file. It's written at the end of the run,
but the human is told not to open it until after the interview's first
section.

**The gate rule in `AGENTS.md`** becomes: "**The brief's gate mode decides
who decides.** In `human` mode the human decides every gate. In `proxy` mode
the orchestrator decides every gate after the brief, logs each one, never
spoils the premise to the human, and never lands a story: landing waits for
the human, after the debrief."

## Decisions

### The cold read takes two turns, and grading uses a separate agent

**Rejected:** questions in the reader's first prompt. They prime the read,
because the persona and prompt are read before the draft.

**Rejected:** orchestrator grading. The orchestrator wrote the ledger, and in
calibration-01 it read a confused reader's report as a pass.

**Rejected:** a separate cold reader for comprehension. That costs a second
read. With two turns, one reader gives both the experience report and the
answers.

### The First Reader stays on sonnet, and the grading gets strict

The draft-2 sonnet reader stated a passable premise and raised the twist,
and the human managed neither. So sonnet already reads more strongly than
this human reads a story, and a pass is weak evidence on its own. Moving to
opus would make the gap worse. **Chosen:** keep sonnet, and require a causal
link in the reader's own words for "got it".

### Understanding is scored only by an outsider

**Rejected:** lenses doing a cold read before opening the bible. A lens that
knows the bible is coming still reads as an insider.

### Proxy is the default; landing stays human

**Rejected:** gates that hide the premise. The human declined them.

**Rejected:** a proxy that also lands. Landing is cheap to hold, and the
debrief is where the human finds out whether the run worked.

## Not decided here

- **Revising Raking Light.** That's a story change. Calibration-02 tests the
  process instead.
- **Whether a passed gate predicts the human.** The test is calibration-02's
  debrief, using the same questions. If the reader and grader pass and the
  human misses, the reader-model and grading-standard decisions reopen.
- **The length heuristic.** It's re-tested on calibration-02.
- **Retro findings deferred earlier:** the story-facts ledger, drafter's-notes
  files and `status.py`. The payoff ledger may absorb the facts ledger, and
  implementation decides that.

## Graduation

- **Decision records** under `dev_docs/decisions/`:
  - the two-turn read with outsider grading;
  - the First Reader staying on sonnet with strict grading;
  - proxy gates with human landing.
- **Conventions:**
  - `AGENTS.md`: the gate-mode rule.
  - `process/PROCESS.md`: the comprehension gate, stage 10, and gate modes.
  - `process/style-guide.md`: the payoff, earned-lyricism and introductions
    rules, plus reworded rules 2–3 and the Invented terms rule.
  - `process/rubric.md`: the three-part draft rubric and the axis mapping.
  - Templates: brief, story bible, outline, critique, and a new debrief.
  - Stage files 02, 03, 06, 07, 08 and 09, plus a new 10.
  - The First Reader and Line Editor personas and definitions, and a new
    `comprehension-grader` definition.
- **Delete this design** as the branch's last commit before it lands.
