---
tags: [quantum, grover]
---
# 02 The Uniform Superposition

## Construction
Start with $n$ qubits in the **ket** $\lvert 0\rangle^{\otimes n} = \lvert 00\ldots0\rangle$ (a ket is a state, a column vector; the bra $\langle 00\ldots0\rvert$ is its conjugate transpose). Apply a Hadamard gate to every qubit (see [[10 The Hadamard Gate]]):

$$
\lvert s\rangle = H^{\otimes n}\lvert 0\rangle^{\otimes n} = (H\lvert 0\rangle)\otimes\cdots\otimes(H\lvert 0\rangle)
$$

Each factor is $H\lvert 0\rangle = \frac{\lvert 0\rangle + \lvert 1\rangle}{\sqrt 2}$. Multiplying $n$ of these out, every term picks $\lvert 0\rangle$ or $\lvert 1\rangle$ for each qubit, giving all $2^n$ bit strings with coefficient $(1/\sqrt2)^n = 1/\sqrt N$:

$$
\boxed{\lvert s\rangle = \frac{1}{\sqrt N}\sum_{x}\lvert x\rangle}
$$

## What the sum means
The sum runs over **all $N = 2^n$ bit strings** of length $n$, not just $0$ and $1$. Here $x$ is the *label* (like $0110$) and $\lvert x\rangle$ is the basis ket for that label.

| $n$ | State |
|---|---|
| 1 | $\frac{1}{\sqrt2}(\lvert 0\rangle + \lvert 1\rangle)$ |
| 2 | $\frac12(\lvert 00\rangle + \lvert 01\rangle + \lvert 10\rangle + \lvert 11\rangle)$ |
| 3 | $\frac{1}{\sqrt8}\sum_{x=000}^{111}\lvert x\rangle$ (8 terms) |

## Probabilities
Every amplitude is $1/\sqrt N$, so measuring now gives each $x$ with probability $1/N$. Finding $w$ has probability $1/N$, no better than a random guess.

The goal of the algorithm is to shift amplitude onto $\lvert w\rangle$ until the final measurement returns $w$ with probability close to $1$.

> [!note] $n$ vs $N$
> Lowercase $n$ is the number of qubits. Capital $N = 2^n$ is the number of states. The amplitude is $1/\sqrt{N}$, not $1/\sqrt{n}$.

---
Previous: [[01 The Search Problem and the Oracle Model]] · Next: [[03 The Oracle as a Phase Flip]]
