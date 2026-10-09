---
tags: [quantum, deutsch-algorithm]
---
# 10 The Hadamard Gate

Previous: [[09 Putting It Together]] | Next: [[11 Preparing the Starting States]]

## Definition
The **Hadamard gate $H$** converts between the two bases we use, $\{|0\rangle,|1\rangle\}$ and $\{|+\rangle,|-\rangle\}$:

- $H|0\rangle=|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}$
- $H|1\rangle=|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}$

As a matrix (columns = inputs $|0\rangle,|1\rangle$):

$$H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$$

## What $H$ does to $|+\rangle$ and $|-\rangle$
By linearity:

$$H|+\rangle=\frac{H|0\rangle+H|1\rangle}{\sqrt2}=\frac{|+\rangle+|-\rangle}{\sqrt2}=\frac{(|0\rangle+|1\rangle)+(|0\rangle-|1\rangle)}{2}=|0\rangle$$

$$H|-\rangle=\frac{H|0\rangle-H|1\rangle}{\sqrt2}=\frac{|+\rangle-|-\rangle}{\sqrt2}=|1\rangle$$

So $|0\rangle\leftrightarrow|+\rangle$ and $|1\rangle\leftrightarrow|-\rangle$ in both directions. Applying $H$ twice gives the identity: **$H$ is its own inverse**, like $U_f$.

## Is it a legal gate?
Yes, it is unitary: the columns $(1,1)/\sqrt2$ and $(1,-1)/\sqrt2$ each have length 1 and their dot product is 0. Unlike $U_f$, it is **not** a permutation matrix (it contains a minus sign). It is the first gate here that **creates superpositions**.

## Why it matters in this algorithm
- To **prepare** $|+\rangle$ and $|-\rangle$: [[11 Preparing the Starting States]]
- To **read out** the answer, by turning a relative sign into a 0 or 1: [[12 Readout]]
