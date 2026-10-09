---
tags: [quantum, deutsch-algorithm]
---
# 11 Preparing the Starting States

Previous: [[10 The Hadamard Gate]] | Next: [[12 Readout]]

## The problem
A quantum computer starts every qubit in $|0\rangle$. We need $|+\rangle$ on the first qubit and $|-\rangle$ on the second, so we build them.

## First qubit: $|+\rangle$
$H|0\rangle=|+\rangle$. One gate.

## Second qubit: $|-\rangle$
$H|0\rangle$ gives $|+\rangle$, not $|-\rangle$. But $H|1\rangle=|-\rangle$, so first flip the qubit to $|1\rangle$ with $X$, then apply $H$:

$$|0\rangle\xrightarrow{X}|1\rangle\xrightarrow{H}|-\rangle$$

## Full recipe

$$|0\rangle|0\rangle\;\xrightarrow{X\text{ on qubit 2}}\;|0\rangle|1\rangle\;\xrightarrow{H\text{ on both}}\;|+\rangle|-\rangle$$

This is the input used throughout [[08 Phase Kickback and Phase Oracle]] and [[09 Putting It Together]]: the first qubit is an equal superposition of the two questions $x=0$ and $x=1$, and the second qubit is in $|-\rangle$, ready for phase kickback.
