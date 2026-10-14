# Handoff: run-05 (*To Be Read Slowly*)

For an agent picking this story up. Read `AGENTS.md` and `process/PROCESS.md`
first. **Don't discuss the story's content with the human until they've
read it**: they read it blind.

Kindle delivery is a separate piece of work, on its own branch and in its
own worktree (`bestdan/agent-abb5ea19820d40edf`), and is not part of this
story.

## Where things are

- **Repo:** `/home/dan/src/ai-scifi`.
- **Story worktree:** `/home/dan/src/worktrees/ai-scifi/story-run-05`, on
  branch `bestdan/story-run-05`. Enter it with `EnterWorktree` and
  `name: story-run-05`, which re-attaches the existing branch. Don't pass a
  path.
- **State:** stage 9 is done and the story is ready. It's at stage 10
  (debrief), waiting on the human's read. Everything is committed and
  nothing is pushed.
  - `stories/run-05/final.md`: 30,420 words.
  - `stories/run-05/To Be Read Slowly.epub`.
  - `stories/run-05/STATUS.md`: every gate decision, the logged gate
    failures, and the seed stock (premise D is the human's chosen
    alternate).
  - `stories/run-05/MORNING.md`: the process retrospective, for the human
    to read after the story.

## Open task 1: the stage 10 debrief, after the human has read it

Follow `process/stages/10-debrief.md` and `templates/debrief.md`, and write
`stories/run-05/debrief.md`. Points the debrief should test against the
human's read are listed in `STATUS.md` → "Gate failures":
- the comprehension gate never passed: Premise, Stakes and Why stayed
  partial, Terms missed, and the lost-list ran 13–17;
- whether part 1's opening hooks;
- whether the part 5 key-handover logic lands.

## Open task 2: landing, only on the human's word

1. Land the lint branch `bestdan/agent-a8e83c3f73f501565` (lint budgets per
   1,000 words) on `main` first. It's already merged into the story branch.
2. Then, from the main checkout, `git merge --ff-only bestdan/story-run-05`.
   If `main` has moved, rebase the story branch first (`AGENTS.md`).
3. Clean up the lint worktree
   (`/home/dan/src/worktrees/ai-scifi/agent-a8e83c3f73f501565`) with the
   workflow-skills plugin's `scripts/worktree-remove.sh <path>`, never
   `rm -rf`.

## Unrelated, but noticed

- `bestdan/story-run-04` holds a different, unlanded story, which is also
  waiting for its own debrief. This run left it unchanged, apart from an
  empty `stories/run-04/research/` directory in its worktree. The directory
  is untracked and harmless, so `rmdir` it if you like.
- Candidate process changes from this run are in `MORNING.md`: keep the
  open-territory list away from ideators; make the lost-list count only
  unresolved confusions; keep real units out of the Terms row; require one
  scene on page 1 for long-form. None of them is applied.
