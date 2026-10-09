---
tags: [quantum, deutsch-algorithm]
---
# 05 Oracle on a Superposition

Previous: [[04 Unitary and Permutation Matrices]] | Next: [[06 Phase: Global vs Relative]]

## Superposition and linearity
$|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}$ is "equal parts 0 and 1" ($\sqrt2$ keeps total probability 1).

Gates are **linear**: they act on each term of a sum separately, then add the results. We already know what $U_f$ does to each basis state (the table in [[04 Unitary and Permutation Matrices]]), so we apply the table term by term.

## Input $|+\rangle|0\rangle$
Multiply out:
$$\frac{|0\rangle+|1\rangle}{\sqrt2}\otimes|0\rangle=\frac{|00\rangle+|10\rangle}{\sqrt2}$$

### Example, $f(x)=x$
$|00\rangle\to|00\rangle$ and $|10\rangle\to|11\rangle$, so the output is $\frac{|00\rangle+|11\rangle}{\sqrt2}$: "either both qubits are 0, or both are 1". This is **entangled**: the input and $f(x)$ are tied together.

### General $f$
$|00\rangle\to|0\rangle|f(0)\rangle$ and $|10\rangle\to|1\rangle|f(1)\rangle$, so

$$U_f\,|+\rangle|0\rangle=\frac{|0\rangle|f(0)\rangle+|1\rangle|f(1)\rangle}{\sqrt2}$$

**One call** produced a state containing both $f(0)$ and $f(1)$, each attached to its input.

## The catch
Measuring gives only **one** pair, $(0,f(0))$ or $(1,f(1))$, each with probability $\tfrac12$. You cannot read out both values, so this alone is no better than one classical call.

Deutsch's algorithm asks something more modest: is $f(0)=f(1)$ or not? That is a property of **both values together**, and one call can reveal it if we arrange things well. The arrangement is the phase trick in [[06 Phase: Global vs Relative]] to [[08 Phase Kickback and Phase Oracle]].
