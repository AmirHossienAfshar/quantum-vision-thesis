---
tags: [quantum, deutsch-algorithm]
---
# 13 The Full Circuit

Previous: [[12 Readout]] | Next: [[14 Exercises and Quick Answers]]

## The algorithm
1. Start with $|0\rangle|0\rangle$, apply $X$ to the second qubit: $|0\rangle|1\rangle$. ([[11 Preparing the Starting States]])
2. Apply $H$ to both qubits: $|+\rangle|-\rangle$.
3. Call the oracle $U_f$ **once**. First qubit becomes $\frac{(-1)^{f(0)}|0\rangle+(-1)^{f(1)}|1\rangle}{\sqrt2}$; second stays $|-\rangle$. ([[08 Phase Kickback and Phase Oracle]])
4. Apply $H$ to the first qubit. ([[12 Readout]])
5. Measure the first qubit: **0 means constant, 1 means balanced**.

## Check of all four possible boxes

| $f$ | $(f(0),f(1))$ | first qubit after oracle | after $H$ | measure | verdict |
|---|---|---|---|---|---|
| always 0 | (0, 0) | $\lvert+\rangle$ | $\lvert0\rangle$ | 0 | constant |
| always 1 | (1, 1) | $-\lvert+\rangle$ | $-\lvert0\rangle$ | 0 | constant |
| $f(x)=x$ | (0, 1) | $\lvert-\rangle$ | $\lvert1\rangle$ | 1 | balanced |
| $f(x)=1-x$ | (1, 0) | $-\lvert-\rangle$ | $-\lvert1\rangle$ | 1 | balanced |

All four give the right verdict with certainty. The two constant boxes differ only by a global sign, and so do the two balanced ones, which is why the measurement cannot tell them apart (and does not need to).

## Recap
- The oracle is a ready-made reversible box $U_f$ ([[02 Making Any Function Reversible]], [[03 The Quantum Oracle]]).
- Output qubit in $|-\rangle$ turns $f(x)$ into a sign: phase kickback.
- Input qubit in $|+\rangle$ puts both signs side by side after one call.
- Final $H$ converts "do the signs match?" into a plain 0 or 1.

Classically two calls to $f$ are needed. The quantum version needs one. The speedup is modest, but the same pattern with more qubits becomes the **Deutsch–Jozsa algorithm**, where the gap is dramatic. That is a natural next topic.
