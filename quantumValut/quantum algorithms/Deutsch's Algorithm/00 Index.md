---
tags: [quantum, deutsch-algorithm]
---
# Deutsch's Algorithm: Index

Notes built step by step while learning the algorithm. The goal: given a black-box function $f:\{0,1\}\to\{0,1\}$ (the **oracle**), decide whether $f$ is **constant** ($f(0)=f(1)$) or **balanced** ($f(0)\neq f(1)$) with **one** call to the oracle. Classically you need two calls.

## Reading order
**Part 1: the oracle**
1. [[01 Reversible Functions]]: why information loss is a problem, and why quantum oracles must be reversible
2. [[02 Making Any Function Reversible]]: the "keep the inputs, XOR into an extra bit" construction
3. [[03 The Quantum Oracle]]: $U_f$ as a sealed box, kets, operator vs state, product vs entangled, what the inputs are
4. [[04 Unitary and Permutation Matrices]]: why a reversible rule is a legal quantum gate
5. [[05 Oracle on a Superposition]]: one call produces $f(0)$ and $f(1)$ together (and the catch)

**Part 2: phase and the key trick**
6. [[06 Phase: Global vs Relative]]: signs, phases, general form of a qubit state
7. [[07 Eigenstates and Eigenvalues]]: $|+\rangle$, $|-\rangle$ and the gate $X$
8. [[08 Phase Kickback and Phase Oracle]]: the key trick
9. [[09 Putting It Together]]: constant vs balanced as $|+\rangle$ vs $|-\rangle$

**Part 3: finishing the algorithm**
10. [[10 The Hadamard Gate]]
11. [[11 Preparing the Starting States]]
12. [[12 Readout]]
13. [[13 The Full Circuit]]: the whole algorithm and a check of all four functions

14. [[14 Exercises and Quick Answers]]

## Big picture in six lines
- Quantum gates are unitary, so they are reversible, so the oracle must be reversible. The problem hands us $U_f$ as a ready-made reversible box.
- Any $f$ has such a box: keep the inputs and XOR $f$ of them into an extra bit.
- With the extra qubit in $|-\rangle$, the value $f(x)$ turns into a sign $(-1)^{f(x)}$ (phase kickback).
- Feeding $|+\rangle$ to the input puts both signs side by side after one call.
- Constant vs balanced is then $|+\rangle$ vs $|-\rangle$ on the first qubit.
- A final Hadamard turns $|+\rangle\to|0\rangle$ and $|-\rangle\to|1\rangle$, so one measurement gives the answer.

15. [[15 State Tracking Through the Circuit]]: $|\psi_0\rangle$ to $|\psi_4\rangle$ with all the algebra
