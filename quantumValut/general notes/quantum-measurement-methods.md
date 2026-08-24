# Quantum Measurement Methods

## 1. Von Neumann (projective) measurement
"Textbook" measurement. Pick a Hermitian observable $O$ with orthogonal eigenstates $|\lambda_i\rangle$ and eigenvalues $\lambda_i$.

- State **collapses** onto one eigenstate on measurement.
- Outcome probability (Born rule): $P(\lambda_i) = |\langle\lambda_i|\psi\rangle|^2$.
- **Repeatable**: measuring again immediately gives the same outcome.
- Math object: orthogonal projectors $P_i$, with $\sum_i P_i = I$, $P_iP_j=0$ for $i\neq j$.

Example: measuring $\sigma_z$ on a qubit → outcomes $\pm1$, collapsing to $|0\rangle$ or $|1\rangle$. Used in the QCNN paper for binary classification readout.

## 2. POVM (Positive Operator-Valued Measure)
Generalization of von Neumann measurement.

- Set of positive operators $\{E_i\}$, $\sum_i E_i = I$ — **not necessarily orthogonal or projectors**.
- $P(i) = \langle\psi|E_i|\psi\rangle$.
- Can have **more outcomes than the Hilbert space dimension** (impossible for von Neumann).
- Arises naturally when measuring indirectly — e.g. couple system to an ancilla, measure the ancilla projectively, then "forget" it.

- Von Neumann measurement is a **special case** of a POVM (where the $E_i$ are orthogonal projectors)


## 3. Weak measurement
Deliberately **weak coupling** to the system → partial info, minimal disturbance.

- State stays close to original (no full collapse).
- Readout is noisy/imprecise per shot.
- Repeated weak measurements → gradually more info, gradually more disturbance.
- Real, experimentally demonstrated (Aharonov, Albert, Vaidman, 1988) — photons, superconducting qubits, trapped ions, NV centers.
- Used today in **continuous/syndrome measurement for QEC** (see [[Quantum Error Correction]]) and some niche QML (mid-circuit readout, quantum control).

## Comparison

| | Von Neumann | POVM | Weak |
|---|---|---|---|
| Outcomes | ≤ Hilbert space dim | can exceed dim | continuous/noisy |
| State after | collapses to eigenstate | implementation-dependent | barely disturbed |
| Repeatable | yes | not guaranteed | no strict repeatability |

---
**See also:** [[Quantum Error Correction]]