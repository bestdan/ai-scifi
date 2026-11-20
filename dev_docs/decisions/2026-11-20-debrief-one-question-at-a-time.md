---
created: 2026-11-20
status: accepted
convention: ../../process/stages/10-debrief.md
---

# The debrief check is asked one question at a time

## Context

Stage 10 showed the whole check at once: six multiple-choice questions
with four long options each, a matching table and a terms list. In run-08
the human asked for it one question at a time through the question dialog
instead. That dialog allows four options, so each question carried three
options plus "can't say".

## Decision

The check is asked through the question dialog, one row per question, with
bare letters as labels and the full text in each option's description.
Each question has the right answer and two wrong ones, the most specific
misreadings, plus "can't say". Who's who is asked per name and Terms as
multi-select groups. The written check stays in `debrief.md` as the
record, and the old written form is the fallback where the dialog isn't
available.

## Consequences

- Good, because each answer is one click and the human isn't reading a
  wall of options.
- Bad, because one fewer wrong option per question makes a lucky pick a
  little likelier.

## Revisit when

A debrief shows picks that look like guessing, or the dialog's option limit
changes.

## Confirmation

Nothing: the stage file holds it.
