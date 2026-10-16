---
tags: [quantum, grover]
---
# 04 The Diffusion Operator

## Definition
$$
D = 2\lvert s\rangle\langle s\rvert - I
$$

Its effect: replace every amplitude $\alpha$ by $2\mu - \alpha$, where $\mu$ is the **average of all the amplitudes**. This is **inversion about the mean**.

## Why $D$ computes the mean
Write the state as $\lvert\psi\rangle = \sum_x \alpha_x\lvert x\rangle$ with mean $\mu = \frac1N\sum_x\alpha_x$. The overlap with $\lvert s\rangle$ is

$$
\langle s\vert\psi\rangle = \sum_x\frac{1}{\sqrt N}\alpha_x = \sqrt N\,\mu
$$

So the overlap with $\lvert s\rangle$ is $\sqrt N$ times the mean. Now look at one slot of $D\lvert\psi\rangle$. The term $2\langle s\vert\psi\rangle\lvert s\rangle$ puts the same value in every slot: $2\sqrt N\mu\cdot\frac1{\sqrt N} = 2\mu$. Subtracting the old amplitude gives

$$
\alpha_x \;\longrightarrow\; 2\mu - \alpha_x
$$

Each amplitude lands as far above the mean as it was below it (or the reverse). The name "diffusion" reflects this redistribution around the average. After the oracle, $w$ is the one amplitude far *below* the mean, so it is thrown far *above* it.

## Two properties
- $D\lvert s\rangle = 2\lvert s\rangle\langle s\vert s\rangle - \lvert s\rangle = \lvert s\rangle$. The uniform state is left alone (every entry is already its own mean).
- $D$ preserves the mean. Inversion about the mean cannot move the mean.

## Example: $N = 4$, $w = 10$ (one round is exact)
After the oracle the amplitudes are $(\tfrac12,\tfrac12,-\tfrac12,\tfrac12)$, mean $\mu = \tfrac14$. Apply $\alpha\to\tfrac12-\alpha$: the three unmarked become $0$, the marked becomes $1$. The state is exactly $\lvert 10\rangle$.

Same thing with the bra-ket definition. First the overlap:

$$
\langle s\vert\psi\rangle = \tfrac14+\tfrac14-\tfrac14+\tfrac14 = \tfrac12
$$

Then $D\lvert\psi\rangle = 2\cdot\tfrac12\lvert s\rangle - \lvert\psi\rangle = \lvert s\rangle - \lvert\psi\rangle$, and the $\lvert00\rangle,\lvert01\rangle,\lvert11\rangle$ terms cancel, leaving $\lvert10\rangle$.

As matrices: $\lvert s\rangle\langle s\rvert$ has every entry $1/N = \tfrac14$, so

$$
D = \frac12\begin{pmatrix}-1&1&1&1\\1&-1&1&1\\1&1&-1&1\\1&1&1&-1\end{pmatrix},
\qquad
D\cdot\frac12\begin{pmatrix}1\\1\\-1\\1\end{pmatrix}=\begin{pmatrix}0\\0\\1\\0\end{pmatrix}
$$

> [!note] Landing exactly on $w$ is special to $N = 4$
> For larger $N$ one round only gets partway. See [[07 How Many Rounds]].

## Example: $N = 8$ (partway)
After the oracle: seven amplitudes of $0.354$ and one of $-0.354$. Mean $\mu = 0.265$. After $D$: unmarked $2(0.265)-0.354 = 0.177$, marked $2(0.265)+0.354 = 0.884$. Probability of $w$: $0.884^2\approx 0.78$.

---
Previous: [[03 The Oracle as a Phase Flip]] · Next: [[05 The Two-Dimensional Plane]]
