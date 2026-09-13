# Quantum Image Matching — Bachelor's Thesis

> Exploring genuinely quantum (not quantum-*inspired*) algorithms for image template matching under geometric distortion — starting from Grover-accelerated search and classical computer vision foundations, working toward full homography-based matching.

**Status:** In progress — thesis direction finalized, implementation underway. See [Current Direction](#current-direction) below.

---

## Overview

This repository documents my bachelor's thesis work at the intersection of quantum computing and computer vision. The core question: **can a real quantum algorithm — not a classical heuristic borrowing quantum vocabulary — provide a genuine advantage for image template/pattern matching under geometric transformation?**

The project deliberately distinguishes two things that get conflated a lot in quantum machine learning literature:
- **Quantum-inspired methods** — classical algorithms (e.g. particle swarm optimization variants) that borrow quantum *concepts* like entanglement as a metaphor, but run entirely on classical hardware.
- **Real quantum methods** — algorithms whose mechanics depend on actually running a quantum circuit: Grover's algorithm, the quantum Fourier transform, quantum Hadamard edge detection.

This repo focuses exclusively on the second category, applied to a concrete, well-defined problem: template/pattern matching (think "find Waldo," or a camera recognizing a known object from an angle) under increasingly general geometric transformations — translation → rotation → full projective (homography) distortion.

## Current Direction

Building on prior published work in Grover-based quantum image matching (Jiang et al. 2016; Tezuka et al. 2021; a 2024 deterministic-matching variant using Long's algorithm), this thesis targets:

1. **Extending Grover-based matching from simple pixel/pattern search to full homography-distorted template matching** — the published work so far handles translation-only search; homography's 8-parameter continuous space is a genuinely open problem.
2. **Improving the measurement-readout bottleneck** flagged (but only partially solved) in the foundational papers — Grover search returns one probabilistic sample per run, and efficiently recovering a usable match remains an open question.
3. **A rigorous classical-vs-quantum benchmark** — comparing against a real, optimized classical baseline (SIFT/ORB feature matching + RANSAC + homography estimation), not just theoretical complexity claims.

## Repository Structure

```
.
├── 00_quantum_circutes.ipynb                 # Introductory Qiskit notebook: circuits, gates, entanglement basics
├── quantumValut/                              # Obsidian vault — all research notes, literature, and derivations
│   ├── Foundations-Classical/                 # Linear → affine → projective transforms, NCC, feature matching, RANSAC, DLT
│   ├── general notes/                         # Circuit-level fundamentals: entanglement, barren plateaus, encoding,
│   │   │                                      #   phase, measurement, error correction, many-body physics, history
│   │   └── formal methods/
│   │   └── quantum history/
│   ├── quantum algorithms/
│   │   └── grover's algorithm.md              # Core algorithm behind the active thesis direction
│   ├── quantum inspired/
│   │   └── Development and application of QEPSO/   # Literature notes on a quantum-inspired optimizer — early
│   │                                                #   exploration, informed the pivot away from "inspired" methods
│   ├── quantum machine learning/               # Prior exploration — see "Research Journey" below
│   │   ├── Is Quantum Advantage the Right Goal for Quantum Machine Learning/
│   │   ├── Quantum Convolutional NN for Classical Data Classification/
│   │   ├── Quanvolutional Neural Networks/
│   │   └── Variational-Quantum-Circuit.md
│   ├── QUANTUM ML.md
│   └── timeline.md                             # Running log of the project's actual research trajectory
├── README.md
└── requirements.txt
```

> **Note on navigating the vault on GitHub:** the notes use Obsidian's `[[wikilink]]` syntax for cross-referencing, which renders as clickable links inside Obsidian but shows as plain bracketed text on GitHub's markdown viewer. For the fullest experience (backlinks, graph view, working cross-links), clone the repo and open `quantumValut/` as an Obsidian vault. The content itself is fully readable either way.

## Research Journey

This repo reflects an actual evolution in scope, which I've left visible rather than cleaned up, since the reasoning behind the pivot is part of the thesis contribution itself:

1. **Started in quantum machine learning for computer vision** (`quantum machine learning/`, `quantum inspired/`) — reviewing QCNNs, Quanvolutional Neural Networks, and quantum-inspired optimization (QEPSO) as candidate architectures, including hands-on notes on barren plateaus and a fully-parameterized PQC as a possible training target.
2. **Critically re-examined that direction** using Schuld & Killoran's *"Is Quantum Advantage the Right Goal for Quantum Machine Learning?"* as a guiding lens — this surfaced a real problem: much of QML work (including my own early direction) amounts to porting a classical architecture into quantum syntax without exploiting anything intrinsically quantum.
3. **Pivoted toward genuinely quantum methods** (`quantum algorithms/`, `Foundations-Classical/`) — Grover's algorithm, quantum Hadamard edge detection, and QFT-based filtering, applied to a concrete, well-defined classical computer vision problem (template/homography matching) where a real quantum mechanism (not a classical heuristic borrowing quantum vocabulary) has a shot at genuine advantage.

The `quantum machine learning/` and `quantum inspired/` notes are kept as-is rather than deleted — they document real, load-bearing groundwork (particularly the barren-plateau and entanglement-trainability material, which resurfaces in the current direction's discussion of QCNN trainability) and the critical reasoning that led to the current, narrower scope.


## Key Concepts Covered

- **Classical foundations:** the full transformation hierarchy (linear → affine → projective), normalized cross-correlation, SIFT/ORB feature matching, RANSAC, and a from-scratch derivation of homography estimation via the Direct Linear Transform and constrained least squares (eigenvalue problem).
- **Quantum circuit fundamentals:** entanglement, phase, measurement, multi-qubit gating, quantum error correction, dense qubit encoding, and the barren plateau problem.
- **Quantum machine learning for computer vision (prior exploration):** Quantum Convolutional Neural Networks, Quanvolutional Neural Networks, variational quantum circuits, and a quantum-inspired optimizer (QEPSO) — reviewed in depth, including a critical read of *"Is Quantum Advantage the Right Goal for Quantum Machine Learning?"* (Schuld & Killoran) that directly shaped the pivot described above.
- **Quantum image processing (active direction):** Grover's algorithm applied to pattern/template matching, quantum Hadamard edge detection, and QFT-based noise filtering — the literature this thesis builds directly on.


## Acknowledgements

This work has been shaped substantially by discussion and guidance from my thesis advisor, Dr. Harati, whose redirection from architecture-porting (e.g. quantum CNNs) toward genuinely quantum, well-scoped problems (Grover-based search, quantum Hadamard edge detection) set the current direction of this project.


## Contact

Amir Hossein Afshar — Afshar.h.amir@gmail.com — Bachelor's Thesis, Ferdowsi University of Mashhad, 2026