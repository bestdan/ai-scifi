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
2. **Live the novum, don't explain it.** Characters who've lived with a thing
   all their lives don't explain it to each other. The reader infers it from
   what people take for granted. Exposition is allowed only where a character
   in the scene has a reason to explain.
3. **Trust the reader.** Leave invented terms undefined when context carries
   them. Cut the sentence that explains the subtext.
4. **Dialogue has friction.** People talk past each other, dodge, lie, and
   mean less than they say or more. Nobody delivers the theme out loud.
5. **Consequences surface sideways.** The big change shows itself through a
   small domestic detail rather than a briefing.
6. **The ending costs something,** and it doesn't have to resolve. An ending
   can open a question instead of closing one.
7. **Names come from the world.** Derive them from the culture, language and
   history the story has built.

## The banned list

The mechanical half of the list is data in
[`prose-rules.toml`](prose-rules.toml), and `just lint <file>` checks a story
against it. It covers:

- stock phrases ("a testament to", "the silence was deafening", "a flicker
  of", …), including therapy-speak in dialogue;
- default "speculative" names (Elara, Kael, Voss, …) and stock ship names;
- counted habits:
  - em-dash pileups;
  - "the way…" similes;
  - "It wasn't X. It was Y." contrasts;
  - short paragraph-closing clauses ("zingers").

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
  time.
- Introduce a term where the meaning can be inferred, never next to a gloss in
  apposition (", a device that…").
- Coin terms the way a culture would: by compounding, clipping, borrowing
  from other languages, slang, or a brand name gone generic. Avoid Latinate
  techno-jargon.
