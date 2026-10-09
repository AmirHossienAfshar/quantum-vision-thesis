---
tags: [quantum, deutsch-algorithm]
---
# 15 State Tracking Through the Circuit

Back to [[00 Index]] | Related: [[13 The Full Circuit]]

Circuit: qubit 1 goes $H\to U_f\to H\to$ measure. Qubit 2 goes $X\to H\to U_f\to$ (unused). The markers $|\psi_0\rangle,\dots,|\psi_4\rangle$ sit between the stages.

## $|\psi_0\rangle$: start
$$|\psi_0\rangle=|0\rangle|0\rangle$$

## $|\psi_1\rangle$: after $X$ on qubit 2
$X|0\rangle=|1\rangle$, qubit 1 untouched:
$$|\psi_1\rangle=|0\rangle|1\rangle$$

## $|\psi_2\rangle$: after $H$ on both qubits
$H|0\rangle=|+\rangle$ and $H|1\rangle=|-\rangle$:
$$|\psi_2\rangle=|+\rangle|-\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}\otimes\frac{|0\rangle-|1\rangle}{\sqrt2}=\tfrac12\big(|00\rangle-|01\rangle+|10\rangle-|11\rangle\big)$$

Regroup by the first qubit, which is the form the oracle needs:
$$|\psi_2\rangle=\frac1{\sqrt2}\big(|0\rangle|-\rangle+|1\rangle|-\rangle\big)$$

## $|\psi_3\rangle$: after the oracle $U_f$
Phase kickback ([[08 Phase Kickback and Phase Oracle]]): $U_f|x\rangle|-\rangle=(-1)^{f(x)}|x\rangle|-\rangle$. Apply it to each term (linearity):
$$|\psi_3\rangle=\frac1{\sqrt2}\Big((-1)^{f(0)}|0\rangle|-\rangle+(-1)^{f(1)}|1\rangle|-\rangle\Big)=\frac{(-1)^{f(0)}|0\rangle+(-1)^{f(1)}|1\rangle}{\sqrt2}\otimes|-\rangle$$

The $|-\rangle$ is unchanged and separate, so it is often dropped from the notation (phase oracle form):
$$|\psi_3\rangle=\frac1{\sqrt2}\Big((-1)^{f(0)}|0\rangle+(-1)^{f(1)}|1\rangle\Big)$$

Four cases:

| $f(0),f(1)$ | $\lvert\psi_3\rangle$ (first qubit) |
|---|---|
| 0, 0 | $\frac1{\sqrt2}(\lvert0\rangle+\lvert1\rangle)=+\lvert+\rangle$ |
| 1, 1 | $\frac1{\sqrt2}(-\lvert0\rangle-\lvert1\rangle)=-\lvert+\rangle$ |
| 0, 1 | $\frac1{\sqrt2}(\lvert0\rangle-\lvert1\rangle)=+\lvert-\rangle$ |
| 1, 0 | $\frac1{\sqrt2}(-\lvert0\rangle+\lvert1\rangle)=-\lvert-\rangle$ |

Summary:
- $f(0)=f(1)$: $|\psi_3\rangle=\pm\frac1{\sqrt2}(|0\rangle+|1\rangle)=\pm|+\rangle$
- $f(0)\neq f(1)$: $|\psi_3\rangle=\pm\frac1{\sqrt2}(|0\rangle-|1\rangle)=\pm|-\rangle$

## $|\psi_4\rangle$: after $H$ on qubit 1
Use $H|0\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}$ and $H|1\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}$:
$$\frac1{\sqrt2}\Big((-1)^{f(0)}\tfrac{|0\rangle+|1\rangle}{\sqrt2}+(-1)^{f(1)}\tfrac{|0\rangle-|1\rangle}{\sqrt2}\Big)$$
Collect the $|0\rangle$ and $|1\rangle$ terms:
$$|\psi_4\rangle=\Big[\tfrac{(-1)^{f(0)}+(-1)^{f(1)}}{2}|0\rangle+\tfrac{(-1)^{f(0)}-(-1)^{f(1)}}{2}|1\rangle\Big]\otimes|-\rangle$$

- $f(0)=f(1)$: the signs are equal, the $|1\rangle$ coefficient is $0$, the $|0\rangle$ coefficient is $\pm1$: $|\psi_4\rangle=\pm|0\rangle|-\rangle$
- $f(0)\neq f(1)$: the $|0\rangle$ coefficient is $0$, the $|1\rangle$ coefficient is $\pm1$: $|\psi_4\rangle=\pm|1\rangle|-\rangle$

Equivalently, from the table: $H|+\rangle=|0\rangle$ and $H|-\rangle=|1\rangle$.

## Measurement
Measure qubit 1: **0 means constant, 1 means balanced**, with certainty. The $\pm$ is a global sign and cannot be observed.
