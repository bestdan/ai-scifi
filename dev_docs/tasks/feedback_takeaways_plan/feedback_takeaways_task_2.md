---
title: Comprehension gate — two-turn First Reader and an outsider grader
priority: high
size: 5
status: new
created: 2026-10-06
source_branch: bestdan/feedback-takeaways
parent: feedback_takeaways
is_blocked_by: feedback_takeaways_task_1
related_files:
  - .claude/agents/first-reader.md
  - .claude/agents/comprehension-grader.md
  - personas/first-reader.md
  - process/stages/07-review.md
  - process/stages/08-revise.md
  - process/stages/09-polish.md
  - tests/test_agents.py
  - stories/calibration-01/human-feedback.md
  - stories/calibration-01/reviews/draft-1/first-reader.md
  - stories/calibration-01/reviews/draft-2/first-reader.md
expires: 2026-12-06
tags: [process, agents, gate]
---

Part of [[feedback_takeaways_plan]].

## Context

**Design section:** "2. The comprehension gate". It needs task 1's payoff
ledger, because the grader grades against the ledger's five graded rows.

**Why the orchestrator doesn't grade:** it wrote the ledger. In
calibration-01 it read two reader reports as passes:
- the draft-1 reader's "lost me" (`reviews/draft-1/first-reader.md:10`);
- the draft-2 reader's open question about the twist
  (`reviews/draft-2/first-reader.md:40`).

**Why two turns:** the persona file and the first prompt are both read
before the draft. A question placed in either one primes the reading. So the
seven questions appear **only** in `07-review.md`, and they reach the reader
in its second message. Today two things break this:
- `personas/first-reader.md` asks for "what I think the story is about" up
  front;
- `07-review.md`'s current reader prompt asks for it in the reply.

**New agent definitions don't load mid-session** (see the dispatch section of
`AGENTS.md`). Test the grader with `claude -p --agent comprehension-grader`,
run unsandboxed from the worktree. The JSON's `modelUsage` names the model.
Strip the sandbox warning line from stdout before parsing.

## Task

1. **The reader's persona** (`personas/first-reader.md`):
   - Remove "what I think the story is about" from the report list. Five
     items remain.
   - Add one sentence: a second message may bring questions, which the
     reader answers from memory without rereading. Not rereading is an
     honour rule.
   - Don't include the questions themselves.

   **The reader's definition** (`.claude/agents/first-reader.md`):
   - Say the same thing.
   - Change "six items" to "five items".
   - Drop the reply's "what I think the story is about".
2. **The grader** (`.claude/agents/comprehension-grader.md`):
   - **Setup:** sonnet, with the tools Read and Write.
   - **Inputs:**
     - a ledger file with **only** the Row and The fact columns of the five
       graded rows;
     - a names-and-roles list taken from the bible's Characters and Glossary
       sections;
     - the reader's answers file.

     The orchestrator writes the first two files into the review folder.
     Phrase the "read nothing else" rule generically, as the first-reader
     definition does, and name no file it must avoid.
   - **Mapping:** Q1–5 → Premise, Stakes, Why, Twist, Ending. Q6 → Who's who,
     graded against the names list. Q7 → reported verbatim as a finding.
   - **Grades:** got it (5), partial (3) or missed (1), each with a quote and
     one sentence of reason. "Got it" requires the causal link in the
     reader's own words. A story with no twist marks that row N/A.
   - **What gates:** only the five ledger rows. Who's who is a score, not a
     gate.
3. **`process/stages/07-review.md`:**
   - Add a **`## Comprehension questions`** numbered list holding the
     design's seven questions, word for word.
   - **Turn 1:** a fresh `first-reader` writes `first-reader.md`. Its prompt
     no longer asks for the premise.
   - **Turn 2:** SendMessage carries the seven questions, and the reader
     writes `comprehension-answers.md`.
   - **The orchestrator:** writes `ledger-rows.md` and `names.md`.
   - **Grading:** a `comprehension-grader` writes `comprehension.md`.

   All of these files go in `reviews/draft-N/`.
4. **`process/stages/08-revise.md`:**
   - Any partial or missed ledger row becomes an automatic structural note.
   - The orchestrator may lower a grade but never raise one.
   - **Loop cap:** after two consecutive failed rounds, log the failure, get
     an `agent-guidance:consultant` opinion, and either take one more round
     or proceed. Either way, record the gap in `STATUS.md` under "Gate
     failures". Task 7 surfaces it at the top of the debrief appendix.
5. **`process/stages/09-polish.md`:** before polish starts, every ledger row
   must be "got it" on the latest draft. After polish, rerun the gate on
   `final.md` with a fresh reader and grader, writing to `reviews/final/`. A
   miss sends the story back to stage 8.
6. **`tests/test_agents.py`:**
   - Add `comprehension-grader` on sonnet. Its tools exclude Bash.
   - Hard-code the seven questions, because the design is deleted at
     graduation. Assert that each one appears in `07-review.md` under
     `## Comprehension questions`.
   - Assert that **none** of the seven appears in `personas/first-reader.md`
     or `.claude/agents/first-reader.md`.

## Acceptance Criteria

- **Code-enforced:**
  - `just check` passes.
  - `tests/test_agents.py` covers the new role and the question placement.
- **User-run:** run `claude -p --agent comprehension-grader` against two
  fixtures, in scratch, not committed. Take the ledger rows from the table
  in `human-feedback.md` §1, because the calibration-01 bible has no ledger.
  - **Negative fixture:** the human's own §1 answers ("some sort of thing
    where people metamorphise…", "no real idea", "not put together"). Expect
    Stakes and Why to come back partial or missed.
  - **Positive fixture:** causal answers written from that table. Expect
    "got it" on those rows.
  - **Model:** `modelUsage` names sonnet in both runs.
