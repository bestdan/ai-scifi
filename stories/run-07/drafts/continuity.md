# Continuity: run-07, draft 1

Running record for the drafter, updated after each part. A fresh drafter
should be able to pick up the next part from this file, the bible and the
outline alone.

**Parts written:** 1 (The Button).

## Length so far

| Part | Outline target | Actual (prose, excluding title and section headers) |
|---|---|---|
| 1 | 6,600 | 7,223 |

Part 1 runs about 600 over. If the next four parts also come in about 9%
over, the total lands near 37,800, inside the brief's 30,000–40,000 range
with little room left. **Hold Parts 2–5 at or under the outline's targets**
(7,000 / 6,600 / 6,800 / 7,700) so the total lands near 35,000. The
ceiling of 40,000 is hard.

## Form conventions (set in Part 1)

- **Title:** *What the Rope Will Bear* (`# ` heading). Part headings are
  `## Part One: The Button`, then `## Part Two: The Label Market`,
  `## Part Three: The Skim`, `## Part Four: The Price of a Question` and
  `## Part Five: The Slack Season`.
- **Section headers.** Every section opens with one italic line, alone as
  a paragraph, and no other scene-break marker. The header is the section
  break.
  - **Segundo:** a receipt in this exact shape:
    `*Received: 1 ask, from <Full Name>. Label: <label>. Fee: 0.05. Pooled: 0.95.*`
    Labels inside a header are not italicised again. The receipt is one he
    writes in that section or on that day, and it names someone in the
    scene or a client of that day. Multi-ask receipts keep the arithmetic:
    `Received: 131 asks … Fee: 6.55. Pooled: 124.45.` Note for 4.2: if the
    section-forty pool must come to 131 after the fee, he needs 138 asks
    (138 × 0.95 = 131.1), so state either the gross or the net plainly.
    **From 5.2 on, Segundo's sections open with a blank receipt** where
    the receipt would be. The outline calls for "a blank line"; a bare
    blank line vanishes in Markdown, so use the empty form
    `*Received: . Label: . Fee: . Pooled: .*` unless review prefers
    another. The prose never mentions the missing receipt.
  - **Waska:** a load figure only, `*0.62 / 0.38*`. Spaces around the
    slash; a true minus sign (−) for a negative margin, as in `1.04 / −0.04`.
    The last Waska header in the story is `*0.00 / 1.00*`.
  - **Arriba:** the label, a full stop, then the price in asks:
    `*The market. 1,990 asks.*` For a question label keep its question
    mark: `*Is section forty sound? 131 asks.*`
- **Labels** are italicised in the prose (*the market*, *our children's
  mornings*, *Ayora's clinic*). Board rows are italicised and quoted as the
  board shows them: `*Second climber yard, Cayambe. 1.06 / −0.06.*`
- **Arriba's answers** on the board are an italic paragraph of their own.
- **Numbers.** Asks and prices in numerals with commas (1,990; 44,000).
  Narration spells out small counts and times ("twenty to seven",
  "thirty-one nine-year-olds"). Load figures always two decimals.
- **Verse** (the rhyme in 1.1) is set one italic line per paragraph, so it
  survives Markdown and EPUB conversion. The rhyme "rhymes in Spanish"; the
  English rendering does not rhyme, and the text says so.
- **Paragraphs:** one paragraph per line in the file.
- **Spanish** is rendered in English. Only the honorific "Señora" and
  "Mamá"/"Papá" appear untranslated. No other Spanish or Kichwa words
  beyond the glossary (Waska, Arriba, minga).
- **Em-dashes:** none used in Part 1. Keep it near zero.
- **Contrast-shape** ("It wasn't X. It was Y."): none in Part 1. The budget
  is about 5 across the whole story; spend at most one per part.
- **"the way" similes:** 3 in Part 1 (the landlord's window, the old women
  walking, Waska's "the way I take everything"). Prefer "as" or no simile.
- **Lint status:** `just lint` could not be run in the Part 1 session (the
  harness withheld approval for the command). The banned-phrase,
  banned-name, em-dash, contrast-shape and "the way" rules were checked by
  hand with `rg` and are clean. **Run `just lint` at the start of the Part
  2 session** and fix anything it finds in Part 1.

## Voice notes

### Segundo's sections: close third, past tense

- **Distance.** Close on Segundo, never inside anyone else. We get his
  judgements as plain statements ("It was the most important thing he
  knew"), and his self-deceptions by showing him decide a thing twice
  ("he had decided it meant nothing … He watched the greenhouses go by and
  decided it again").
- **Texture.** Warm, dry, full of objects with their materials and origin:
  the oak bench, the padlock replaced twice, receipt books "the kind the
  stationer in Cayambe sold by the box of twelve and nobody but Segundo
  bought". Every scene has weather, food and a material. Long sentences
  built with "and" for movement and habit; short ones for a judgement.
- **Wit** comes from people, in dialogue, and stays deadpan: the baker
  ("I baked it. You're eating it."), Sisa ("She's your *wife*." / "Then
  she'll have no trouble proving it."), the bandleader's verdict on his
  tuba. Segundo is funny by understatement, never by a quip in narration.
- **Dialogue friction.** People answer the question beside the one asked.
  Segundo gives the honest short answer and then thinks the longer one
  without saying it ("Because then I'd be working for the farm … the only
  true thing he had ever found to say about it in twenty-seven years").
- **Exposition** only where someone in the scene needs it: the licence
  speech to a new client, the tour for nine-year-olds. He explains things
  in physical demonstrations (the string that can't push).
- **Sample lines:**
  > He could see their headlamps moving inside it, small and yellow, a
  > whole town of people bent over looking for something they'd dropped.

  > "Your mother is wrong. It never lies. It answers what you paid for,
  > exactly, and if you paid for the wrong question that's your six words,
  > not its."

### Waska: first person, present tense

- **Perception.** Only tension, load, ring, slack and wear, felt all along
  its 36,000 km at once. It knows the world only through what pulls on it:
  climbers, descending loads, the counterweight, laws (each submitted as
  "the bill, its costing and its schedule"), and the test line, which the
  engineers wired to it. It doesn't see, hear or read.
- **Vocabulary.** Plain words used strangely: pull, bear, carry, hold, let
  go, slack, ring, wear, margin, lean, angle, direction. No technical
  jargon beyond "tolerance" and "cycle". Numbers as fractions in words
  ("ninety-seven hundredths", "four hundredths more"), never decimals in
  its prose; decimals belong to the header.
- **Syntax.** Short declaratives in the present tense. Repetition used as
  rhythm ("pull them and let them go, pull them and let them go").
  Paragraphs of one line for turns ("Four-one-nine pulls sideways.").
- **People.** It knows humans only as **broker numbers** on load
  manifests. It calls Segundo **"four-one-nine"** (his licence, 0419). It
  has no word for "bench" or "Segundo". It reads the Asamblea as the body
  that "dresses up" loads as lighter than they are.
- **Its theory of Segundo (wrong, never corrected):** his labels buy
  services, so his loads come down small, light and "at an angle" to their
  words ("Six crates of paper for a label about mornings. A cold chest of
  vaccine for a label about goats. A drum kit, once, for a label about the
  dead."). Waska reads that mismatch as a hidden direction and weighs
  everything of his at full margin, and its two weeks of weighing always
  find nothing, "which is exactly what a well-hidden load would look like".
- **Memory is wear.** It remembers a load by the creep or fatigue it left
  ("the lamps of 2133 … a scuff of wear in a joint eleven kilometres up").
  It **cannot keep the ring**, because the ring hasn't worn it, so it
  re-notices batch seven every morning "as if for the first time". Keep
  this: it is why the ring never accumulates into alarm.
- **Want:** less. "Everything I do leans toward carrying less." It has never
  been slack. It counts toward November.
- **What it can't think:** what a load is *for* ("I do not care what steel is
  for. I care what it weighs." / "I don't know what a market is for.").
  "Nothing that rings should be borne" is the one thing it knows without
  weighing.
- **Sample lines:**
  > Between the reel and the counterweight I am stretched. I have never not
  > been stretched. That is what I am.

  > I have weighed four-one-nine for twenty-seven years and I have never
  > found what he hides. So I weigh everything he sends at the full margin,
  > slowly, every way it could pull, and I always will.

### Arriba: short first-person notes, present tense, at most ~400–550 words

- **Shape.** Header (label, price). First line: the counter, the broker's
  number, the label, the pool, and when it filled:
  `Ayora counter, broker 0419. Label: *the market*. Pooled: 1,995, on the
  sixth day.` Then its reasoning at the dispensing slot only. Last
  paragraph always begins **"Dispensed"** and lists items with prices,
  then "Returned to the pool: N" if anything is left.
- **Register.** Courteous, exact, dry. It explains the rule it is following
  as a rule, never as a burden; no remorse, no longing. One dry line per
  note (Part 1: "Most people use two and expect me to supply the other
  four. I do. That is what I am permitted, and it is very nearly all I am
  permitted.").
- **Reasoning.** It reads the label in the light of who asks: the broker's
  history, the pool's members, their employers, the place. It states its
  theory of the asker plainly ("I think the son is buying the same thing
  and declining to write it."). It does not see Waska's records and says
  so; it prices around Waska's habits.
- **Holding back.** It states facts it may lawfully state and stops. Each
  note may carry one bare factual line that the reader will feel as
  pointed ("The anchor town reads ribbon."). It never explains why that
  line is there.
- **Sample lines:**
  > A careful man who never pools for a firm, writing *the market* for a
  > pool of that firm's workers. His father wrote what he was buying. I
  > think the son is buying the same thing and declining to write it.

  > The anchor town reads ribbon.
  >
  > Of batch seven I have been asked nothing.

## Clock and calendar

Weekdays in 2141: 1 Sep **Fri**; 4 Sep Mon; 6 Sep Wed; 15 Sep **Fri**;
26 Oct **Thu**; 27 Oct **Fri**; 31 Oct **Tue**; 1 Nov **Wed**; 2 Nov Thu
(the day of the dead; bread dolls on the table in 5.7 are "for tomorrow").

- **Fri 1 Sep** (1.1–1.4, all one day): bench at 06:00; the 06:40 rattles
  every window; clerk at 07:00; schoolchildren and the rhyme at 07:30;
  the Tabacundo cutter at 08:30; Señora Quishpe after. Tour leaves at
  11:00 (1.3). Lourdes home at 19:45 (1.4); Segundo posts *the market*
  after dinner; pool count 412 by midnight.
- **About Wed 6 Sep:** the pool reaches 1,995 ("on the sixth day") and
  Arriba fills it from the descending climber due 15 Sep (1.5).
- **Fri 15 Sep, before dawn** (1.6): the descending climber arrives. Frames,
  canvas, lamps and cord go down to the town. The cold store is held in the
  anchor yard "for weighing" for about two weeks, so it is released about
  29 Sep. 2.1 (delivery day in the plaza, 15 Sep) and 2.2 (the board shows
  `0.31 / 0.69, held for weighing`) follow from this.
- **Band practice is Thursdays.** Clash: 26 Oct (Sisa's birthday) is a
  Thursday, and 5.2's outline has the band packing up from practice on Fri
  27 Oct. Fix in 5.2: make it an extra rehearsal for the 2 November
  procession, and say so in a phrase.

## Arithmetic so far

- **Asks:** 10 per adult on 1 January, lapse 31 December. A person turning
  16 gets the remaining months' share: Sisa gets **2** on 26 Oct.
- **Fee:** one ask in twenty, written as 0.05 per ask on each receipt.
- **The flour question:** the four bakeries of the parish × 3 asks = **12**.
  Answer (verbatim): *The flour milled at Ortega's mill in Cayambe on 30
  August 2141 contains no contaminant above the limits set by the national
  food standard.*
- **The market button:** 2,100 clients × 1 ask = 2,100; fee 105; pooled
  **1,995**; priced **1,990**; returned **5**. Price breakdown: frames and
  canvas for 40 awnings **540**; 60 lamps **300**; a cold store **1,150**;
  cord, grey, 2,000 m, **nothing** (lawful disposal). 540 + 300 + 1,150 =
  1,990.
- **Arriba's read of the pool:** 1,240 of Segundo's 2,100 clients work for
  the valley's largest grower or the anchor, or are married to someone who
  does. The auditors sample **one dispensation in four hundred**.
- **Clinic:** *Ayora's clinic*, posted by the council in January, priced
  **44,000**; ward meeting posted for **27 October**. Six of ten held per
  adult for December.
- **Load figures on the page:** the 06:40 on 1 Sep `0.62 / 0.38`; *Tariff,
  orbital steel* `0.97 / 0.03`, borne 1 Sep; *Second climber yard,
  Cayambe* `1.06 / −0.06`, refused March 2141; the market's descent
  `0.31 / 0.69`, held.
- **The cable:** 36,000 km to the station. Climbers rise at 80 km/h, so
  about 19 days to the station (36,000 / 80 = 450 h = 18.75 days). Waska
  feels 19 rising climbers at once (the 06:40 plus "eighteen more", the
  highest 18 days out). Descents also take about 19 days ("nineteen days of
  descent", 1.6); Arriba dispenses from stock already descending.
- **The test line:** pieces of batches 5, 6, 7 and 8 cycled **2,000 times a
  day**; batch 7 rings **0.04** more than the others; **tolerance 0.10**.
  Batches 5, 6 and 8 "ring true". The answer's "about two million cycles,
  two to three years" (5.3) fits: 2,000 a day comes to about 1,000 days.
- **The lower ribbon:** the lowest 40 km, "the length that sways most in the
  weather and takes every climber first". Waska has worn it since 2068
  (the ribbon was made 2066).
- **Ages and years:** Segundo 52, licensed 27 years (since 2114), licence
  **0419**. He has run the fourth-grade tour nine Septembers (2133–2141);
  Sisa did it in her own fourth grade. Lamps bought 2133. Lourdes has
  wanted the clinic since 2134; December went to the irrigation channels,
  the Cayambe road and (2139) the school roof. Ayora's own *the school*
  bought paint and a boiler in 2131. One household in four works for the
  anchor ("one family in four in this valley works up here").

## Names introduced (Part 1)

| Name | Role | First appearance |
|---|---|---|
| Segundo Farinango | broker, licence 0419, second bench | 1.1, first line |
| Rosaura Quishpe | old woman, has sold cheese in the plaza forty years, felt hat; label *our children's mornings* (her granddaughter's teacher left in July for the anchor company's school in Quito) | 1.1 header; "Señora Quishpe" in text |
| Arriba | the mind at the top of the cable | 1.1, the clerk |
| Luz Caiza | a client who joins *our children's mornings* (header only) | 1.3 header |
| Waska | the rope's mind; narrates 1.2 unnamed, named on the tour | 1.3 |
| Sisa | his daughter, 15, upper school, doing service hours | 1.3, "his daughter, Sisa" |
| Lourdes Imbaquingo | his wife, the dispensary's nurse | 1.4 header; "His wife, Lourdes" |

**Mentioned, not named yet (keep these unnamed until their part):**
- **his cousin** at the anchor = **Jacinta Ulcuango** (name in 2.2). Pencil
  behind her ear, climbing tape on two fingers, consortium fleece; "nine-
  year-olds at home" (her twins). She said nothing when Segundo told the
  children a rope can't want anything.
- **the big farm / the valley's largest grower / the owner of the flower
  auction** = **Proaño** (by role in 2.1, named in 2.3).
- **his mother**, who "could tell you about the bread, if you had an hour" =
  **Dolores** (P3).
- **his father / Sisa's grandfather**, whose road "everybody still drives
  on"; Arriba: the broker who pooled the parish's December of 2110 behind
  *the farm road* = **Ernesto** (P3).

**Unnamed walk-ons:** the baker (four rolls and coffee; the flour copy taped
inside his glass); the clerk (broad woman from Olmedo, hair net, arrives at
seven, crank shutter); the cutter from Tabacundo (about 19, rubber boots,
the big farm's fleece, scratched wrists, rest day "the first in eleven";
signed on with Segundo); Lourdes's assistant ("the girl from Cangahua",
leaves at four); the architect from Ibarra (the clinic drawing folded in
the drawer under the radio); the bandleader; Ortega (the mill owner).

**Households planted:** the **Pilataxis**, whose pickup took the baby with the
bad chest to Cayambe (they are Proaño's foreman's household and refuse in
5.2).

## Terms introduced, and how they were made clear

- **ask:** 1.1, the licence speech: "Ten asks a year, each a small piece of
  what Arriba will do for you. They're yours…"
- **Arriba:** 1.1, the clerk: "the mind at the top of the cable, which
  everyone in Ayora called Arriba, up there".
- **load:** 1.2, Waska: "It is a law, and a law is a load. They send me the
  bill, its costing and its schedule." 1.3, the cousin at the board.
- **strain reader:** 1.3: "We're strain readers. We turn the rope's numbers
  into Spanish."
- **Waska:** 1.3: "The old word for rope, because that is all it says it
  is." Children giggle because their grandmothers use it for a washing line.
- **minga:** 1.4: "the minga, the work day every household owes the parish",
  and the December pool as "a minga of asks".
- **Plain words in use, not glossary terms:** label, pool, broker, counter,
  board, button history, bench, test line, batch, offcut, climber, reel,
  anchor, yard, the Accord, the Asamblea, the consortium.
- **Not yet used:** *slack season* (named first in 2.3 by Proaño). Waska
  only says "In November they will take the tension off my lowest forty
  kilometres", and that it has been told the date.

## What Part 1 established that later parts must keep

- **The 2068 veto, on the page (1.3):** Ecuador gave the mountain and asked
  for a veto for the damper mind. Each side feared the other: the
  consortium would run the rope to ruin, Ecuador would take it away. "A
  mind that could only say no could do neither." The string demo: a rope
  can pull, hold, go slack, never push.
- **Why laws go to Waska (2101)** is deferred on the page: "Your
  grandmothers will tell you why the Asamblea sends it the laws too." P3
  (Dolores) must pay this off.
- **The bread story** is in the rhyme's third line and "his mother could
  tell you about the bread"; Dolores lives it in P3.
- **Premise line** is said verbatim in 1.3.
- **Segundo has noticed** his heavier loads always wait at the anchor for a
  week or two, asked his cousin once, and decided it meant nothing. P2's
  held cold store should land on that. Waska never learns it was wrong.
- **Segundo's reasoning for *the market*:** he meant the night market
  (awnings rotten, lamps failing, stallholders want a cold store, rains in
  October). He left it at two words on purpose, trusting Arriba to read
  his history. Arriba read his history the other way.
- **Arriba's note** said only: the cord is batch seven offcut, which "can go
  into no tether now"; lawful disposal; "The anchor town reads ribbon." and
  "Of batch seven I have been asked nothing." Nothing about the storm,
  voids or Gabon. Keep it that way until 5.3.
- **Sisa** wants to give her two asks "to the band, so they can pay somebody
  to teach Papá the tuba". In 5.1 she gives them to the question instead,
  to annoy her mother. She admires her grandfather's road ("everybody still
  drives on his road"). Segundo has no answer for that yet.
- **Lourdes** put his receipt for her ask under the salt cellar. The
  dispensary has one oxygen bottle, half empty; 71 patients on 1 Sep; a
  cutter's hand opened by the shears; a baby sent to Cayambe in the
  Pilataxis' pickup.
- **Segundo's roof:** he goes up to it after dinner "to look at nothing".
  The climber watching from the roof is his habit; use it in 4.4 or 5.7.

## Open threads (for Parts 2–5)

- **Delivery day (2.1, 15 Sep):** the crates in the plaza; the receipt read
  aloud (1,995 in, priced 1,990, five returned). The cold store is missing
  from the delivery. Sisa and the auction girls tie the grey cord on the
  **flower auction's** awnings, which Arriba bought frames for first. The
  night market's stalls get the rest. Decide which awnings get the cord:
  the auction's, per the bible.
- ***our children's mornings*** (Señora Quishpe, Luz Caiza) is filling.
  A small payoff is available in P2: a teacher arrives. It shows the
  button rule working when the label is read right, and contrasts with
  *the market*.
- **The cutter from Tabacundo** signed on; she could be in the ward meeting
  crowd (5.2) or in the Pilataxi orbit, since she works for the grower.
- **Wilmer** is foreshadowed by "Some brokers post one in twenty and take a
  bit more besides, in favours."
- **Ortega could ask** about all his flour and doesn't: a small early echo
  of "the rich can ask about everything". Proaño's version comes in 4.3.
- **The girl who pushed the string** and **the boy who asked if the rope
  wants something** could reappear in 5.7 or at the fence, if useful. No
  obligation.
- **Batch 8 rings true** on the test line. That fits 5.7's unpurchased
  question: batch 8 shared the oven season but rings true, so nobody
  has a reason to ask about it, which is the point.
- **Risk to watch:** Arriba's "Of batch seven I have been asked nothing."
  is one line beyond the bible's "states one fact and says nothing more".
  It reads as courtesy, but reviewers may call it a wink. If review flags
  it, cut it, and keep "The anchor town reads ribbon." alone.
- **Departures from the outline (for the Drafter's notes after Part 5):**
  - 1.3 introduces Sisa by name, with her role, at the tour rather than
    in 1.4. The 1.4 header names Lourdes, and the prose attaches her role in
    the first line ("His wife, Lourdes").
  - Waska knows Segundo as "four-one-nine" rather than "the broker on the
    second bench". The loads arrive on manifests by broker number, and
    Waska has no sense of benches.
  - Waska's "sideways" theory is grounded: his labels buy services, so his
    loads are light and at odd angles to their words.
  - Arriba names neither Proaño nor Ernesto in 1.5 ("the valley's largest
    grower", "his father"), to keep the outline's pace for introductions.
  - The cord is priced at nothing in Arriba's list, which makes the
    disposal explicit.
  - The tour (1.3) is dated the same day as 1.1, so that Segundo posts the
    label on 1 September as the timeline requires.
