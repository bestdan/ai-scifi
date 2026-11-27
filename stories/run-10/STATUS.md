# Status: run-10

- **Gate mode:** proxy. The human decides stages 0 and 10; the
  orchestrator decides the rest by proxy.
- **Current stage:** 8 (revise, round 1)
- **Next action:** Gemini writes draft 2 from `06-revision-plan.md`.

## Drafter notes for next time
- agy denied a `read_file` (target not named) and later a `command` after writing the draft. Inline any newly written file in the prompt, and name the exact commands it may run.
- Gemini's own word count was wrong again (it reported 5,451 for 9,286). The length round with per-scene targets landed at 5,984.

## Drafter
Stages 6, 8 and 9 use **Gemini 4 Argon** (`gemini-4-argon-high`) through
`~/.local/bin/agy`, at the human's request, in one resumed conversation,
per `dev_docs/external-drafter.md`. Conversation ID: `c98e3640-cc08-4f65-867b-521742297881`. The agy grants (`just lint`, `wc -w`, `write_file(stories/)`) are in place.

> **Proxy mode:** this file names the premise once stage 3 decides it. The
> human doesn't open anything in this story's directory except `final.md`
> until they have read the story.

## Source
Seed issue #51 (https://github.com/bestdan/ai-scifi/issues/51), filed
2026-11-26 from an idea the orchestrator pitched and the human chose.

## Gate decisions
| Stage | Date | Decided by | Decision | Reasons | Runner-up |
|---|---|---|---|---|---|
| 0 Brief | 2026-11-26 | the human | Approved: short story 3,000–6,000, proxy, F3, tone fun and warm with friction, seed from #51 with a seed-adherence line, 3 cards per lens, default panels, Gemini 4 Argon drafts and polishes | The human chose the seed from the orchestrator's pitches, asked for it to be started, and asked for a Gemini drafter | The usual Claude `drafter` role (replaced at the human's request) |
| 2 Audit | 2026-11-26 | orchestrator (proxy) | Shortlisted four distinct cores: A We-Two (le-guin/We-Two × chiang/Small Clauses, 37); B The Uncut (le-guin/The Uncut × chiang/What It Costs to Keep, 35); C True Finds Only (watts/True Finds Only × lem/Rouge, 33); D The Long Quiet (egan/The Last Round × tchaikovsky/Endurance Limit, 32) | Top-5 entries 2 and 4 reuse A's cards, so they're skipped; True Finds Only taken as Collision 3 so its push (recruiting the amateurs) has a source. Premises must stay specific in the companion-as-party lane and off the keeper's-one-switch entry, now hard | Collision 5, The Left Hemisphere for Hire × The Gloss (31) |
| 3 Synthesize | 2026-11-26 | orchestrator (proxy) | A, We-Two (le-guin/We-Two × chiang/Small Clauses), with six conditions (in `03-synthesis.md`): the being decides the we-three question, its love reads as grammar failing, the dual has light legal force, a vastness image and a persuasive named delegate, a hiring reason specific to Sione, the companion-as-party attractor named | Mean rank 1.0, first for every lens; the only premise strong on all four seed lines; reader-profile pull 1. Consultant 88% on A | B, The Uncut (mean rank 2.0) |
| 4 Build | 2026-11-26 | orchestrator (proxy) | Bible approved after the stress test; all must-fix notes resolved (stress-test log in the bible) | The notes converged on ennu's want (now a register's gradient, and grammar: it has no "I", so promising back means saying ennu), on who is displaced and who pays (seats per promise; Ressa's contract; Vell's career), on why a human (exclusion unmarked by design; children as the next Listeners), the clause-close gap, the cough rate tied to open promises, and the calendar (Drilling now 68 years ago) | A second stress-test round (declined: the stage 5 panel sees the fixes in use) |
| 5 Structure | 2026-11-26 | orchestrator (proxy) | Outline approved: seven scenes, about 5,500 words, with register entries from ennu's side. All ten must-fix notes resolved (its Stage 5 lens notes) | The notes converged on one cough rule (every cough global; the read-back private, so nobody else can correlate), on scene 5 trying the obvious cure and failing so the trial asks a new question, on planting the climax's reason in the rehearsal promises, on the before-and-after "you" mechanism, on felt scale (the hauler on her sled) and on the cost planted early (Ressa in scene 3). Sione's choice in scene 6: flagging the rehearsals sinks his own seat | Cutting scene 6 into scene 7 (declined: it carries Reach and Sione's choice) |
| 6 Tone sample | 2026-11-26 | orchestrator (proxy) | Sample accepted (818 words). Cold reader: "dry, wry, warm". Banks lens: Match yes | Carried into the draft: other characters carry jokes too, not only Sione; his self-satisfaction gets punctured (Tikk, the misflag); the cough scenes are where the fun sits | A rewrite of the sample (declined: the tone matched) |
| 7 Review (round 1) | 2026-11-26 | orchestrator (proxy) | Gate **fail** on draft 1 (5,984 words). Who's who got it; Premise, Stakes, Why, Twist, Ending, Reach partial (omits); Terms missed (lu pulu). Lost-list entries 2, 3, 4, 8, 10–13 touch Premise, Why, Twist, Ending | Grader's result accepted. Checked dramatisation: Stakes shown in scene 5 (Ressa's contract), Reach in scene 6 (the unison cough), but Premise, Why, Twist and Ending have lost-list entries, so the dramatised-partial rule can't pass them. Tone: reader "wry, tender, clever" vs brief "fun and warm, with friction": a match | none |
| 8 Revise (round 1) | 2026-11-26 | orchestrator (proxy) | Revision plan approved: 24 items (12 consensus, 6 comprehension, 6 single-lens), 3 declined; draft 2 to be a full redraft at 5,800 words with per-scene targets | The lenses converged on one plain rule for ennu, the register entries' voice (no "I"), the cheat beats repeated while the reader was ahead, the broken-promise logic, the three rehearsals, ennu-sa "unread" where it should be refused, and the doubled "you" explanation. Sione now finds the "you" fix himself | Replacement paragraphs only (declined for this round: the changes are structural) |

## Seed stock
- B, The Uncut: a treaty as the load in a salt bed's pillar web, fed only by costly restraint.
- C, True Finds Only: a companion whose own chemistry fakes the being's health.
- D, The Long Quiet: a treaty dying of fatigue from festivals eleven years apart.

## Token use
| Stage | Tokens | Notes |
|---|---|---|
| 1 Ideate | ~572k | ten lens-ideators |
| 2 Audit | ~120k | cartographer |
| 3 Synthesize | ~296k | four critics and a consultant |
| 4 Build | ~285k | five critics |
| 5 Structure | ~174k | three critics |
| 6 Draft | Gemini 89,802 + 132,742 + 507,996 (draft 1 and its length round; the first call produced nothing after a denied read) | first draft 9,286 words, cut to 5,984 |
| 6 Tone sample | Gemini 86,800 (input 71,376, output 15,424, thinking 8,205); Claude ~79k | first-reader and Banks |

## Open questions
- none
