---
tags: [quantum, grover, circuits]
---
# 12 Building the Diffusion Operator

Recall $D=2\lvert s\rangle\langle s\rvert-I$ ([[04 The Diffusion Operator]]). Three ideas turn it into gates.

## Idea 1: move $\lvert s\rangle$ to $\lvert0\ldots0\rangle$
Since $\lvert s\rangle=H^{\otimes n}\lvert0\rangle^{\otimes n}$ and $H^{\otimes n}$ is its own inverse,

$$
\lvert s\rangle\langle s\rvert=H^{\otimes n}\lvert0\rangle\langle0\rvert H^{\otimes n}
$$

(here $\lvert0\rangle\langle0\rvert$ is shorthand for the projector onto $\lvert0\ldots0\rangle$). Substituting, and using $I=H^{\otimes n}IH^{\otimes n}$:

$$
D=H^{\otimes n}\big(2\lvert0\rangle\langle0\rvert-I\big)H^{\otimes n}
$$

## Idea 2: the middle piece is a one-state phase flip
$$
2\lvert0\rangle\langle0\rvert-I=\text{diag}(1,-1,-1,\ldots,-1)=-\,\big(I-2\lvert0\rangle\langle0\rvert\big)
$$

The overall $-1$ is a **global phase** ([[06 Phase: Global vs Relative]]): it multiplies the whole state by the same number, so it changes no measurement outcome and no later round. Drop it. What remains, $I-2\lvert0\ldots0\rangle\langle0\ldots0\rvert$, is the same kind of operation as the oracle: a sign flip on one basis state.

## Idea 3: move $\lvert0\ldots0\rangle$ to $\lvert1\ldots1\rangle$
The easiest one-state sign flip in hardware is on $\lvert1\ldots1\rangle$, via a **multi-controlled Z** ($C^{n-1}Z$). So wrap it with $X$ on every qubit.

## The circuit (up to global phase)
$$
D\simeq H^{\otimes n}\ X^{\otimes n}\ C^{n-1}Z\ X^{\otimes n}\ H^{\otimes n}
$$

Order of action on the state: $H$'s, $X$'s, $C^{n-1}Z$, $X$'s, $H$'s. The multi-controlled $Z$ comes from known gates: $Z=HXH$, so wrap a multi-controlled NOT with an $H$ on each side of its target. For $n=2$ it is a CZ; for $n=3$ it is a Toffoli with $H$'s around the target (called CCZ).

## Check, $n=2$
The $X$-CZ-$X$ block gives $\text{diag}(-1,1,1,1)$ (the CZ's flip on $\lvert11\rangle$ becomes a flip on $\lvert00\rangle$). Then

$$
H^{\otimes2}\,\text{diag}(-1,1,1,1)\,H^{\otimes2}=I-2\lvert s\rangle\langle s\rvert=-D
$$

which is $D$ up to the global phase $-1$. Without dropping the sign, $H^{\otimes2}\text{diag}(1,-1,-1,-1)H^{\otimes2}$ gives exactly
$D=\tfrac12\begin{pmatrix}-1&1&1&1\\1&-1&1&1\\1&1&-1&1\\1&1&1&-1\end{pmatrix}$.

## Cost
Each round uses two multi-controlled gates plus $O(n)$ single-qubit gates, so the gate cost per round scales with $n=\log_2N$, not with $N$. That is why the oracle-query count is the quantity that matters.

---
Previous: [[11 CNOT and Toffoli Gates]] · Next: [[13 The Grover Circuit]]
