# 0 — About this paper

**Title:** Quanvolutional Neural Networks: Powering Image Recognition with Quantum Circuits

**Authors:** Maxwell Henderson, Samriddhi Shakya, Shashindra Pradhan, Tristan Cook (QxBranch, Inc.)

**arXiv:** [1904.04767](https://arxiv.org/abs/1904.04767) (2019)

**Published:** *Quantum Machine Intelligence* 2, 2 (2020) — https://doi.org/10.1007/s42484-020-00012-y

## One-line summary

Introduces the **quanvolutional layer**: a convolution-style layer where each
"filter" is a small, fixed, *random* quantum circuit rather than a set of
trained weights — used as a non-linear feature extractor slotted into an
otherwise ordinary classical CNN.

## Why it matters

The core idea isn't "quantum circuits are trained better." It's the opposite: they're **not trained at all**. The paper's bet is that a random quantum circuit can act as a non-linear feature extractor the same way random classical filters and echo state networks already do — but potentially reach a *richer class* of functions than a classical random filter can, because of entanglement.

See → [[../../general notes/random-non-linear-features|Random non-linear features]] for the classical-ML backdrop this paper is leaning on.

## Sub-notes in this folder

1. [[1-design-motivations|Design motivations]] — random features, and why quantum circuits specifically
2. [[2-quanvolutional-filter-definition|Filter definition]] — the formal `Q = d(q(e(u_x)))` pipeline
3. [[3-filter-generation-methodology|Filter generation methodology]] — how one random circuit is actually built
4. [[4-encoding-and-decoding|Encoding & decoding]] — classical data in, scalar out
5. [[5-static-vs-variational-qml|Static vs. variational QML]] — where this paper sits relative to trainable-circuit QML
6. [[6-tested-models-and-results|Tested models & results]] — CNN vs QNN vs Random, what they found

## My reimplementation

Independent PennyLane reimplementation (bachelor's thesis project, not the authors' code) lives in a separate repo:

