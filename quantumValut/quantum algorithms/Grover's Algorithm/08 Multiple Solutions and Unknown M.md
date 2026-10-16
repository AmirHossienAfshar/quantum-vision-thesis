---
tags: [quantum, grover]
---
# 08 Multiple Solutions and Unknown M

## $M$ marked items
Let $M$ items be marked. Redefine the vertical axis as the uniform mix of all marked states, $\lvert w\rangle=\frac1{\sqrt M}\sum_{x\ \text{marked}}\lvert x\rangle$, and the horizontal axis as the uniform mix of all unmarked ones. The decomposition of $\lvert s\rangle$ is the same, with

$$
\sin\theta=\sqrt{\frac MN}
$$

Everything else carries over: $O$ and $D$ are still two reflections, each round still rotates by $2\theta$, and we still need a quarter turn:

$$
\boxed{k\approx\frac\pi4\sqrt{\frac NM}}
$$

More solutions means a bigger starting angle, so fewer rounds.

> [!example] $N=16$, $M=4$
> $\sin\theta=\tfrac12$, so $\theta=30^\circ$ and $k=1$ lands exactly at $90^\circ$, like the $N=4$ single-solution case. In general one round is exact when $M/N=1/4$.

If $M\ge N/2$ the method stops being useful: a random guess already succeeds half the time (and the angle is large enough that rounds can overshoot).

## When $M$ is unknown
The formula needs $M$, and a wrong $k$ can overshoot. Two standard fixes:

1. **Quantum counting** (Brassard, Høyer, Tapp): use phase estimation on $G$. Its rotation angle encodes $M$, so you estimate $M$ first and then choose $k$.
2. **Randomized restarts** (Boyer, Brassard, Høyer, Tapp): try a random number of rounds from a geometrically growing range, measure, and verify with the oracle. This finds a solution in $O(\sqrt{N/M})$ queries without ever learning $M$.

## Generalization
The same "oracle reflection plus reflection about the start state" idea works for any starting state and any "good subspace". This is **amplitude amplification**, a natural next topic.

---
Previous: [[07 How Many Rounds]] · Next: [[09 Limits of the Speedup]]
