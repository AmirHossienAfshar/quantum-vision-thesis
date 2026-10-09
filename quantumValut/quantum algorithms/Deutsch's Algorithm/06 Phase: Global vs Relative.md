---
tags: [quantum, deutsch-algorithm]
---
# 06 Phase: Global vs Relative

Previous: [[05 Oracle on a Superposition]] | Next: [[07 Eigenstates and Eigenvalues]]

## Basis and amplitudes
$|0\rangle,|1\rangle$ are the **computational basis**: every single-qubit state is $a|0\rangle+b|1\rangle$ with $|a|^2+|b|^2=1$. Another basis is $\{|+\rangle,|-\rangle\}$, and the Hadamard gate converts between the two. We default to $\{|0\rangle,|1\rangle\}$ because measurement reports in it.

$$|+\rangle=\tfrac{|0\rangle+|1\rangle}{\sqrt2},\qquad|-\rangle=\tfrac{|0\rangle-|1\rangle}{\sqrt2}$$

## Phase and sign
Amplitudes can be negative. The sign in front of an amplitude is a **phase**. More generally an amplitude is a size times a phase factor $e^{i\theta}$:
- $+1=e^{i\cdot0}$ (angle 0)
- $-1=e^{i\pi}$ (angle $\pi$, half a turn)

"Sign" is the special case where the angle is 0 or $\pi$. Deutsch's algorithm only uses these two.

## Global phase: invisible
A sign (or phase) on the **whole** state cannot be detected: $|0\rangle$ and $-|0\rangle$ give the same probabilities since $(-1)^2=1$, and gates are linear so $U(-\psi)=-U(\psi)$ always carries it along.

## Relative phase: meaningful
A sign on **one part** of a superposition matters. $|+\rangle\neq|-\rangle$.

Experiment (using the Hadamard gate $H$, with $H|0\rangle=|+\rangle$, $H|1\rangle=|-\rangle$, $H|+\rangle=|0\rangle$, $H|-\rangle=|1\rangle$):
- $H|+\rangle=|0\rangle$ then measure: **0** for sure
- $H(-|+\rangle)=-|0\rangle$ then measure: **0** for sure (same, the sign vanishes)
- $H|-\rangle=|1\rangle$ then measure: **1** for sure

Direct measurement of all three gives 50/50, but after $H$ the relative sign becomes a visible 0 vs 1. That is the plan: **hide $f$'s answer in a relative sign, then use $H$ to read it.**

## General form of a one-qubit state
$$|\psi\rangle=e^{i\gamma}\Big(\cos\tfrac\theta2\,|0\rangle+e^{i\varphi}\sin\tfrac\theta2\,|1\rangle\Big)$$
- $\gamma$: **global phase** (multiplies everything, ignorable)
- $\varphi$: **relative phase** (only on the $|1\rangle$ part, measurable after mixing)
- $\theta$: weight split. Probabilities: $\cos^2\frac\theta2$ for 0, $\sin^2\frac\theta2$ for 1

Equivalent two-amplitude form: $a=|a|e^{i\alpha}$, $b=|b|e^{i\beta}$. Only $\beta-\alpha$ matters.

- **Relative phase** = the *difference* between the phase angles of the two amplitudes ($\varphi=\beta-\alpha$).
- **Global phase** = a factor shared by both amplitudes. It shifts $\alpha$ and $\beta$ equally, so the difference is unchanged. Phases only matter when two things are compared, and a global phase gives nothing to compare.

$|+\rangle$: $\theta=\pi/2,\varphi=0$. $|-\rangle$: $\theta=\pi/2,\varphi=\pi$ (since $e^{i\pi}=-1$).

$\theta,\varphi$ are the Bloch-sphere angles, to be met later.
