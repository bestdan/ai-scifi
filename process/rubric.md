# Rubric

## Idea cards (stage 2)

The Cartographer scores every card from 1 to 5 on each axis, and writes one
line of justification per score.

| Axis | 1 | 5 |
|---|---|---|
| **Novelty** | A direct match exists in published SF | No close prior art; the nearest match differs in kind |
| **Futurity** | Next year's headline | Past the event horizon (see the scale below) |
| **Rigor** | Hand-waved, or contradicts itself | Holds up when pushed; its costs are as clear as its benefits |
| **Yield** | An interesting fact with no story in it | Forces a choice on someone, and the conflict comes from the novum itself |
| **Estrangement** | Familiar once you hear it explained | Makes the present look strange in hindsight |
| **Stakes** | Nobody in particular is affected | Someone specific loses something they can't get back |

**Novelty and Yield are weighted double.** A strange, rigorous idea that
doesn't generate a story belongs in an essay.

Weighted total = 2·Novelty + Futurity + Rigor + 2·Yield + Estrangement + Stakes
(maximum 40).

## The Futurity scale

The Cartographer scores Futurity; the ideators don't rate their own cards.

The brief sets a floor on this scale, and **F3 is the default.**

| Level | Name | Shape |
|---|---|---|
| F1 | Extrapolation | Today, plus one technology |
| F2 | Transformation | One generation out; society reorganized around the change |
| F3 | Divergence | Humans still recognizable, but their basic categories (self, death, place, kin) have changed |
| F4 | Posthuman | The main minds aren't human, or aren't single, or aren't continuous |
| F5 | Event horizon | Deep time, alien physics, or minds whose motives can only be shown in outline |

F5 is Vinge's problem: past a certain point the story becomes unwriteable,
because the characters are smarter than the author. Known workarounds include
Vinge's own Zones of Thought, viewpoint characters who are the slow ones,
documents and artifacts in place of scenes (Lem), and showing the edge of the
unknowable rather than its inside. Inventing a new workaround counts as a
novum.

## Drafts (stage 7)

A draft is scored from 1 to 5 in three groups. They come apart in practice: a
reader can feel a story's loss without being able to say what was lost.

- **Felt:** what a reader experiences.
- **Understood:** what a reader could explain afterwards.
- **Craft:** how well the thing is built.

The lenses have read the bible, so they know what the story means to say.
That makes them insiders, and they don't score the Understood group. The
`comprehension-grader` scores it from a cold reader's answers, in
`reviews/draft-N/comprehension.md`.

| Group | Axis | The question | Scored by |
|---|---|---|---|
| Felt | Atmosphere | Does the world feel like a place? | the panel, with the First Reader's turn-1 report as evidence |
| Felt | Weight | Does the ending carry emotional force? | the panel, with the First Reader's turn-1 report as evidence |
| Understood | Premise | Could a reader say what the story is about? | the grader |
| Understood | Stakes | Could a reader say what the protagonist stands to win or lose? | the grader |
| Understood | Why | Could a reader say why the powers in the story set things up as they did? | the grader |
| Understood | Twist | Could a reader say what the twist was? (N/A if none) | the grader |
| Understood | Ending | Could a reader say what happened at the end, and why? | the grader |
| Understood | Reach | Could a reader say what the story's central change means for people beyond its main characters? | the grader |
| Understood | Who's who | Could a reader place each named character? | the grader |
| Understood | Terms | Could a reader get every coined or foreign term from the page itself? | the grader |
| Craft | Structure | Does every scene turn? Does the form serve the idea? | the panel |
| Craft | Character | Does the protagonist want something, and does the novum make it harder to get? | the panel (construction), plus the grader's Who's who (legibility) |
| Craft | Consequence | Does the story live in the second-order effects? | the panel (construction), plus the grader's Stakes, Why and Reach (legibility) |
| Craft | Prose | Is it specific, and does every ornate line earn its place? | the panel |

The grader's grades map onto the scale as got it 5, partial 3, missed 1.
Terms has no partial: one term the reader got only from outside the story,
or never got, is a miss. Terms covers only the coined, foreign and slang words in
the glossary. Real units and scientific words, such as kelvin or
astronomical unit, are not terms: a reader who knew them from outside the
story hasn't failed the row.

**Character and Consequence carry two scores each,** reported side by side
and never averaged: construction from the panel, legibility from the grader.
A well-built character the reader couldn't place is a legibility failure,
not a construction one.

**No mean mixes the groups.** Report each group separately. The comprehension
gate, not an average, decides whether a draft can go to polish. It reads the
graded rows, Terms and whether any of the First Reader's lost-list entries
concern a graded row; Who's who is a score only.

### Mapping from the old axes

Stories reviewed before this rubric used six axes. To compare them:

| Old axis | New axes |
|---|---|
| Novum delivery | Atmosphere, plus Understood: Premise |
| Consequence | Consequence (construction, plus legibility) |
| Character | Character (construction, plus legibility) |
| Structure | Structure |
| Prose | Prose |
| Ending | Weight, plus Understood: Ending |
