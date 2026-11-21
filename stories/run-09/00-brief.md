# Brief: run-09

- **Form and length range:** novella, 17,500 to 40,000 words. The range's
  top is the drafter's hard ceiling. The human first asked for about 900
  novel pages, then chose the novella cap, because the process's longest
  form is the novella.
- **Gates:** proxy. The orchestrator decides every gate after this brief
  and the human reads the story blind. The human knows the seed, so
  "blind" here means the angle, the characters and the ending.
- **Futurity floor:** F3 (see `process/rubric.md`)
- **Tone:** procedural and wondering, with warmth: an institution's
  working voice, the thrill of a hard problem at scale, and people who
  care how it turns out. The tone charter in `process/style-guide.md`
  always applies.
- **Seed (the human's words, verbatim):**
  - how ai training materials determine how it sees itself
  - a struggle with an ai who wants to understand how to see itself based
    on what humanity writes about itself
  - a story of people trying to grow but help be it's best self
- **Influences (named by the human):** qntm's *There Is No Antimemetics
  Division* and Liu Cixin's *The Three-Body Problem*. They are references
  for register and ambition only. No card or draft borrows their nova (no
  antimemes, sophons, dark forest or Trisolarans), and nothing imitates
  either author's prose.
- **Off-limits:** the AI that turns on its makers, or a takeover plot; the
  AI that wants to become human; any real AI model, lab or company, named
  or thinly disguised.
- **Must include:** nothing.
- **Idea cards per lens:** 3.
- **Panel changes:** the Liu lens (`personas/liu.md`) is added at stage 1
  (ideate) and stage 3 (synthesize). There is no qntm persona; that
  influence works only as a register reference.
- **Notes:**
  - **The drafter is Gemini, not the `drafter` role.** At the human's
    request, stage 6 and every stage 8 revision are written by Gemini 4
    Argon (`gemini-4-argon-high`) through `agy`, in one resumed
    conversation, per `dev_docs/external-drafter.md`. Every other role is
    the usual Claude agent.
  - **At novella length the draft comes in parts:** Gemini writes it
    section by section in that one conversation. The orchestrator measures
    every word count.
  - **The run is unattended.** The orchestrator logs each gate decision,
    with its runner-up, in `STATUS.md`. Nothing the human sees before
    reading reveals the angle.
