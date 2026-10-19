# ai-scifi

An experiment: can an AI write science fiction that is actually *new*?

Human SF has mapped a lot of territory. Uploads, generation ships, first
contact, the Singularity, the post-scarcity utopia: each has a canonical
treatment, and most new ideas turn out to be variations on one of them. This
project treats that saturation as the problem to solve. Every idea has to name
its closest prior art and say what it does that the prior art could not.

## How it works

A story moves through ten stages, from a brief to a polished manuscript and
the human's debrief. At each stage a panel of **editorial lenses** works on
it. Each lens is modelled on the published sensibility of a major SF author,
and each has a defined job, so they disagree with each other on purpose. The
human writes the brief and decides whether the finished story lands. The
gates in between are decided by the human, or by the orchestrator acting as
proxy so the human can read the story blind; the brief chooses which.

```
Brief → Ideate → Audit → Synthesize → Build → Structure → Draft → Review → Revise → Polish → Debrief
         (panel)  (Cartographer)                                (cold reader + outsider grader)
```

Process, gates and rubric are in [`process/PROCESS.md`](process/PROCESS.md).

## Layout

| Path | What's in it |
|---|---|
| `process/PROCESS.md` | The stages, their inputs and outputs, who works at each one, and the gates |
| `process/rubric.md` | How ideas and drafts are scored, including the Futurity scale |
| `process/attractors.md` | Ground the generating model keeps returning to, kept by the Cartographer. Ideators stay off it |
| `process/stimuli.toml` | Lists `scripts/assign_ideation.py` draws each lens's random starting point from |
| `process/reader-profile.md` | What the human likes to read, from their ratings and debriefs. Ideation, the premise pick and drafting aim at it |
| `process/style-guide.md` | Prose rules, and the failure modes of machine-written fiction to avoid |
| `personas/` | The editorial lenses. Start at `personas/README.md` |
| `templates/` | Fill-in forms for each stage's artifact |
| `stories/<slug>/` | One directory per story, holding every stage's artifact and a `STATUS.md` |

## A note on the personas

The personas are critical lenses built from what each author published and
said in public: their preoccupations, their methods, the questions their work
keeps asking. They don't imitate anyone's voice, and they never put invented
opinions or quotes in a real person's mouth. A persona note reads "the Watts
lens asks whether this character needs to be conscious at all", not "Peter
Watts thinks…".
