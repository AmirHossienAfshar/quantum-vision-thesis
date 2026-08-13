# Particle vs. qubit

These are related but **not the same thing** — one is a physics concept, the other is a computing concept.

- **Particle** — a physical object (electron, atom, spin, photon) that exists in an experiment or material. This is *physics-framing*: it describes what the thing *is*.
- **Qubit** — the basic unit of information in a quantum computer. It's *computing-framing*: it describes what role the thing *plays*, not what it physically is.

A qubit is often **implemented using** a particle (e.g. an electron's spin, a photon's polarization, a superconducting circuit) — but "qubit" refers to the computational role, while "particle" refers to the physical object.

## How they relate in practice

When many-body physics (see [[many-body-physics]]) is studied *using* a quantum computer — as in QCNN work — each physical particle in the system typically gets **mapped onto** one qubit. So in that specific setting, particle ≈ qubit. But this is a **modeling choice for a given system**, not a general rule that particle and qubit are interchangeable terms.

## Where this shows up

- [[Quantum Convolutional NN for Classical Data Classification/0-about-paper|QCNN for Classical Data Classification]] — Cong et al.'s many-body states are represented as qubits going into the QCNN circuit.