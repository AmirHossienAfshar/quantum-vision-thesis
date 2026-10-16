---
tags: [quantum, grover, circuits, gates]
---
# 11 CNOT and Toffoli Gates

## CNOT (controlled-NOT)
Two qubits: a **control** $c$ and a **target** $t$. If the control is $1$, flip the target. Otherwise do nothing.

$$
\text{CNOT}\lvert c\rangle\lvert t\rangle=\lvert c\rangle\lvert t\oplus c\rangle
$$

| $c\,t$ | output |
|---|---|
| 00 | 00 |
| 01 | 01 |
| 10 | 11 |
| 11 | 10 |

The control never changes. In the basis $(\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle)$ with the control first:

$$
\text{CNOT}=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}
$$

"Identity if the control is $0$, apply $X$ to the target if the control is $1$."

- **Entanglement.** Control $\frac{\lvert0\rangle+\lvert1\rangle}{\sqrt2}$ and target $\lvert0\rangle$ give the Bell state $\frac{\lvert00\rangle+\lvert11\rangle}{\sqrt2}$. CNOT is the basic way to create entanglement.
- **Phase kickback.** With the target in $\lvert-\rangle$: $\text{CNOT}\lvert c\rangle\lvert-\rangle=(-1)^c\lvert c\rangle\lvert-\rangle$. This is the same idea as the oracle in [[10 Building the Oracle from Gates]].

## CCNOT (Toffoli)
Same idea with **two controls**: flip the target only if *both* controls are $1$.

$$
\text{CCNOT}\lvert c_1\rangle\lvert c_2\rangle\lvert t\rangle=\lvert c_1\rangle\lvert c_2\rangle\lvert t\oplus(c_1\wedge c_2)\rangle
$$

Out of the 8 input patterns only $110\leftrightarrow111$ change. As an $8\times8$ matrix (basis $000,001,\dots,111$): the identity everywhere except the last two rows and columns, which swap.

$$
\text{CCNOT}=\begin{pmatrix}I_6&0\\0&\begin{pmatrix}0&1\\1&0\end{pmatrix}\end{pmatrix}
$$

With the target at $\lvert0\rangle$ the output is $c_1\wedge c_2$, a reversible AND. That is why it matters for oracles: checking "$x_1=1$ and $x_0=0$" is an AND.

## Shared properties
- **Reversible and self-inverse.** Applying either twice returns the input. Required, since every gate must be unitary ([[04 Unitary and Permutation Matrices]]).
- **Permutations of basis states.** On computational-basis inputs they act like classical logic gates. Quantum behavior appears only for superpositions.
- **They generalize.** $C^kX$ flips the target when all $k$ controls are $1$. This is what Grover's oracle uses for larger $n$.

## "3 qubits, 8 basis states"
CCNOT acts on **3 qubits**, so it works on 3-bit strings. A 3-qubit register has $2^3=8$ basis states, which is why the matrix is $8\times8$. It is not an 8-bit gate. CNOT is 2 qubits with a $4\times4$ matrix.

## Gates are built from other gates
- Hardware provides a small **native gate set**: single-qubit gates ($H$, $X$, $T$, rotations) plus one two-qubit entangling gate such as CNOT (or CZ).
- That set is **universal**: any quantum operation can be built, or approximated to any precision, from it.
- Bigger gates are **compiled** into native ones. Toffoli becomes about 6 CNOTs plus single-qubit gates ($H$, $T$, $T^\dagger$). A multi-controlled NOT becomes a network of Toffolis or CNOTs, often with helper qubits.
- Toffoli is universal for classical reversible computing, so any classical $f$ can be computed reversibly. That guarantees $U_f$ exists for any $f$ we can compute classically.

So the oracle and $D$ are the high-level blocks we reason with, and a compiler lowers them to hardware gates.

---
Previous: [[10 Building the Oracle from Gates]] · Next: [[12 Building the Diffusion Operator]]
