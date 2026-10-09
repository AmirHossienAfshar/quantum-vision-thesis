---
tags: [quantum, deutsch-algorithm]
---
# 04 Unitary and Permutation Matrices

Previous: [[03 The Quantum Oracle]] | Next: [[05 Oracle on a Superposition]]

## A gate is a table
Defining a gate means saying where each basis state goes. Example, $f(x)=x$, so $U_f|x\rangle|y\rangle=|x\rangle|y\oplus x\rangle$ (this is the **CNOT** gate):

- $|00\rangle\to|00\rangle$
- $|01\rangle\to|01\rangle$
- $|10\rangle\to|11\rangle$
- $|11\rangle\to|10\rangle$

As a matrix (columns = inputs in order $00,01,10,11$; the 1 marks where it lands):

$$U_f=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}$$

Every column and every row has exactly one 1. This is a **permutation matrix**: it only shuffles basis states (here it swaps $|10\rangle$ and $|11\rangle$). One 1 per column and row is the "no collisions" property from [[01 Reversible Functions]].

## What "unitary" means
A state of two qubits is a list of four **amplitudes**. Their squared sizes sum to 1 (total probability). A gate must keep this true for every state and must be undoable. In matrix terms this holds exactly when the **columns are orthonormal**:
- each column has length 1
- any two different columns are perpendicular (dot product 0)

## Why a permutation matrix is unitary
- **Length 1:** each column is a single 1 with zeros elsewhere.
- **Perpendicular:** two different columns have their 1 in different rows, so their entrywise product is 0 everywhere.

Direct view: amplitudes $(a,b,c,d)$ come out as $(a,b,d,c)$, the same numbers reordered, so the sum of squares cannot change.

## The chain
$$\text{reversible classical rule}\;\Rightarrow\;\text{no collisions}\;\Rightarrow\;\text{permutation matrix}\;\Rightarrow\;\text{unitary}\;\Rightarrow\;\text{legal quantum gate}$$
