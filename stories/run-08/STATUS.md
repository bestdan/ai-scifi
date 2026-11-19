# Status: run-08

- **Gate mode:** proxy. The human decides stages 0 and 10; the
  orchestrator decides the rest by proxy.
- **Current stage:** 4, Build
- **Next action:** write the bible and its payoff ledger, then the stage 4 stress test.

> **Proxy mode:** this file names the premise. The human doesn't open
> anything in this story's directory except `final.md` until they have read
> the story.

## Drafter
Stages 6 and 8 use **Gemini 4 Argon** (`gemini-4-argon-high`) through
`~/.local/bin/agy`, at the human's request, in one resumed conversation.
Conversation ID: _set at stage 6_. Every other role is the usual Claude
agent. The debrief should compare this prose with earlier runs.

## Gate decisions
| Stage | Date | Decided by | Decision | Reasons | Runner-up |
|---|---|---|---|---|---|
| 0 Brief | 2026-11-19 | the human | Approved: short story 3,000–7,500, proxy, F3, tone funny and wry (Murderbot Diaries as the register reference), defaults elsewhere, Gemini 4 Argon drafts | The human's approval in chat, with the tone added | none |
| 2 Audit | 2026-11-19 | orchestrator (proxy) | Shortlisted five distinct cores: C1 egan/Cromwell's Rule × tchaikovsky/Cached (37); watts/The Cold Minute with its push, dropping the report (36); C2 banks/Once-Fired × egan/The Glass Takes Months (35); le-guin/Something Worth Fixing with its push, the mother forging the need (34); vinge/Below the Line (32) | Top 5 minus #4 (tchaikovsky/Cached alone, which is C1's core), replaced by the highest-scoring distinct core. Premises must steer off this run's new attractors: the service's instrument misreading a healthy world, the agent made smaller, the staged crisis, and tone words written into the protagonist instead of the prose | vinge/The Tun Season (32) |
| 3 Synthesize | 2026-11-19 | orchestrator (proxy) | A, The Prior (egan/Cromwell's Rule × tchaikovsky/Cached), with Vinge's push as the turn: the birds hide things from her installed prior, not from her | Mean rank 1.0, first for all four lenses. N5, F4, reader-profile pull 1. Under the ceiling at about 6,000. Consultant (fable) 95% on A, 70% on the turn. The synthesis's 'cache shows the service' turn was replaced as a placeholder, not cut for length | C, The Signatory with the slowing dropped (tie at 3.25 with B and D; C chosen on the gate's ambition rule, not on panel votes) |

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

## Gate failures

## Seed stock

- **C, The Signatory** (banks/Once-Fired × egan/The Glass Takes Months), best without the slowing.
- **B, The Ending Technician** (watts/The Cold Minute): the peak-end service.
- **D, The Fee** (le-guin/Something Worth Fixing).
- **E, North for Lunch** (vinge/Below the Line).

## Open questions
