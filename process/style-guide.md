# Style guide

Machine-written fiction has habits as recognizable as a fingerprint. A reader
spots them within a paragraph and stops trusting the story. This guide lists
them so the drafter can avoid them and the Line Editor can strip them out.
Every drafting and editing agent reads it.

## Tone charter

These stories are written for enjoyment, not nightmares. That sets the
default tone for every stage, from ideation on.

- **Darkness has to be earned by novelty.** Violence, loss, grief, cruelty and
  hard endings are all allowed, and a story without stakes is a weak story.
  What's banned is darkness used as a default setting or as a stand-in for
  seriousness.
- **No stock dystopias.** That means no post-apocalyptic wastelands, no
  Mad Max scavenger worlds, no surveillance or corporate tech dystopias, no
  "technology ruined us" parables, no cosy collapse. A bleak world is allowed
  only when the bleakness is itself the novum, uncharted and specific, and
  the Cartographer agrees it's off the map.
- **Not Panglossian either.** The opposite failure is a frictionless utopia,
  costless technology, or conflict resolved by everyone being reasonable.
  Wonder needs friction, and good futures still have someone paying for them.
- **Aim for the Banks, Chiang and Le Guin register:** worlds you'd want to
  visit, or at least find fascinating to stand in, where terrible things can
  still happen.

## The positive rules

1. **Specific over general.** Not "advanced technology" but the one device,
   what it's made of, and what it smells like when it overheats.
2. **Live the novum, don't lecture it.** Characters who've lived with a thing
   all their lives don't explain it to each other. The reader infers it from
   what people take for granted. Exposition comes where a character in the
   scene has a reason to explain, or from the narration at the payoff point
   the bible's payoff ledger names. Living the novum is not a reason to leave
   its mechanism unstated: what it does, and why this world needs it, is
   said plainly on the page.
3. **Every term earns its place, and the page makes it clear.** A coined or
   foreign word stays only when it does a job the plain word can't: it names
   something the reader's world has no word for, or its strangeness is the
   point. Its meaning is clear from the page at its first use, to a reader
   who doesn't speak the language. Slang and dialect for local colour alone
   don't qualify; use the plain word. Subtext may stay subtext, as long as
   every fact in the payoff ledger is explicit on the page.
4. **Dialogue has friction.** People talk past each other, dodge, lie, and
   mean less than they say or more. Nobody delivers the theme out loud.
5. **Consequences surface sideways.** The big change shows itself through a
   small domestic detail rather than a briefing.
6. **The ending costs something,** and it doesn't have to resolve. An ending
   can open a question instead of closing one.
7. **Names come from the world.** Derive them from the culture, language and
   history the story has built.
8. **Inference pays off.** The reader may be asked to work things out, and
   working them out is part of the pleasure. But every load-bearing fact
   (the novum's mechanism, the stakes, the twist, why the people with power
   did what they did, and what the change means beyond the main
   characters) is made explicit on the page eventually, so a
   reader who didn't work it out still gets the payoff.
9. **Names arrive slowly.** Every named character and invented term arrives
   with its role attached, and the opening scene introduces few of them. A
   reader keeps track of people in scenes with few people in them.
10. **Lyricism earns its place.** An ornate line stays when it is a concrete
    physical image or a moment between people. These are lines the human
    protected in calibration-01:
    - "...with the oilskin satchel held level in front of him, the way other
      men carry a full bowl."
    - "It tasted of nothing, the way a word goes to nothing when you have
      said it forty times."
    - "She laughed. It came up out of her like a hiccup, too loud for the
      kitchen, and then it kept coming, and she had to hold the edge of the
      table."

    An abstract, stacked construction doesn't earn it, and neither does
    slang the reader can't decode. The human couldn't follow these:
    - "Twenty-two years of reading things that wanted a reaction from her
      had left her face with almost nothing to do on its own." (calibration-01)
    - "...two labs answered and one not yet, which would, obviously,
      ceiling, the whole thing ceiling." (run-02)

## The banned list

The mechanical half of the list is data in
[`prose-rules.toml`](prose-rules.toml), and `just lint <file>` checks a story
against it. It covers:

- stock phrases ("a testament to", "the silence was deafening", "a flicker
  of", …), including therapy-speak in dialogue;
- default "speculative" names (Elara, Kael, Voss, …) and stock ship names;
- counted habits:
  - em-dash pileups;
  - "It wasn't X. It was Y." contrasts;
- reported for judgement, never failing:
  - "the way…" similes;
  - short paragraph-closing clauses ("zingers").

A warning isn't an instruction to cut. A simile or a short closing beat that
earns its place stays, and concrete physical images earn it most often.

The file is the source of truth for the exact patterns and budgets.

What no regex can judge stays here:

### Tics

- Adjectives or clauses in threes as a reflex
- Senses listed one after another ("the smell of ozone, the taste of metal,
  the sound of…")
- Names that don't come from the world's culture, even when they aren't on
  the list

### Characters

- Everyone articulate, self-aware and emotionally literate
- Therapy-speak in dialogue ("I hear you", "that's valid", "I need you to
  understand")
- The villain as a faceless corporation or as pure ideology
- The scientist who explains everything to a less-informed colleague

### Plots and endings

- The AI that learns to feel or love, or that turns out to be the most human
  one in the room
- "It was a simulation all along"
- The noble sacrifice that solves everything
- The ending that affirms humanity's resilience or hope by default
- The last line echoing the first line, used as a reflex
- An epiphany that resolves the emotional arc in a single paragraph
- Contact that ends in mutual understanding
- Post-apocalypse, scavenger wastelands, and tech or corporate dystopia as
  the setting (see the tone charter)
- Misery as the ending by reflex: the bleak twist, everyone dead, the
  pointless loss

Any of these can be broken on purpose. Name the rule being broken in the
bible or the outline, and say why. For a rule the linter checks, the waiver
goes in `stories/<slug>/lint-waivers.toml` as a `[[waiver]]` entry with
`rule` and `reason`, and the bible points to that file.

## Invented terms

- Keep a glossary in `04-bible.md`. Use each term with the same meaning every
  time. Each term in it names its **Job**, what the plain word couldn't do,
  and the line that makes it **clear at first use**. A term with no Job is
  cut, and the plain word used instead. A coined, foreign or slang word that
  isn't in the glossary doesn't go in the draft.
- Introduce a term with its role attached, so its meaning is clear from its
  use. Saying in the same sentence what the thing does, or who the person is
  to the scene, is fine. A dictionary-style gloss in apposition (", a device
  that…") is not.
- Coin a term that has passed the Job test the way a culture would: by
  compounding, clipping, borrowing from other languages, slang, or a brand
  name gone generic. Avoid Latinate techno-jargon. Slang that is there only
  for local colour gets the plain word.
