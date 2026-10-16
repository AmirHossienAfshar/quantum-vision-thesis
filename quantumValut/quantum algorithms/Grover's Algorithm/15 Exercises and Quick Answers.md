---
tags: [quantum, grover, exercises]
---
# 15 Exercises and Quick Answers

Try each before opening the answer.

**1.** What is the probability of measuring $w$ in $\lvert s\rangle$ when $N=1024$?

> [!success]- Answer
> $1/1024$, since every amplitude is $1/\sqrt{1024}$.

**2.** For $n=2$ and $w=01$, write the state right after one oracle call on $\lvert s\rangle$.

> [!success]- Answer
> $\tfrac12(\lvert00\rangle-\lvert01\rangle+\lvert10\rangle+\lvert11\rangle)$.

**3.** For $N=4$, $w=11$: apply $O$ then $D$ to $\lvert s\rangle$ using inversion about the mean.

> [!success]- Answer
> After $O$: $\tfrac12(1,1,1,-1)$, mean $\tfrac14$. Apply $\alpha\to\tfrac12-\alpha$: $(0,0,0,1)=\lvert11\rangle$.

**4.** Apply inversion about the mean to the list $(1,1,1,5)$ (just arithmetic, no normalization).

> [!success]- Answer
> Mean $=2$, so $\alpha\to4-\alpha$: $(3,3,3,-1)$. The mean is still $2$.

**5.** For $N=16$, find $\theta$, the best $k$, and the success probability.

> [!success]- Answer
> $\sin\theta=\tfrac14$, $\theta\approx14.48^\circ$. $k\approx\frac{\pi}{4\theta}-\tfrac12\approx2.6$, so $k=3$. $P=\sin^2(7\theta)=\sin^2(101.3^\circ)\approx0.96$. ($k=2$ gives about $0.91$.)

**6.** Where does the "$2\theta$ per round" come from?

> [!success]- Answer
> $O$ is a reflection across the axis at angle $0$ and $D$ is a reflection across the line at angle $\theta$. Two reflections rotate by twice the angle between the mirrors: $2\theta$.

**7.** For $N=4$, what is $P(w)$ after $k=2$ rounds? Why?

> [!success]- Answer
> $\sin^2(5\cdot30^\circ)=\sin^2150^\circ=0.25$. One round already hit $90^\circ$; a second round overshoots.

**8.** For what $M/N$ is a single round exact?

> [!success]- Answer
> We need $3\theta=90^\circ$, so $\theta=30^\circ$ and $\sin\theta=\tfrac12=\sqrt{M/N}$: $M/N=\tfrac14$.

**9.** Why must the ancilla be prepared in $\lvert-\rangle$?

> [!success]- Answer
> With $\lvert-\rangle$, flipping the ancilla multiplies it by $-1$ and leaves it otherwise unchanged. That turns the bit-flip form $U_f$ into the phase flip $(-1)^{f(x)}$ on the register (phase kickback).

**10.** Give the oracle circuit for $n=3$, $w=110$ ($q_2q_1q_0$).

> [!success]- Answer
> $w$ has a $0$ only at $q_0$. So: $X$ on $q_0$, a $C^3X$ with controls $q_2,q_1,q_0$ and target the ancilla, then $X$ on $q_0$.

**11.** Show $D\lvert s\rangle=\lvert s\rangle$ and say what it means in the "mean" picture.

> [!success]- Answer
> $D\lvert s\rangle=2\lvert s\rangle\langle s\vert s\rangle-\lvert s\rangle=\lvert s\rangle$. Every amplitude of $\lvert s\rangle$ already equals the mean, so inversion about the mean changes nothing.

**12.** Roughly how many oracle calls does Grover need to find one 128-bit key (so $N=2^{128}$)?

> [!success]- Answer
> About $\frac\pi4\sqrt{2^{128}}=\frac\pi4\cdot2^{64}\approx2^{64}$ calls.

**13.** Why does running more rounds not always help?

> [!success]- Answer
> The state rotates through $\lvert w\rangle$ and keeps going. Past $90^\circ$ the vertical component, and hence $P(w)$, decreases again (overshoot).

**14.** CCNOT acts on how many qubits, and how many basis states does its matrix cover?

> [!success]- Answer
> Three qubits, $2^3=8$ basis states, so an $8\times8$ matrix.

---
Previous: [[14 Worked Example N=8]] · Next: [[16 Clarifications]]
