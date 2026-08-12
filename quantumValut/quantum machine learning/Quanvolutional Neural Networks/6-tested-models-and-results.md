# 6 — Tested models & results (Section 3.2)

## Three models compared, on MNIST

1. **CNN MODEL** — purely classical baseline:
   `CONV1(5x5,50) - POOL1 - CONV2(5x5,64) - POOL2 - FC1(1024, dropout .4) - FC2(10)`
2. **QNN MODEL** — one quanvolutional layer prepended, rest identical to CNN:
   `QUANV1 - CONV1 - POOL1 - CONV2 - POOL2 - FC1 - FC2`
   — number of quanvolutional filters swept from 1 to 50
3. **RANDOM MODEL** — same architecture as QNN, but the first transform is a **purely classical random non-linear transformation** instead of a quantum circuit

## Why the Random model is the important one

This is the control condition — the only way to separate two different possible explanations for any observed benefit:
- (a) "any fixed random non-linear projection helps, regardless of what generates it" (the classical random-features story, see [[../../general notes/random-non-linear-features|note]])
- (b) "something *specific to quantum circuits* (entanglement, richer function class) is doing extra work beyond what a classical random transform could do"

Without this control, seeing "QNN beats CNN" alone would be uninformative — (a) alone could fully explain it.

## Headline result (per abstract)

QNN models showed **both higher test accuracy and faster training** than the purely classical CNN. (Need to go back and check specifically how QNN compared against the Random model, not just against plain CNN — that's the comparison that actually tests claim (b) above; note to self to re-read Section 4 results carefully for this.)

