---
tags: [quantum, deutsch-algorithm]
---
# 01 Reversible Functions

Back to [[00 Index]] | Next: [[02 Making Any Function Reversible]]

## Is it true that the oracle must be reversible?
Yes. Quantum gates are **unitary** operations, and a unitary can always be undone, so every quantum gate is reversible. The oracle has to be built from quantum gates, so it must be reversible too.

## What "reversible" means
A function is **reversible** if you can look at the output and recover the input **uniquely**. Equivalently: no two different inputs give the same output. A reversible gate on $n$ bits is a **permutation** of all $2^n$ bit strings.

## Why AND is not reversible
Take $\text{AND}(A,B)=A\wedge B$:

| A | B | A∧B |
|---|---|-----|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

If you see output $0$, you cannot tell which of three inputs produced it. Information was destroyed. That is exactly what makes AND irreversible.

## Takeaway
Reversible = no collisions = information is never thrown away. See [[02 Making Any Function Reversible]] for the fix.
