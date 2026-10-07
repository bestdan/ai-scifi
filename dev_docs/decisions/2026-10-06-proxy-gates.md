---
created: 2026-10-06
status: accepted
convention: ../../AGENTS.md
---

# The orchestrator decides the gates by default, and only the human lands a story

## Context

The human wants to read each story blind: "I want to not know the idea
behind the next story, to keep me and you honest."
(`stories/calibration-01/human-feedback.md`, section 3.) Every gate from
stage 2 on shows the premise. The audit, the synthesis, the bible and the
outline all name it. So a human who decides those gates can't read blind,
and the rule "the human decides at every gate" can't stand alongside that
wish. For calibration-01 the orchestrator already acted as proxy, informally.

## Decision

The brief carries a **Gates** field, `human` or `proxy`, and `proxy` is the
default. In proxy mode the human writes the brief and reads only the
finished story. The orchestrator decides every gate from stage 2 to stage
9, and logs each decision in `STATUS.md` with its reasons and runner-up. It
gets an `agent-guidance:consultant` second opinion before choosing the
premise at stage 3. The run is unattended. The slug is chosen from the brief
and never renamed. Commit messages name the stage, not the premise, and the
end-of-run message says only where the story is. In both modes a story lands
only on the human's word, after the stage 10 debrief.

## Consequences

- Good, because the human's debrief is an honest test: the first time the
  human meets the premise is on the page, like any reader.
- Good, because landing is cheap to keep human, and it's where the human
  finds out whether the run worked.
- Bad, because the human gives up steering the premise. A weak pick shows
  up only at the debrief, after a whole run.
- Bad, because the proxy's gate decisions get no human check before the
  story is built on them. The `STATUS.md` log and the stage 3 consultant are
  the only review.

## Revisit when

- The human wants to steer a premise again.
- A proxy run produces a story the debrief rejects at the premise level.

## Confirmation

`tests/test_process.py` checks that every stage file's Gate paragraph names
both modes. Keeping spoilers away from the human rests on `AGENTS.md`
alone.

## Alternatives

- **Gates that hide the premise from the human:** offered, and the human
  declined them.
- **A proxy that also lands the story:** landing is cheap to hold, and the
  debrief is where the human judges the run.
