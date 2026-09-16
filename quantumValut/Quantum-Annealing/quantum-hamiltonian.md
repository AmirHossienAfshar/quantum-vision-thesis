---
tags: [quantum-computing, quantum-mechanics, foundations, thesis-core]
status: foundation
related:
  - "[[adiabatic-theorem]]"
  - "[[qubo-explained]]"
  - "[[ising-model-and-qubo]]"
  - "[[quantum-annealing-overview]]"
  - "[[annealing-hardware-details]]"
---

# The Quantum Hamiltonian

> This note is broader than annealing specifically — the Hamiltonian is the central object of quantum mechanics generally, and shows up identically whether done annealing, gate-model circuits, VQE, or QAOA. [[adiabatic-theorem]], [[qubo-explained]] (Section 18), and [[annealing-hardware-details]] all lean on the concept defined here rather than re-deriving it.

## One-line definition
The **Hamiltonian** $H$ is the operator (mathematically: a matrix) representing the **total energy** of a quantum system. Its eigenvalues are every possible energy the system could be measured to have; its eigenvectors are the corresponding states.

## Why "operator that measures energy" is the right way to say it

In quantum mechanics, physical quantities you can measure (energy, position, spin, momentum) are each represented by their own operator — energy's operator is specifically called the Hamiltonian. For a Hamiltonian $H$ and a state $|\psi\rangle$:

$$
H|\psi_n\rangle = E_n|\psi_n\rangle
$$

This is an eigenvalue equation, structurally identical to the $A^TA\mathbf{h}=\lambda\mathbf{h}$ eigenvalue problem already worked through in [[computing-homography]] — same mathematical object (find eigenvectors/eigenvalues of a matrix), completely different context. Here, $|\psi_n\rangle$ is an **energy eigenstate** (a state with a definite, well-defined energy) and $E_n$ is the actual energy value you'd get if you measured the system while it was in that state. A general quantum state doesn't have to be a clean eigenstate — it can be a superposition of several energy eigenstates at once — but measuring its energy will always return one of the $E_n$ values, never anything in between.

**The lowest $E_n$ is called the ground state energy**, and its eigenvector is the **ground state** — this is exactly the object [[adiabatic-theorem]] cares about tracking throughout the anneal. Every $E_n$ above that is an **excited state**.

## A single-qubit example

The simplest nontrivial Hamiltonian is built from a **Pauli operator**. For a single qubit, the Pauli-Z operator is the $2\times2$ matrix:

$$
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

Its eigenvectors are exactly the computational basis states $|0\rangle = \begin{pmatrix}1\\0\end{pmatrix}$ and $|1\rangle = \begin{pmatrix}0\\1\end{pmatrix}$, with eigenvalues $+1$ and $-1$ respectively — check directly: $Z|0\rangle = (+1)|0\rangle$, $Z|1\rangle = (-1)|1\rangle$. If you set $H = Z$, then "measuring the energy" of a qubit sitting exactly in state $|0\rangle$ always returns $+1$; sitting in $|1\rangle$ always returns $-1$.

**This is precisely why [[qubo-explained]]'s Section 18 replaces the classical spin $s_i \in \{-1,+1\}$ with the Pauli-Z operator $Z_i$** — $Z$'s eigenvalues are *literally* $+1$ and $-1$, so it's the natural quantum stand-in for a classical spin variable; measuring $Z_i$ on qubit $i$ returns exactly the spin value $s_i$ would have held classically.

## Building up multi-qubit problem Hamiltonians

An Ising-style energy function ([[ising-model-and-qubo]]), $E(\mathbf{s}) = -\sum_{i<j}J_{ij}s_is_j - \sum_i h_i s_i$, becomes a genuine quantum Hamiltonian by replacing every classical spin with its operator, $s_i \to Z_i$, and every product with a tensor product of operators, $s_is_j \to Z_iZ_j$:

$$
H = CI + \sum_i h_i Z_i + \sum_{i<j} J_{ij} Z_iZ_j
$$

($I$ is the identity operator; $C$ is any constant offset.) This is exactly the "problem Hamiltonian" $H_{problem}$ referenced throughout [[adiabatic-theorem]] and [[quantum-annealing-overview]] — its ground state, by construction, is whichever spin/bit configuration minimizes the original classical energy function. That's the entire point of building it this way: solving the *quantum* ground-state problem solves the *classical* optimization problem, because the two were engineered to coincide.

## Expectation values — what you get when the state isn't an eigenstate

A quantum state in superposition doesn't have one definite energy — repeated measurements on identically-prepared copies return different $E_n$ values, each with some probability. The **expectation value**:

$$
\langle H \rangle = \langle\psi|H|\psi\rangle
$$

is the average energy you'd get over many measurements — not something you read off in one shot, but something you estimate statistically by repeating the measurement many times and averaging (this is exactly the "many shots" statistical-sampling behavior flagged much earlier in this vault's discussion of measurement bottlenecks across different quantum algorithm families). This expectation-value framing is specifically how **VQE** (Variational Quantum Eigensolver) and gate-model **QAOA** work: prepare a parameterized state, measure $\langle H\rangle$, adjust the parameters classically to push $\langle H\rangle$ lower, repeat — hill-climbing (or more precisely, hill-*descending*) toward the ground state using measurement statistics rather than annealing's physical evolution.

## Two different roles "the Hamiltonian" plays — worth keeping straight

- **Fixed problem Hamiltonian** (VQE, QAOA cost Hamiltonian, gate-model robust fitting): $H$ doesn't change over the course of the algorithm. You repeatedly prepare states and measure $\langle H \rangle$ against this one fixed operator, adjusting parameters classically in between.
- **Time-dependent annealing Hamiltonian** ([[adiabatic-theorem]]): $H(t) = A(s)H_{start} + B(s)H_{problem}$ genuinely changes shape as the anneal progresses, and the physical system evolves continuously along with it — no repeated measure-and-adjust loop; you read out only once, at the very end.

Both use "Hamiltonian" to mean exactly the same underlying mathematical object (an energy operator), applied in two structurally different algorithmic patterns — worth not conflating when reading across papers that use one or the other.
