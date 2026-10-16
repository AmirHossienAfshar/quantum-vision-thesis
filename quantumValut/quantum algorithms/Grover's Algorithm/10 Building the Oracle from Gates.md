---
tags: [quantum, grover, circuits]
---
# 10 Building the Oracle from Gates

Hardware has no "flip the sign if $x=w$" gate. It has ordinary reversible gates, so the usual oracle is built in **bit-flip form**:

$$
U_f\lvert x\rangle\lvert y\rangle=\lvert x\rangle\lvert y\oplus f(x)\rangle
$$

It reads the input register $\lvert x\rangle$ and XORs $f(x)$ into an extra **ancilla** qubit $\lvert y\rangle$. This is easy to build: it is a reversible way of computing $f$. (Background: [[03 The Quantum Oracle]], [[08 Phase Kickback and Phase Oracle]].)

## The trick: ancilla in $\lvert-\rangle$
Prepare the ancilla in

$$
\lvert-\rangle=\frac{\lvert0\rangle-\lvert1\rangle}{\sqrt2}
$$

(apply $X$ then $H$ to $\lvert0\rangle$). Then

$$
U_f\lvert x\rangle\lvert-\rangle=\lvert x\rangle\frac{\lvert0\oplus f(x)\rangle-\lvert1\oplus f(x)\rangle}{\sqrt2}
$$

- $f(x)=0$: unchanged, $\lvert x\rangle\lvert-\rangle$.
- $f(x)=1$: the two terms swap, giving $\frac{\lvert1\rangle-\lvert0\rangle}{\sqrt2}=-\lvert-\rangle$, so $-\lvert x\rangle\lvert-\rangle$.

Combined:

$$
U_f\lvert x\rangle\lvert-\rangle=(-1)^{f(x)}\lvert x\rangle\lvert-\rangle
$$

The ancilla comes out exactly as it went in, and the sign has been **kicked back** onto the register. That is the phase flip $O\lvert x\rangle=(-1)^{f(x)}\lvert x\rangle$. By linearity the same happens to a superposition, term by term. The ancilla stays in $\lvert-\rangle$ throughout, so it never becomes entangled with the register.

## Concrete circuit: $n=2$, $w=10$
Register qubits $x_1x_0$. We need $f(x)=1$ only when $x_1=1$ and $x_0=0$.

1. $X$ on $x_0$ (turns "$x_0=0$" into "$x_0=1$").
2. **Toffoli** (CCNOT) with controls $x_1,x_0$, target the ancilla.
3. $X$ on $x_0$ again (undo step 1).

Check on $x=10$: step 1 makes $x_0=1$, both controls are $1$ so the ancilla flips, step 3 restores $x_0$. For any other $x$, at least one control is $0$ after step 1, so the ancilla is untouched.

## General recipe for any $w$
1. Apply $X$ to every qubit where $w$ has a $0$.
2. Apply a multi-controlled NOT ($C^nX$) with all $n$ register qubits as controls and the ancilla as target.
3. Undo the $X$'s.

## Example: $n=3$, $w=101$ ($q_2q_1q_0$)
$w$ has a $0$ only at $q_1$. So: $X$ on $q_1$, a triple-controlled NOT onto the ancilla, $X$ on $q_1$. This is the oracle block in [[13 The Grover Circuit]].

See [[11 CNOT and Toffoli Gates]] for the gates used.

---
Previous: [[09 Limits of the Speedup]] · Next: [[11 CNOT and Toffoli Gates]]
