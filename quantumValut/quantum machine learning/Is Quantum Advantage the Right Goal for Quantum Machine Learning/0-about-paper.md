---
title: "Is Quantum Advantage the Right Goal for Quantum Machine Learning?"
type: perspective
authors: [Maria Schuld, Nathan Killoran]
affiliation: Xanadu, Toronto
journal: PRX Quantum
citation: "PRX Quantum 3, 030101 (2022)"
doi: 10.1103/PRXQuantum.3.030101
tags: [quantum-machine-learning, quantum-advantage, perspective, meta-science]
---

## One-line thesis
Machine learning may be one of the *hardest* domains in which to prove a real quantum advantage, because classical ML is already extremely strong and messy/unstructured, while the proof tools quantum computing has (asymptotic speed-ups on structured problems) don't transfer well to it — the field should consider research questions other than "does quantum beat classical."

## Table I — Quantum-friendly problems vs. real ML problems

| Property | Problems QC is typically good at | Problems ML actually solves |
|---|---|---|
| Classical performance | Low (chosen to be classically hard) | High (industrial-scale, near-linear time algorithms) |
| Input size | Small (limited by near-term qubit counts) | Huge (millions of parameters/entries) |
| Problem structure | Highly structured / periodic (exploitable via interference) | "Messy," human-domain, hard to formalize |
| Theoretical accessibility | High (chosen *because* we can reason about them) | Shifting (deep learning is upending theory) |
| Evaluating performance | Computational complexity / asymptotic scaling | Empirical benchmarks |


## Five concrete reasons ML is a uniquely hard QML target
1. ML baselines are already extremely strong in practice.
2. Real ML inputs are huge — hard to load onto near-term quantum hardware.
3. Real-world data is "messy" — not the clean, structured problems quantum
   algorithms are usually designed around.
4. ML theory itself is currently being rewritten (deep learning), so there's
   no stable ground truth to benchmark quantum methods against.
5. We have very few reliable ways to empirically benchmark QML models at
   realistic problem scales.

## Structure covered in these notes
This vault section covers **Sections I–III** of the paper only (the "problem" half):
- Section II — why machine learning is a fundamentally hard target for quantum speedup claims
- Section III — a critical dissection of how "quantum advantage" claims are currently made, and why the authors think they're structurally weak

**Not covered here:** Section IV (the paper's constructive half — quantum perceptrons, quantum kernels, quantum gradients as examples of advantage-agnostic research) and Section V (moving forward / conclusion). Add separate notes for those if revisited later.
