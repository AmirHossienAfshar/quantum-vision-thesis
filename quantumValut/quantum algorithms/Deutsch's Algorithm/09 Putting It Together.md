---
tags: [quantum, deutsch-algorithm]
---
# 09 Putting It Together

Previous: [[08 Phase Kickback and Phase Oracle]] | Next: [[10 The Hadamard Gate]]

## Superposition on the input, $|-\rangle$ on the output
Input: $\frac{|0\rangle+|1\rangle}{\sqrt2}\otimes|-\rangle$. Apply the kickback formula to each term (linearity):

- $|0\rangle|-\rangle\to(-1)^{f(0)}|0\rangle|-\rangle$
- $|1\rangle|-\rangle\to(-1)^{f(1)}|1\rangle|-\rangle$

$$\frac{(-1)^{f(0)}|0\rangle+(-1)^{f(1)}|1\rangle}{\sqrt2}\otimes|-\rangle$$

The output qubit is untouched. This time the result is a **product state** (no entanglement, unlike the $f(x)=x$ example with $|0\rangle$ output in [[05 Oracle on a Superposition]]). All the information about $f$ sits in the **signs on the first qubit**.

## Constant vs balanced
- **Constant** ($f(0)=f(1)$): signs equal, first qubit is $\pm|+\rangle$ (global sign, unobservable).
- **Balanced** ($f(0)\neq f(1)$): signs differ, first qubit is $\pm|-\rangle$.

So "constant or balanced?" became "is the first qubit in $|+\rangle$ or $|-\rangle$?", after a single call to the oracle.

## The remaining problem
Measuring directly, $|+\rangle$ and $|-\rangle$ both give 0 or 1 with probability $\tfrac12$. We need a gate that turns $|+\rangle\to|0\rangle$ and $|-\rangle\to|1\rangle$. That is the Hadamard gate: see [[10 The Hadamard Gate]], and [[12 Readout]] for how it is used.
