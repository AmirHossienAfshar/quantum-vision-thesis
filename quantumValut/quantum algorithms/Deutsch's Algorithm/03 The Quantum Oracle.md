---
tags: [quantum, deutsch-algorithm]
---
# 03 The Quantum Oracle

Previous: [[02 Making Any Function Reversible]] | Next: [[04 Unitary and Permutation Matrices]]

## Notation
A qubit's classical values are the basis states $|0\rangle$ and $|1\rangle$. Two qubits: $|x\rangle|y\rangle$, also written $|xy\rangle$. In Deutsch's algorithm:
- first qubit = **input register** ($x$)
- second qubit = **output register** (plays the role of $C$)

## Definition of the oracle
$$U_f\,|x\rangle|y\rangle=|x\rangle\,|y\oplus f(x)\rangle$$

This is exactly the classical rule from [[02 Making Any Function Reversible]] written with kets. There are four basis inputs: $|00\rangle,|01\rangle,|10\rangle,|11\rangle$.

## Operator vs state
- $U_f$ is the **operator** (a $4\times4$ matrix). "Applying" it means multiplying the matrix by the state.
- $|x\rangle|y\oplus f(x)\rangle$ is a **state**: the *result* of applying $U_f$ to $|x\rangle|y\rangle$. The inside of the ket just labels which basis state we land on.

So the line reads: operator $U_f$ applied to input state $|x\rangle|y\rangle$ gives output state $|x\rangle|y\oplus f(x)\rangle$.

## Product states vs entangled states
- $\frac{|0\rangle+|1\rangle}{\sqrt2}$ is **one** qubit in a superposition. The "+" does not mean two qubits.
- $|01\rangle$ is shorthand for $|0\rangle|1\rangle$: qubit 1 definitely 0, qubit 2 definitely 1. Not entangled.
- A **product state** can be written as (state of qubit 1) $\otimes$ (state of qubit 2).
- **Entangled** means it cannot be factored that way. Classic example: $\frac{|00\rangle+|11\rangle}{\sqrt2}$.

The standard input $\frac{|0\rangle+|1\rangle}{\sqrt2}\otimes|0\rangle$ is a product state. For $f(x)=x$ the oracle turns it into an entangled state (see [[05 Oracle on a Superposition]]).

## $f$ is not an input: the sealed box picture
$f$ is **not** fed to the oracle. It is built into the gate. Think of $U_f$ as a sealed box: someone hands you a box with their secret $f$ inside, and you can only send qubits in and look at what comes out. Different $f$ means a **different gate**. For a one-bit $f$ there are only four possible boxes:

| $f$ | what $U_f$ does | gate |
|---|---|---|
| $f(x)=0$ (constant) | nothing | identity |
| $f(x)=1$ (constant) | always flips $y$ | $I\otimes X$ |
| $f(x)=x$ (balanced) | flips $y$ when $x=1$ | CNOT |
| $f(x)=1-x$ (balanced) | flips $y$ when $x=0$ | CNOT with $X$ on $y$ afterwards |

The formula for $U_f$ is the **definition** of what the box does. The whole puzzle: you get one unknown box out of these four, and you may use it **once**. Is it constant or balanced?

## What are the two inputs, and can we put "anything" in?
- The definition of $U_f$ is only stated for the four **basis states**, where $x,y\in\{0,1\}$. So $f$ is only ever evaluated on 0 and 1.
- "Anything" means any **superposition** of those. Gates are linear, so the action on the four basis states fixes the action on every mix of them. A superposition on the first qubit is handled term by term, each term being a basis state with $x=0$ or $x=1$. $f$ is still only used on 0 and 1.
- **We** choose the starting states of the two qubits. Choosing them well is the design of the algorithm: $|+\rangle$ on the first qubit and $|-\rangle$ on the second (see [[11 Preparing the Starting States]]).
