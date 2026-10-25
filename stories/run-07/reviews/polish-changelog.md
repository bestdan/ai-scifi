# Polish change log: run-07, draft 3 → final.md

## Word count

- Draft 3, story text only: **36,198**
- final.md: **36,333**
- Delta: **+135**. The required items add about 300 words of plain statement (glosses, stakes, why, the premise link, the courtesy line, the cutters' shifts, shielding). The cuts take out about 165.

## Lint

**I could not run `just lint stories/run-07/final.md`.** This session refused it, and `python3 scripts/lint_prose.py` too, with "This command requires approval", sandboxed or not. The orchestrator has to run it before the spot-checks. What I checked by hand:

- **Banned phrases, names and ships, and em-dashes:** I searched the file. There is no em-dash anywhere and no banned phrase. "the weight of every splice" (3.5) is a near miss, but the rule's pattern doesn't match it. Draft 3's text passed the error rules, and no added line uses those shapes.
- **Contrast shape:** no added sentence uses "it wasn't X. It was Y."
- **Zinger closers:** judged by eye against the rule's definition, since I could not get the count. See "Zinger pass" below.

## Changes by category (counts)

| Category | Count |
|---|---|
| Plain-words glosses for failing terms (dispensed, map, derate) | 10 edits |
| Comprehension rows (Premise, Why, Stakes) | 6 edits |
| Le Guin cuts (the third telling, Arriba's explaining line, the repeated rope line) | 6 edits |
| Continuity and physics (31 years, the carrying injury ×2, shielding, the rope's memory) | 5 edits |
| World texture (the label courtesy, the cutters' shifts) | 2 edits |
| Slack notice made legible | 1 edit |
| Zinger and slack cuts | 9 edits |

## Required items

1. **"dispensed" (1.5).** Arriba's first note now says: "I may dispose of it by dispensing it. To dispense is to send down the rope whatever answers a label; it is how I fill every pool." The note's later "dispensation" (twice) became "what I dispensed" and "one fill in four hundred", so one word does the job. "Dispensed: an answer." is unchanged.
2. **"map" and "derate" (lab wall, 3.3).** The sign now reads: a complete map is "a list of every section in the batch, each one checked, and what was found"; under Rule 5 "the whole batch is rated down by the share of its sections found bad." "Derate" is gone from the story. The plain sense follows wherever the word appears again: Jacinta in 4.1 ("every section checked and written down"), Segundo in 4.2 ("found without checking every section"), the certifier in 5.3 ("a complete map, every section checked"), the rope in 5.4 ("the list of every section checked and what was found"), and the certifier in 5.5 ("Rated down", "rate it down", "the map, which tells us exactly which sections are bad").
3. **Premise (1.3).** Segundo's speech before the protected line now names both halves: Arriba "knows almost everything and can send almost anything, but only as an answer, and only when somebody asks. Not the Asamblea. People, at a counter, with their asks. And Waska, the rope, can't do anything at all except refuse." The protected line follows unchanged. One narration sentence, which replaces the paragraph cut under item 7, states the link: "So nothing happened in this country unless an ordinary person asked, and the rope agreed."
4. **Why (Dolores, 3.1).** Two sentences go in after "before it could be a law": "We did that after the two budgets, when we'd watched both governments get bought. Nobody can buy a thing that can only refuse." Her protected lines are unchanged, and "you can't pay a rope to push" still closes the thought.
5. **Stakes.** These are additions; no protected line is replaced.
   - **4.1, Jacinta:** "the climbers on that length come down" became "the bottom of the rope parts with them, and the climbers on that length fall, and the crews in them die." That passage is not on the protect list.
   - **4.4:** a sentence is added after the protected "If I don't…" line: "The bottom of it parts, and every crew on that length dies."
   - **The answer's aftermath (5.3):** "everyone in the plaza knew what *parts* meant at the foot of a rope: the lowest length coming away under a loaded climber, and the crew in it dying."
6. **Cut** "I think the son is buying the same thing and declining to write it." (1.5).
7. **Cut** the tour narration paragraph ("He let it sit. It was the whole country in two sentences…") and the cousin's "That's my job." The string, the plaque and the protected line are unchanged. The one-sentence replacement is described under item 3.
8. **The rope's repeated line.** The required item names "2.5 and the last rope section", but neither of those sections contains the line. It appears at 1.2, at the end of 1.6, at 3.5 and at 4.5. I kept it once, at 1.2, where it is explained ("My memory is my wear"). I cut it from 1.6 and from 4.5, the last section it appears in. At 3.5, "as I did yesterday, and the day before, as if for the first time" became "There is nowhere in me to keep them, so each time they are new." That removes the claim to remember. Also from Watts's note, 5.4's "as I have felt them since yesterday" became "as I feel the rest of my foot". **For the human:** 2.5's "where I put it every morning" is still there; it reads as habit, not memory.
9. **Continuity.** "He had kept to it for thirty-one years." became "He had kept to it." The "thirty-one years ago" lines (2110 to 2141) are correct and unchanged.
10. **Taken.** At the ward meeting, after the Pilataxis speak: "In Ayora you didn't ask a neighbour which label their asks went behind, and you didn't tell them yours, and the people round the family flinched to hear it said out loud."
11. **Taken, from Lourdes's queue.** This is the first scene after "Half the roses" that has the queue in it, at Segundo's bench on 31 October: "at noon he heard two cutters in it say the farms had put every shed on three days a week from Monday, for as long as the roses went up at half." Le Guin's warning about sermons is respected: the line is overheard, not stated by the narration.
12. **Carrying injury.** Dolores now carries the drums "full, on her right shoulder, one all the way up the hill and then back down for the other". There is no head strap. "Her right arm stops there." and Ernesto's "Her shoulder" now fit, and 5.6's "carried up the hill … in a shawl" became "on her shoulder".
13. **Shielding.** The crew chief, in 2.3: "Nineteen days. In a cabin walled with water tanks, for the radiation up there."
14. **Zingers.** See "Zinger pass" below.
15. **Slack notice (5.6).** It now reads: "Laws passed in this period take effect at once, provisionally. When the rope bears again on 10 December, every one of them goes to the rope to be weighed, and any law the rope refuses falls." Proaño reads it, and his "We'll see on the tenth" follows on from it.

## Zinger pass

I cut or folded seven reflexive closers:

- "That is what I am." (1.2)
- "It pulls like nothing." (1.6, which repeated "as if it isn't there")
- "She didn't wait to see." (2.4)
- "…which was how she found most things." (2.2)
- "It is cleaner than most things this country sends me." (3.5)
- "It always does." (Arriba, 5.2; the narration has already said it in 4.2)
- "…which is not the same thing." (Wilmer, 4.3)

Two more paragraph endings were folded into the sentence before them:

- "There was nothing to send anywhere." (5.6)
- "He had read the board." (4.3)

I kept the closers that are concrete images or turns between people, among them:

- "and the cord didn't care"
- "I remember the flat place."
- "and lost."
- "which was worse than a slam"
- "He hadn't seen her go."
- "For forty days nothing rings."

**I estimate the density at about 7.0 per 1,000 words, down from 7.4, but I could not measure it.** The linter will give the real figure.

## Protected lines

- **Changed:** "He had kept to it for thirty-one years" is part of the protected fiesta memory. The count was cut under item 9. "He had not known… that it worked" is unchanged.
- **Next to protected lines, wording unchanged:**
  - 1.3: the line before the protected premise line was rewritten, and the narration after it was replaced.
  - 4.4: a sentence was added after "If I don't…".
  - 3.1: two sentences were added inside Dolores's protected passage, between its quoted parts. Every protected sentence is unchanged.
- **Unchanged:**
  - the tumpline passage's "Her right arm stops there. It has since 2115.", although the carrying sentence before it changed
  - "Dispensed: an answer."
  - the 132-word answer
  - "Proof climb, 06:40. 1.04 / −0.04. Refused."
  - every other line on the list

## Judgement calls for the human

- **Item 3 against item 7.** Le Guin asked to cut the third telling of the mechanism, and the grader asked for the link said plainly in the same place. I kept one plain sentence of narration where the cut paragraph stood. If it reads as a fourth telling, the speech now names both halves, and that may be enough on its own.
- **Item 8's locations didn't match the text.** See the note under item 8 above.
- **The stakes are now stated three times:** in 4.1, in 4.4 and on the morning of the answer. That is deliberate, because the grader missed it on all three drafts. 4.1 could lose its "and the crews in them die" if it reads as heavy.
- **Lint not run in this session.** Run it before the spot-checks.

## Structure

Unchanged. Nothing structural was found.
