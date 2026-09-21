# Reason 4: Small-Scale Empirical Benchmarks Are Shaky

## The setup
Some QML papers skip theoretical proofs entirely and just run a quantum model on real data (e.g., MNIST-style datasets), measuring empirical accuracy against a classical baseline. This is a *different* kind of evidence from the artificially-structured proofs discussed in note 4 — no reverse-engineered dataset involved, just real data on constrained hardware.

## Why the authors are still cautious
Current quantum hardware can only handle a handful of qubits, so these experiments necessarily run on **very small datasets** (small subsets or heavily compressed versions of things like MNIST). This creates several compounding problems:

- Hard to tell if a reported "win" is a genuine structural quantum advantage, or just an artifact of which classical model was chosen for comparison (a weak/poorly-tuned baseline flatters the quantum result), or how hyperparameters happened to be tuned.
- Circuit designs used are often **ad hoc** (built by trial and error, not derived from theory) — small architecture tweaks can swing results significantly, so results may not be robust.
- Very few studies attempt to **reproduce** each other's results, so reliability of individual findings is largely unknown.
- We have very little idea how any small-scale result will **scale up** to realistic problem sizes — the tiny regime where experiments are currently feasible might behave nothing like a larger, practically relevant regime.

> **This is where an "I read a paper that used MNIST and got a result" example belongs** — such results are not "artificially structured" in the discrete-log sense (note 4), but they fall squarely into this small-scale/cherry-picked/unreproduced-benchmark critique instead.