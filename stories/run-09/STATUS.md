# Status: run-09

- **Gate mode:** proxy. The human decides stages 0 and 10; the
  orchestrator decides the rest by proxy.
- **Current stage:** 8, Revise (round 1)
- **Next action:** Gemini writes draft 2 from `06-revision-plan.md`.

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

## Gate failures

## Seed stock
- **C, Reheat or Overload** (liu/The Pour × banks/Overload Retardation): a mind cast in cooling glass holds a decade's contempt; reheat it, or blunt the flaw with a true hard overload from someone who loves it.
- **E, The Drove** (rajaniemi): young minds herded across a continent to graze on place-locked writing; on a dry crossing the crew must become better people.
- **B, The Commons in a Clear Year** (chiang × lem): a made mind's form regrows toward what people write about minds; in the Clear Year the minds go dark and people write alone.
- **D, Spread or Place** (le-guin × tchaikovsky): a self built from human writing can't close; spread the error or put it in one honest place.
- Audit runner-up: **Contributing Factors to a Change of Heart** (vinge × banks).

## Open questions
