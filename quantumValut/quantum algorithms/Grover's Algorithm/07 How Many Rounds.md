---
tags: [quantum, grover]
---
# 07 How Many Rounds

After $k$ rounds the state is at angle $(2k+1)\theta$ ([[06 Two Reflections Make a Rotation]]), so

$$
P(w)=\sin^2\big((2k+1)\theta\big)
$$

## Choosing $k$
We want the angle near $\pi/2$:

$$
(2k+1)\theta\approx\frac\pi2\ \Longrightarrow\ k\approx\frac{\pi}{4\theta}-\frac12
$$

With $\sin\theta=1/\sqrt N$ and $\theta\approx1/\sqrt N$ for large $N$:

$$
\boxed{k\approx\frac\pi4\sqrt N}
$$

Plain words: each round rotates by about $2/\sqrt N$ radians, we need a quarter turn ($\pi/2$), so the number of rounds scales like $\sqrt N$.

## Examples
| $N$ | best $k$ | $P(w)$ |
|---|---|---|
| 4 | 1 | 1 |
| 8 | 2 | 0.945 |
| 16 | 3 | 0.96 |
| $10^6$ | 785 | $\approx 0.999999$ |

For $N=10^6$ a classical search needs about $500{,}000$ queries on average; Grover needs about $785$.

## Success probability vs round
| | $k=0$ | $k=1$ | $k=2$ | $k=3$ |
|---|---|---|---|---|
| $N=4$ ($\theta=30^\circ$) | 0.25 | **1.00** | 0.25 | 0.25 |
| $N=8$ ($\theta\approx20.7^\circ$) | 0.125 | 0.781 | **0.945** | 0.327 |

## Accuracy despite integer $k$
Each step moves the angle by $2\theta$, so after rounding $k$ we land within $\theta$ of $\pi/2$. If the leftover error is $\delta\le\theta$, the failure probability is $\sin^2\delta\le\sin^2\theta=1/N$. So the chance of a wrong answer is at most about $1/N$. Since the oracle can verify any answer, a failure is cheap: rerun.

## Do not run too long
The rotation does not stop at $\lvert w\rangle$; it keeps turning. Past $90^\circ$ the vertical component shrinks again (the **overshoot**). For $N=8$, $k=3$ gives only $0.33$. Grover is **not** "repeat until it's right". You must stop at about $\frac\pi4\sqrt N$ rounds and then measure.

---
Previous: [[06 Two Reflections Make a Rotation]] · Next: [[08 Multiple Solutions and Unknown M]]
