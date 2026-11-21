# Status: run-09

- **Gate mode:** proxy. The human decides stages 0 and 10; the
  orchestrator decides the rest by proxy.
- **Current stage:** 3, Synthesize
- **Next action:** write premises for the five shortlisted entries.

> **Proxy mode:** this file names the premise. The human doesn't open
> anything in this story's directory except `final.md` until they have read
> the story.

## Drafter
Stages 6 and 8 use **Gemini 4 Argon** (`gemini-4-argon-high`) through
`~/.local/bin/agy`, at the human's request, in one resumed conversation,
per `dev_docs/external-drafter.md`. Conversation ID: not started yet.

## Gate decisions
| Stage | Date | Decided by | Decision | Reasons | Runner-up |
|---|---|---|---|---|---|
| 0 Brief | 2026-11-21 | the human | Approved: novella 17,500–40,000, proxy, F3, tone procedural and wondering with warmth, Antimemetics Division and Three-Body Problem as register references, Liu added at stages 1 and 3, Gemini 4 Argon drafts | The human asked for ~900 pages, chose the novella cap when told the process tops out at 40,000 words, and approved the drafted brief in chat | Book one of a longer arc; a full novel with process changes (both offered, not chosen) |
| 2 Audit | 2026-11-21 | orchestrator (proxy) | Shortlisted the Top 5, all distinct cores: The Addressee's Reply (asimov/Line Blend × liu/The Minor Third, 35); The Commons in a Clear Year (chiang/The Shape It Heals Toward × lem/The Clear Year, 34); Reheat or Overload (liu/The Pour × banks/Overload Retardation, 34); Spread or Place (le-guin/Misclosure × tchaikovsky/The Wolf Interval, 33); rajaniemi/The Drove (32) | No two entries share a card, so no skip was needed. Premises must steer off this run's new attractors: the monster-and-kinder-library card, the teacher at the bench, the mind as strata, one household as its whole humanity, writing reformed for the mind, the woman specialist as tender, the keeper's one switch. Watts/The Antenna's real-lab citation stays out | Contributing Factors to a Change of Heart (vinge × banks, 32) |

## Token use
One row per stage, added at its gate. Agent tokens are the sum of each
dispatched agent's usage report; the orchestrator's own turns are an
estimate.

| Stage | Agents dispatched | Agent tokens | Orchestrator (est.) |
|---|---|---|---|
| 1 Ideate | 11 lens-ideator | 806,955 | 15,000 |
| 2 Audit | 1 cartographer | 171,223 | 12,000 |

## Gate failures

## Seed stock

## Open questions
