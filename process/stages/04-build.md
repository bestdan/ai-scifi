# Stage 4: Build

**Dispatch:** `lens-critic`, once per lens on the stage 4 panel (by default
Watts, Egan, Le Guin, Lem and Tchaikovsky), in parallel. Use this prompt:

`Lens: <lens>. Stage: process/stages/04-build.md. Story: stories/<slug>.`

Don't pass `model:`.

## For the orchestrator

1. Before dispatching, write `stories/<slug>/04-bible.md` from
   `templates/story-bible.md`.
   - **Ending direction.** The bible settles where the ending goes and what
     it costs.
   - **Numbers.** It states every number and date the story depends on,
     together with its arithmetic, as traced rows of the payoff ledger.
   - **The payoff ledger.** Fill in every row: the six graded rows, plus a
     traced row for each mechanism the plot turns on. Each row names the
     scene where it is made explicit. "Never explained" is not an entry, and
     Stakes is explicit before the climax. Each graded row is both stated, in
     plain words, and shown, as a consequence in a scene. A statement can't
     be a quoted document of more than about 150 words.
   - **The protagonist's own stake.** A want and a wound that belong to
     the protagonist and not to the plot's task, and the scene where they
     change their mind about something personal. A narrator who only
     reports the novum, however well, reads as flat.
   - **The world list.** Three to five facts of daily life the premise rests
     on, in plain words, under "What the reader needs about the world".
   - **A reason for every rule.** Each of the novum's rules, and each limit
     the plot leans on (a delay, a boundary, a thing the system can't see),
     has an in-world reason: why it is this way and not the obvious simpler
     way. The bible names the scene where the reader learns that reason. A
     rule with no reason, even in the bible, reads to the reader as
     arbitrary; run-06's gazette read lag did.
   - **The world's shape and its history.** Say why power sits where it
     does, and why it covers these functions and not those: one machine or
     many, this city, these hospitals and not those. Give it a history a
     reader can feel, an event or a fight that left it this way, and the
     scene where that history reaches the page. A reason that lives only in
     the bible doesn't count.
   - **The glossary.** Every coined, foreign or slang word the story will
     use, each with its Job and the line that makes it clear at first use.
     Cut any term with no Job; the story uses the plain word.
2. After the stress test, resolve every must-fix note into the bible. Log
   each note in the bible's stress-test log, with what was done about it or
   why it was declined.

**Gate:** the bible is approved. In `human` mode, the human approves it. In
`proxy` mode, the orchestrator approves it and logs the decision and its
reasons in `STATUS.md`.

## For the agent

**Read:**
- `stories/<slug>/00-brief.md`
- the Decision section of `stories/<slug>/03-synthesis.md`
- `stories/<slug>/04-bible.md`

**Task:** stress-test the bible from your lens.

| Lens | Questions |
|---|---|
| Watts | Is the biology or neuroscience right, and which real mechanisms support or contradict it? Are minds more coherent or self-aware than the evidence allows? Where does the story flinch? Aim at wonder and unsettling truth, not misery. |
| Egan | Does the logic hold? Find every edge case that breaks the novum, its rules or its arithmetic. Do posthuman minds think like posthumans? What next logical step does the story not take? Can every payoff-ledger row be made explicit on the page without breaking the novum? |
| Le Guin | Does the society feel lived-in, with children and the old in it? Are the characters people or functions? Who pays, and do we see them? Do the children act their age? Do the invented words imply a culture, and does each glossary term have a Job the plain word can't do? Are the names plausible and respectful? |
| Lem | Is the alien truly alien, or a human in costume? Does the story flatter anyone's ability to understand? Where is the irony? Does it resolve too much? Could a document or fragment do more than narration? Can every payoff-ledger row be made explicit without explaining the alien away? |
| Tchaikovsky | Is the other mind written from the inside, or described from outside? Does its biology account for its culture and its mistakes? Is any of it a human trait in costume? Does the encounter cost something on both sides? |
| other | Your persona's "In critique" questions. |

Every lens also asks, for each rule and limit the plot leans on: why is it
this way, and where does the reader learn why? A rule a reader would ask
"why not just…" about, with no answer on the page, is a must-fix. So is a
world whose shape (where power sits, what it covers) has no history the
reader meets in a scene.

Give at most 6 notes. Tag each one [must-fix], [should] or [could], and
give each a concrete suggestion that fits the brief's length. Keep the
whole critique under 600 words.

**Write:** `stories/<slug>/04-critique/<lens>.md`

**Reply:** your must-fix notes, one line each.
