# Reason 2: Extreme Data-Loading and Readout Assumptions

## The "traditional approach" recap
Early QML speedup proofs (e.g., for SVMs, matrix inversion, neural nets) work by speeding up an internal subroutine on a quantum computer, borrowing the "modus operandi" of traditional quantum computing: pick a clean, well-defined subroutine, prove a rigorous asymptotic speedup for it (like Shor's or Grover's algorithms).

## The catch: getting data onto the quantum computer
These proofs typically **assume** classical data is already loaded onto the quantum computer efficiently, and that results can be read out efficiently too. In practice this efficient loading step is a huge unsolved problem — the assumption does a lot of hidden work in the proof. Past comparisons to classical algorithms under these generous assumptions have been challenged (Aaronson's "read the fine print"; Tang's "dequantization" work, which showed a classical algorithm could match a claimed quantum speedup once the same generous data-access assumptions were granted to the classical side too).

## Status check (as of 2026, via live search)
This is **still an open, actively-researched bottleneck**, not a solved problem:
- Quantum RAM (QRAM) — the main proposed data-loading architecture — is still described in current papers as **not realized**: "a realisation of this fundamental building block is still outstanding, since existing proposals require prohibitively many resources for reliable implementations, or are not compatible with current architectures... present approaches cannot be scaled-up, as they do not allow for efficient quantum error-correction."
- Educational material still frames QRAM as something algorithms "quietly assume" rather than something that exists as a working component.
- New QRAM designs are still being proposed in 2026 specifically because the basic building block doesn't yet work at scale.

> **Takeaway:** the "extreme assumptions about data loading" critique from 2022 is not outdated — four years later, the hardware component that would make that assumption realistic still doesn't exist in scalable, error-corrected form.