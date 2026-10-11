# Debrief: Strike Note (run-02)

The human's read of `final.md`, gathered by interview. The orchestrator
writes it up in the human's own words and adds no critique of its own. Tag
every note **[story]**, meaning the text should change, or
**[process: stage N]**, meaning the pipeline should have caught it at
stage N.

## 1. Unprimed interview

**1. What is this story about, in two sentences?**

> I kind of don't know. It's vaguely a coming of age story, that part I got.
> However, the mechanism and the importance of the netting is unclear. Why the
> relationship inverts at the end to the older woman being an apprentice is
> unclear. And the nature of the decision the main character has to made was
> unclear. I'll be quite blunt, this was not well written.

**2–7.** The human's answer to each was "I don't know / I'm not sure". The
human gave one answer for all of them, along with where the read snagged:

> This story was particularly opaque. The use of novel words/terms without
> benefit was particularly high. There was some passage about three quarters
> of the way through where an entire sentence was meaningless. It was trying
> to give me ambiance or set, but it was just gibberish. The mechanisms of the
> changes to the characters were completely unclear. You need to spend more
> time making clear what's happening and why, and not trying to use fancy
> language.

**Against the gate.** The human missed every graded row, and that includes
the two the reader got. The gate didn't predict the human on any row: a
model reader recovered meaning from this text that a human reader couldn't.

| Row | Reader (`reviews/final/comprehension.md`) | Human |
|---|---|---|
| Premise | partial (3) | missed: "the nature of the decision ... was unclear" |
| Stakes | partial (3) | missed: "I don't know" |
| Why | got it (5) | missed: "I don't know". **The gate didn't predict the human.** |
| Twist | N/A | N/A |
| Ending | partial (3) | missed: "why the relationship inverts at the end ... is unclear" |
| Who's who | got it (5) | missed: "I don't know". **The gate didn't predict the human.** |

**A second example of jargon that blocks meaning,** from the 27 September
fountain paragraph:

> ...two labs answered and one not yet, which would, obviously, ceiling, the
> whole thing ceiling.

> What does 'ceiling, the whole thing ceiling' mean? I got the rest of the
> sentence, but that wasn't clear. It's like there's too much slang / jargon.

## 2. Rubric scores

The Understood rows are all 1: the interview missed every one.

| Group | Axis | Human | Panel / grader | Why (the human's words) |
|---|---|---|---|---|
| Felt | Atmosphere | _pending_ | | |
| Felt | Weight | _pending_ | | |
| Understood | Premise | 1 | 3 | "the nature of the decision ... was unclear" |
| Understood | Stakes | 1 | 3 | "I don't know" |
| Understood | Why | 1 | 5 | "I don't know" |
| Understood | Twist | N/A | N/A | |
| Understood | Ending | 1 | 3 | "why the relationship inverts ... is unclear" |
| Understood | Who's who | 1 | 5 | "I don't know" |
| Craft | Structure | _pending_ | | |
| Craft | Character | _pending_ | | |
| Craft | Consequence | _pending_ | | |
| Craft | Prose | _pending_ | | |

## 3. The run's open questions

**Should the Premise and Ending ledger rows state the chose-or-drifted
ambiguity as the point?** The human's answer was that the question doesn't
arise, because the story never earned the human's interest:

> To be honest, I don't care about Davi. Why the heck are they making bells?
> Why would that benefit from intelligence boosting? What's the tension?

- **[story]** The premise doesn't explain itself. The text never connects the
  treatment to bell founding in a way the reader can follow, so neither the
  choice nor its cost is clear.
- **[process: stage 3]** Synthesis chose a premise without testing it with a
  plain-language question: why does this world need this novum, and what is
  the tension, stated in one sentence a non-SF reader would accept?

## 4. Lines to protect

Skipped. The run failed, so nothing from it carries forward.

## 5. Process takeaways

- **[process: stage 7] The cold reader saw no inside information, but it is
  not a human reader.** The `first-reader` agent ran with no prior context:
  it read only `personas/first-reader.md` and the draft
  (`.claude/agents/first-reader.md`). The persona file describes the target
  reader and leaks nothing about the story. Its answers still beat the
  human's on every row, for reasons on the model's side, not the human's:
  - It decodes the story's Portuguese (*uai*, *brabo*, *agarrada*,
    *cata-vento*) from its own knowledge, which the story never supplies.
  - It reads every word at full attention and can reconstruct a mechanism
    from scattered hints a human reads past.
  - Its report invents human experience: "That one hit hardest. I thought
    about it for days." It is performing a reader, which makes its "moved"
    and "kept reading" signals unreliable as well.
- **[process: stage 7–8] The reader flagged the human's snags, and the process
  didn't act on them.** `reviews/final/first-reader.md`'s "Where I got lost"
  names "Max", the bell code, the legal reading, five slang terms, the
  22 September fountain paragraph, the 27 September entry and the 28 September
  notebook paragraph. It says "the opening pages were work". The gate counts
  only the comprehension rows, so none of that failed the story. A
  lost-list that long should fail the gate by itself.
- **[process: stage 7] The grader's names list doubles as a glossary.**
  `names.md` defines every invented term, so the grader knows what the terms
  mean even when the story doesn't say. It can credit an answer that uses a
  term correctly, even though the reader may have pieced the meaning together
  from Portuguese rather than from the page.
- **[process: stage 6, 9; style guide] Jargon has to pay for itself.** The
  human's rule:

  > Jargon can be cool when it serves a purpose and is clear what it conveys.
  > When it's just random words to indicate local slang, less so.

  > You need to spend more time making clear what's happening and why, and
  > not trying to use fancy language.

  Every coined or foreign term needs a job the plain word can't do, and its
  meaning on the page at first use. Local colour alone doesn't qualify.
  Both the drafter and the line editor need this rule, and the lint could
  count unexplained terms.
- **[process: stage 4–5] The mechanism comes first.** What the treatment does,
  why the town requires it, and why it matters to this trade must be plain on
  the page early. Atmosphere can't carry it.

## Landing

**Not landed.** The human's decision: "Yes, failed run, iterate on the
process." The branch stays unmerged as the record of the run.

## Appendix

### Gate failures

Copied from `STATUS.md`.

- **Gate on final.md** (fresh reader and grader, `reviews/final/comprehension.md`): Premise partial (missed the rite-day deadline and the town shaming his mother), Stakes partial (read the hands as a gain of setting), Ending partial (missed that he can't tell whether he chose, and her hand slowing his). Why and Who's who got it. Across four rounds each graded row except Why has been both partial and got it, depending on the reader.
- **Premise** (partial in rounds 1, 2 and 3). Last answer: "whether to take a drug that permanently fixes his brain so he can inherit his mother's foundry licence, or stay 'open' for another year". Missing: that staying open means learning her trade at a child's speed while the town shames her.
- **Stakes** (partial in rounds 1 and 3, got it in round 2). Last answer has the set branch and the agarrada cost, but not the delay branch's gain (about eight bells at a child's speed) or the Belo Horizonte drift.

### The run's report

`MORNING.md`.
