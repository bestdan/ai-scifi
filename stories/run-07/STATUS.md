# Status: run-07

- **Gate mode:** proxy. The human decides stages 0 and 10; the
  orchestrator decides the rest by proxy.
- **Current stage:** 10, Debrief
- **Next action:** the human reads `final.md`; then the stage 10 debrief. The story lands only on the human's word.

> **Proxy mode:** this file names the premise. The human doesn't open
> anything in this story's directory except `final.md` until they have read
> the story.

## Gate decisions
| Stage | Date | Decided by | Decision | Reasons | Runner-up |
|---|---|---|---|---|---|
| 0 Brief | 2026-10-25 | the human | Approved: run-06's answers carried (novella 30–40k, proxy gates, F3, earnest and morally serious tone, Stephenson at stages 1, 3, 4 and 7, no caricatured camps, governing mechanics on the page, each card answers whether the AI has a voice), plus the run-06 debrief's additions (the AI visibly reasons, the handover of power lived, the world's shape explained, more colour, mechanics in moderation) | The human confirmed the carried defaults in one question | — |
| 2 Audit | 2026-10-25 | orchestrator (proxy) | Shortlisted five distinct cores: C1 Regent of the Dark Months × The Fixed Point (37); C2 The Heater List × The Gearing (36); C3 The Spun Statutes × Nose-Blind (35); C4 The Cleaner Station × Intercepts, Volume IX (35); C5 What the Tether Will Bear × Exact Change (collision 5; Exact Change alone scores 34) | Ranks 1–4, then the best distinct core: rank 5 (egan/Fixed Point) is C1's core. Collision 5 is taken over Exact Change alone because it adds a counterpart power and answers the seed's national-versus-global question as a constitution. Premises must steer off the new attractors: the woman envoy or minister bargaining with the governor (C1, C2), the town a statute closes as the stake (C1), the reasons sealed or delayed (run-06 ground), and the time-rate cluster (C2, C3) | vinge/Exact Change as a single card (34) |
| 3 Synthesize | 2026-10-25 | orchestrator (proxy) | E, Two Half-Powers, with the five fixes in `03-synthesis.md` (dread from the two halves of one text; the tether mind as the main interior voice; parts that escalate the exploit; the veto's history lived; the anchor moved to the Andes, a male broker, no coercive-wording ending) | Mean rank 1.8 (first for Banks, Cartographer and Stephenson). The only premise whose engine is the seed's national-versus-global question, with procedure as scene action. Uncharted, F4. Consultant agreed at 72% | A, The Grudge-Keeper (mean 2.0) |
| 4 Build | 2026-10-25 | orchestrator (proxy) | Bible approved after the stress test. All 17 must-fix notes resolved in the bible, logged in its stress-test log | The six lenses converged on five problems, each fixed in-world: the ask arithmetic (the December-pool custom; all numbers recomputed and traced), the "why not just…" holes (a patchy flaw, the cheap question as a scene, the lab's blind spot, why nobody asks), Arriba's remorse (cut), the slack season (no 2101 clause; the 2140 provisional rule; derating makes the refusal arithmetic), and over-resolution (named refusals, an unsettled change of mind, a household that pays) | A second stress-test round (declined: the fixes are mechanical and traced, and stage 5's panel will see the bible in use) |
| 5 Structure | 2026-10-25 | orchestrator (proxy) | Outline approved: five parts, about 34,700 words, with an arc map, the parts' questions, a calendar and scene tables. All eight must-fix notes resolved (see its Stage 5 lens notes); the bible gets a Stage 5 amendments section | The panel converged on the repeated good-name tradeoff (P2/P3) and the cord unrecognised for 13,000 words; both fixed by folding and moving Jacinta's recognition to ~40%. Sampling rejected on the page; Gabon and the question mechanism planted early; the cost paid in a scene (Lourdes at the board); scale felt in 1.2 and 4.4 | A sixth part for the slack season itself (declined: Part 5's question is answered in 5.6, and 40 days of slack would repeat the provisional-law beat) |
| 8 Revise (round 1) | 2026-10-25 | orchestrator (proxy) | Revision plan approved: 24 items (5 comprehension, 9 consensus, 10 adopted single-lens). The gate failed on draft 1: Premise, Why and Reach partial; Terms missed (the Accord, the Day of the Dead items, lupin beans); Stakes, Ending and Who's who got it | Five lenses converged on the clinic refunding the sacrifice (made late and costly, not cut) and on the honest-broker choice repeating; the comprehension misses are links the page states once or not at all (the asker-and-bearer link, the deliberate split, the histories market) and terms never defined | Cutting the clinic gift entirely (the Cartographer's; declined, because the First Reader valued its ambiguity) |
| 8 Revise (round 2, loop cap) | 2026-10-25 | orchestrator (proxy) | Narrow round 3: 9 items (the button gloss; the two voices made distinct and the asker-and-bearer chain shown; Why as one lived cause-and-effect beat in place of five dates; Stakes' cost side stated; four cheap routes closed). **Stop rule:** stage 9 follows round 3 whatever the gate says, with unclosed rows going to the line editor as Required items; no round 4 | The loop cap fired (draft 1 and draft 2 both failed). Consultant (fable, 65%): the Premise and Why partials trace to text the reader couldn't follow (lost-list 5 and 7), not recall, and stage 9 can't take structural notes. Round 3's success test: Terms got it, Premise and Why got it, Stakes back to got it, no row to missed | Stage 9 now, with "button" as a Required item (the consultant's runner-up) |
| 8 Draft structurally done | 2026-10-25 | orchestrator (proxy) | Draft 3 is called structurally done under the loop cap's stop rule; proceed to stage 9 | The stop rule was logged before round 3. Round 3 closed "button" and held Ending, Reach and Who's who at got it; no row fell to missed. Premise, Why and Stakes stay partial, each answer omitting one clause of a multi-clause fact (run-05 and run-06's pattern). The unclosed rows and the three new terms go to the line editor as Required items | Round 4 (declined: no round 4 under the stop rule) |
| 9 Polish (sign-off) | 2026-10-25 | orchestrator (proxy) | The story is ready. `final.md` is about 36,300 words | Polish closed Stakes and Terms on the final gate. Premise, Why and Reach are logged per the stage 9 rules (Reach's text unchanged in polish). Spot-checks applied, with two declines logged. `dli check` passes | Another stage 8 round (declined: the loop cap's stop rule) |

## Token use
| Stage | Agents dispatched | Agent tokens | Orchestrator (est.) |
|---|---|---|---|
| 1 Ideate | 11 `lens-ideator` | 2,267,598 | ~20k |
| 2 Audit | 1 `cartographer` | 1,026,902 | ~15k |
| 3 Synthesize | 5 `lens-critic`, 1 consultant | 1,191,230 | ~60k |
| 4 Build | 6 `lens-critic` | 1,153,806 | ~90k |
| 5 Structure | 3 `lens-critic` | 571,699 | ~70k |
| 6 Draft | 1 `drafter` (five parts, resumed), 5 per-part `lens-critic` checks | 21,939,006 | ~120k |
| 7 Review (draft 1) | 6 `lens-critic`, `first-reader` (two turns), `comprehension-grader` | 3,201,215 | ~60k |
| 8 Revise (round 1) | 1 `drafter` (resumed) | 15,315,052 | ~40k |
| 7 Review (draft 2) | 4 `lens-critic`, `first-reader` (two turns), `comprehension-grader` | 2,719,139 | ~40k |
| 8 Revise (round 3) | 1 `drafter` (resumed), 1 consultant | 9,465,993 | ~40k |
| 7 Review (draft 3) | 1 `lens-critic`, `first-reader` (two turns), `comprehension-grader` | 1,186,131 | ~20k |
| 9 Polish | 1 `line-editor`, 2 `lens-critic` spot-checks | 3,887,423 | ~30k |
| 9 Gate on final.md | `first-reader` (two turns), `comprehension-grader` | 634,874 | ~10k |
| **Total** | | **64,560,068** | ~0.6M |

## Polish spot-check decisions

- **Asimov:** applied all five (the plan borne "on Friday"; "Twenty-six days"; "nothing came down from Arriba unless an ordinary person asked", twice, since the Asamblea passes laws unasked; "twenty hours").
- **Rajaniemi:** applied 2 (the double delivery in the rope's section) and 4 (dispensing folded into Arriba's practice). **Declined 1** (the narration line as a picture): Asimov's fix to the same line corrects a false claim, and accuracy wins over texture on a Premise line. **Declined 3** ("The bottom parts under a loaded climber, with the crew in it."): it drops "dies", which is the clause the gate graded missing on Stakes in all three rounds.
- `dli check` passed.

## Gate failures

- **Round 1 (draft 1):** Premise, Why and Reach partial. Terms missed (the Accord, the Day of the Dead items, lupin beans). Stakes, Ending and Who's who got it. Lost-list 11 entries, 7 on graded rows.
- **Round 2 (draft 2):** Premise, Stakes and Why partial. Terms missed (button, never glossed). Reach and Ending got it; Stakes regressed from got it. Lost-list 10 entries, 4 on graded rows (the two voices blur; the dates; the refusal; the farms' label). **The loop cap fires:** two consecutive fails. Consultant (fable, 65%): one narrow round 3, then stage 9 whatever the result.
- **Round 3 (draft 3):** Premise, Stakes and Why partial. Terms missed (dispensed, derate, map: "button" closed, three new words failed). Ending, Reach and Who's who got it. Lost-list 11 entries, 5 on graded rows (Arriba's offcut note; Rules 4 and 5 and the derating; 1.04; Arriba against the rope in Part One; how the slack laws fit). Against the round-3 success test: Terms **not met**; Premise and Why **not met**; Stakes back to got it **not met** (the reader's "would come down" omits that the crews die); no row to missed **met**. **Per the stop rule, the story proceeds to stage 9.** The unclosed rows and terms go to the line editor as Required items, and the gate runs again on final.md.
- **Gate on final.md** (fresh reader and grader, `reviews/final/comprehension.md`): Premise, Why and Reach partial. **Stakes, Ending and Terms got it**, so Stakes and Terms closed in polish. The page-2 answer is "yes, but only just". Premise and Why failed on draft 3 too, so they are logged under the loop cap. Reach passed on draft 3, but polish changed neither of its explicit lines (Proaño's "price of a straight question", Wilmer's "A good name's a thing you can sell now"), so it is the reader, not the text, and it is logged. Across four readers, Premise and Why were never got: each answer drops one clause of a multi-clause fact, the pattern run-05 and run-06 logged. The debrief should test whether the human's read matches.

## Seed stock

- **A, The Grudge-Keeper** (watts/Regent × egan/Fixed Point), with Stephenson's grudge-keeper order. *Early Riser* charts the sleeping nation.
- **B, The Heater List** (watts/Heater List × egan/Gearing).
- **C, The Felt Law** (le-guin/Spun Statutes × asimov/Nose-Blind).
- **D, The Overheard** (tchaikovsky/Cleaner Station × lem/Intercepts); needs the Ultra fix.
- **B × E:** requests that cost heat (the Cartographer's collision).

## Open questions
