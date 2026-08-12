# 1 — Design motivations (Section 2.1)

Two separate observations get merged into this paper's core idea.

## Observation 1: random non-linear features already work classically

Well established in classical ML that you don't always need to *learn* useful features — a fixed, random, non-linear transformation of the input is often already a decent feature extractor. Examples the paper cites:

- **Random convolutional filters** (Jarrett et al., Ranzato et al., Saxe et al.): untrained, randomly-initialized conv filters already produce reasonably useful feature maps
- **Echo State Networks**: a recurrent reservoir with fixed random weights; only the linear readout layer is trained

Full write-up → [[../../general notes/random-non-linear-features|Random non-linear features]]

## Observation 2: quantum circuits can model functions classical circuits can't (efficiently)

Citing Mitarai et al. (2018): quantum circuits can model complex functional relationships — e.g. universal quantum cellular automata — that are infeasible to simulate with polynomial-sized classical resources.

## The merge

> random non-linear projections are already useful in classical ML
> **+**
> quantum circuits can express a richer class of non-linear functions than
> classical circuits (specifically via entanglement)
> **=**
> a *random, untrained* quantum circuit might be an even better free
> non-linear feature extractor than a classical random filter

This is the whole motivation for the quanvolutional layer — it's not about better training, it's about a richer *fixed* feature map.
