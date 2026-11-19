# Brief: run-08

- **Form and length range:** short story, 3,000 to 7,500 words. The range's
  top is the drafter's hard ceiling.
- **Gates:** proxy. The orchestrator decides every gate after this brief
  and the human reads the story blind. The human knows the seed, so
  "blind" here means the angle, the characters and the ending.
- **Futurity floor:** F3 (see `process/rubric.md`)
- **Tone:** funny and wry. The tone charter in `process/style-guide.md`
  always applies.
- **Seed (from issue #43, verbatim):** An agent of a benevolent
  interstellar meddling service, sent to fix a world that is already doing
  fine without help.
- **Off-limits:** nothing beyond the style guide.
- **Must include:** nothing.
- **Panel changes:** defaults.
- **Notes:**
  - **The drafter is Gemini, not the `drafter` role.** At the human's
    request, stage 6 and every stage 8 revision are written by Gemini 4
    Argon (`gemini-4-argon-high`) through the Antigravity CLI (`agy`),
    signed in to the human's Google subscription. All revisions resume the
    same `agy` conversation, so the one-drafter rule holds. The drafter
    gets the same inputs, stage file and binding style guide as the
    `drafter` role, and runs `just lint` itself. Every other stage runs
    with the usual Claude role agents.
  - **The run is unattended.** The orchestrator logs each gate decision,
    with its runner-up, in `STATUS.md`. Nothing the human sees before
    reading reveals the angle.
