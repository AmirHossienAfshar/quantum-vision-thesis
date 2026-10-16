---
tags: [quantum, grover]
---
# 03 The Oracle as a Phase Flip

## Definition
The oracle $O$ acts on basis states as

$$
O\lvert x\rangle = (-1)^{f(x)}\lvert x\rangle
$$

So $O\lvert x\rangle = \lvert x\rangle$ for $x \neq w$, and $O\lvert w\rangle = -\lvert w\rangle$. As an operator:

$$
O = I - 2\lvert w\rangle\langle w\rvert
$$

This is the identity with a single diagonal entry flipped to $-1$ (the $w$-th one). See [[08 Phase Kickback and Phase Oracle]] for how this is built, and [[10 Building the Oracle from Gates]] for the circuit.

## Effect on the uniform state
$$
O\lvert s\rangle = \frac{1}{\sqrt N}\sum_{x\neq w}\lvert x\rangle - \frac{1}{\sqrt N}\lvert w\rangle
$$

All $N$ basis states are still there. Only $w$'s amplitude has changed sign. The oracle does **not** output $w$; it returns the entire state with one hidden minus sign.

## The sign is invisible to measurement
$\left(-\tfrac{1}{\sqrt N}\right)^2 = \tfrac1N$, so measuring right now still finds $w$ with probability $1/N$. The marking lives in the **relative phase** (see [[06 Phase: Global vs Relative]]). The next step ([[04 The Diffusion Operator]]) converts that hidden sign into a visible difference in amplitude size.

## Example: $n = 2$, $w = 10$
Basis order $\lvert 00\rangle, \lvert 01\rangle, \lvert 10\rangle, \lvert 11\rangle$:

$$
O = \begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&-1&0\\0&0&0&1\end{pmatrix},
\qquad
O\lvert s\rangle = \frac12\begin{pmatrix}1\\1\\-1\\1\end{pmatrix}
$$

Before: $\frac12(\lvert00\rangle + \lvert01\rangle + \lvert10\rangle + \lvert11\rangle)$. After: $\frac12(\lvert00\rangle + \lvert01\rangle - \lvert10\rangle + \lvert11\rangle)$.

---
Previous: [[02 The Uniform Superposition]] · Next: [[04 The Diffusion Operator]]
