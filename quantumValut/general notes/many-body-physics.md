# Many-body physics

"Many-body" means a system made of **many interacting particles** — electrons, atoms, spins, photons, etc. — rather than one or two particles studied in isolation. Many-body physics is the study of what happens when these particles interact.

## Why it's hard

For a single quantum particle, the physics is manageable. Once particles interact, the full quantum state can become **[[entanglement|entangled]]** — particles' properties become correlated in ways that can't be described independently. The amount of information needed to describe the state grows **exponentially** with the number of particles (e.g. ~50 particles can already require more numbers than there are atoms in the universe to describe classically).

This is exactly why quantum computers are attractive here: they can natively represent these entangled states, while classical computers choke on them.

## Typical questions in the field

- What **[[phase]]** is the system in? (e.g. is this material a magnet or not? superconducting or not?)
- Does it have topological order? (relevant to quantum error correction)
- How does **[[entanglement]]** spread through the system over time?

## Relation to entanglement

Many-body physics is the **broader field** — the study of any system with many interacting particles (classical or quantum). Entanglement is one specific, especially important phenomenon that shows up *within* quantum many-body physics; it's a major reason these systems are hard to simulate classically, but it isn't a synonym for the whole field. See [[entanglement]] for more.

## Where this shows up

- [[Quantum Convolutional NN for Classical Data Classification/0-about-paper|QCNN for Classical Data Classification]] — Cong et al.'s prior QCNN work classified quantum many-body states (e.g. detecting phases of matter, error-correcting code states) before this line of work moved to classical data.