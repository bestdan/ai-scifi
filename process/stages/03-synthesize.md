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

   Each premise also gets two lines:
   - **Load:** each novum it carries, and its twist if it has one.
   - **Estimated minimum:** 3,000 words, plus about 1,500 for each novum or
     twist after the first. A premise with two nova and a twist needs about
     6,000. This is a heuristic resting on one story, calibration-01; check
     it against each story's outcome.
2. After the critiques are in, add a summary table and a **Decision** to
   `03-synthesis.md`. The Decision names the chosen premise, says how it
   answers the panel's warnings, and lists what was declined.

**Gate:** one premise. Reject a premise whose estimated minimum is above the
top of the brief's length range, or narrow it until it fits. In `human`
mode, recommend one and the human picks it. In `proxy` mode, first get an
`agent-guidance:consultant` second opinion on the choice, then the
orchestrator picks it and logs the choice, its reasons and the runner-up in
`STATUS.md`. Either way, record the runners-up in `STATUS.md` as seed stock.

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
| Chiang | What philosophical question is it really about? Does the feeling grow out of the concept? What form does the idea require? What is the most likely way it fails at this length? |
| Banks | Is there moral friction? Who does the dirty work? Where does the humour live? Does it hold scale and intimacy together? Is it enjoyable to inhabit under the tone charter? |
| Cartographer | Re-check novelty as now written, including any new combinations or twists. Search for any new prior art they bring in. Give a revised Novelty score and status, and flag any attractor clusters from the audit. |
| other | Your persona's "In critique" questions. |

Then rank the premises, and give one paragraph on why your top choice should
win. The Cartographer ranks on novelty alone.

**Write:** `stories/<slug>/03-critique/<lens>.md`

**Reply:** your ranking, with a one-line reason.
