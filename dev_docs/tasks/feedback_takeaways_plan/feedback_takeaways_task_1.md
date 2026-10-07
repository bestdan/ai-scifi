---
title: Payoff ledger and the writing rules that feed it
priority: high
size: 5
status: new
created: 2026-10-06
source_branch: bestdan/feedback-takeaways
parent: feedback_takeaways
related_files:
  - process/style-guide.md
  - templates/story-bible.md
  - templates/outline.md
  - process/stages/04-build.md
  - process/stages/05-structure.md
  - process/stages/06-draft.md
  - process/stages/08-revise.md
  - stories/calibration-01/human-feedback.md
expires: 2026-12-06
tags: [process, writing]
---

Part of [[feedback_takeaways_plan]].

## Context

**Design sections:** "1. The payoff ledger" and "5. Names arrive slowly".

**The evidence**, from `stories/calibration-01/human-feedback.md`, sections 1
and 5.1–5.3:
- The human's rule is that inference has to pay off and be made "explicit
  eventually".
- The **Stakes** row must be explicit *before the climax*. The human
  confirmed this on 2026-10-06.

**Rules that currently fight this:**
- `process/style-guide.md` rule 2: "exposition only where a character in the
  scene has a reason to explain".
- Rule 3: "Cut the sentence that explains the subtext".
- The Invented terms rule: "never next to a gloss in apposition".
- The bible template has no place to record when a withheld fact becomes
  explicit.

`process/stages/06-draft.md` already says to "withhold only … until the payoff
point the outline gives". This task defines that payoff point.

## Task

1. **`process/style-guide.md`:**
   - Add the design's **Inference pays off** rule word for word. It says
     "explicit eventually"; it does not say "stated plainly".
   - Add the **Earned lyricism** rule. Its examples are the human's
     protected lines from `human-feedback.md` §4, and its counter-example is
     "Twenty-two years of reading things that wanted a reaction from her…".
   - Add the **Introductions** rule.
   - Reword rule 2. Exposition may also come from the narration, at the
     payoff point the ledger names.
   - Reword rule 3. Subtext may stay subtext, as long as the ledger's facts
     are explicit.
   - Reword the Invented terms rule, so a role in the same sentence is
     allowed and only a dictionary-style gloss is banned.
2. **`templates/story-bible.md`:**
   - Add the **Payoff ledger** table, with the five fixed graded rows
     (Premise, Stakes, Why, Twist, Ending) plus traced rows for mechanisms.
   - Note that the Stakes row is explicit before the climax.
   - Remove or reword any template prompt that invites "never explained".
   - Decide whether the story-facts ledger (numbers and their arithmetic)
     folds in as traced rows, and record the decision in the commit message.
3. **`templates/outline.md`:**
   - Add a **Made explicit by** column to the information plan, keyed to the
     ledger rows.
   - Add an **Introduces** column to the scene table.
4. **`process/stages/04-build.md`:** the orchestrator fills in the ledger,
   and Egan and Lem check that every ledger row can be made explicit without
   breaking the novum.
5. **`process/stages/05-structure.md`:** add the Asimov question "is every
   ledger row made explicit, with Stakes before the climax?", and the Chiang
   or Le Guin question "does any scene introduce more names than it anchors?"
6. **`process/stages/06-draft.md`** and **`08-revise.md`:** the drafter's
   notes quote the explicit line for each ledger row. Every draft after the
   first comes from stage 8, so both files need it.

## Acceptance Criteria

- **Code-enforced:**
  - `just check` passes.
  - `tests/test_templates.py`, a new test, asserts the following:
    - `templates/story-bible.md` contains a "Payoff ledger" heading and all
      five graded row names;
    - the bible template contains the phrases "not a valid ledger entry"
      and "before the climax". The template must name "Never explained" in
      order to reject it, so the test checks for those two phrases rather than
      banning that one;
    - `templates/outline.md` contains the columns "Made explicit by" and
      "Introduces".
- **User-run:**
  - Read the new style-guide rules beside the human's quotes in
    `human-feedback.md` §1. They should say what the human said, and no
    more.
