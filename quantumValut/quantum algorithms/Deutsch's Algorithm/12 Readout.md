---
tags: [quantum, deutsch-algorithm]
---
# 12 Readout

Previous: [[11 Preparing the Starting States]] | Next: [[13 The Full Circuit]]

## Where we are after the oracle
From [[09 Putting It Together]]:
- **constant** ($f(0)=f(1)$): first qubit is $\pm|+\rangle$
- **balanced** ($f(0)\neq f(1)$): first qubit is $\pm|-\rangle$

Measuring now is useless: both give 0 or 1 with probability $\tfrac12$.

## Apply $H$ to the first qubit
By [[10 The Hadamard Gate]], $H|+\rangle=|0\rangle$ and $H|-\rangle=|1\rangle$. The $\pm$ is a global sign and does not matter:

- constant $\to\pm|0\rangle\to$ measure **0** with certainty
- balanced $\to\pm|1\rangle\to$ measure **1** with certainty

The result is **deterministic**, not just likely.

## General formula
$$H\!\left(\frac{(-1)^{f(0)}|0\rangle+(-1)^{f(1)}|1\rangle}{\sqrt2}\right)=\frac{(-1)^{f(0)}+(-1)^{f(1)}}{2}|0\rangle+\frac{(-1)^{f(0)}-(-1)^{f(1)}}{2}|1\rangle$$

If the two signs are equal, the $|1\rangle$ part cancels. If they differ, the $|0\rangle$ part cancels.

## Concrete check, $f(x)=x$ (balanced)
Signs are $(-1)^0=+1$ and $(-1)^1=-1$, so the first qubit is $|-\rangle$. $H|-\rangle=|1\rangle$, so we measure 1: "balanced". Correct.

## The second qubit
It is still $|-\rangle$ and carries no answer, so it is ignored at the end.
