# Research dossier: holography, AdS/CFT, and physics as translation

For the fiction team. These are mental models, not a textbook. Each claim carries
one of these tags:

- **[E] Established.** A theorem, a calculation the field agrees on, or an experimental fact.
- **[S] Strong.** Not proven, but backed by a great deal of independent evidence, and most working physicists treat it as true.
- **[C] Conjecture.** An active proposal the field takes seriously, with the evidence still incomplete or contested.
- **[F] Fringe or fiction.** Not supported. Usable in a story only as invention, and should read as invention.

AdS/CFT itself sits at **[S]**. Nobody has proven it in its original form. The
evidence is overwhelming: thousands of independent checks, and exact derivations
in a few simplified cousins. Calling it "proven" is an error. So is calling it
"speculation".

---

## 1. Bottom line

1. **One reality, two complete descriptions [S]:** in AdS/CFT, a universe with gravity, and with one more dimension, is *exactly the same physics* as a quantum system without gravity on its boundary, so neither description is the "real" one and neither is an approximation of the other.
2. **Space is made of entanglement, redundantly encoded [S/C]:** in the cases physicists can compute, the distances and connections of the gravitational interior are set by quantum entanglement on the boundary, and the encoding works like an error-correcting code: every interior region is written several times over, so the interior survives the loss of part of the boundary.
3. **The dictionary is a translation, and the translation is incomplete and sometimes ruinously expensive [S/C]:** physicists know how to translate a lot between the two "languages", but not all of it, and there are serious arguments that translating the deepest interior of a black hole takes exponentially long computation (more than the age of the universe for any real black hole), even though, in principle, the information is all there.
4. **Many exact descriptions of one reality is the norm, not the exception [E/S]:** T-duality, mirror symmetry, electric–magnetic duality and the physics side of the Langlands program all show the same pattern, in which two formalisms that look nothing alike describe identical physics, and a calculation that is impossible in one is easy in the other.
5. **Our universe is not the one where this works best [E]:** AdS/CFT needs a negative cosmological constant, and ours is positive (de Sitter-like), so whether our universe has a holographic description, and where its "boundary" would be, is open research as of 2026 [C].
6. **Holography sets hard limits on information [E/S]:** the most information any region can hold grows with its surface area, not its volume (about one bit per four Planck areas, after a factor of ln 2), and that bound also caps any civilization's storage and computing in a de Sitter universe at roughly 10^122 bits.

---

## 2. The core correspondence

### The holographic principle (the background, 1972–1995)

- **Black holes have entropy proportional to area [E].** Jacob Bekenstein argued
  in 1972–73 that black holes must carry entropy. Stephen Hawking's 1974–75
  discovery that they radiate fixed the coefficient: S = A / 4 in Planck units
  (A is the horizon area, and a Planck length is about 1.6 × 10⁻³⁵ m). This is
  the Bekenstein–Hawking entropy. A solar-mass black hole carries about 10⁷⁷ in
  units of Boltzmann's constant. That is vastly more than the star that made it.
- **The startling part is *area*, not *volume*.** In ordinary physics, entropy
  (roughly, the number of bits needed to specify a system's exact state) scales
  with volume. Twice the box holds twice the stuff. Gravity breaks this. Try to
  pack more information into a region than its surface allows, and the region
  collapses into a black hole whose entropy is set by its area. So the maximum
  information content of *any* region scales with its boundary area [S, and
  widely accepted for gravity in general].
- **'t Hooft (1993) and Susskind (1994–95)** turned this into the
  **holographic principle**: a theory of quantum gravity in a region should be
  describable by degrees of freedom on the region's boundary, about one per
  Planck area. Susskind's paper was titled "The World as a Hologram". The
  metaphor: a hologram is a 2D film that encodes a 3D image. **Raphael Bousso**
  (1999) gave the careful general statement, the *covariant entropy bound*,
  which uses light-sheets rather than naive spatial surfaces [S].
- In 1995 this was a principle with no concrete example. Maldacena supplied one.

### Maldacena 1997: the concrete example

Juan Maldacena's paper ("The Large N Limit of Superconformal Field Theories and
Supergravity", arXiv hep-th/9711200, submitted November 1997, published 1998)
conjectured an exact equivalence:

- **Type IIB string theory on AdS₅ × S⁵** (a 10-dimensional spacetime: five
  dimensions of anti-de Sitter space times a five-dimensional sphere) **is the
  same theory as N = 4 supersymmetric Yang–Mills theory** (a 4-dimensional
  quantum field theory, a souped-up cousin of the theory of quarks and gluons,
  with gauge group SU(N)).
- He arrived at it by looking at a stack of N D3-branes (membranes in string
  theory where open strings end) from two viewpoints. At low energy, one view
  gives the gauge theory living on the branes. The other gives the curved
  spacetime the branes create around themselves. Both describe the same
  object, so they must agree.
- It is one of the most-cited papers in the history of physics.

### What "anti-de Sitter" means, geometrically

- **AdS is spacetime with constant *negative* curvature** (a negative
  cosmological constant). Its spatial slices look like the hyperbolic plane.
  The best picture is **M. C. Escher's *Circle Limit* woodcuts**. The fish are
  all the same size by the disk's own geometry, yet they crowd toward the rim,
  because the rim is infinitely far away when you measure from inside.
- Stack those disks through time and **global AdS is a solid cylinder**. The
  interior is the "bulk", and the cylinder's surface is the "boundary".
- **Light reaches the boundary in finite time, even though the boundary is
  infinitely far away [E].** A massive particle thrown outward always falls
  back, so AdS acts like a box with reflecting walls. That box-like property is
  part of why AdS holography is well-defined. The universe has a clean edge
  where you can set conditions and read off answers.
- **The "conformal boundary"** is the rim, reached by rescaling distances
  ("conformal" means you keep angles and shapes but discard absolute scale).
  The boundary has no particular size. Only shapes and ratios are meaningful
  there. This is why the boundary theory has to be a *conformal* field theory
  (CFT), a theory with no built-in length scale.
- **One fewer dimension:** AdS₅ has 4 space dimensions plus time. Its boundary
  has 3 space dimensions plus time, the same as the ordinary spacetime the
  gauge theory lives in. The S⁵ is a compact extra space that rides along. On
  the boundary side it shows up as an internal symmetry, not as extra
  directions.
- Our universe has a *positive* cosmological constant. That is **de Sitter**
  space, which curves the other way and has no such boundary (see §5).

### The GKPW dictionary (1998)

Steven Gubser, Igor Klebanov and Alexander Polyakov, and independently Edward
Witten (both papers 1998), made the conjecture computable [S]:

- **Fields ↔ operators.** Every field in the bulk (graviton, scalar, gauge field)
  corresponds to a specific observable ("operator") in the boundary theory. The
  bulk graviton corresponds to the boundary's stress-energy tensor, and a bulk
  gauge field to a boundary conserved current.
- **Boundary values ↔ sources.** The value a bulk field approaches at the rim
  acts as a knob (a "source") that you turn in the boundary theory. Then
  *Z_gravity[field → source at boundary] = Z_CFT[source]*: the two theories'
  generating functions are equal.
- **Mass ↔ scaling dimension.** A bulk scalar's mass m sets how its boundary
  operator scales under zoom: Δ(Δ − d) = m²L², where d is the boundary dimension
  and L the AdS radius. Heavier bulk particles map to operators that fall off
  faster with distance.
- **Bulk black hole ↔ boundary at finite temperature [S, well-tested].** A hot
  soup on the boundary *is* a black hole in the bulk. Hawking–Page (1983) found
  a transition in AdS between thermal gas and black hole. Witten (1998)
  identified it with the deconfinement transition of the gauge theory.

### Large N and strong/weak duality: why anyone cares

- The two sides are controlled by two numbers: **N** (the matrix size of the
  gauge group, which sets how many "colours" there are) and the **'t Hooft
  coupling λ = g²N** (how strongly the gauge fields interact).
- **Large N ↔ weak gravity.** N² sets the ratio of the AdS radius to the Planck
  length (L³/G ~ N²). Big N means the bulk is a large, gently curved space where
  quantum-gravity effects are small.
- **Large λ ↔ classical geometry.** L⁴/ℓ_s⁴ = λ, so strong boundary coupling means
  the strings are tiny compared with the curvature, and you can use plain
  Einstein gravity (supergravity) instead of full string theory.
- **The payoff is strong/weak duality [E as a feature of the conjecture].** When
  the boundary theory is strongly coupled, which is the hardest regime in
  quantum field theory, since perturbation theory fails, the bulk is weakly
  curved classical gravity, which is easy (you solve Einstein's equations). It
  runs the other way too: a weakly coupled boundary is an impossibly stringy,
  quantum bulk. *Each side is hard exactly where the other is easy.* That is
  why the two sides almost never contradict each other in practice: when one
  side is tractable, the other usually is not, and checks require quantities
  protected by symmetry, or exact methods.
- **Evidence it is real [E for the checks, S for the conjecture]:**
  - Symmetry groups match exactly (SO(4,2) × SO(6), plus supersymmetry).
  - Thousands of protected quantities agree.
  - **Integrability** lets physicists compute the spectrum of N = 4 SYM at
    *every* coupling and match it to string theory (review: Beisert et al.,
    2010).
  - In the simplified AdS₃/CFT₂ case, Eberhardt, Gaberdiel and Gopakumar (2019)
    *derived* a version of the correspondence.
- **Real-world use [E as calculations, S as applications]:** The ratio of
  viscosity to entropy density, η/s = 1/4π (Kovtun, Son and Starinets, 2004–05),
  came out of a black-hole horizon calculation. The quark–gluon plasma at RHIC
  and the LHC turned out to be close to it. "AdS/CMT" applies similar tools to
  strange metals. These are analogies with real predictive value, not proofs
  that QCD has an exact gravity dual.

---

## 3. The entanglement turn ("it from qubit")

From 2006 onward, the main question changed from "what does the dictionary map?"
to "*what is space made of?*". The answer that emerged: quantum entanglement, and
specifically the structure of a quantum error-correcting code. (The phrase echoes
John Wheeler's 1989 "it from bit". "It from Qubit" became the name of a Simons
Foundation collaboration in 2015.)

- **Ryu–Takayanagi (2006) [S, derived for broad classes of cases by Lewkowycz
  and Maldacena in 2013].**
  - Take a region A of the boundary. Its entanglement entropy with the rest of
    the boundary (how many qubits' worth of correlation link A to its
    complement) equals the area of the minimal surface in the bulk that hangs
    down from A's edges, divided by 4G.
  - S(A) = Area(γ_A) / 4G. It is the Bekenstein–Hawking formula, generalized
    from black-hole horizons to *any* region.
  - Extensions:
    - Hubeny–Rangamani–Takayanagi (2007), for time-dependent cases.
    - Faulkner–Lewkowycz–Maldacena (2013), for quantum corrections.
    - Engelhardt–Wall (2014), the "quantum extremal surface", which became the
      key tool of 2019.
- **Van Raamsdonk, "Building up spacetime with quantum entanglement" (2010)
  [S].**
  - Take two boundary systems whose combined state makes an eternal two-sided
    black hole, connected by a wormhole.
  - Reduce the entanglement between them and the wormhole thins. Remove the
    entanglement entirely and the spacetime pinches off into two disconnected
    pieces.
  - The slogan: *entanglement is the glue that holds space together*.
  - Faulkner, Guica, Hartman, Myers and Van Raamsdonk (2013) showed that
    Einstein's equations, at linear order, *follow from* the first law of
    entanglement on the boundary.
- **ER = EPR, Maldacena and Susskind (2013) [C].** The conjecture is that
  entangled pairs (EPR, after Einstein–Podolsky–Rosen 1935) are connected by
  some kind of wormhole (ER, Einstein–Rosen bridge 1935). For two entangled
  black holes the connection is a smooth, non-traversable wormhole [S]. For a
  pair of entangled electrons it would be a highly quantum "wormhole" with no
  classical geometry. That extension is a slogan, not a calculation [C, and
  contested].
- **Tensor networks and MERA, Swingle (2009, arXiv 0905.1317) [S as a toy
  model].**
  - MERA (Vidal, 2007) is a way to write down a many-body quantum state as a
    layered network, coarse-graining scale by scale.
  - Brian Swingle noticed that the network is a discretized hyperbolic space,
    and that the number of bonds cut by the minimal cut through the network
    reproduces Ryu–Takayanagi.
  - **The radial direction of the bulk is the renormalization-group scale:**
    near the boundary means short distances and high energies. Deep inside
    means long distances and low energies (the "UV/IR connection" [E]).
- **Holographic quantum error correction, Almheiri, Dong and Harlow (2014,
  arXiv 1411.7041) [S].**
  - They resolved a paradox: a bulk operator at the centre can be reconstructed
    from several *different* boundary regions, so it seemed to be in several
    places at once.
  - Their resolution: the bulk-to-boundary map is a **quantum error-correcting
    code**. Bulk ("logical") information is spread non-locally across boundary
    ("physical") qubits so that it survives the erasure of any one region.
  - Their simplest example is the 3-qutrit secret-sharing code: one qutrit of
    secret, stored in three, recoverable from any two.
- **The HaPPY code, Pastawski, Yoshida, Harlow and Preskill (2015, arXiv
  1503.06237) [E as a construction, S as a model].**
  - An explicit code built from "perfect tensors" tiled on a hyperbolic
    pentagon lattice. It reproduces RT and bulk reconstruction.
  - It is the canonical concrete picture: an Escher tiling where every tile is
    a little error-correcting code feeding outward to the rim.
  - Limitations: no dynamics, and it gets some features of real gravity wrong.
- **Entanglement wedge reconstruction, Dong, Harlow and Wall (2016) [S].** A
  boundary region A can reconstruct everything in the bulk region between A and
  its RT surface (its "entanglement wedge"). **Bulk locality is emergent and
  redundant:**
  - A point deep in the bulk lies in the wedges of many different large
    boundary regions, and in none of the small ones.
  - The deeper the point, the more of the boundary you need to recover it.
  - *Depth is a measure of how widely the information has been smeared.*
- **Complexity = volume (Susskind, 2014) and complexity = action (Brown, Roberts,
  Susskind, Swingle and Zhao, 2015) [C].**
  - The interior of a black hole (the wormhole) keeps growing for an
    exponentially long time after the black hole has thermalized, when
    entanglement has stopped changing.
  - Proposal: its volume tracks the *quantum computational complexity* of the
    boundary state, meaning the minimum number of simple operations needed to
    make that state.
  - "Complexity = anything" (Belin, Myers, Ruan, Sárosi and Speranza, 2021)
    found a large family of geometric quantities that behave this way. So the
    proposal is suggestive but not unique.
- **The black hole information problem and the Page curve [S for the 2019
  results].**
  - Hawking (1976) argued that evaporation destroys information, which would
    violate quantum mechanics.
  - Don Page (1993): if the information is preserved, the entropy of the
    radiation must rise, then fall back to zero. The turnover is the "Page
    time", around half-evaporation.
  - AMPS (Almheiri, Marolf, Polchinski and Sully, 2012) sharpened the paradox
    into the "firewall".
  - In **2019**, Penington (arXiv 1905.08255) and Almheiri, Engelhardt, Marolf
    and Maxfield (arXiv 1905.08762) found that after the Page time the quantum
    extremal surface jumps to just inside the horizon. Then Almheiri, Mahajan,
    Maldacena and Zhao (1908.10996) named the region beyond it an **island**.
  - The island is part of the black-hole *interior* that belongs to the
    *radiation's* entanglement wedge. After the Page time, the interior is
    encoded in the radiation that has flown away.
  - In November 2019 two groups derived this from the gravitational path
    integral ("replica wormholes"): Penington–Shenker–Stanford–Yang, and
    Almheiri–Hartman–Maldacena–Shaghoulian–Tajdini.
  - Status: the Page curve can be derived inside semiclassical gravity [S]. What
    the mechanism means in ordinary real-time physics, and how far it extends
    beyond special models, is still debated [C].
  - AdS/CFT is the strongest single argument that information is preserved,
    because the boundary is ordinary unitary quantum mechanics [S].

**The mental model to keep:** bulk space is not a container. It is an emergent,
redundant description of how the boundary's quantum information is entangled.
Distance tracks entanglement. Depth tracks how non-local the encoding is. The
interior of a black hole tracks computational complexity.

---

## 4. The dictionary as a translation problem

This is where the physics touches the "language" half of the seed. It is the
section that most rewards precision.

### Two languages, one reality

- **Bulk and boundary are not two worlds that interact. They are one world
  written in two languages [S].** Any experiment you can describe in one has an
  exact counterpart in the other. A bulk observer who falls into a black hole,
  a gravitational wave crossing AdS, a star forming: each corresponds to some
  intricate pattern of a strongly interacting, hot quantum field theory with no
  gravity at all. A single bulk graviton is a particular collective vibration
  of the boundary. The languages share no vocabulary at the level of
  "particles at locations", because **the boundary has no word for "here" in
  the bulk.** Bulk locality has to be *composed* from boundary phrases.
- Philosophers of physics debate whether such dualities mean the two
  descriptions are the *same theory* or *empirically equivalent different
  theories* (Rickles 2011; de Haro 2017; de Haro and Butterfield). The
  mainstream physicist's stance is "same theory, two presentations". Either
  stance is defensible in a story, provided a character does not present it as
  settled.

### The dictionary is incomplete

- **The forward map is well understood near the boundary [E/S].** HKLL (Hamilton,
  Kabat, Lifschytz and Lowe, 2006) gives explicit "smearing" formulas: a bulk
  field at a point equals a weighted integral of boundary operators over a
  region. Its subtleties (it cannot be state-independent everywhere, and it
  needs corrections from gravitational interactions) are an active topic.
- **We have no full dictionary for general states, for the stringy regime, or
  for the black-hole interior [E that it is unknown].** Bouland, Fefferman and
  Vazirani (2019) put it bluntly: the dictionary "is not well understood" and
  has been computed only on specially structured instances.
- **State dependence [C].** Papadodimas and Raju (2013) argued that the
  operators describing a black hole's interior may depend on which state the
  system is in. That would be an odd property for a dictionary: the meaning of
  a word that depends on the whole conversation so far. It is controversial,
  but taken seriously.

### Translation can be exponentially hard, even when nothing is hidden

- **Harlow–Hayden (2013, "Quantum Computation vs. Firewalls", arXiv 1301.4504)
  [S as an argument].** To verify the firewall paradox, an observer must decode
  the Hawking radiation to find the partner of an outgoing particle. Harlow and
  Hayden argued this decoding is so computationally hard (under standard
  cryptographic assumptions) that it would take exponentially long in the black
  hole's entropy. The black hole evaporates long before. *The paradox may be
  protected by computational complexity.* Physics may be consistent only
  because certain translations can't be completed in time.
- **The Python's Lunch (Brown, Gharibyan, Penington and Susskind, 2019, arXiv
  1912.00228) [C].**
  - They gave a geometric reason for that hardness. When the wormhole between a
    black hole and its radiation has a "bulge", like a python that has
    swallowed something, the cost of decoding grows exponentially in the
    entropy difference between the bulge and its narrow neck.
  - Engelhardt, Penington and Shahbazi-Moghaddam (2021) argued that such
    non-minimal surfaces are *the* source of exponential complexity in the
    dictionary.
  - Akers, Engelhardt, Harlow, Penington and Vardhan (2022, arXiv 2207.06536)
    model the interior as a "non-isometric code". The interior has *more*
    apparent degrees of freedom than the fundamental description. That is
    possible because the extra ones can only be detected by exponentially
    complex operations, which no low-complexity observer can do.
- **Bouland–Fefferman–Vazirani (2019, arXiv 1910.14646) [C, with a precise
  complexity-theory statement].** If wormhole volume tracks complexity, then
  *either* the AdS/CFT dictionary is itself exponentially complex to compute,
  *or* quantum gravity can efficiently compute things quantum computers cannot
  (violating the "quantum extended Church–Turing thesis"). Yoshida (2020) and
  Susskind argued for the first horn: the dictionary is an exponentially
  complex map. **This is the cleanest real-physics hook for the seed. The
  translation between two complete descriptions of one reality can be so
  expensive that, for practical purposes, some truths exist in one language
  and are unreadable in the other.**

### Dualities in general: one reality, many exact descriptions

- **Electric–magnetic duality (Montonen–Olive, 1977) and S-duality [S].** In N = 4
  Yang–Mills, the theory at coupling g is the same as the theory at coupling
  ~1/g, with electric and magnetic charges swapped. Seiberg–Witten (1994)
  solved a related theory exactly using this kind of reasoning.
- **T-duality [E within string perturbation theory].** A string on a circle of
  radius R gives exactly the same physics as one on a circle of radius α'/R
  (α' is set by the string length). Momentum modes on one circle are winding
  modes on the other. "Large" and "small" are not invariant notions. Below the
  string length, distance has no unique meaning.
- **Mirror symmetry [E as mathematics, with physics origins].**
  - Two geometrically different six-dimensional Calabi–Yau spaces give the
    same string physics.
  - In 1991 Candelas, de la Ossa, Green and Parkes used it to *predict* the
    number of rational curves of each degree on the quintic threefold. That was
    a hard problem in enumerative geometry, solved by a calculation on the
    mirror side. It gives 2875 lines and 609,250 conics.
  - Mathematicians' independent computer count of the conics first disagreed.
    They then found an error in their own program, and the physicists'
    number stood. *A translation, done in the "wrong" language, corrected the
    native speakers.*
  - Kontsevich's homological mirror symmetry (1994) recast the duality as an
    equivalence of categories. Proven in many cases, open in general.
- **Langlands and physics [E for the 2024 proof, S for the physics link].** The
  Langlands program is a web of conjectured correspondences between number
  theory and harmonic analysis. Weil called it a "Rosetta stone". Kapustin and
  Witten (2006) showed that the *geometric* Langlands correspondence arises from
  S-duality of N = 4 Yang–Mills compactified on a surface. A proof of the
  (unramified, de Rham) geometric Langlands conjecture by Gaitsgory, Raskin and
  collaborators was announced in 2024: nine authors, around 800 pages. It did
  not go via physics, but physics had predicted the shape of the answer.
- **The pattern to hold:** these are not approximations or analogies. Each is an
  exact equivalence between formalisms that look unrelated. Each is valuable
  *because* a problem hard in one becomes easy in the other. The theme a writer
  can use: **choosing the language you describe reality in decides which truths
  are cheap to reach.** Physicists' experience strongly supports this [S as an
  observation about practice]. It is *not* a claim that reality depends on the
  language.

---

## 5. What is not known: where fiction can legitimately speculate

### Our universe is not AdS

- **Observed: positive cosmological constant, or something like it [E].** The
  universe's expansion is accelerating (1998, Riess, Perlmutter and Schmidt;
  Nobel Prize 2011). The far future of a Λ-dominated universe approaches de
  Sitter space, which has positive curvature, no spatial infinity you can
  signal to, and a cosmological horizon around every observer.
- **DESI (2024, 2025) hints that dark energy is weakening [C].**
  - DESI DR2 (March 2025, arXiv 2503.14738) prefers evolving dark energy over a
    constant Λ at 2.8σ to 4.2σ, depending on which supernova sample is combined.
  - A recalibration of the DES supernovae lowered the top figure to about 3.2σ.
  - Bayesian analyses are more cautious. The case is not closed. If dark energy
    is evolving, the far-future geometry is uncertain.
- **dS/CFT (Strominger, 2001) [C].** Places a Euclidean CFT on the infinite
  future of de Sitter space. The dual theories appear to be non-unitary, and
  there is no working example for our universe. (A higher-spin toy example
  exists: Anninos, Hartman and Strominger, 2011.)
- **Static-patch holography [C].** This puts the degrees of freedom on or near
  the *cosmological horizon* each observer sees (Susskind; Anninos and others).
  Narovlansky and Verlinde (2023, arXiv 2310.16994) proposed double-scaled SYK
  (a solvable quantum many-body model) as a dual for 3D de Sitter. Follow-ups
  through 2025–26 are active. Lecture notes from 2023 (Galante, arXiv
  2306.10141) say plainly that "we still lack a full framework". As of late 2026
  that remains true [E that it is open].
- **Observers as part of the physics [C, very active in 2022–2026].**
  - Chandrasekaran, Longo, Penington and Witten (2022) showed that the algebra
    of observables in de Sitter becomes well-defined, with a finite entropy,
    only once you include an *observer* as a physical system.
  - Harlow, Usatyuk and Zhao (arXiv 2501.02359, JHEP 2026) build on earlier
    arguments that a closed universe's quantum-gravity Hilbert space is
    **one-dimensional**: it has exactly one state. They propose that an
    internal observer restores a rich effective description. A rival
    prescription (Abdalla, Antonini, Iliesiu and Levine) differs in detail.
  - *This is unusually fertile ground for the seed. Current work says that
    for a closed or de Sitter universe, a meaningful physical description may
    require writing the describer into the description.* Treat it as [C], and
    don't let a character claim it is settled.
- **Flat-space holography [C].** Two programs:
  - **Celestial holography** (Strominger, Pasterski and others, from about
    2016): scattering amplitudes in flat spacetime written as correlators of a
    2D CFT on the "celestial sphere" at null infinity.
  - **Carrollian holography** (Donnay, Fiorucci, Herfray and Ruzziconi, 2022):
    a 3D theory living on null infinity.

  Both are research programs, not established dualities.

### Is gravity emergent in our universe at all?

- In AdS, the answer is yes, as far as anyone can tell [S]. In our universe it
  is unknown [C].
- Erik Verlinde's "entropic gravity" (2010) and his 2016 "emergent gravity"
  proposal for dark matter are taken as interesting but unsuccessful or
  unconfirmed by most specialists [C, leaning F for the dark-matter claims].
- Popular claims that "gravity is an illusion, proven" are overstated.

### Experiments

- **The 2022 "wormhole on a quantum computer" (Jafferis, Zlokapa, Lykken,
  Kolchmeyer, Davis, Lauk, Neven, Spiropulu; *Nature* 612, 51, 30 November
  2022):** used 9 qubits of Google's Sycamore processor to run a teleportation
  protocol with the signature of traversable-wormhole dynamics in a learned,
  heavily simplified SYK-like model.
  - [E] that the experiment ran and matched its model.
  - [C, contested] that it probed holographic dynamics in any meaningful sense.
  - Kobrin, Schuster and Yao (arXiv 2302.07897, February 2023) showed the
    learned Hamiltonian's terms all commute, and argued that it does not behave
    like a gravitational system. Independent experts quoted by *Quanta* found
    the critique compelling.
  - The press framing, "physicists created a wormhole", was wrong. **No
    spacetime was created.** It was a quantum simulation of a toy model whose
    dual, *if* it had one, would include a wormhole.
- **Analog systems [E as engineering, not tests of quantum gravity].** These
  emulate the *mathematics* of holography; they do not test whether our
  universe is holographic. Examples:
  - Hyperbolic lattices in circuit QED (Kollár, Fitzpatrick and Houck, *Nature*
    2019).
  - Tensor-network simulations.
  - Small-scale quantum simulations of SYK.
- **Fermilab "Holometer" (2014–15) [E null result].** Searched for "holographic
  noise" in spacetime and found none at its sensitivity. The model it tested
  was never mainstream holography.

### The swampland

- **The swampland program (Vafa, 2005) asks which low-energy theories can arise
  from consistent quantum gravity [C].** The rest are "the swampland".
- The **de Sitter conjecture** (Obied, Ooguri, Spodyneiko and Vafa, 2018) holds
  that stable de Sitter vacua cannot exist in quantum gravity, so dark energy
  would have to evolve [C, and strongly disputed]. KKLT (2003) argued the
  opposite.
- Swampland proponents have read DESI's hints as supporting evidence [C].

### Grading for fiction

- **Safe to state as fact:** that AdS/CFT exists and is very well-tested; RT;
  the error-correcting-code picture as a property of AdS/CFT; the Page curve
  from islands in model calculations; the 2022 experiment and its critique; the
  Bekenstein–Hawking formula; that our universe is not AdS.
- **Safe as an open question characters argue over:** de Sitter holography,
  ER=EPR in full generality, complexity=volume, observer-dependent
  descriptions, the swampland, evolving dark energy.
- **Fiction must own it as invention:**
  - a working dS dictionary;
  - a measured holographic signature in our universe;
  - sending signals "to the boundary";
  - a machine or AI that *completes* exponential-complexity decoding of a real
    black hole (that would need either new physics or a violation of
    complexity-theoretic beliefs);
  - entangled particles as usable wormholes for messages.

---

## 6. Common misconceptions a writer will make

1. **"The universe is a hologram" or "we are a 2D projection".** Holography does
   not say the bulk is fake or that the boundary is more real. Both are
   complete, and the dimension count is not a fact about reality. It is a
   fact about which description you use. In addition, the clean version is
   about AdS, which is not our universe.
2. **"The boundary is a wall or membrane somewhere far away."** The AdS boundary
   is at infinite distance and is a *conformal* limit, not a place you can
   travel to. It has no thickness, and no one stands on it. Even in proposals
   that put a "screen" at a cosmological horizon, the horizon is
   observer-dependent: each observer has their own.
3. **"Information is stored on a surface like data on a hard drive."** It is not
   stored locally at all. The encoding is massively non-local and redundant
   (error-correcting). The area law is a *bound on how much*, not a statement
   about *where*. No patch of boundary "holds" the cat.
4. **"The duality is an approximation that works in some limit."** The
   conjecture is an exact equivalence. Practical *calculations* use limits
   (large N, strong coupling) because each side is tractable only there. The
   classical-gravity description is the approximation. The equivalence isn't.
5. **"AdS/CFT is proven" or "AdS/CFT is a wild guess."** Neither. See the
   opening of this document: [S].
6. **"Entanglement lets you send messages or travel through wormholes."**
   Entanglement alone cannot transmit signals (the no-signalling theorem, [E]).
   ER=EPR wormholes are non-traversable. Gao–Jafferis–Wall (2016) traversable
   wormholes need a direct coupling between the two sides and never beat the
   ordinary route: you cannot get anywhere faster than light.
7. **"Gravity is just entanglement, proven."** It is shown at linearized order
   in AdS with specific assumptions [S]. In general it is not.
8. **"The 2022 experiment made a wormhole."** No (see §5).
9. **"The extra dimension is a hidden spatial direction you could point to."**
   The radial direction is *emergent*. On the boundary it corresponds to energy
   scale, or to how coarse-grained you are. It is not an extra place.
10. **"N = 4 Yang–Mills is the Standard Model."** It is a highly symmetric cousin
    with no confinement and no ordinary particles. Results carry over
    qualitatively at best.
11. **"Holography is string theory, so it's untestable."** The *framework* uses
    string theory, but RT, the code structure and the Page curve have been
    studied in models that need no strings (JT gravity, SYK). The tools are now
    used across quantum information and condensed matter.

---

## 7. Story-usable images and mechanics

Each image is followed by the point where the metaphor breaks.

1. **Space as the redundancy of a code.** The interior of the universe is what
   an error-correcting code "looks like from inside": the more protected and
   widely smeared a piece of information is, the deeper it sits.
   - *Bends to:* a character thinking of a place as robust because it is
     encoded everywhere.
   - *Breaks if:* you say deleting one region of boundary deletes the matching
     region of space (only deep enough erasures matter, and then they remove
     the deep bulk first), or that our own space has been shown to be a code.
2. **Distance is a measure of entanglement.** Two regions are close because they
   share a lot of entanglement. Disentangle them and the space between them
   stretches and tears (Van Raamsdonk's pinch-off).
   - *Bends to:* a relationship or conversation metaphor, done explicitly as
     metaphor.
   - *Breaks if:* entangling two lab objects makes them physically closer.
     That doesn't happen in our universe.
3. **The radial direction is zoom.** Moving inward is moving from fine detail to
   coarse summary, like a mipmap or a summary of a summary. The deepest bulk is
   the most compressed, long-wavelength description. This is renormalization.
   - *Bends to:* a story about reading text at different levels of
     abstraction, or a model's layers. Treat the layers analogy as analogy: a
     network's layers are not literally a holographic bulk [F as a literal
     claim].
   - *Breaks if:* you treat it as an extra spatial place you can go to.
4. **A black hole interior that exists only as a hard computation.** After the
   Page time the interior is encoded in the radiation that has escaped, but
   reading it out takes exponentially many steps. The interior is "there"
   exactly as much as the solution to an intractable problem is.
   - *Bends to:* the strongest image for the seed. Truth that is fully present
     in a description yet out of reach.
   - *Breaks if:* someone actually decodes a real astrophysical black hole.
     For a solar-mass black hole the exponent is about 10⁷⁷ (in natural log
     units), and no amount of AI changes that number.
5. **The wormhole that keeps growing.** A two-sided black hole's interior grows
   linearly for a time exponential in its entropy. That tracks the growing
   complexity of the quantum state long after everything measurable has
   settled [C].
   - *Bends to:* "the system looks finished from outside but is still getting
     more intricate inside". An image of a mind, a language, a relationship.
   - *Breaks if:* the growth is read as anything visible or usable from outside.
6. **Two languages that cannot both be easy.** Whenever one description is
   simple (weakly coupled), its dual is fiendish (strongly coupled), and vice
   versa.
   - *Bends to:* translation between a child's language and an adult's, or
     between a person and an AI. Each can say easily what the other can say
     only with great effort.
   - *Breaks if:* a character claims the duality *forbids* both from being easy
     in every case. Protected quantities are easy on both sides.
7. **The mirror counted the curves first.** Physicists' calculation in the mirror
   language corrected mathematicians' direct count, which had a bug in its code
   (true history, 1991). A good small anecdote for a character to tell, and
   exact.
8. **The island.** After a black hole is half evaporated, part of its inside
   "belongs" to the radiation scattered across the universe. The owner of the
   inside changes hands at the Page time [S in models].
   - *Bends to:* inheritance, ownership of memories, a diary now readable only
     by someone else.
   - *Breaks if:* someone treats the island as a place you can visit from
     outside.
9. **The universe with one state.** Current research suggests a closed universe,
   described from nowhere, has exactly one quantum state. Rich physics appears
   only relative to an observer inside it [C].
   - *Bends to:* "a description needs a describer", which matches the seed's
     language-and-AI theme directly.
   - *Breaks if:* stated as proven, or as consciousness creating reality. The
     "observer" in these papers is a physical clock-and-memory system, not a
     mind [F if mystical].
10. **The Escher rim.** All the fish are the same size. It's the language of the
    rim that makes them look crowded. A child could understand this
    picture.
    - *Breaks if:* you call the edge a place to visit.

---

## 8. Scale and time

### Horizons

- **Cosmological event horizon [E].** In a universe dominated by Λ, there is a
  maximum distance from which light emitted now will ever reach us. Today it is
  roughly 16 billion light-years (proper distance). In the asymptotic de Sitter
  future it settles near c/H_∞, about 16–17 billion light-years, if Λ is truly
  constant.
- **Galaxies beyond it are fading from causal contact [E].** In ~100 billion
  years, everything outside the Local Group's merged galaxy will have
  redshifted beyond observation. Future astronomers would infer a static island
  universe (Krauss and Scherrer, 2007).
- **The horizon has a temperature and an entropy [S].** Gibbons and Hawking
  (1977) found that the de Sitter horizon radiates at T = ħH/2πk ≈ 2 × 10⁻³⁰ K for
  our Λ. Its entropy is A/4 ≈ 10¹²² (in Boltzmann units). That is the largest
  entropy our observable universe can ever have, and in static-patch proposals
  it is the number of the "boundary" degrees of freedom [C].
- **The de Sitter horizon as our "boundary" [C].** It is a candidate, but it
  differs from the AdS boundary in three ways:
  - it is at finite distance;
  - it is observer-dependent;
  - nothing on it can be set or read like an AdS boundary.
- **If dark energy evolves (DESI), all of the above changes [C].** The horizon
  might grow or vanish, depending on the model.

### Heat death and Boltzmann brains

- **Heat death [E as the ΛCDM projection].** Stars stop forming by about 10¹⁴
  years. Then come black-hole-dominated eras, then evaporation: a solar-mass
  black hole lasts ~10⁶⁷ years, and the largest ~10¹⁰⁰. What remains is cold
  near-vacuum at the de Sitter temperature.
- **Boltzmann brains [C as a problem, not a prediction].** In an eternal de
  Sitter space with a finite temperature, thermal fluctuations would eventually
  assemble anything, including a brain with false memories. This would happen
  far more often than real observers evolve. Dyson, Kleban and Susskind (2002)
  and Albrecht and Sorbo (2004) treat this as a *reductio*, a sign that
  something in the assumptions is wrong:
  - de Sitter is not eternal;
  - the static patch is not really thermal;
  - or the counting is wrong.

  It is a puzzle, not a forecast.
- **Recurrence [C].** With finite entropy ~10¹²², a static patch would have a
  Poincaré recurrence time of order e^(10¹²²). That is used in arguments about
  whether eternal de Sitter is even consistent (the swampland folks say no).

### Limits on computation and storage

- **Bekenstein bound (1981) [S].** The entropy of a system of energy E and radius
  R is at most 2πkRE / ħc. Weakly gravitating systems sit far below it.
- **Holographic bound [S].** No region holds more than A/4 (Planck units) of
  entropy, about 10⁶⁹ bits per square metre of bounding area. Any civilization
  confined to a region, however advanced, is capped by its boundary area.
- **Landauer (1961) [E, verified experimentally since 2012].** Erasing one bit
  costs at least kT ln 2 of energy, about 3 × 10⁻²¹ J at room temperature. Cold
  computing is cheaper, which is why Dyson (1979) imagined "eternal
  intelligence" slowing as the universe cools. Krauss and Starkman (2000)
  argued that a Λ universe allows only finite total computation, because of the
  horizon [S given constant Λ].
- **Bremermann's limit (1962) [S].** About 1.36 × 10⁵⁰ bits per second per
  kilogram, from E = mc² and quantum uncertainty.
- **Lloyd's "ultimate laptop" (2000, *Nature* 406, 1047) [E as a calculation].**
  - A 1 kg, 1 litre computer can do at most ~5 × 10⁵⁰ operations per second.
    That follows from the Margolus–Levitin theorem: the operation rate is
    bounded by energy.
  - It can store about 10³¹ bits, limited by entropy, as matter at around a
    billion kelvin.
  - Compress it to a black hole and it becomes the densest possible memory,
    but it evaporates in far less than a femtosecond.
  - Lloyd (2002) estimated the whole observable universe has performed ~10¹²⁰
    operations on ~10⁹⁰ bits, or 10¹²⁰ bits counting gravitational degrees of
    freedom. Note the coincidence with the de Sitter entropy.
- **The bound that matters for "AI that represents the universe" [S/C]:** a
  model of the universe built inside the universe, by any agent in a de Sitter
  patch, cannot contain more than ~10¹²² bits. And the parts of reality encoded
  in exponential-complexity form (black-hole interiors, possibly much else) are
  out of reach even with all of it. A complete internal model is ruled out on
  information grounds alone.

---

## 9. Key people and sources

- **Jacob Bekenstein** (1972–73): black-hole entropy ∝ area. [Phys. Rev. D 7, 2333 (1973)](https://doi.org/10.1103/PhysRevD.7.2333). Bekenstein bound 1981.
- **Stephen Hawking** (1974–76): black-hole radiation; the information paradox. [Commun. Math. Phys. 43, 199 (1975)](https://doi.org/10.1007/BF02345020).
- **Gerard 't Hooft** (1993): first statement of the holographic principle. [gr-qc/9310026](https://arxiv.org/abs/gr-qc/9310026).
- **Leonard Susskind** (1994): "The World as a Hologram". [hep-th/9409089](https://arxiv.org/abs/hep-th/9409089). Later complexity=volume: [1402.5674](https://arxiv.org/abs/1402.5674).
- **Raphael Bousso** (1999, review 2002): covariant entropy bound. [hep-th/0203101](https://arxiv.org/abs/hep-th/0203101).
- **Juan Maldacena** (1997): AdS/CFT. [hep-th/9711200](https://arxiv.org/abs/hep-th/9711200). With Susskind, ER=EPR (2013): [1306.0533](https://arxiv.org/abs/1306.0533).
- **Gubser, Klebanov, Polyakov** (1998): dictionary. [hep-th/9802109](https://arxiv.org/abs/hep-th/9802109).
- **Edward Witten** (1998): dictionary, and black holes as deconfinement. [hep-th/9802150](https://arxiv.org/abs/hep-th/9802150). With Kapustin, Langlands from S-duality (2006): [hep-th/0604151](https://arxiv.org/abs/hep-th/0604151).
- **Shinsei Ryu and Tadashi Takayanagi** (2006): entanglement = minimal area. [hep-th/0603001](https://arxiv.org/abs/hep-th/0603001).
- **Mark Van Raamsdonk** (2010): spacetime from entanglement. [1005.3035](https://arxiv.org/abs/1005.3035).
- **Brian Swingle** (2009): MERA as holography. [0905.1317](https://arxiv.org/abs/0905.1317).
- **Almheiri, Dong, Harlow** (2014): bulk locality as quantum error correction. [1411.7041](https://arxiv.org/abs/1411.7041).
- **Pastawski, Yoshida, Harlow, Preskill** (2015): HaPPY code. [1503.06237](https://arxiv.org/abs/1503.06237).
- **Dong, Harlow, Wall** (2016): entanglement wedge reconstruction. [1601.05416](https://arxiv.org/abs/1601.05416).
- **Daniel Harlow and Patrick Hayden** (2013): decoding radiation is computationally hard. [1301.4504](https://arxiv.org/abs/1301.4504). Harlow's review "Jerusalem Lectures on Black Holes and Quantum Information" (2014): [1409.1231](https://arxiv.org/abs/1409.1231).
- **Almheiri, Marolf, Polchinski, Sully** (2012): firewalls. [1207.3123](https://arxiv.org/abs/1207.3123).
- **Brown, Roberts, Susskind, Swingle, Zhao** (2015): complexity = action. [1509.07876](https://arxiv.org/abs/1509.07876).
- **Geoff Penington** (2019): Page curve from entanglement wedge reconstruction. [1905.08255](https://arxiv.org/abs/1905.08255).
- **Almheiri, Engelhardt, Marolf, Maxfield** (2019): same result, independently. [1905.08762](https://arxiv.org/abs/1905.08762).
- **Almheiri, Mahajan, Maldacena, Zhao** (2019): islands. [1908.10996](https://arxiv.org/abs/1908.10996). Review "The entropy of Hawking radiation" (2020): [2006.06872](https://arxiv.org/abs/2006.06872).
- **Brown, Gharibyan, Penington, Susskind** (2019): the Python's Lunch. [1912.00228](https://arxiv.org/abs/1912.00228).
- **Bouland, Fefferman, Vazirani** (2019): dictionary may be exponentially complex. [1910.14646](https://arxiv.org/abs/1910.14646).
- **Akers, Engelhardt, Harlow, Penington, Vardhan** (2022): interior as a non-isometric code. [2207.06536](https://arxiv.org/abs/2207.06536).
- **Candelas, de la Ossa, Green, Parkes** (1991): mirror symmetry counts curves. [Nucl. Phys. B 359, 21](https://doi.org/10.1016/0550-3213(91)90292-6).
- **Andrew Strominger** (2001): dS/CFT. [hep-th/0106113](https://arxiv.org/abs/hep-th/0106113). Celestial holography review (Pasterski, Pate, Raclariu, 2021): [2111.11392](https://arxiv.org/abs/2111.11392).
- **Chandrasekaran, Longo, Penington, Witten** (2022): de Sitter observables need an observer. [2206.10780](https://arxiv.org/abs/2206.10780).
- **Narovlansky, Verlinde** (2023): DSSYK and de Sitter. [2310.16994](https://arxiv.org/abs/2310.16994).
- **Harlow, Usatyuk, Zhao** (2025): closed universes and observers. [2501.02359](https://arxiv.org/abs/2501.02359).
- **Galante** (2023): lecture notes on de Sitter holography. [2306.10141](https://arxiv.org/abs/2306.10141).
- **Jafferis et al.** (2022): wormhole-dynamics simulation. [Nature 612, 51](https://www.nature.com/articles/s41586-022-05424-3). Critique: Kobrin, Schuster, Yao [2302.07897](https://arxiv.org/abs/2302.07897). Quanta coverage: [2022](https://www.quantamagazine.org/physicists-create-a-wormhole-using-a-quantum-computer-20221130/), [2023](https://www.quantamagazine.org/wormhole-experiment-called-into-question-20230323/).
- **Obied, Ooguri, Spodyneiko, Vafa** (2018): de Sitter swampland conjecture. [1806.08362](https://arxiv.org/abs/1806.08362).
- **DESI collaboration** (2025): DR2 cosmology. [2503.14738](https://arxiv.org/abs/2503.14738).
- **Seth Lloyd** (2000): ultimate physical limits to computation. [quant-ph/9908043](https://arxiv.org/abs/quant-ph/9908043). Computational capacity of the universe (2002): [quant-ph/0110141](https://arxiv.org/abs/quant-ph/0110141).
- **Krauss and Starkman** (2000): life and computation in an accelerating universe. [astro-ph/9902189](https://arxiv.org/abs/astro-ph/9902189).
- **Dyson, Kleban, Susskind** (2002): disturbing implications of a cosmological constant. [hep-th/0208013](https://arxiv.org/abs/hep-th/0208013).
- **Accessible reading:**
  - Susskind, *The Black Hole War* (2008).
  - *Quanta Magazine*'s holography and "It from Qubit" coverage, e.g. ["How Space and Time Could Be a Quantum Error-Correcting Code"](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103/) (2019).
  - Harlow's "TASI Lectures on the Emergence of Bulk Physics in AdS/CFT" (2018): [1802.01040](https://arxiv.org/abs/1802.01040).
  - Stanford Encyclopedia of Philosophy, "Quantum Gravity" and "Philosophy of Cosmology" entries, for the philosophical framing of dualities.

*Verification note:* I checked the 2019 Page-curve papers, the Python's Lunch,
Bouland–Fefferman–Vazirani, the 2022 wormhole paper and its critique, DESI DR2's
significances, the de Sitter holography status, Narovlansky–Verlinde and
Harlow–Usatyuk–Zhao against arXiv and journal listings in October 2026. The other
citations are standard and well known in the field, but their arXiv numbers come
from memory, so spot-check any number before it appears in the prose.
