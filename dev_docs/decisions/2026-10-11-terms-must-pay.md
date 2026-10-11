---
created: 2026-10-11
status: accepted
convention: ../../process/style-guide.md
---

# Every coined or foreign term earns its place and is clear from the page

## Context

The style guide's rule 3 was "Trust the reader, then pay them. Leave
invented terms undefined while context carries them." Run-02's drafter
followed it. "Strike Note" used untranslated Portuguese throughout (*uai* 7
times, *brabo* 6, *agarrada* 6) and invented slang ("ceiling" 7 times,
"bricked" 5) that no stage checked, because neither was in the bible's
Glossary. The human's verdict, from `stories/run-02/debrief.md`:

> Jargon can be cool when it serves a purpose and is clear what it conveys.
> When it's just random words to indicate local slang, less so.

## Decision

Rule 3 becomes "Every term earns its place, and the page makes it clear". A
coined or foreign word stays only when it does a job the plain word can't,
and its meaning is clear at first use to a reader who doesn't speak the
language. Slang for local colour alone gets the plain word. The bible's
Glossary gives each term a **Job** and a **Clear at first use by** line, a
term with no Job is cut at stage 4, the drafter uses no such word outside
the Glossary, and the line editor replaces any the Glossary doesn't justify.
Rule 2 now adds that living the novum is no reason to leave its mechanism
unstated.

## Consequences

- Good, because each term now has to be justified at the point where it is
  cheapest to cut: in the bible, before drafting.
- Good, because the rule is the human's own test, purpose and clarity,
  rather than a proxy for it.
- Bad, because whether a term has a Job is a judgement, and no lint holds
  it up.

## Revisit when

- A debrief again names unexplained terms as a snag although the Glossary
  justified them: the judgement isn't working, and a per-story terms file
  the lint can check is the next step.
- The human finds a story's texture flattened by plain words.

## Confirmation

`tests/test_templates.py` checks the Glossary's Job and Clear at first use
by columns. The Terms row of the comprehension gate catches a term a cold
reader got only from outside the story. The rest rests on the style guide.

## Alternatives

- **A numeric cap on invented terms, enforced by lint:** the human's rule is
  about purpose, not count, and a lint can't tell a coined word from an
  ordinary one without a per-story list.
