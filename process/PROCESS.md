# The process

Ten stages take a story from brief to final manuscript and the human's
debrief. Each stage produces one artifact on disk in `stories/<slug>/` and
ends at a **gate**, where someone chooses what goes forward. The brief's
gate mode says who. In `human` mode the human decides every gate. In
`proxy` mode (the default) the orchestrator decides every gate after the
brief and logs each one, so the human can read the story blind. Either way,
only the human lands a story. `AGENTS.md` has the full rule. The
orchestrator (the main agent session) runs the stages, dispatches the agents
and keeps `STATUS.md` current.

Each stage with agent or orchestrator work has a **stage file** in `stages/`. A stage
file holds the agent's task text and the orchestrator's part of that stage.
This page is the overview: who works at each stage, what it produces, and its
gate. Agents are dispatched by role. Each role is defined in
`.claude/agents/`, and the definition fixes the model.

Two principles hold the stages together:

- **The novum comes first.** Darko Suvin's term for the new thing a story
  turns on: an invention, a law, a kind of mind, a social form. A story with a
  weak novum can't be rescued by good prose. So the first three stages search
  for one, test it and harden it, before any characters exist.
- **Pohl's traffic jam.** Frederik Pohl's line is that good SF predicts the
  traffic jam, not the automobile. We judge a novum by the consequences it
  forces, two or three steps out, and the story lives in those consequences.

## Story directory

```
stories/<slug>/
  STATUS.md                  stage, gate decisions, seed stock, open questions
  00-brief.md                constraints for this story
  01-ideas/<lens>.md         idea cards, one file per lens
  02-audit.md                the Cartographer's prior-art map and scores
  03-synthesis.md            premises, the panel summary, the Decision
  03-critique/<lens>.md      stage 3 critiques
  04-bible.md                world, consequences, characters, glossary
  04-critique/<lens>.md      stage 4 stress tests
  05-outline.md              shape, information plan, scenes
  05-critique/<lens>.md      stage 5 critiques
  drafts/draft-N.md          full drafts, each ending in "## Drafter's notes"
  reviews/draft-N/<lens>.md  critiques of draft N, plus first-reader.md
  reviews/draft-N/comprehension-answers.md   the First Reader's turn-2 answers
  reviews/draft-N/ledger-rows.md   the graded ledger rows, for the grader
  reviews/draft-N/names.md   characters and their roles, for the grader
  reviews/draft-N/terms.md   coined and foreign terms, for the grader's Terms row
  reviews/draft-N/comprehension.md   the grader's grades and gate result
  06-revision-plan.md        the latest round's triaged notes
  reviews/protect-list.md    lines the Line Editor must not cut unlogged
  reviews/polish-changelog.md   the Line Editor's log
  reviews/polish-<lens>.md   stage 9 spot-checks
  reviews/final/             the comprehension gate rerun on final.md
  final.md                   the polished manuscript: title and story only
  debrief.md                 stage 10: the human's interview and scores
  lint-waivers.toml          optional: linted rules broken on purpose
  MORNING.md                 optional: a report for the human after an unattended run
  <title>.epub               optional: scripts/make_epub.py output
```

## Stages

| # | Stage | Who | Output | Gate |
|---|---|---|---|---|
| 0 | Brief | the human and the orchestrator | `00-brief.md` (`templates/brief.md`) | the human approves the brief, in either mode |
| 1 | [Ideate](stages/01-ideate.md) | `lens-ideator` × every author lens, blind to each other | `01-ideas/<lens>.md` | none; the cards go to audit |
| 2 | [Audit](stages/02-audit.md) | `cartographer` | `02-audit.md` | a shortlist of 3–5 cards or collisions |
| 3 | [Synthesize](stages/03-synthesize.md) | the orchestrator writes premises; `lens-critic` × the panel | `03-synthesis.md` | one premise; the runners-up become seed stock |
| 4 | [Build](stages/04-build.md) | the orchestrator writes the bible and its payoff ledger; `lens-critic` × the panel stress-tests it | `04-bible.md` | the bible is approved |
| 5 | [Structure](stages/05-structure.md) | the orchestrator writes the outline; `lens-critic` × the panel | `05-outline.md` | the outline is approved |
| 6 | [Draft](stages/06-draft.md) | one `drafter` | `drafts/draft-1.md` | none; the draft goes to review |
| 7 | [Review](stages/07-review.md) | a fresh `first-reader` (two turns), then `lens-critic` × the panel and a `comprehension-grader` | `reviews/draft-N/` | none; the critiques and the comprehension result go to revision |
| 8 | [Revise](stages/08-revise.md) | the orchestrator triages; the same `drafter` revises | `06-revision-plan.md`, `drafts/draft-N+1.md` | the plan is approved. Stages 7–8 repeat until the draft is structurally done and the comprehension gate passes |
| 9 | [Polish](stages/09-polish.md) | `line-editor`, then `lens-critic` spot-checks, then the comprehension gate again | `final.md` | the story is ready |
| 10 | [Debrief](stages/10-debrief.md) | the orchestrator interviews the human | `debrief.md` | the human decides whether the story lands, in either mode |

Gates 2 to 9 are decided by whoever the brief's gate mode names.

**Stage 0** has no stage file. The brief sets:

- the length range, with a waiver line if it starts below the floor in the
  Lengths table;
- the Futurity floor (see `rubric.md`);
- the tone;
- anything off-limits;
- any seed the human brings;
- the number of idea cards per lens (3 by default);
- any changes to the default panels below.

**Stage 2's charted cards.** A card whose closest prior art is a direct match
is marked **charted**. It can still feed a collision, but it can't be the core
novum by itself.

**The comprehension gate stands between stage 7 and stage 9.** A cold
reader reports where it got lost and answers fixed questions, and the
`comprehension-grader`, who sees only the bible's payoff-ledger rows, a
names list, a terms list, the reader's lost-list and its answers, grades
them. Polish starts only when every graded row and the Terms row are "got
it" and the lost-list is short and touches no graded row. The gate runs
again on `final.md`. The orchestrator never grades comprehension itself.

**A structural problem found at stage 9,** or a comprehension miss on
`final.md`, sends the story back to stage 8. The exception is a story the
stage 8 loop cap let through: a miss on `final.md` is then logged, and if
the row passed on draft N and polish changed its quoted text, draft N's
text is restored (`process/stages/09-polish.md`).

## Default panels

| Stage | Lenses |
|---|---|
| 1 Ideate | Asimov, Banks, Watts, Egan, Chiang, Le Guin, Lem, Vinge, Rajaniemi, Tchaikovsky |
| 2 Audit | Cartographer |
| 3 Synthesize | Vinge, Chiang, Banks, Cartographer |
| 4 Build | Watts, Egan, Le Guin, Lem, Tchaikovsky |
| 5 Structure | Asimov, Chiang, Banks |
| 7 Review | Asimov, Watts, Le Guin, Chiang, Cartographer, plus the First Reader (report, then comprehension answers) and the comprehension grader |
| 9 Polish | Line Editor, then Asimov and Rajaniemi spot-checks |

## Lengths

| Form | Words |
|---|---|
| Short story | 3,000 – 7,500 |
| Novelette | 7,500 – 17,500 |
| Novella | 17,500 – 40,000 |

The brief gives a range within its form's row. The bottom of each row is a
floor: a brief that goes below it says why in a waiver line. Stage 3 checks
each premise's load against the range's top.
