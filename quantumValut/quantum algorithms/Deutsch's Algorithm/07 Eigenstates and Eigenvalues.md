---
tags: [quantum, deutsch-algorithm]
---
# 07 Eigenstates and Eigenvalues

Previous: [[06 Phase: Global vs Relative]] | Next: [[08 Phase Kickback and Phase Oracle]]

## The gate X
$X$ is the quantum NOT: $X|0\rangle=|1\rangle$, $X|1\rangle=|0\rangle$.

## What X does to three states
- $|0\rangle\to|1\rangle$: a **different** state, so $X$ changed it.
- $|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}\to\frac{|1\rangle+|0\rangle}{\sqrt2}=|+\rangle$: the **same** state, times $+1$.
- $|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}\to\frac{|1\rangle-|0\rangle}{\sqrt2}=-|-\rangle$: the same state times $-1$ (only a global phase).

## Definition
If a gate only multiplies a state by a number, the state is an **eigenstate** of the gate and the number is its **eigenvalue**.

$$X|+\rangle=(+1)|+\rangle,\qquad X|-\rangle=(-1)|-\rangle$$

For an eigenstate the gate has no visible effect on the state itself. All it leaves behind is that multiplying number. This is the idea that powers [[08 Phase Kickback and Phase Oracle]].
