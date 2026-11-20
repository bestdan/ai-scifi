# Status: run-08

- **Gate mode:** proxy. The human decides stages 0 and 10; the
  orchestrator decides the rest by proxy.
- **Current stage:** 9, Polish
- **Next action:** dli check, then the comprehension gate on final.md.

> **Proxy mode:** this file names the premise. The human doesn't open
> anything in this story's directory except `final.md` until they have read
> the story.

## Drafter
Stages 6 and 8 use **Gemini 4 Argon** (`gemini-4-argon-high`) through
`~/.local/bin/agy`, at the human's request, in one resumed conversation.
Conversation ID: `9d475cfe-3afc-4e71-a21d-c4af218cadce`. Auto mode refused `--dangerously-skip-permissions`, so Gemini gets no tool access: the orchestrator inlines every input into the prompt, Gemini returns the draft as text, and the orchestrator writes the file and runs `just lint`. **Gemini can't count its own words:** it reported 6,812 for a 10,985-word draft and 6,758 for 8,142. Two length rounds inside stage 6, the second with per-section counts, brought it to 6,255. Every other role is the usual Claude
agent, except stage 9's line edit: at the human's word (2026-11-19, mid-run), Gemini also does the polish, in the same conversation, as replacement paragraphs, so the final prose stays Gemini's. The Claude spot-checks and the final comprehension gate still run. The debrief should compare this prose with earlier runs.

## Gate decisions
| Stage | Date | Decided by | Decision | Reasons | Runner-up |
|---|---|---|---|---|---|
| 0 Brief | 2026-11-19 | the human | Approved: short story 3,000–7,500, proxy, F3, tone funny and wry (Murderbot Diaries as the register reference), defaults elsewhere, Gemini 4 Argon drafts | The human's approval in chat, with the tone added | none |
| 2 Audit | 2026-11-19 | orchestrator (proxy) | Shortlisted five distinct cores: C1 egan/Cromwell's Rule × tchaikovsky/Cached (37); watts/The Cold Minute with its push, dropping the report (36); C2 banks/Once-Fired × egan/The Glass Takes Months (35); le-guin/Something Worth Fixing with its push, the mother forging the need (34); vinge/Below the Line (32) | Top 5 minus #4 (tchaikovsky/Cached alone, which is C1's core), replaced by the highest-scoring distinct core. Premises must steer off this run's new attractors: the service's instrument misreading a healthy world, the agent made smaller, the staged crisis, and tone words written into the protagonist instead of the prose | vinge/The Tun Season (32) |
| 3 Synthesize | 2026-11-19 | orchestrator (proxy) | A, The Prior (egan/Cromwell's Rule × tchaikovsky/Cached), with Vinge's push as the turn: the birds hide things from her installed prior, not from her | Mean rank 1.0, first for all four lenses. N5, F4, reader-profile pull 1. Under the ceiling at about 6,000. Consultant (fable) 95% on A, 70% on the turn. The synthesis's 'cache shows the service' turn was replaced as a placeholder, not cut for length | C, The Signatory with the slowing dropped (tie at 3.25 with B and D; C chosen on the gate's ambition rule, not on panel votes) |
| 4 Build | 2026-11-19 | orchestrator (proxy) | Bible approved after the stress test; every must-fix resolved (stress-test log in the bible) | 16 must-fix notes from five lenses, all mechanical or additive: the table made physical (witnessed single-atom syntheses), the twist given an observable mechanism (UV glint, eyes-shut tests, a partly wrong model), trust grounded in memory, the public decoy naming rule, a fledgling, the moot vote with a dissenter, scene 7 touch-only and scene 8 the one sighted spend | A second stress-test round (declined: the fixes are local and stage 5's panel sees them in use) |
| 5 Structure | 2026-11-19 | orchestrator (proxy) | Outline approved: seven dated sections and a coda, about 6,800 words, headings carrying her number. All must-fix notes resolved (its Stage 5 lens notes) | Nine must-fix notes from three lenses, converging on a repeated middle: old scene 5 cut and split, the moot carrying Stakes and the proof, the jigsaw misreading as scene 4's engine, the scale seen in the bellows hall, the hearing clue made consistent, the coda split out | Keeping a separate stakes scene before the moot (declined: Chiang and Asimov both flagged it as a repeated tradeoff) |
| 8 Revise (round 1) | 2026-11-19 | orchestrator (proxy) | Revision plan approved: 24 items (7 consensus, 7 adopted single-lens, 10 comprehension). The gate failed on draft 1: Premise, Ending and Reach partial; Terms missed; Stakes, Why, Twist and Who's who got it | Every lens scored Structure 3 or 4, with the hearing rule, the lectures and the Day 117–118 repetition as shared causes. The comprehension misses are fixable with plain statements and plain words. Watts's physics fixes give the climax an act (waiting at the detector) | Cutting the coda (declined: the Reach row's Concern side lives there) |
| 8 Revise (round 2, loop cap) | 2026-11-19 | orchestrator (proxy) | Narrow round 3: 4 items (the whisper and glint rules separated, what evidence counts, element 120's history, Seven-Holes right and the archive untrusted). **Stop rule:** stage 9 follows round 3 whatever the gate says. No round 4. Drafter returns replacement paragraphs only, to hold the word count | The loop cap fired. Consultant (fable, 75%): the open notes are rule contradictions stage 9 can't take; Stakes and Ending are already on the page, so their partials are recall. Success test: no higher word count, the eyes-shut question gone from the lost-list, Twist holds, no row to missed | Proceed to stage 9 now (the consultant's alternative if the glint fix were phrasing only) |
| 8 Draft structurally done | 2026-11-19 | orchestrator (proxy) | Draft 3 is called structurally done under the loop cap's stop rule; proceed to stage 9 | The stop rule was logged before round 3. Lenses: no rule contradiction remains (Chiang, Asimov), Structure 3–4. Round 3's success test is only partly met (see Gate failures). The open rows go to the line editor as required items, and the gate reruns on final.md | Round 4 (declined: no round 4 under the stop rule) |

## Polish spot-check decisions

Applied by the orchestrator as word-level edits to Gemini's polished text, logged here and in the polish changelog.

- **Asimov:** applied 1 ("morning" → "evening"), 4 (the furnace-heat sentence contradicted Day 117's "nothing shows from orbit"; replaced with "a new yard three ridges east of the old hall, its straw and broken pots already in place", the orchestrator's wording, not Asimov's suggested one, which also stated no heat) and 5 (quartz → glass). **Declined 2** ("since day nine" → "since the first day"): day nine is correct, as it is the day they stopped hiding from her and started hiding from the lens. **Declined 3** ("exactly as sure"): a protected line, and the cold reader sat up at it.
- **Rajaniemi:** applied all five (the doubled moot gloss, the run-on sentence on page 1, "snatched" → "hidden", the relief sentence trimmed, "pistol-crack" → "flint-crack", since there are no pistols on this world).

## Token use
One row per stage, added at its gate. Agent tokens are the sum of each
dispatched agent's usage report; the orchestrator's own turns are an
estimate. Gemini's usage is on the human's subscription and is noted
where `agy` reports it.

| Stage | Agents dispatched | Agent tokens | Orchestrator (est.) |
|---|---|---|---|
| 1 Ideate | 10 lens-ideator | 574,839 | 15k |
| 2 Audit | 1 cartographer | 155,190 | 5k |
| 3 Synthesize | 4 lens-critic, 1 consultant | 312,616 | 15k |
| 4 Build | 5 lens-critic | 274,957 | 25k |
| 5 Structure | 3 lens-critic | 179,289 | 15k |
| 7 Review (draft 1) | 1 first-reader, 5 lens-critic, 1 comprehension-grader | 470,934 | 20k |
| 8 Revise r1 | Gemini 4 Argon, 1 turn | 266,192 (Gemini) | 10k |
| 7 Review (draft 2) | 1 first-reader, 4 lens-critic, 1 comprehension-grader, 1 consultant | 541,026 | 15k |
| 8 Revise r3 | Gemini 4 Argon, 1 turn (replacement paragraphs) | 300,160 (Gemini) | 10k |
| 7 Review (draft 3) | 1 first-reader, 3 lens-critic, 1 comprehension-grader | 446,306 | 10k |
| 6 Draft | Gemini 4 Argon via agy, 3 turns (on the human's subscription) | 435,915 (Gemini) | 30k |

## Gate failures

- **Round 1 (draft 1):** Premise, Ending and Reach partial; Terms missed (prior, posterior, Hessary Schedule C, element names, detector parts, several plain-English craft words). Lost-list 11, 7 tied to graded rows.
- **Round 2 (draft 2):** Stakes and Ending partial (both stated on the page; the answers omit one clause each); Terms missed (californium, Actuarial, from outside knowledge). Premise and Reach closed. Lost-list 11, 8 tied to rows. **The loop cap fires:** two consecutive fails.
- **Round 3 (draft 3):** Premise, Stakes, Ending and Reach partial; Terms missed (californium, titanium-50, from outside knowledge); Why, Twist, Who's who got it. Lost-list 12, 9 on rows. Against the success test: word count down (met: 7,223); lint passes (met); the eyes-shut question gone from the lost-list (**not met**: entries 8 and 9); Twist holds (met); no row to missed (met); Premise and Reach hold (**not met**: both fell to partial, though round 3 changed no text they rest on, so this is reader variance). **Per the stop rule, the story proceeds to stage 9.** Persistent across all three rounds: the opening number on page 1, and the completed-and-spent moment. These go to the line editor as required items.

## Seed stock

- **C, The Signatory** (banks/Once-Fired × egan/The Glass Takes Months), best without the slowing.
- **B, The Ending Technician** (watts/The Cold Minute): the peak-end service.
- **D, The Fee** (le-guin/Something Worth Fixing).
- **E, North for Lunch** (vinge/Below the Line).

## Open questions
