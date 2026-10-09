---
tags: [quantum, deutsch-algorithm]
---
# 14 Exercises and Quick Answers

Back to [[00 Index]]

## Exercise 1: the constant-1 oracle
For $f(x)=1$ for both $x=0,1$, what does $U_f$ do to $(x,y)$?

**Answer:** $U_f(x,y)=(x,\,y\oplus1)$. It always flips the second qubit and ignores $x$, i.e. it is $I\otimes X$.

## Exercise 2: global or relative?
Is the minus sign in $\frac{-|0\rangle+|1\rangle}{\sqrt2}$ global or relative? Is it the same state as $|-\rangle$?

**Answer:** The signs are opposite on the two amplitudes, so it is a **relative** sign. Factoring out $-1$ gives $-\frac{|0\rangle-|1\rangle}{\sqrt2}=-|-\rangle$, which is $|-\rangle$ times a global phase. So it is the **same physical state** as $|-\rangle$.

## Exercise 3: why does "keep the inputs" matter?
Explain why keeping the inputs makes $U_f$ a permutation of basis states.

**Hint:** if the inputs are carried to the output, two different inputs can never produce the same output, because they already differ in the part we kept.

## Exercise 4: run the full circuit by hand
Run [[13 The Full Circuit]] for $f(x)=1-x$ and confirm you measure 1.

**Answer:** after the oracle the signs are $(-1)^1=-1$ and $(-1)^0=+1$, so the first qubit is $\frac{-|0\rangle+|1\rangle}{\sqrt2}=-|-\rangle$. $H$ gives $-|1\rangle$, and the measurement is 1 (balanced).

## Exercise 5: Hadamard twice
Show $HH|0\rangle=|0\rangle$.

**Answer:** $H|0\rangle=|+\rangle$ and $H|+\rangle=|0\rangle$ ([[10 The Hadamard Gate]]).

## Quick-check questions
- Why can the oracle not be $f$ alone? (Because $f$ loses information.)
- Is $f$ an input to the oracle? (No, it is built into the gate. The inputs are the two qubits.)
- Why is $U_f$ its own inverse? (Inputs pass through, and $x\oplus x=0$.)
- What turns the oracle's flip into a sign? (The output qubit being in $|-\rangle$, an eigenstate of $X$ with eigenvalue $-1$.)
- Which phase can be detected, global or relative? (Relative.)
- Why does the final $H$ matter? (It turns $|+\rangle/|-\rangle$, which look identical to a direct measurement, into $|0\rangle/|1\rangle$.)
