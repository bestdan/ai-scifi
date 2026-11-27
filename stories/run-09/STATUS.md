# Status: run-09

- **Gate mode:** proxy. The human decides stages 0 and 10; the
  orchestrator decides the rest by proxy.
- **Current stage:** done (debriefed and landed, 2026-11-26)
- **Next action:** none. The debrief is in `debrief.md`.

> **Proxy mode:** this file names the premise. The human doesn't open
> anything in this story's directory except `final.md` until they have read
> the story.

## Drafter
Stages 6 and 8 use **Gemini 4 Argon** (`gemini-4-argon-high`) through
`~/.local/bin/agy`, at the human's request, in one resumed conversation,
per `dev_docs/external-drafter.md`. Conversation ID: `73c0777a-28b2-4ede-8157-e90c0fa958de`. The agy grants (`just lint`, `wc -w`, `write_file(stories/)`) are in place, so Gemini writes and lints its own files. The draft is written one part per turn.

## Gate decisions
| Stage | Date | Decided by | Decision | Reasons | Runner-up |
|---|---|---|---|---|---|
| 0 Brief | 2026-11-21 | the human | Approved: novella 17,500–40,000, proxy, F3, tone procedural and wondering with warmth, Antimemetics Division and Three-Body Problem as register references, Liu added at stages 1 and 3, Gemini 4 Argon drafts | The human asked for ~900 pages, chose the novella cap when told the process tops out at 40,000 words, and approved the drafted brief in chat | Book one of a longer arc; a full novel with process changes (both offered, not chosen) |
| 2 Audit | 2026-11-21 | orchestrator (proxy) | Shortlisted the Top 5, all distinct cores: The Addressee's Reply (asimov/Line Blend × liu/The Minor Third, 35); The Commons in a Clear Year (chiang/The Shape It Heals Toward × lem/The Clear Year, 34); Reheat or Overload (liu/The Pour × banks/Overload Retardation, 34); Spread or Place (le-guin/Misclosure × tchaikovsky/The Wolf Interval, 33); rajaniemi/The Drove (32) | No two entries share a card, so no skip was needed. Premises must steer off this run's new attractors: the monster-and-kinder-library card, the teacher at the bench, the mind as strata, one household as its whole humanity, writing reformed for the mind, the woman specialist as tender, the keeper's one switch. Watts/The Antenna's real-lab citation stays out | Contributing Factors to a Change of Heart (vinge × banks, 32) |
| 3 Synthesize | 2026-11-21 | orchestrator (proxy) | A, The Addressee's Reply (asimov/Line Blend × liu/The Minor Third), with the tempo cause stated, the burn as a three-party bargain, the slow self building the relay through maintenance orders, and the story opening on a recipient | Mean rank 1.2, first for Vinge, Chiang, Banks and Liu, second for the Cartographer on novelty. Only F4 premise; rests on the reader profile's top three pulls. Consultant (fable) 88% on A; 65% on the conditions, the relay-builder choice being taste | C, Reheat or Overload (mean rank 2.2) |
| 4 Build | 2026-11-21 | orchestrator (proxy) | Bible approved after the stress test; all 17 must-fix notes resolved (stress-test log in the bible) | The notes converged on the Hum: it got senses (ring length as posture) and an output organ (symptoms: thinned signal → true fault reports → standard orders), a recall rule (keeps the strong and repeated), three competing readings of its motive with the mechanism explicit, a small change (a salutation clause) and a foresight mistake (its sending caused the filing). Orbital mechanics, snapshot and gravity fixed; Teresa, Rui, Pieter and Albano added as people who pay or remember | A second stress-test round (declined: the fixes are integrated and stage 5's panel sees them in use) |
| 5 Structure | 2026-11-21 | orchestrator (proxy) | Outline approved: four parts, 26 scenes, about 34,600 words, with a lap calendar and routing lines on every document. All seven must-fix notes resolved (its Stage 5 lens notes) | The notes converged on fair play (the symptom-to-order rule, the honest orders and the dossier clue planted early), on a repeated Part II middle (merged, with Arvo now acting in scene 12), on scale stood in (the drone footage of station 23), and on Graça's answer and Arvo's cost dramatised rather than stated | Keeping Arvo's letter to Liv after the verdict (declined: before it, the change is his own rather than a reaction to the outcome) |
| 6 Tone sample | 2026-11-21 | orchestrator (proxy) | Sample accepted (1,065 words). Cold reader: "wry, tender, uncanny". Chiang lens: Match yes | Warmth and wonder are carried, and the docket forms carry the procedural register. Carried into the draft: Nominal's scene-1 reply must not reveal the beam's origin (held to scene 13), Graça must not yet know about the closed box, and scene 1's jargon is trimmed | A rewrite of the sample (declined: the tone matched, and the notes are content fixes the draft can take) |
| 7 Review (round 1) | 2026-11-21 | orchestrator (proxy) | Gate **fail** on draft 1 (34,798 words). Got it: Why, Twist, Who's who. Partial (omits): Premise, Stakes, Ending, Reach. Terms missed ("the chord"). Lost-list entries 1, 2, 3, 5, 6, 7, 9, 10 touch graded rows | Grader's strict result accepted. Checked dramatisation: Twist shown in scene 18 (the letter to the one who signs), Why in scene 10 (Teresa at the plaque), Stakes in scene 17 (crew meeting), Ending partly in scene 22 (Arvo's letter) but the Hum's surrender is only a concordance clause, which is item 15. Tone: reader "warm, wry, grave" vs brief "procedural and wondering, with warmth"; wondering missing, so it becomes item 17 | none |
| 8 Revise (round 1) | 2026-11-21 | orchestrator (proxy) | Revision plan approved: 24 items (17 consensus or comprehension, 7 adopted single-lens), 5 declined | The lenses converged on Part IV's docket run (cut to three documents, weight in rooms), the reveal told three times, a uniformly consoling Hum voice, the date error under the ending, and Graça and the Achterbergs dropping out. The comprehension gaps (chord, 5:4, circularity, the Hum's surrender) each get a plain line. New scenes: Graça in November, Desmond in December, a Hum interlude in which it lets the Reply fade, and a Nikolasi beat | Revising by replacement paragraphs only (declined for this round: the hearing cut and the four new scenes are structural; replacement paragraphs return in round 2) |
| 7 Review (round 2) | 2026-11-21 | orchestrator (proxy) | Gate **fail** on draft 2 (34,681 words). Got it: Ending, Who's who. Partial: Premise, Why, Twist, Reach (omits); Stakes (errs). Terms missed (Article 9, minor third, 5:4). Lenses rose: Asimov 4/4/4/4/4/3, Le Guin 4/4/3/4/4/3, Chiang 4/4/4/–/4/3 | Grader's result accepted. Twist fell from got it to partial on mechanism text unchanged from draft 1 (Hamid's symptom paragraph), so it is reader variance, not text. Reach is dramatised (Basra, crew meeting, the flood) but not passed, because the gate has failed on other rows anyway. Tone: reader "tender, procedural, wistful", which now matches "procedural" and "warmth"; "wondering" still only implicit | none |
| 8 Loop cap | 2026-11-21 | orchestrator (proxy) | **Proceed to stage 9; no draft 3.** The page-closable fixes go to polish as required items (replacement scale); the unclosed rows are logged under Gate failures | Second consecutive gate failure, so the loop cap fired. Consultant (fable): B at 78%. Basis checked: Twist fell on unchanged text; round 1's plain-sentence fixes for Stakes and Reach didn't move their rows; run-08's narrow round 3 lost rows to reader variance. The orchestrator's prior leaning was a narrow round 3 at about 70%; it changed to agree on that evidence. Crux: Asimov's Tierce-evidence holes can be fixed by moving a lap number and cutting a clause, without a new scene | Narrow round 3, replacement paragraphs only, with a stop rule (run-08's shape) |
| 9 Polish | 2026-11-21 | orchestrator (proxy) | Polish by Gemini as the single writer, in the same conversation, against 13 required items; `final.md` at 34,886 words; spot-checks applied with one decline | The human asked for Gemini to do the writing and voice, so the polish stays in its prose (run-08 precedent). The Claude spot-checks and the final gate still run | The Claude `line-editor` role (declined: it would put a second voice into the prose) |
| 9 Polish (sign-off) | 2026-11-21 | orchestrator (proxy) | **The story is ready.** `final.md` is 34,886 words; EPUB built | The final gate fails on recall (Premise, Stakes, Why, Ending partial; Reach errs; Terms missed on "the chord" and "the Tierce"), with Twist and Who's who got it. Per stage 9 step 5: Ending passed on draft 2, but its quoted line (the Tierce's withholding) is protected and unchanged, and the omitted facts (Arvo's certificate, his letter to Liv) sit in scenes polish didn't alter, so it is reader variance and nothing is restored. Every other failing row already failed on draft 2 and came through the loop cap. `dli check` passes | Another stage 8 round (declined: the loop cap's decision stands) |
| 10 Landing | 2026-11-26 | human | **Land.** Fast-forward `main` to `bestdan/story-run-09` | Debrief: all six graded rows got it, Who's who 9 of 12, Terms missed ("the Reply", "folar"); Felt 4, Craft 4. The human rated Gemini's voice better than earlier drafters | Revise first, then land |

## Polish spot-check decisions

Applied by the orchestrator as word-level edits to Gemini's polished text.

- **Asimov:** applied all five, and the two extras in its file:
  - Pieter's age, 38 → 32, and Desmond's age at the lathe, 34 → 29. The bible's "38" was wrong: Pieter was 11 months old in August 2099.
  - The Tierce-to-Ceres lag sentence made self-consistent.
  - "seven words" → "nine words", in two places.
  - "four weeks" → "seven weeks" before the docket closed.
  - "Tomorrow was Tuesday" → "On Tuesday", since 20 March 2132 is a Thursday.
  - "four months and nine days" → "ten days".
  - Arvo came in at 0420, not 0400, before the 04:15 ticket.

  Prompted by the weekday slips, the orchestrator also checked every weekday against the real calendar and fixed fourteen. 20 March 2131 replaces 18 March as the plaque scene's date (a Tuesday), and 13 April replaces 11 April as the "second Friday of April".
- **Rajaniemi:**
  - Applied 1 in contrast-safe form: "table of weights" and "only the price list for blood", with no "never X. It was Y" split, which the contrast-shape rule counts.
  - Applied 2, cutting the italic gloss after "a demonstration".
  - Applied 3, "a precise professional sense".
  - **Declined 4** ("postage unpaid"): the fragments are stamped "Postage assessed: 0.00", which means free, not owed, so "unpaid" would contradict them.

`dli check` passes.

## Token use
One row per stage, added at its gate. Agent tokens are the sum of each
dispatched agent's usage report; the orchestrator's own turns are an
estimate.

| Stage | Agents dispatched | Agent tokens | Orchestrator (est.) |
|---|---|---|---|
| 1 Ideate | 11 lens-ideator | 806,955 | 15,000 |
| 2 Audit | 1 cartographer | 171,223 | 12,000 |
| 3 Synthesize | 5 lens-critic, 1 consultant | 433,423 | 25,000 |
| 4 Build | 5 lens-critic | 314,927 | 45,000 |
| 5 Structure | 3 lens-critic | 220,143 | 30,000 |
| 6 Draft | 1 first-reader, 1 lens-critic (Claude); Gemini via agy, 5 turns | 80,354 Claude; 2,154,107 Gemini (agy usage totals) | 60,000 |
| 7 Review (round 1) | 1 first-reader (2 turns), 5 lens-critic, 1 comprehension-grader | 950,175 | 40,000 |
| 8 Revise (round 1) | Gemini via agy, 2 turns | 3,242,958 Gemini | 35,000 |
| 7 Review (round 2) | 1 first-reader (2 turns), 3 lens-critic, 1 comprehension-grader, 1 consultant | 664,227 | 30,000 |
| 9 Polish | Gemini via agy, 1 turn; 2 lens-critic spot-checks, 1 first-reader (2 turns), 1 comprehension-grader | 2,471,115 Gemini; 346,211 Claude | 30,000 |

## Gate failures
Unclosed after the stage 8 loop cap (draft 2, 2026-11-21). Rounds tried: 2. The final gate on `final.md` (fresh reader and grader) also failed: Premise, Stakes, Why and Ending partial (omits), Reach partial (errs), Terms missed ("the chord", "the Tierce"); Twist and Who's who got it. No row was broken by polish (see the 9 sign-off row). The debrief should test these rows on the human first.
- **Premise:** partial (omits) in both rounds. The reader misses the Bell taking itself for "you" and the non-addressee question.
- **Stakes:** partial in both rounds (omits in round 1, errs in round 2). The decision is deliberately not Arvo's, so "if he fails" has no clean answer.
- **Why:** got it in round 1, partial in round 2, after round 1's rewrite of the 3 March ratio paragraph. Polish required item R1.
- **Twist:** got it in round 1, partial in round 2, on unchanged mechanism text.
- **Reach:** partial (omits) in both rounds; dramatised.
- **Terms:** missed in both rounds ("the chord", then Article 9 and the thirds). Polish required item R1.

## Seed stock
- **C, Reheat or Overload** (liu/The Pour × banks/Overload Retardation): a mind cast in cooling glass holds a decade's contempt; reheat it, or blunt the flaw with a true hard overload from someone who loves it.
- **E, The Drove** (rajaniemi): young minds herded across a continent to graze on place-locked writing; on a dry crossing the crew must become better people.
- **B, The Commons in a Clear Year** (chiang × lem): a made mind's form regrows toward what people write about minds; in the Clear Year the minds go dark and people write alone.
- **D, Spread or Place** (le-guin × tchaikovsky): a self built from human writing can't close; spread the error or put it in one honest place.
- Audit runner-up: **Contributing Factors to a Change of Heart** (vinge × banks).

## Open questions
