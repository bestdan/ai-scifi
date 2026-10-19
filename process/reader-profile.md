# Reader profile

What the human likes to read. Stories here are written for one reader, so
this is the target the rubric can't give: which nova pull, which shapes of
story pay, and which disappoint. It describes taste, never a premise, so the
human still reads every story blind.

Two sources agree on most of it:

- **The human's Goodreads `read` shelf,** 281 books and 229 ratings, pulled
  on 2026-10-19. Ratings run 4.18 on average, almost exactly the community
  mean (4.19), so a 5 is a real signal and a 3 is a disappointment.
- **The debriefs** of calibration-01, run-03 and run-05.

Where a line below rests on an inference from ratings rather than the
human's own words, it says so.

## Who reads it

- **Ideators (stage 1)** read *What pulls* and *What disappoints*. Each lens
  is assigned one pull (`scripts/assign_ideation.py`), so the pulls spread
  the cards rather than drawing every lens to the same one. A card in a pull
  still has to clear the Cartographer: these are the human's favourite
  territories, so they are also the most charted.
- **The orchestrator at stage 3** uses the whole profile, after the brief's
  seed and ambition, to judge which premise this reader would enjoy most.
- **The drafter (stages 6 and 8)** reads *How the best-loved stories
  are built*.

## What pulls

Ordered by how strongly the ratings show it.

1. **Minds that are genuinely not human.** The strongest signal. The
   uplifted spiders of *Children of Time*, the scramblers of *Blindsight*,
   the robot of *A Psalm for the Wild-Built*, the Culture's Minds, *Rendezvous
   with Rama*, *There Is No Antimemetics Division*, *Alien Clay*. The rating
   is highest when the other mind thinks differently, not when it is a human
   in a costume. Adrian Tchaikovsky is the most-read author on the shelf (15
   books, 9 of them 5 stars).
2. **Copied, uploaded and forked selves.** The Bobiverse, *Diaspora*,
   *Valuable Humans in Transit*, *Axiomatic*, *Oceanic*. The question is what
   a self is once it can be duplicated.
3. **Deep time and vast scale.** *House of Suns*, *Death's End*,
   *Noumenon*, *Seveneves*, *A Deepness in the Sky*, *Hyperion*.
   Civilizations measured in millennia, and scale itself as the reveal.
4. **Technology as magic, seen from both sides.** *Elder Race* and *Engines
   of Reason*, *Lord of Light*, *The Expert System's Champion*. The pleasure
   is the dramatic irony between a viewpoint that sees magic and one that
   sees engineering.
5. **Reasoning as the way through.** *The Martian*, the Bobiverse, *The
   Three-Body Problem*, *The Dark Forest*. Problems are solved by thinking,
   and the logic is fair.
6. **The same questions in nonfiction.** Why minds believe what they do
   (*Thinking, Fast and Slow*, *The True Believer*, *Big Gods*, *The
   Alignment Problem*, *But What If We're Wrong?*), and how to face death
   (*Being Mortal*, *When Breath Becomes Air*). A novum that bears on either
   reaches this reader twice.

Run-05's debrief adds the human's own word: ambition is credited, not
punished. "The premise was extremely ambitious accommodation of theoretical
quantum physics and information theory" was praise.

## What disappoints

- **Physics the reader can't follow, at a length that won't wait.** The one
  adult 1-star on the shelf is Greg Egan's *Dichronauts*, from an author the
  human otherwise rates 5. The human's reasons: the physics was too hard to
  follow, so the story got lost in it, and it was a slog for what it gave
  back. Ambition is still welcome (run-05 was praised for it); what fails is
  a mechanism the reader is never handed a way into, with no pace to carry
  them while they work it out.
- **Strangeness that never resolves.** *Annihilation* 3, *Way Station* 2,
  and in run-05 the final lamp "did just seem throwaway mysterious." The
  style guide's rule against the mysterious final image is this reader's
  rule.
- **Character without an idea under it.** *The Long Way to a Small, Angry
  Planet* got 3 where the same author's *A Psalm for the Wild-Built* got 5.
  The difference is a philosophical core. (Inferred.)
- **Sprawl and pastiche.** *Ilium* and *Olympos* 3, *The Atlantis Gene* 2.
- **Volume military SF is filler, not a model.** 15 books from Evan Currie
  and Craig Alanson average about 3.5. In the human's words they are "the
  junk food of my genres": quick to publish, so there is always one to read.
  Don't borrow from them. A military setting is welcome when it carries an
  idea: *Ender's Game*, *Speaker for the Dead*, *The Forever War*, *Old Man's
  War* and *The Last Colony* all rate 4 or 5.
- **Flat protagonists.** Run-05's Ilse "felt flat"; run-03's Tamsin "seemed
  robotic". Both were otherwise well-received stories.

## How the best-loved stories are built

The drafter's half. These sit beside the style guide, which already holds
the rules the debriefs set (inference pays off, few names introduced slowly,
lyricism that earns its place).

- **Render the other mind from inside.** The spider chapters of *Children of
  Time* are the model: its senses, its priorities, its mistakes, in its own
  terms, without a human translator in the room.
- **Two viewpoints, two levels of understanding.** When the novum can be
  seen as magic by one side and engineering by the other, let the reader
  hold both.
- **Hand the reader a way into hard physics.** Start from something a human
  body would sense, and let momentum carry the reader while the mechanism
  comes clear. Run-05's debrief asked for exactly this ("starting from the
  deep allows you to begin with a human senses reference").
- **Escalate the scale.** Each movement of the story shows the stakes are
  bigger than the last one let on.
- **The idea pays off in a choice.** The novum resolves into a consequence
  or a decision a character has to make, not a description of how it works.
- **Clever people with a voice.** Bob, Mark Watney and the Culture's drones
  are competent, funny and good company. The hard ideas stay readable
  because the people carrying them are a pleasure to be around. This is the
  likeliest cure for the flat protagonists above.
- **A big question underneath.** Personhood, mortality, what a civilization
  owes what it makes. *A Psalm for the Wild-Built* and *Flowers for
  Algernon* outrank books that only have a cool machine.

## Refreshing it

Goodreads has no open API, but each shelf has a public RSS feed:
`https://www.goodreads.com/review/list_rss/<user-id>?shelf=read&page=N`, 100
books a page. The human's user ID is deliberately not stored in this public
repo; ask for it. Refresh after a run of new reading, and say here what
changed.
