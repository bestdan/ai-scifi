# Stage 3: Synthesize

**Dispatch:** `lens-critic`, once per lens on the stage 3 panel (by default
Vinge, Chiang, Banks and Cartographer), in parallel. Use this prompt:

`Lens: <lens>. Stage: process/stages/03-synthesize.md. Story: stories/<slug>.`

Don't pass `model:`.

## For the orchestrator

1. Before dispatching, write `stories/<slug>/03-synthesis.md`. It holds one
   premise per shortlisted option, labelled A, B, C and so on. Each premise
   is one paragraph covering the novum, who it happens to and what they are
   forced to choose. Fold in the Cartographer's push past the map, and list
   one line each of **Strengths** and **Risks**.

   Each premise also gets three lines:
   - **Plain pitch:** two sentences to a smart reader outside the genre,
     with no coined words: why this world does this, why it matters to
     this person's life or trade, and what they are torn between.
   - **Reach:** what the novum changes for people beyond the main
     characters (whose work, money or power it moves), and the scene where
     the story makes a character weigh it.
   - **Load:** each novum it carries, and its twist if it has one.
   - **Estimated minimum:** 3,000 words, plus about 1,500 for each novum or
     twist after the first. A premise with two nova and a twist needs about
     6,000. This is a heuristic resting on one story, calibration-01; check
     it against each story's outcome.
2. After the critiques are in, add a summary table and a **Decision** to
   `03-synthesis.md`. The Decision names the chosen premise, says how it
   answers the panel's warnings, and lists what was declined.

**Gate:** one premise. Reject a premise whose estimated minimum is above the
top of the brief's length range, or narrow it until it fits. Reject a
premise whose plain pitch doesn't hold up, whose novum doesn't bear
directly on what the protagonist does all day, or whose Reach stays inside
the household. Pick on the brief's seed. Among premises that serve the seed
equally, prefer the one `process/reader-profile.md` says this reader would
enjoy most, and say which of its pulls the choice rests on. A note the brief carries from an
earlier debrief is a constraint every premise has to meet, not the reason to
prefer one. In `human` mode, recommend one and the human picks it. In
`proxy` mode, first get an `agent-guidance:consultant` second opinion on the
choice, then the orchestrator picks it and logs the choice, its reasons and
the runner-up in `STATUS.md`. Either way, record the runners-up in
`STATUS.md` as seed stock.

## For the agent

**Read:**
- `stories/<slug>/00-brief.md`
- `stories/<slug>/03-synthesis.md`
- `stories/<slug>/02-audit.md` (skim it for context)

**Task:** critique each premise from your lens, in about 120 words per
premise.

| Lens | Questions |
|---|---|
| Vinge | Which Futurity level does it actually reach? What in it is still too familiar? Does the viewpoint trick hold? Name one change that would push it further at this length. |
| Chiang | What philosophical question is it really about? Does the feeling grow out of the concept? What form does the idea require? What is the most likely way it fails at this length? Would a reader care about this person in the first page, and why? |
| Banks | Does the plain pitch hold up: would a reader outside the genre see why this world does this? Is there moral friction? Who does the dirty work? Where does the humour live? Does it hold scale and intimacy together: does its Reach go past the household? Is it enjoyable to inhabit under the tone charter? |
| Cartographer | Re-check novelty as now written, including any new combinations or twists. Search for any new prior art they bring in. Give a revised Novelty score and status, and flag any attractor clusters from the audit. |
| other | Your persona's "In critique" questions. |

Then rank the premises, and give one paragraph on why your top choice should
win. The Cartographer ranks on novelty alone.

**Write:** `stories/<slug>/03-critique/<lens>.md`

**Reply:** your ranking, with a one-line reason.
