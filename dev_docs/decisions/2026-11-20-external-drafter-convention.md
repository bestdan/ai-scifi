---
created: 2026-11-20
status: accepted
convention: ../external-drafter.md
---

# Drafting with a model outside Claude Code follows a convention, not a stage change

## Context

Run-08 drafted with Gemini through the `agy` CLI at the human's request,
on their Google subscription. It took workarounds nobody had written down:
signing in on the subscription rather than with an API key; inlining every
input while Gemini had no tools; measuring every word count, because Gemini
reported 6,812 words for a 10,985-word draft; per-section counts for length
rounds; and replacement-paragraph patches to hold the length. The human
later added `agy` permission grants so Gemini can write, count and lint for
itself.

## Decision

The mechanics live in `dev_docs/external-drafter.md`. Stage 6 gains one
line pointing to it when the brief names an outside model. The one-drafter
rule and every other role are unchanged.

## Consequences

- Good, because the stage files stay true for any drafter.
- Good, because the next external run starts with the sign-in, grants and
  length method in hand.
- Bad, because `agy`'s flags and config may change between versions, and
  the file then needs keeping current.

## Revisit when

A second outside model is used, or `agy` changes its CLI or grant format.

## Confirmation

Nothing: the convention is followed by hand.
