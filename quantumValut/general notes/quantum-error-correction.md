# Quantum Error Correction (QEC)

## Core problem it solves
Qubits are fragile — they suffer **decoherence** from interaction with the environment (stray fields, heat, imperfect control pulses). Unlike classical bits (only flip 0↔1), qubit errors can be continuous: phase errors, amplitude errors, or combinations.

Extra difficulty: you can't just "check" a qubit's state directly — measuring it collapses the state (see [[Von Neumann Measurement]]).


## Core idea
1. **Encode** — one *logical* qubit is spread redundantly across many *physical* qubits (e.g. surface code: ~10–1000+ physical qubits per logical qubit, depending on code distance / error rate).
2. **Syndrome measurement** — periodically measure special *syndrome qubits*. These reveal *whether* and *what kind* of error occurred, **without** revealing (and thus without collapsing) the encoded logical information itself.
   - This relies on measuring error-information subspaces that are orthogonal to the logical information — a clever use of measurement design, not weak measurement per se, but conceptually related to "extract partial info without full collapse."
3. **Correct** — classical control hardware computes the needed correction from the syndrome and applies it (or tracks it virtually).

## What kind of "thing" is QEC?
Not hardware, not an algorithm — it's an **infrastructure / protocol layer**:

| | |
|---|---|
| Hardware | physical qubits, control electronics |
| **QEC** | **protocol layered on top, protects logical info from noise** |
| Algorithm | Grover's, Shor's, QCNNs, etc. — run *using* logical qubits |

You don't "call" QEC inside an algorithm — it runs continuously underneath, IF the machine supports fault tolerance.

## Current state (as of the papers I'm reading)
- Most present-day machines (IBM, Google, etc.) are **NISQ** (Noisy Intermediate-Scale Quantum) — **no full QEC in production**.
- QML/QCNN papers I'm reading generally use raw, noisy physical qubits directly — no logical qubits.
- Full fault-tolerant QEC is still mostly experimental (e.g. Google's "below threshold" results, 2023–2024).

## Relevance to QML (important distinction for thesis)
QEC is **purely protective** — preserves existing quantum information against noise. It does **not** compute anything.

This is a different problem from **gradient computation** in QML training (e.g. via the parameter-shift rule) — see [[Parameter Shift Rule]].

> [!warning] Common misconception
> QEC ≠ a mechanism for backpropagation/gradient descent. They solve unrelated problems.

Indirect connection worth noting: noisier/deeper circuits → less reliable gradient estimates → related to the **barren plateau** problem (see [[Barren Plateaus]]). Better error mitigation/correction on future fault-tolerant hardware *could* improve gradient estimation reliability — but that's a hardware-quality improvement, not QEC repurposed as a computational method.

## Open questions / to look into
- [ ] How does surface code distance scale with logical error rate?
- [ ] What's the current physical-to-logical qubit ratio on real hardware?
- [ ] Any QEC-adjacent techniques used in near-term (NISQ) QML specifically? (error *mitigation* vs error *correction*)

---
**See also:** [[Von Neumann Measurement]] · [[Weak Measurement]] · [[Barren Plateaus]] · [[Parameter Shift Rule]]