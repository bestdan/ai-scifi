# Status: run-10

- **Gate mode:** proxy. The human decides stages 0 and 10; the
  orchestrator decides the rest by proxy.
- **Current stage:** 4 (build)
- **Next action:** write `04-bible.md`, then the stage 4 stress test.

## Drafter
Stages 6, 8 and 9 use **Gemini 4 Argon** (`gemini-4-argon-high`) through
`~/.local/bin/agy`, at the human's request, in one resumed conversation,
per `dev_docs/external-drafter.md`. Conversation ID: not yet started.

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

## Seed stock
- B, The Uncut: a treaty as the load in a salt bed's pillar web, fed only by costly restraint.
- C, True Finds Only: a companion whose own chemistry fakes the being's health.
- D, The Long Quiet: a treaty dying of fatigue from festivals eleven years apart.

## Token use
| Stage | Tokens | Notes |
|---|---|---|

## Open questions
- none
