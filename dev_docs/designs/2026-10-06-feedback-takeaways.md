---
created: 2026-10-06
status: proposed
---

# Make stories legible to a blind reader: payoffs, a comprehension gate, a proxy for every gate

Calibration-01 ended with a story whose prose the human scored 5/5 and
whose point the human couldn't state. Asked what the story was about, what
was at stake and what the twist was, the human had "no real idea". Every
answer was in the story bible. The process had put those answers there and
then kept them off the page on purpose. The lens panel, having read the
bible, scored the draft as if the answers had landed. The human also wants
to read the next story blind, without knowing the premise, so the
orchestrator must decide every gate from stage 2 onward.

This design makes four changes:

1. **The process enforces payoffs.** Anything withheld is stated on the page
   by the end.
2. **A gate is added before polish.** A reader who sees only the manuscript
   must be able to explain the story.
3. **The rubric is split.** Feeling it, understanding it and craft are scored
   separately, and the understanding scores come from the outsider, not the
   panel.
4. **A proxy-gate mode is written down,** so the human can read blind.

It covers the eight takeaways in section 5 of
`stories/calibration-01/human-feedback.md`, which hold the evidence:

| # | Takeaway |
|---|---|
| 1 | Every inference pays off explicitly |
| 2 | Length follows ambition |
| 3 | Fewer names, introduced slowly, each with an anchor |
| 4 | Comprehension check before polish |
| 5 | The panel over-scores comprehension and under-scores prose |
| 6 | Polish protects lyricism as well as cutting it |
| 7 | Feeling isn't understanding |
| 8 | The human reads blind, with the orchestrator as proxy |

## What is true today

**The evidence**, from `stories/calibration-01/human-feedback.md`:

- **Takeaway 1.** All four of the human's "why" questions have answers in
  `04-bible.md`:
  - why the agreement exists;
  - what is at stake;
  - where the metamorphosis comes from;
  - how integral it is to the plot.

  The bible itself marked those answers as "never explained" and "explained
  only through the treaty text and the clerk". Given the answers, the human
  found the premise "definitely a lot better and more interesting."
- **Takeaways 5 and 7.** The human's scores were 2 for Consequence and 2 for
  Character, against the panel's 4s; 5 for Prose, against 3–4; and 4.5 for
  Novum delivery, despite being unable to explain the novum. On the ending:
  "Didn't understand it, but felt the loss."
- **Takeaway 4.** Two fresh First Readers missed the reveal. Neither was asked
  to state it, and nobody compared what they understood against the bible.
- **Takeaway 2.** The brief set 2,500 words, below `PROCESS.md`'s 3,000-word
  floor. The story carried two nova (the turn and the posthuman escrow), two
  polities and a twist. The human: "Twenty five hundred words was just too
  short for such an ambitious set of ideas."
- **Takeaway 3.** The opening scene introduces Pell, Mrs. Okonjo, Oyelaran,
  Bisi, the Standing Revision, the Disputed Volume and § 14, and the next
  scene adds the Mbathas and Dr. Ferreira.
- **Takeaway 6.** Every line the human protected is a concrete physical image
  or a moment between people. Two of them are "the way…" similes.
- **Takeaway 8.** Decided by the human: the orchestrator acts as proxy at the
  gates, and the human reads only the finished story.

**Where the process encodes the problem today:**

| File | What it says now |
|---|---|
| `process/style-guide.md` rules 2 and 3 | "Live the novum, don't explain it." "Leave invented terms undefined when context carries them." Both are right as far as they go, but neither requires a payoff. |
| `templates/story-bible.md` | No place to say when a withheld fact becomes explicit. |
| `templates/outline.md` | The information plan has "Where it surfaces" and "How". It has no "made explicit by". |
| `process/stages/07-review.md` | Lenses read "whatever context your lens needs: the bible…", then score every axis, including the ones that depend on understanding. |
| `process/rubric.md` | Draft axes mix feeling and understanding: Novum delivery, Consequence, Ending. |
| `.claude/agents/first-reader.md` | Reports where it got lost, bored or moved. It is never asked to state the premise, the stakes or the twist. |
| `personas/line-editor.md`, `process/stages/09-polish.md` | "Cut 5 to 10 percent" and "Cut 3% to 6%" are quotas. Nothing protects a line. |
| `AGENTS.md`, `process/PROCESS.md` | "The human decides at every gate … Don't advance a story past a gate on your own." |
| `process/PROCESS.md` | The lengths table has a 3,000-word floor, which the brief can silently override. |

## Proposal

### 1. The payoff ledger (takeaway 1)

**The rule.** The style guide gains a positive rule that sits beside "trust
the reader":

> **Inference pays off.** The reader may be asked to work something out, and
> working it out is part of the pleasure. But by the end, every load-bearing
> fact (the novum's mechanism, the stakes, the twist, and why the people in
> power did what they did) is stated plainly on the page, so the reader who
> didn't work it out still gets the payoff.

**The bible.** `templates/story-bible.md` gains a **Payoff ledger** table.

| Withheld | Why it's withheld | Hinted at | Made explicit in (scene) | How (line or event) |
|---|---|---|---|---|

The table needs one row for each of:

- the premise;
- the stakes;
- the twist, if there is one;
- each mechanism the plot turns on;
- each "why" a reader would ask.

"Never explained" isn't a valid entry. A fact can be withheld until a
particular scene, and no later than the final one. The bible template's
headings that invite "never explained" are reworded.

**The outline.** The information plan in `templates/outline.md` gains a
**Made explicit by** column, keyed to the ledger. Then:

- Stage 5's Asimov question becomes: *is every ledger row made explicit
  before the end?*
- Stage 6 requires the drafter to put each ledger row on the page.
- The drafter's notes quote the line that does it.

### 2. A comprehension gate before polish (takeaways 4, 5 and 7)

**What the First Reader answers.** After its single cold read, the First
Reader answers these questions in its report, without rereading:

- **Premise:** what is this story about, in two sentences?
- **Stakes:** what does the protagonist stand to gain or lose, and what
  happens if they fail?
- **Turn or twist:** what did you learn late that changed how you saw the
  earlier part, if anything?
- **The ending:** what happened at the end, and why?
- **Who's who:** one line for each named character, with their role.

**Why this doesn't need a new role.** One cold read can serve both purposes:
the reader reports its experience first, then answers. The persona's rule
against rereading keeps the answers honest.

**The orchestrator compares** the answers against the payoff ledger and grades
each row **got it** (5), **partial** (3) or **missed** (1). The grades go into
`06-revision-plan.md` as the **Understood** scores.

**The gate.** Polish (stage 9) may start only when every ledger row is graded
*got it* by a fresh reader on the latest draft. A *missed* or *partial* row
is a structural note for stage 8, automatically. Polish can blur a line that
carried a payoff, so the gate runs again on `final.md` after polish, with
another fresh reader. A miss there sends the story back to stage 8.

**The panel stops scoring understanding.** In stage 7, lenses still read the
bible for logic checks (Egan, Asimov), but they no longer score the
Understood axes. Those come only from the outsider. That fixes takeaway 5's
mechanism: the insiders were scoring what they knew was meant.

### 3. A three-part rubric (takeaways 5 and 7)

`process/rubric.md`'s Drafts section splits into three groups:

| Group | Axes | Scored by |
|---|---|---|
| **Felt** | Atmosphere and texture; emotional weight of the ending | the panel and the First Reader's "moved" notes |
| **Understood** | Premise, Stakes, Twist, Ending (one per ledger row) | the orchestrator, from the First Reader's answers against the ledger |
| **Craft** | Structure, Character, Prose, Consequence | the panel |

Character and Consequence count as Craft here because the panel judges how
they're built. Whether a reader *grasps* them is measured in the Understood
group.

Prose criticism gets a counterweight (takeaway 5). Every lens reviewing
prose names at least one line it would protect, and the template's "What to
protect" section becomes required.

### 4. Polish protects (takeaway 6)

- **The protect list.** `09-polish.md` builds one before the Line Editor
  runs. It's the union of three sources:
  - every review's "What to protect" lines;
  - the First Reader's "moved, surprised or delighted" passages;
  - every line that carries a payoff-ledger row.

  The Line Editor may not cut or reword a protected line without logging why.
- **No cut quota.** The quota goes from both the persona and the stage file.
  The Line Editor cuts slack. The change log reports the word delta, but no
  target is set.
- **Lyricism has a positive rule.** The style guide gains a short rule saying
  an ornate line earns its place when it is a concrete physical image or a
  moment between people. The human's protected lines are the examples. The
  abstract, stacked construction the human couldn't follow is the
  counter-example ("Twenty-two years of reading things that wanted a reaction
  from her…").

### 5. Names arrive slowly (takeaway 3)

**The judgement rule.** The style guide and the outline template gain an
**introductions** rule:

- every named character and invented term arrives with its role attached,
  within the same sentence or the next;
- the opening scene introduces few of them.

The outline's scene table gains an **Introduces** column, so the load per
scene is visible at stage 5.

**The mechanical check.** A new warn-only lint rule, `name-load`, counts the
distinct capitalised names and terms in each scene (from heading to heading)
and warns above a threshold set in the TOML. It's tuned against
calibration-01's opening scene, the "Nine" scene, which the human named as
too dense, used as the positive fixture. It is warn-only because
capitalisation is a rough proxy for "a new thing to remember".

### 6. Length follows load (takeaway 2)

- **A range, not a point.** `templates/brief.md` asks for a **length range**
  (for example 4,000–7,000), not a single figure. A brief below
  `PROCESS.md`'s floor must say why, in a waiver line.
- **The load estimate.** Each premise in `03-synthesis.md` gains a **Load**
  line, which counts:
  - its nova;
  - its factions or institutions the reader must understand;
  - its twist;
  - its viewpoint characters.

  From the load, the orchestrator estimates the minimum words the premise
  needs. As a starting heuristic, recorded as a heuristic and not a rule:
  3,000 words, plus about 1,500 for each novum or twist after the first.
- **The gate check.** The stage 3 gate rejects a premise whose estimated
  minimum is above the brief's range, or else narrows the premise first.
  Calibration-01's premise carried two nova and a twist, so the heuristic
  gives about 6,000 words, against a brief of 2,500.

### 7. A gate mode in the brief (takeaway 8)

`templates/brief.md` gains a **Gates** field: `human` or `proxy`. It defaults
to `proxy` from now on, because the human has asked to read blind.

**In `proxy` mode:**

- **The brief is the human's only gate.** The human sets the brief (stage 0)
  and reads the finished story.
- **The orchestrator decides every later gate.** It writes each decision, its
  reasons and the runner-up to `STATUS.md`, as it did for calibration-01.
- **A second opinion before the premise.** At the stage 3 gate, the
  orchestrator gets an independent opinion before choosing, using the
  `agent-guidance:consultant` agent with the audit and the critiques.
  Choosing the premise is the gate where the proxy's own bias costs the most.
- **No spoilers.** Every message to the human during the run is
  premise-free. Progress reports give stage names, counts and scores only:
  no titles, no nova, no character names. `STATUS.md` and the artifacts hold
  the premise, so the human is told not to open them until they've read the
  story.
- **Reading order.** When the run ends, the orchestrator tells the human that
  `final.md` (or the EPUB) is ready, and nothing more. The debrief comes
  after the human has read it.

**The debrief becomes stage 10,** with a stage file and a template drawn from
the structure of `human-feedback.md`:

1. the unprimed interview first;
2. then rubric scores, using the three-part rubric;
3. then the questions for the human;
4. then the lines to protect;
5. then the process takeaways.

`MORNING.md` merges into the debrief as its "what the run decided" appendix.
It is shown only after the interview's unprimed questions.

`AGENTS.md`'s gate rule becomes: "**The brief's gate mode decides who decides.**
In `human` mode the human decides at every gate. In `proxy` mode the
orchestrator decides every gate after the brief, logs each decision with its
runner-up, and never spoils the premise to the human."

## Decisions

### The First Reader answers the comprehension questions; no separate role

**Rejected:** a separate `comprehension-reader` agent. A second cold reader
costs a second read for no gain, because the questions come after the read
and the no-reread rule already keeps the answers unprimed. One role keeps
"experience" and "understanding" from the same reading, which is what the
human gave.

### The First Reader stays on sonnet

**Rejected:** moving the reader to opus. A stronger reader infers more from
subtle cues, which makes it a worse stand-in for a human reading at leisure
on a Kindle. The calibration-01 readers didn't fail by being too weak to
infer the twist. They failed because nobody asked them. A reader that misses
an under-stated payoff is the signal this gate needs.

### Understanding is scored only by the outsider

**Rejected:** having lenses do a cold read before opening the bible. A lens
that knows it will read the bible later still reads as an insider, and the
human's scores showed insider grading as the failure.

### The proxy is the default gate mode, and `human` remains available

**Rejected:** gates that hide the premise. The human declined them. Also
rejected: dropping human gates entirely. A future story may want them.

## Not decided here

- **Revising Raking Light** to apply the takeaways. That's a story change, not
  a process change. Calibration-02 tests the process instead.
- **The exact length heuristic and the `name-load` threshold.** Both get
  tuned in implementation against calibration-01, and the numbers are
  recorded as heuristics that calibration-02 will re-test.
- **Whether a passed comprehension gate predicts the human's
  understanding.** The debrief of calibration-02 is the test. If the reader
  gets it and the human doesn't, the reader is too strong a proxy, and the
  model decision above reopens.
- **Retro findings deferred earlier:** the story-facts ledger, separate
  drafter's-notes files and `status.py`. The payoff ledger overlaps with the
  facts ledger, and implementation may fold them together.

## Graduation

- **Decision records** under `dev_docs/decisions/`:
  - the First Reader as the comprehension gate (covering both the
    single-role and the sonnet choices);
  - understanding scored only by the outsider;
  - proxy gates as the default mode.
- **Conventions:**
  - `AGENTS.md`: the gate-mode rule and the no-spoilers rule.
  - `process/PROCESS.md`: the comprehension gate, stage 10, and gate modes.
  - `process/style-guide.md`: the payoff, lyricism and introductions rules.
  - `process/rubric.md`: the three-part draft rubric.
  - The templates (brief, story bible, outline, critique, and a new debrief
    template), the stage files, the First Reader and Line Editor personas and
    definitions, and `prose-rules.toml`.
- **Delete this design** as the branch's last commit before it lands.
