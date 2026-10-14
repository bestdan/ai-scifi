# Research dossier: language, representation, and AI as a representational instrument

Companion to the physics dossier. Status as of October 2026. Claims are marked
**[shown]** (published, replicated or formally verified), **[contested]** (published
but disputed in the literature), or **[speculation]** (extrapolation, including mine).
Where a source was checked during research, a link is given in section 10.

---

## 1. Bottom line

1. **Mathematics works on the world and nobody agrees why.** Wigner's puzzle (1960) is still open; a character can be a Platonist, a structuralist, or a "we invented it and kept the bits that worked" pragmatist, and each one is a respectable position with named defenders.
2. **Every formal language has provable blind spots, and they are precise.** Gödel, Turing, Tarski, Chaitin and Löwenheim–Skolem do not say "some things are ineffable"; they say no single consistent, checkable system can prove all truths about arithmetic, decide its own halting, define its own truth, certify complexity beyond a fixed bound, or pin down which world it is talking about.
3. **Prediction is compression, and a physical law is a very short program, but a good compressor need not have found the law.** The equivalence is a theorem; the 2025 finding that transformers trained on orbits predict well yet do not use Newton's force law is the live counterweight.
4. **AI models show real but partial convergence on shared internal structure, and reading that structure is translation work.** Linear "world models", features in superposition, and cross-model embedding translation are shown; the strong claim that all models converge on one "Platonic" representation came under serious attack in 2026.
5. **Two descriptions can be exactly equivalent and still mutually unintelligible.** Physical dualities, equivalence of categories, and Quine's indeterminacy all make the same point: a perfect dictionary preserves structure, not the ease of any particular thought, so what is trivial in one language can be intractable in its twin.
6. **Formal verification has split trust from understanding.** Since 2025 machines have produced olympiad-gold proofs and machine-checked results no human has read line by line; we can now know that something is true without anyone knowing why, and whether understanding can be extracted back out (as AlphaZero's chess concepts were, in a small study) is the open question of the decade.

---

## 2. Why mathematics works

**Wigner (1960).** Eugene Wigner's essay "The Unreasonable Effectiveness of Mathematics in the Natural Sciences" (*Communications on Pure and Applied Mathematics* 13, 1960) makes two claims a character should state precisely: mathematical concepts developed for internal, aesthetic reasons turn up in physics with uncanny accuracy (complex numbers in quantum mechanics; Riemannian geometry in general relativity), and the accuracy often exceeds the data the theory was built from (he cites quantum electrodynamics and the Lamb shift). He calls this "a wonderful gift which we neither understand nor deserve." He does not argue for Platonism. He argues the fact is unexplained.

**Hamming (1980).** Richard Hamming's reply of the same title (*American Mathematical Monthly* 87) offers four partial explanations, each one a voice a skeptical character can borrow: we see what we look for (the mathematics shapes the observation); we select the mathematics that fits and discard the rest; science answers comparatively few questions (most of life, he notes, is not captured by equations); and evolution built brains on regularities of a world that already had them. Hamming's honest ending is that the four together "are not enough" and the puzzle remains.

**Positions a character can hold and argue:**

- **Platonism** (Gödel, and many working mathematicians): mathematical objects exist independently of minds; we discover them. Strength: explains why independent cultures find the same primes and why proofs feel found. Weakness: the access problem (Benacerraf, 1973): how does a physical brain causally contact a non-physical object?
- **Mathematical universe hypothesis** (Max Tegmark, *Foundations of Physics*, 2008; *Our Mathematical Universe*, 2014): the physical world *is* a mathematical structure, so effectiveness is no surprise. Strength: dissolves Wigner's puzzle. Weakness: no clear test; it implies every consistent structure exists, which raises a measure problem about why ours looks simple. Tegmark himself floats a restriction to computable structures. Treat as **[speculation]** with a real author.
- **Structural realism** (John Worrall, "Structural Realism: The Best of Both Worlds?", *Dialectica*, 1989; the "ontic" form from James Ladyman, 1998): what survives theory change is mathematical structure, not the objects. Worrall's example: Fresnel's equations for light survived the death of the ether intact, carried over into Maxwell's theory. Ladyman's stronger version says structure is all there is. This is the position most useful to a story about dualities, because it says that two theories with the same structure are the same theory.
- **Formalism** (Hilbert's program; Haskell Curry): mathematics is the manipulation of symbols by rules; "existence" means consistency. Gödel damaged Hilbert's version (section 3), but a modern formalist can say: the rules are what we have, and Lean checks them.
- **Fictionalism** (Hartry Field, *Science Without Numbers*, 1980): numbers are useful fictions, like characters in a novel; Field tried to rewrite Newtonian gravitation without quantifying over numbers to show they are dispensable. Opponent: the Quine–Putnam indispensability argument (we must believe in what our best science quantifies over).
- **Embodied or cognitive** (Lakoff and Núñez, *Where Mathematics Comes From*, 2000): mathematics is built from bodily metaphor (numbers as points on a path). Critics say it explains the psychology of learning, not the truth of results.
- **Intuitionism** (Brouwer): mathematics is mental construction; the law of the excluded middle is not given. Matters later because constructive logic is the logic of programs (section 7).

**Discovered or invented?** The answer that survives cross-examination is the hybrid: the *rules* are chosen (axioms, notations, which questions to ask), and once chosen, the *consequences* are not up to us. Chess is invented; that a given endgame is a forced win is discovered. A character arguing this well will say that language (the axioms) is human and the theorems are not.

---

## 3. Limits of formal language

These are the strongest "what can't be said" results in existence, and critics will check each.

- **Gödel's first incompleteness theorem (1931).** Any consistent, effectively axiomatized system strong enough to do basic arithmetic contains true arithmetic statements it cannot prove. **Second theorem:** such a system cannot prove its own consistency. Common errors to avoid: it does not say "truth is unknowable," it does not apply to systems too weak for arithmetic, and the unprovable sentence is unprovable *in that system* (a stronger system can prove it, and has its own blind spot). Concrete natural examples exist: Goodstein's theorem (1944; shown independent of Peano arithmetic by Kirby and Paris, 1982) and the Paris–Harrington theorem (1977).
- **Turing's halting problem (1936).** No program decides, for all programs and inputs, whether they halt. Same diagonal trick as Gödel. Story-usable modern fact: the fifth Busy Beaver number, BB(5) = 47,176,870, was settled in 2024 by the online bbchallenge collaboration with a Coq-verified proof. Small Turing machines (Yedidia and Aaronson, 2016, with later reductions to under 800 states) have halting behaviour independent of ZFC, the standard foundation of mathematics: the boundary of the unknowable sits a few hundred states away.
- **Tarski's undefinability of truth (1933/1936).** A sufficiently expressive language cannot define its own truth predicate; truth for language L must be defined in a richer metalanguage. This is the formal version of "no language can fully describe itself," and it is the cleanest image for an AI asked to certify its own outputs.
- **Kolmogorov complexity** (Solomonoff 1964, Kolmogorov 1965, Chaitin 1966/69): the complexity of a string is the length of the shortest program that outputs it. It is uncomputable. Most strings are incompressible: random in the precise sense.
- **Chaitin's incompleteness and Ω (1975).** Any formal system can prove "K(x) > n" only for n below a constant fixed by the system's own complexity. A theory cannot certify that anything is much more complex than itself. Chaitin's Ω, the probability that a random program halts, is a well-defined real number whose digits are algorithmically random; a system can determine at most finitely many of them. Chaitin's slogan, that mathematics contains "irreducible" facts true for no reason, is his gloss and is disputed as philosophy, but the theorems are **[shown]**.
- **Löwenheim–Skolem (1915, 1920s).** A first-order theory with an infinite model has models of every infinite size. Hence "Skolem's paradox": if set theory is consistent, it has a *countable* model, in which the sentence "there are uncountable sets" is still true. Related: compactness gives non-standard models of arithmetic containing "numbers" larger than every 1, 2, 3, ... yet satisfying all the same first-order sentences. The consequence for fiction: **a first-order language cannot tell apart certain worlds it is describing.** Hilary Putnam's "Models and Reality" (1980) turned this into an argument that reference itself is indeterminate, which links directly to Quine (section 6).

What these do *not* license: "AI can never be conscious" (the Lucas–Penrose argument is widely rejected, because it assumes humans know their own consistency); and "physics is incomplete" (whether a physical theory inherits Gödel incompleteness depends on whether it encodes arithmetic in its predictions; results exist showing undecidable physical quantities, e.g. Cubitt, Pérez-García and Wolf, *Nature* 2015, on the spectral gap problem, but these are about idealized infinite systems).

---

## 4. Language as compression and prediction

- **Solomonoff induction (1960, 1964).** Predict the next symbol by weighting every program that reproduces the data so far by 2^(−length). It is provably optimal in the limit and uncomputable. It is the mathematical form of Occam's razor. Marcus Hutter's AIXI (2000s) adds action and is likewise uncomputable. The Hutter Prize (since 2006) pays for compressing a Wikipedia snapshot on the stated premise that compression is intelligence.
- **Minimum description length** (Jorma Rissanen, 1978): the best model of data minimizes the length of the model plus the length of the data encoded with the model. The practical version of the same idea, and the formal reason overfitting is bad.
- **Prediction equals compression [shown].** With arithmetic coding, any predictor becomes a lossless compressor whose code length equals its cumulative prediction loss. Delétang et al., "Language Modeling Is Compression" (ICLR 2024), showed Chinchilla 70B, trained mostly on text, compressing ImageNet patches to 43.4% of raw size and LibriSpeech audio to 16.4%, beating PNG (58.5%) and FLAC (30.3%). Caveat the critics will raise: counted honestly, the model's own parameters are part of the description, and then a 70B model is a terrible compressor for small files. Ilya Sutskever's 2023 Simons Institute talk is the popular source of "understanding is compression."
- **Physics laws as maximal compressions.** Ernst Mach's "economy of thought" (1880s) is the ancestor. Kepler's three laws compress Tycho Brahe's tables; Newton compresses Kepler plus Galileo plus tides. A law is a short program whose output is the observations. Good line for a physicist character: a duality is two equally short programs for the same output, which is why "which is real?" has no compression answer.
- **Predictive processing** (Rao and Ballard, 1999; Karl Friston's free-energy principle, 2005 on; Andy Clark, "Whatever Next?", 2013, and *The Experience Machine*, 2023): the brain is a hierarchical prediction machine that perceives by minimizing prediction error. Widely influential, **[contested]** as a complete theory; the free-energy principle is criticized as unfalsifiable in its general form.
- **Does next-token prediction force a world model? [contested, the central live debate].**
  - For: to predict text well about the world, you must model the world. Othello-GPT (Li et al., ICLR 2023) learned a board representation from move sequences alone; Nanda, Lee and Wattenberg (2023) showed it is *linear* once you probe for "mine/theirs" rather than "black/white", which is the image of the model's point of view being different from ours. Gurnee and Tegmark (2023) found linear representations of geography and dates in Llama-2.
  - Against: Bender and Koller (2020, the "octopus" paper) argue form alone cannot yield meaning. More damaging because empirical: Vafa et al. (NeurIPS 2024) found a transformer trained on New York taxi routes navigates well yet its implied street map is incoherent; and Vafa, Chang, Rambachan and Mullainathan, "What Has a Foundation Model Found?" (ICML 2025), trained models on planetary orbits: they predict trajectories well, but when adapted to new tasks their implied force law is not Newton's; they behave as if they learned task-specific heuristics. In their words, the model is Kepler, not Newton. A 2026 follow-up (arXiv 2602.06923) argues small inductive biases recover the Newtonian structure.
  - Defensible synthesis: prediction pressure produces *some* internal model; whether it is the compact, transferable one depends on architecture, data and training, and must be tested, not assumed.

---

## 5. AI as a representational instrument (October 2026)

### 5.1 Convergence

- **Platonic Representation Hypothesis** (Huh, Cheung, Wang, Isola; ICML 2024 position paper, oral). Claim: as models scale, their representations become more similar across architectures, objectives and even modalities (vision and language), converging toward "a shared statistical model of reality." Evidence: mutual-nearest-neighbour alignment between vision and language models rises with capability. **[contested]**: in 2026 Gröger, Wen and Brbić (arXiv 2602.14486) argued the global alignment metrics are confounded by model scale and that, after calibration, global convergence largely disappears while local neighbourhood agreement survives (they propose an "Aristotelian" variant); Koepke, Zverev, Ginosar and Efros (arXiv 2604.18572) found alignment measured on ~1,000 samples degrades substantially at millions of samples and reflects coarse semantics. A character in 2026 who cites PRH as settled is behind; one who cites it as "local structure converges, global geometry doesn't" is current.
- **Cross-model translation without a dictionary [shown].** Jha, Zhang, Shmatikov and Morris, "Harnessing the Universal Geometry of Embeddings" (NeurIPS 2025): vec2vec translates text embeddings between models with different architectures and training data with no paired examples, well enough to extract information about the underlying documents. This is the nearest real thing to translating between two alien languages by structure alone. It works between models trained on human text; it says nothing yet about truly alien sources.

### 5.2 Mechanistic interpretability

- **Linear representation hypothesis:** concepts are directions in activation space (lineage: word2vec "king − man + woman ≈ queen", Mikolov 2013; formalized by Park, Choe and Veitch, 2023). Partly **[shown]**, with counterexamples (some features are circular, e.g. days of the week).
- **Superposition** (Elhage et al., Anthropic, "Toy Models of Superposition", 2022): networks represent more features than they have neurons by packing them into nearly orthogonal directions, so individual neurons are polysemantic. The image: a language with more words than letters, every letter doing several jobs at once.
- **Sparse autoencoders** (Bricken et al., "Towards Monosemanticity", 2023; Cunningham et al., 2023; Templeton et al., "Scaling Monosemanticity", 2024, millions of features in Claude 3 Sonnet, including the "Golden Gate Bridge" feature that, clamped high, made the model identify as the bridge). Caveat: SAE features are not canonical; different runs and sizes split concepts differently, and Google DeepMind's interpretability team publicly deprioritized SAEs in 2025 after weak downstream results. Features are a *chosen* dictionary, not the model's own words.
- **Circuits and attribution graphs** (Lindsey, Olah, Batson et al., "On the Biology of a Large Language Model", March 2025): traced Claude 3.5 Haiku doing two-hop reasoning internally (Dallas → Texas → Austin) and choosing rhyme words before writing the line that ends in them. The authors present these as case studies covering a fraction of computation, not a general theory.
- What is shown: models contain decodable, causally active internal structure that sometimes matches human concepts and sometimes does not. What is hype: that we can read a frontier model's "thoughts" in general. Most of the computation in a large model remains unexplained.

### 5.3 AI in mathematics

- **Lean and Mathlib.** Lean 4 (Leonardo de Moura) plus Mathlib, a community library of roughly two million lines. Milestones: Scholze's Liquid Tensor Experiment (2020–22); Tao and collaborators formalized the Polynomial Freiman–Ruzsa proof in about three weeks (2023); Kevin Buzzard's Fermat's Last Theorem project (from 2024).
- **AlphaGeometry** (Trinh et al., *Nature*, January 2024; AlphaGeometry 2, 2025): neuro-symbolic, language model proposes auxiliary constructions, symbolic engine deduces.
- **AlphaProof** (IMO 2024 with AlphaGeometry 2: 4 of 6 problems, silver-equivalent; *Nature* paper, Hubert et al., November 2025): AlphaZero-style RL inside Lean, trained on about 80 million autoformalized statements, with test-time RL on generated variants of the problem. Statements were formalized by humans at the competition, and some solutions took days.
- **IMO 2025 [shown, with caveats].** Google DeepMind's Gemini Deep Think scored 35/42 (five of six), gold-level, graded by IMO coordinators, in natural language within the time limit. OpenAI's experimental model also reported 35/42, graded by former medallists rather than through the IMO's process. Both failed problem 6. In Lean, ByteDance's Seed-Prover and Harmonic's Aristotle formally proved five of six, with problems formalized for them.
- **Autoformalization:** Math Inc.'s Gauss agent reported completing the strong Prime Number Theorem formalization (Tao–Kontorovich challenge) in about three weeks, roughly 25,000 lines of Lean (September 2025). Self-reported; code is public.
- **Open problems:** October 2025, OpenAI claims that GPT-5 had solved ten Erdős problems collapsed when the solutions were found already in the literature. January 2026, GPT-5.2 Pro produced a near-autonomous solution to Erdős problem 728, formalized in Lean by Aristotle; Tao called it a real improvement while noting such problems are the low-hanging fruit and that success rates across attempts are a few percent. Also AlphaEvolve (May 2025): evolutionary code search found a 48-multiplication algorithm for 4×4 complex matrices, beating Strassen-derived records from 1969.
- Shown versus hype: machines now produce correct competition proofs and occasional minor new results, and formal checking makes their correctness verifiable. Claims of autonomous deep research mathematics are not yet supported.

### 5.4 AI in physics

- **Symbolic regression.** Schmidt and Lipson (*Science*, 2009) recovered conservation laws from pendulum motion; Udrescu and Tegmark's AI Feynman (*Science Advances*, 2020) recovered all 100 equations from the Feynman Lectures from generated data, using physics-inspired tricks (dimensional analysis, symmetry, separability). Cranmer et al. (2020) distilled a graph neural network into a new analytic formula for dark matter halo properties. Lemos, Jeffrey, Cranmer, Ho and Battaglia (2022) "rediscovered" Newton's law of gravitation and inferred planetary masses from solar-system trajectory data. Caveat: these rediscover laws whose form is low-complexity and whose variables are chosen in advance by humans.
- **String landscape.** From 2017 (Yang-Hui He; Krefl and Seong; Ruehle; Carifio, Halverson, Krioukov and Nelson) neural networks have been trained to predict Calabi–Yau topological invariants (Hodge numbers) at high accuracy, to search for vacua with chosen properties, and to approximate Ricci-flat metrics numerically. The number of string vacua is often quoted as 10^500 (with F-theory estimates far larger), which makes the landscape a natural place for machine search. What the networks learn is a predictor, not a theorem; there are cases where ML pattern-spotting led humans to provable results (e.g. murmurations of elliptic curves, He, Lee, Oliver and Pozdnyakov, 2022, now partly proved).
- **Correct but uninterpretable models.** AlphaFold 2 (2020–21; Chemistry Nobel 2024 to Hassabis and Jumper, with Baker) predicts protein structure better than physics-based methods without supplying a theory of folding. The precedent every pessimistic character will cite.

---

## 6. Language shaping thought, and translation

**Sapir–Whorf.** Benjamin Lee Whorf's essays (collected 1956) claimed language structures thought; his flagship claim, that Hopi has no concept of time, was refuted by Ekkehart Malotki's *Hopi Time* (1983). Strong Whorf (language determines thought) is dead. Weak Whorf (language biases attention, memory and ease) has evidence:
- Russian obligatory distinction between light blue (*goluboy*) and dark blue (*siniy*) speeds colour discrimination across the boundary, and verbal interference abolishes the effect (Winawer et al., *PNAS*, 2007).
- Speakers of Kuuk Thaayorre and Guugu Yimithirr (Australia), who use cardinal directions instead of left/right, stay oriented and arrange time east to west (Haviland; Levinson; Boroditsky and Gaby, 2010).
- Pirahã and Munduruku, with few or no exact number words, perform poorly on exact matching of large quantities while approximate magnitude is intact (Gordon, 2004; Pica et al., 2004; Frank et al., 2008).
- Failed replication to be aware of: Boroditsky's 2001 Mandarin vertical-time effect (failed in Chen 2007 and January and Kako 2007).
- Dan Slobin's "thinking for speaking" (1996) is the best modern frame: language shapes what you must attend to in order to speak, not what you can think.

The Le Guin lens will want this nuance, and also the warning that anthropology has been embarrassed by outsiders' claims about "languages without X."

**Quine (1960, *Word and Object*).** A field linguist hears "gavagai" when a rabbit runs past. Every possible observation is consistent with it meaning "rabbit", "undetached rabbit part", or "rabbit-stage." Indeterminacy of translation says there may be no fact of the matter which translation is right, beyond fit with behaviour; two incompatible translation manuals can both be perfect. Davidson's principle of charity (assume the speaker is mostly right) is the standard reply. Kuhn's incommensurability (1962) is the scientific cousin: theories across a revolution can't be translated term for term.

**Wittgenstein.** *Tractatus* (1921): a sentence is a logical picture of a fact; what cannot be pictured (ethics, logic's own form) can only be shown, and the final line, "Whereof one cannot speak, thereof one must be silent." *Philosophical Investigations* (1953, posthumous): meaning is use within a "language game" embedded in a form of life; the rule-following problem (popularized by Kripke, 1982) says no finite set of examples fixes a rule. The line every writer reaches for: "If a lion could talk, we could not understand him." The point is not that lions are stupid but that understanding needs a shared form of life. That is the sharpest available challenge to "AI understands us."

**Chomsky.** The Chomsky hierarchy (1956): regular, context-free, context-sensitive, recursively enumerable grammars, with matching machines up to the Turing machine. Universal grammar: humans have an innate, specific language faculty, with recursion as its core. Challenges: Daniel Everett's Pirahã-lacks-recursion claim (2005, fiercely disputed); Steven Piantadosi, "Modern language models refute Chomsky's approach to language" (2023); Chomsky's reply, *New York Times*, March 2023 ("The False Promise of ChatGPT"): LLMs learn impossible languages as readily as possible ones, so they explain nothing about humans. Kallini et al. (2024) tested that and found GPT-2 learns impossible languages *less* readily. Live.

**Leibniz.** *Dissertatio de arte combinatoria* (1666) and later writings: a *characteristica universalis* (a universal symbolic language in which concepts are composed from primitives) and a *calculus ratiocinator* (mechanical reasoning over it), so that disputes could be settled by saying "*Calculemus*", let us calculate. Frege's *Begriffsschrift* (1879), Russell and Whitehead, and now Lean are partial realizations of the calculus; the universal characteristic, a single language for all concepts, is the part that failed. A character can argue that embedding spaces are Leibniz's characteristic, learned instead of designed. **[speculation]**, and attractive.

**Messages for strangers.** Hans Freudenthal's *Lincos: Design of a Language for Cosmic Intercourse* (1960) teaches mathematics from scratch by ostension (pulses for numbers), then logic, then behaviour through little dialogues between characters. The Arecibo message (16 November 1974, Frank Drake with Carl Sagan and others) was 1,679 bits, the product of primes 23 and 73, so a recipient could arrange it in a rectangle; it showed numbers, DNA elements, a human figure, the telescope. Cosmic Call (1999 and 2003, Yevpatoria RT-70) used Yvan Dutil and Stéphane Dumas's noise-resistant bitmap "lexicon" building from arithmetic to physics. The design assumption shared by all: mathematics is the universal starting point. That assumption is Wigner's puzzle in disguise, and the Lem lens (*His Master's Voice*, 1968) will attack it: a message may be decodable in structure and still opaque in meaning.

**The specific question: exactly equivalent, mutually unintelligible?** Yes, and physics supplies the paradigm.

- **Dualities.** Kramers–Wannier (1941) maps the 2D Ising model at high temperature to the same model at low temperature. Electric–magnetic duality swaps charges and monopoles, and strong and weak coupling. T-duality makes a string on a circle of radius R indistinguishable from one on radius α′/R. Mirror symmetry pairs Calabi–Yau spaces so that a counting problem hard on one side is a routine integral on the other (Candelas, de la Ossa, Green and Parkes, 1991, predicted the number of degree-two rational curves on the quintic, 609,250, before mathematicians could compute it). AdS/CFT (Maldacena, 1997) is a weak–strong duality: when the gravity side is easy to compute, the field theory side is strongly coupled and hard, and the reverse. Same physics, different tractability. The physics dossier covers the details.
- **Philosophy of duality.** Sebastian De Haro and Jeremy Butterfield (2017–2019) treat a duality as an isomorphism between two models of a common "bare theory"; whether dual theories are *physically equivalent* depends on whether they are interpreted "internally" (meaning only what the shared structure fixes). This is the precise version of a structural realist's "they are the same theory" and an opponent's "they say different things about the world."
- **Category theory.** Two categories can be *equivalent* without being *isomorphic*: they share all structural properties up to coherent re-identification, yet their objects need not correspond one-to-one. Hans Halvorson and Thomas Barrett (2016) proposed categorical equivalence and Morita equivalence as criteria for when two scientific theories are the same; James Owen Weatherall (2016) used this to ask whether Newtonian gravitation and its geometrized (Newton–Cartan) form are equivalent. Equivalence is about what is preserved; it is silent on which questions are easy to ask.
- **Isomorphism versus understanding.** A dictionary between two languages can be complete (every sentence maps, truth preserved) while the *cost* of the translation is enormous: the image of a short sentence can be astronomically long. Computational complexity, not semantics, is where mutual unintelligibility lives. Quine says the dictionary may not be unique; complexity says that even the unique one may be unreadable. **[my synthesis; defensible]**

---

## 7. Programming languages as a third kind

Natural language describes; mathematical language proves; programming language *does*. A program is a sentence that, read by a machine, changes the world.

- **Church–Turing (1936).** Church's lambda calculus and Turing's machines define the same class of functions; the thesis says this is everything effectively calculable. David Deutsch's physical version (1985): every finitely realizable physical process can be simulated by a universal computing machine. The physical version is a conjecture about physics, not a theorem.
- **Curry–Howard correspondence** (Curry, 1934 and 1958; William Howard's manuscript, 1969, published 1980; extended to categories by Lambek): propositions are types, proofs are programs, proof simplification is program execution. A proof of "A implies B" *is* a function that turns evidence for A into evidence for B. The logic involved is intuitionistic (constructive), which is why Brouwer comes back. Philip Wadler's "Propositions as Types" (2015) is the readable account. Lean and Coq are built on this: checking a proof is type-checking a program.
- **Homotopy type theory and univalence.** Vladimir Voevodsky (Fields Medal 2002) turned to formal verification after errors were found in his own published work. His univalence axiom (c. 2009), developed in *Homotopy Type Theory* (the Univalent Foundations Program, IAS, 2013), says that equivalence of types is equivalent to equality: (A ≃ B) ≃ (A = B). Equivalent structures are interchangeable in every context the language can express, *by fiat of the foundation*. Cubical type theory (Cohen, Coquand, Huber, Mörtberg, 2015 on) gives this computational content: a proof of equivalence can actually transport a construction across.
  - **The resonance with dualities**, stated carefully: in a univalent foundation, the question "which of two equivalent descriptions is the real one?" cannot be formulated. A structural realist reading of AdS/CFT says the same of bulk and boundary. **[analogy, not a result]**: no one has formalized AdS/CFT in HoTT, and the holographic dictionary is not known to be a complete equivalence outside special regimes. But univalence also makes the gap visible: transport along an equivalence is *defined*, yet the transported object can be enormous and opaque. Equal is not the same as equally legible.
- **A good enough representation is a simulation.** If a description is executable and complete, running it reproduces the phenomenon. Egan built *Permutation City* (1994) on this. The modern near-real version: "world models" and neural simulators (weather models like GraphCast, 2023, outperforming physics-based forecasts at medium range) that are representations you can run but not read. The Lem lens will ask whether a simulation that matches every observation is an explanation; the honest answer is that it is a compression without a reader.

---

## 8. The deep-future question

**Precedents: proofs beyond reading.**
- Four colour theorem: Appel and Haken (1976), computer case-check; Robertson, Sanders, Seymour and Thomas simplified it (1997); Georges Gonthier fully formalized it in Coq (2005).
- Kepler conjecture: Thomas Hales (1998); *Annals* referees after years said they were "99% certain"; the Flyspeck project completed a formal proof in HOL Light and Isabelle (2014, published 2017).
- Classification of finite simple groups: tens of thousands of journal pages across hundreds of papers by about a hundred authors, declared complete around 1983, with a gap closed by Aschbacher and Smith in 2004; a "second generation" proof is still being written partly because the experts are ageing.
- Boolean Pythagorean triples (Heule, Kullmann and Marek, 2016): a 200-terabyte SAT certificate that the numbers 1 to 7,824 can be two-coloured with no monochromatic Pythagorean triple and 7,825 cannot. True, checked, and with no human insight.
- The inverse case: Shinichi Mochizuki's claimed proof of the abc conjecture (2012) is written by a human yet most experts can't read it; Scholze and Stix (2018) identified a step they consider fatal; the dispute is unresolved. Unreadable is not a machine-only problem.

**"The end of theory."** Chris Anderson (*Wired*, 2008): with enough data, correlation supersedes causation and models. Widely rebutted (data needs a model to be data), but AlphaFold and neural weather models revived a weaker version: predictive accuracy without human-legible theory.

**Ted Chiang, "Catching Crumbs from the Table"** (*Nature*, 2000; reprinted as "The Evolution of Human Science" in *Stories of Your Life and Others*, 2002): a mock editorial from a future in which "metahumans" do all original science in a form humans can't follow, and human scientists do hermeneutics on their artifacts. It is prior art the Cartographer will flag on sight; a story must go somewhere it didn't.

**Strongest optimistic position.** Trust and understanding were always separable: nobody personally checks the compiler, the CFSG, or a bridge's finite-element model; we trust processes. Formal verification makes the process airtight, so machine results are more trustworthy than human ones. Understanding can be extracted back: Schut et al. (*PNAS*, 2025) mined novel concepts from AlphaZero's internals and taught them to four top grandmasters, all of whom improved on the concept puzzles; Go professionals improved measurably after AlphaGo (2016's move 37 became a new idea in human play). Interpretability is translation, and translation has always been possible in part. William Thurston's "On Proof and Progress in Mathematics" (1994) argued that mathematics is about human understanding, and an optimist reads AI as a tutor that serves that goal. Tao's stated view is that AI will change mathematics toward large-scale, collaborative, verified work while humans choose the questions.

**Strongest pessimistic position.** Understanding is not compressible below a certain size: if the shortest true explanation of a phenomenon is longer than a human life's reading, no translation can deliver it, and Chaitin guarantees such explanations exist in mathematics. The extracted concepts in the chess study are the human-sized ones, a selection effect. As tools improve, the incentive to understand fades: reading the machine is slower than asking it, and a generation that never derives anything can't check that a translation is faithful (Tarski: the checker needs a richer language than the checked). The end state is Chiang's: humans as commentators on a literature they can verify but not read. The Lem version is harsher: we may not even know which questions the representation answers.

**Middle position worth giving a character.** Understanding becomes stratified: a few people read the machine's concepts directly, as a few once read Latin; everyone else holds certified results the way most people hold the germ theory, on trust in a process.

---

## 9. Story-usable images and mechanics

Each with how far it bends before it breaks.

1. **The two dictionaries.** Two translation manuals, both perfect, that disagree (Quine). *Bends:* use it for a child and an AI agreeing on every sentence while meaning different things. *Breaks:* if the two manuals ever predict different behaviour, it is no longer indeterminacy, just error.
2. **The short sentence with the enormous translation.** A statement that is one line on one side of a duality and a million lines on the other. *Bends:* any weak–strong duality, mirror symmetry's curve counts. *Breaks:* if you claim the translation loses information; an exact duality loses none, only legibility.
3. **"Mine" and "theirs."** Othello-GPT's board was legible only when probed from the player's point of view. *Bends:* a model's world can be correct and indexed to a perspective we didn't think to adopt. *Breaks:* don't make it a hidden personality; it is a coordinate choice.
4. **A model that predicts the planets but doesn't know gravity.** Vafa et al. (2025). *Bends:* the difference between being right and having the law; a child who aces the homework with a trick. *Breaks:* don't claim all models are like this; the result is specific to the setups tested and is being argued over.
5. **More meanings than words.** Superposition: thousands of features packed into fewer neurons, each neuron a pun. *Bends:* a language where every word does several jobs depending on context. *Breaks:* features are not secret messages; they are statistical directions, and reading them requires a dictionary someone chose.
6. **Two strangers' maps aligned with no shared words.** vec2vec translation between embeddings without paired data. *Bends:* structure alone can carry meaning across. *Breaks:* demonstrated only between models trained on overlapping human text.
7. **The machine-checked proof nobody has read.** Flyspeck, the 200-terabyte certificate, AI-generated Lean proofs. *Bends:* certainty without insight, a stamp that says "true" and nothing else. *Breaks:* the checker itself is small and human-readable; that kernel is the human foothold, and it's a good scene.
8. **The number whose digits are true for no reason.** Chaitin's Ω. *Bends:* there are facts no theory can compress. *Breaks:* Ω is defined relative to a choice of universal machine; it is not a mystical constant.
9. **The Busy Beaver wall.** BB(5) is known (2024); a few-hundred-state machine's fate is independent of mathematics' standard axioms. *Bends:* the limit of knowledge has an address, a machine you could print on a page. *Breaks:* "independent of ZFC" is not "unknowable in principle"; a stronger axiom could settle it.
10. **Lincos and the 1,679-bit postcard.** Composing a message from arithmetic up. *Bends:* a child designing a message for an AI or a future, starting from counting. *Breaks:* real METI designers know the mathematics-is-universal assumption is an assumption; let a character know it too.
11. **"If a lion could talk."** *Bends:* shared form of life as the precondition of understanding, and the question of whether an AI trained on human text shares ours more than a lion does. *Breaks:* Wittgenstein was not claiming communication is impossible across forms of life, only that words alone won't do it.
12. **Univalence: equivalent means equal.** *Bends:* a foundation in which asking "which description is the real one?" is ungrammatical. *Breaks:* don't claim physics has adopted HoTT, or that AdS/CFT is proven as an equivalence in general.
13. **Calculemus.** Leibniz's dream of settling arguments by calculation. *Bends:* parents or teachers saying "let's ask it" as the new Calculemus. *Breaks:* formal languages settle questions within their axioms; choosing axioms remains an argument.
14. **Concepts taught back.** Grandmasters learning AlphaZero's new ideas. *Bends:* translation from machine to human is sometimes possible and leaves the human changed. *Breaks:* a four-person proof-of-concept study in a closed game; don't generalize it to science.

Prior art the Cartographer will raise: Chiang, "Story of Your Life" (1998; Sapir–Whorf), "Catching Crumbs from the Table" (2000), "Division by Zero" (1991); Egan, "Luminous" (1995) and "Dark Integers" (2007), *Permutation City* (1994), *Diaspora* (1997); Stephenson, *Anathem* (2008; Platonism as cosmology); Lem, *His Master's Voice* (1968), *Golem XIV* (1981); Liu Cixin, *The Three-Body Problem* (2006); Watts, *Blindsight* (2006; intelligence without understanding); Le Guin, "The Author of the Acacia Seeds" (1974; therolinguistics); Delany, *Babel-17* (1966).

---

## 10. Key people and sources

- **Eugene Wigner** (1960). "The Unreasonable Effectiveness of Mathematics in the Natural Sciences." https://www.maths.ed.ac.uk/~v1ranick/papers/wigner.pdf
- **Richard Hamming** (1980). "The Unreasonable Effectiveness of Mathematics," *Amer. Math. Monthly*. https://math.dartmouth.edu/~matc/MathDrama/reading/Hamming.html
- **Max Tegmark** (2008). "The Mathematical Universe." https://arxiv.org/abs/0704.0646
- **John Worrall** (1989), **James Ladyman** (1998). Structural realism. https://plato.stanford.edu/entries/structural-realism/
- **Hartry Field** (1980). *Science Without Numbers*; fictionalism. https://plato.stanford.edu/entries/fictionalism-mathematics/
- **Kurt Gödel** (1931). Incompleteness. https://plato.stanford.edu/entries/goedel-incompleteness/
- **Alan Turing** (1936). "On Computable Numbers." https://plato.stanford.edu/entries/turing-machine/
- **Alfred Tarski** (1933/36). Undefinability of truth. https://plato.stanford.edu/entries/tarski-truth/
- **Gregory Chaitin** (1975). Ω and algorithmic information. https://plato.stanford.edu/entries/kolmogorov-complexity/ (no SEP entry by that name; see also https://en.wikipedia.org/wiki/Chaitin%27s_constant)
- **Löwenheim, Skolem** (1915, 1920). https://plato.stanford.edu/entries/paradox-skolem/
- **bbchallenge** (2024). BB(5) = 47,176,870. https://bbchallenge.org
- **Ray Solomonoff** (1964), **Jorma Rissanen** (1978), **Marcus Hutter** (2005). https://www.hutter1.net/ai/uaibook.htm
- **Delétang et al.** (2024). "Language Modeling Is Compression." https://arxiv.org/abs/2309.10668
- **Andy Clark** (2013). "Whatever Next?" predictive processing. https://doi.org/10.1017/S0140525X12000477
- **Li et al.** (2023). Othello-GPT. https://arxiv.org/abs/2210.13382 ; **Nanda, Lee, Wattenberg** (2023), linear version: https://arxiv.org/abs/2309.00941
- **Vafa et al.** (2025). "What Has a Foundation Model Found?" https://arxiv.org/abs/2507.06952 ; 2026 follow-up: https://arxiv.org/abs/2602.06923
- **Huh, Cheung, Wang, Isola** (2024). Platonic Representation Hypothesis. https://arxiv.org/abs/2405.07987
- **Gröger, Wen, Brbić** (2026), critique: https://arxiv.org/abs/2602.14486 ; **Koepke, Zverev, Ginosar, Efros** (2026): https://arxiv.org/abs/2604.18572
- **Jha, Zhang, Shmatikov, Morris** (2025). vec2vec. https://arxiv.org/abs/2505.12540
- **Elhage et al.** (2022). Toy Models of Superposition. https://transformer-circuits.pub/2022/toy_model/
- **Templeton et al.** (2024). Scaling Monosemanticity. https://transformer-circuits.pub/2024/scaling-monosemanticity/
- **Lindsey, Olah, Batson et al.** (2025). On the Biology of a Large Language Model. https://transformer-circuits.pub/2025/attribution-graphs/biology.html
- **Trinh et al.** (2024). AlphaGeometry. https://www.nature.com/articles/s41586-023-06747-5
- **Hubert et al.** (2025). AlphaProof, *Nature*. https://www.nature.com/articles/s41586-025-09833-y
- **Google DeepMind** (2025). Gemini Deep Think IMO gold. https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/
- **ByteDance Seed** (2025). Seed-Prover. https://arxiv.org/abs/2507.23726
- **Math Inc.** (2025). Gauss, strong PNT in Lean. https://github.com/math-inc/strongpnt
- **Terence Tao** and Erdős problems (2025–26). https://www.erdosproblems.com ; reporting: https://the-decoder.com/terence-tao-says-gpt-5-2-pro-cracked-an-erdos-problem-but-warns-the-win-says-more-about-speed-than-difficulty/
- **Udrescu & Tegmark** (2020). AI Feynman. https://arxiv.org/abs/1905.11481
- **Lemos et al.** (2022). Rediscovering orbital mechanics. https://arxiv.org/abs/2202.02306
- **Yang-Hui He** (2017). ML the string landscape. https://arxiv.org/abs/1706.02714 ; review: https://arxiv.org/abs/2006.16623
- **Schut et al.** (2023; *PNAS* 2025). AlphaZero concept transfer. https://arxiv.org/abs/2310.16410
- **Benjamin Lee Whorf** (1956), **Malotki** (1983), **Winawer et al.** (2007). https://plato.stanford.edu/entries/linguistics/ ; Winawer: https://doi.org/10.1073/pnas.0701644104
- **W. V. O. Quine** (1960). *Word and Object*. https://plato.stanford.edu/entries/quine/
- **Ludwig Wittgenstein** (1921, 1953). https://plato.stanford.edu/entries/wittgenstein/
- **Noam Chomsky** (1956, 2023); **Piantadosi** (2023): https://lingbuzz.net/lingbuzz/007180 ; **Kallini et al.** (2024): https://arxiv.org/abs/2401.06416
- **G. W. Leibniz** (1666). Characteristica universalis. https://plato.stanford.edu/entries/leibniz-logic-influence/
- **Hans Freudenthal** (1960). *Lincos*. https://en.wikipedia.org/wiki/Lincos_language
- **Frank Drake, Carl Sagan** (1974). Arecibo message. https://www.seti.org/seti-institute/project/details/arecibo-message
- **De Haro & Butterfield** (2018–19). Dualities and equivalence. https://philsci-archive.pitt.edu/14736/ ; https://arxiv.org/abs/1810.08192
- **Barrett & Halvorson** (2016). Morita equivalence. https://arxiv.org/abs/1506.04675
- **Philip Wadler** (2015). "Propositions as Types." https://homepages.inf.ed.ac.uk/wadler/papers/propositions-as-types/propositions-as-types.pdf
- **Univalent Foundations Program** (2013). *Homotopy Type Theory*. https://homotopytypetheory.org/book/
- **Thomas Hales et al.** (2017). Flyspeck. https://arxiv.org/abs/1501.02155
- **Heule, Kullmann, Marek** (2016). Boolean Pythagorean triples. https://arxiv.org/abs/1605.00723
- **William Thurston** (1994). "On Proof and Progress in Mathematics." https://arxiv.org/abs/math/9404236
- **Chris Anderson** (2008). "The End of Theory," *Wired*. https://www.wired.com/2008/06/pb-theory/
- **Ted Chiang** (2000). "Catching Crumbs from the Table," *Nature* 405. https://doi.org/10.1038/35014679

*Verification note:* the 2024–2026 AI results (IMO 2025, AlphaProof's *Nature* paper, vec2vec, Vafa 2025, the 2026 PRH critiques, the Erdős episodes, Gauss) were checked against primary or near-primary sources during research. Some specific numbers came from secondary reports and are flagged in the text. Several links (Chaitin, Lincos, Piantadosi) point to overviews or preprint servers rather than the journal of record. The reduction of the ZFC-independent Turing machine to under 800 states is from memory and should be checked before a character quotes an exact figure.
