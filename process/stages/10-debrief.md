# Stage 10: Debrief

**Who:** the orchestrator interviews the human. No agent is dispatched.

## For the orchestrator

1. **Start only after the human has read `final.md`.** In proxy mode the
   human has seen nothing else.
2. **Prepare the check before the interview.** The human answers by
   picking, not by writing summaries. Write the check into
   `stories/<slug>/debrief.md` section 1 from `reviews/final/ledger-rows.md`,
   `names.md` and `terms.md`:
   - **One multiple-choice question per graded row.** It has one right
     answer, taken from the ledger, and two or three wrong ones. Build each
     wrong answer from a specific misreading: a cold reader's partial
     answer or lost-list entry, a premise or ending the run rejected, or an
     inversion of cause and effect. Every option uses only names and things
     the story puts on the page, and no option is absurd. A wrong option
     that is easy to rule out tests nothing. Vary where the right answer
     sits, and end each question with "can't say".
   - **Who's who:** the names in one list and their roles, shuffled, in
     another. The human matches them, or marks a name "don't remember".
   - **Terms:** the glossary terms. The human marks any they didn't get
     from the page.

   The human has finished the story, so an option reveals nothing they
   haven't read. But picking is easier than recalling, so a right pick
   shows the beat landed, not that the human could reconstruct it.
3. **Ask two open questions first,** before showing the check, because its
   options would prime them:
   - Where did the read snag, and what are you still unsure about?
   - How did the ending land?

   Then show the whole check at once. The human replies with one letter
   per question, plus the matches and any marked terms.
4. **Follow up only on a wrong pick or "can't say".** Ask, in one line,
   what the human took it to be. A wrong pick is the finding: the option
   chosen names the misreading. Grade a right pick "got it", a wrong pick
   "missed" and "can't say" "partial", and quote any follow-up.
5. **Then the rest.** Only after section 1 is graded may the human open
   `MORNING.md`, the reviews or the bible. Then take the rubric scores, the
   run's open questions, the lines to protect, and the process takeaways.
   The check already gives the Understood scores, so ask the human only for
   Felt and Craft. A score per group is enough; ask for a word of why where
   it differs from the panel's.
6. **Compare with the gate.** Set the human's picks beside the reader's
   grades on `final.md`. The cold reader answers open questions and the
   human picks, so a reader's partial beside a human's right pick means the
   reader recalled less, not that the story failed. Where the reader
   passed a row and the human missed it, say so plainly in the debrief:
   the gate didn't predict the human.
7. **Gate failures first in the appendix.** Copy `STATUS.md`'s "Gate
   failures" section to the top of the appendix.

**Gate:** landing. In `human` mode and in `proxy` mode alike, the story
lands only if the human approves after the debrief (see `AGENTS.md`). Log
the decision in `STATUS.md`.
