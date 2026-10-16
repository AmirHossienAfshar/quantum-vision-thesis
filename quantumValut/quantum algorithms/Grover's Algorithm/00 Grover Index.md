---
tags: [quantum, grover, index]
---
# Grover's Algorithm: Index

Grover's algorithm finds a marked item among $N$ possibilities using about $\frac{\pi}{4}\sqrt{N}$ queries to an oracle, where any classical method needs about $N$. It does this by repeatedly nudging amplitude toward the marked item, without ever "looking inside" the search space. The speedup is **quadratic**, not exponential, and it is provably optimal in the query model.

The whole algorithm in one breath:

1. Prepare the uniform superposition $|s\rangle$.
2. Repeat about $\frac{\pi}{4}\sqrt{N}$ times: apply the **oracle** $O$ (flip the sign of the marked state), then the **diffusion** $D$ (invert every amplitude about the mean).
3. Measure.

Geometrically: the state lives in a 2D plane, starts at a small angle $\theta$ from the "all unmarked" axis, and each round rotates it by $2\theta$ toward the marked state.

## Prerequisites (from the Deutsch notes)
- [[03 The Quantum Oracle]]
- [[04 Unitary and Permutation Matrices]]
- [[08 Phase Kickback and Phase Oracle]]
- [[10 The Hadamard Gate]]

## Reading order
| # | Note | What it covers |
|---|---|---|
| 01 | [[01 The Search Problem and the Oracle Model]] | The problem, the black box, classical cost |
| 02 | [[02 The Uniform Superposition]] | The starting state $\lvert s\rangle$ |
| 03 | [[03 The Oracle as a Phase Flip]] | Marking $w$ with a hidden sign |
| 04 | [[04 The Diffusion Operator]] | Inversion about the mean |
| 05 | [[05 The Two-Dimensional Plane]] | Why everything happens in a plane, and the angle $\theta$ |
| 06 | [[06 Two Reflections Make a Rotation]] | Why each round rotates by $2\theta$ |
| 07 | [[07 How Many Rounds]] | The $\sqrt{N}$ count and the overshoot |
| 08 | [[08 Multiple Solutions and Unknown M]] | Several marked items |
| 09 | [[09 Limits of the Speedup]] | What the speedup does and does not mean |
| 10 | [[10 Building the Oracle from Gates]] | Phase kickback, concrete circuits |
| 11 | [[11 CNOT and Toffoli Gates]] | The gates used above |
| 12 | [[12 Building the Diffusion Operator]] | $D$ from $H$, $X$ and a multi-controlled $Z$ |
| 13 | [[13 The Grover Circuit]] | The complete 3-qubit circuit |
| 14 | [[14 Worked Example N=8]] | Full numeric run with $w = 101$ |
| 15 | [[15 Exercises and Quick Answers]] | Practice with answers |
| 16 | [[16 Clarifications]] | The questions that came up while learning this |

## Notation
| Symbol | Meaning |
|---|---|
| $n$ | number of qubits in the search register |
| $N = 2^n$ | number of items (basis states) |
| $w$ | the marked item (when there is exactly one) |
| $M$ | number of marked items |
| $f(x)$ | the function: $1$ if $x$ is marked, else $0$ |
| $\lvert s\rangle$ | uniform superposition $\frac{1}{\sqrt N}\sum_x \lvert x\rangle$ |
| $\lvert w\rangle$ | the marked state (the answer) |
| $\lvert w^\perp\rangle$ | uniform mix of all unmarked states |
| $O$ | oracle, $O = I - 2\lvert w\rangle\langle w\rvert$ |
| $D$ | diffusion, $D = 2\lvert s\rangle\langle s\rvert - I$ |
| $G = DO$ | one Grover iteration |
| $\theta$ | $\sin\theta = 1/\sqrt{N}$, the starting angle |

## Cheat sheet
- Starting state: $\lvert s\rangle = H^{\otimes n}\lvert 0\rangle^{\otimes n}$
- One round: $G = DO$, a rotation by $2\theta$
- After $k$ rounds the state is at angle $(2k+1)\theta$
- Success probability: $P(w) = \sin^2\big((2k+1)\theta\big)$
- Best number of rounds: $k \approx \frac{\pi}{4}\sqrt{N}$ (or $\frac{\pi}{4}\sqrt{N/M}$ with $M$ solutions)
- Do not run longer: the rotation overshoots and the probability falls again
