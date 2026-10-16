---
tags: [quantum, grover, example]
---
# 14 Worked Example N=8

$N=8$ ($n=3$ qubits), marked item $w=101$. Circuit: [[13 The Grover Circuit]].

To keep arithmetic clean, measure every amplitude in units of $c=\frac1{8\sqrt2}\approx0.0884$. Then $\frac1{\sqrt8}=4c$, and a state is normalized when the squares of its entries sum to $128$ (since $c^2=1/128$).

## Setup
- Rounds: $k\approx\frac\pi4\sqrt8\approx2.22$, so $k=2$.
- Angle: $\sin\theta=1/\sqrt8$, so $\theta\approx20.7^\circ$.

## Step 0: initialization
Register $\lvert000\rangle$, ancilla $\lvert0\rangle$. Apply $H^{\otimes3}$ to the register to get $\lvert s\rangle$, and $X$ then $H$ to the ancilla to get $\lvert-\rangle$.

## Round 1
- **Oracle:** the sign of $\lvert101\rangle$ flips. Mean $\mu=\frac{7\cdot4-4}8=3$.
- **Diffusion:** each amplitude $\alpha\to2\mu-\alpha=6-\alpha$.

## Round 2
- **Oracle:** the sign of $\lvert101\rangle$ flips. Mean $\mu=\frac{7\cdot2-10}8=\frac12$.
- **Diffusion:** each amplitude $\alpha\to2\mu-\alpha=1-\alpha$.

## Amplitudes (units of $c$)
| State | Start | After $O$ (r1) | After $D$ (r1) | After $O$ (r2) | After $D$ (r2) |
|---|---|---|---|---|---|
| each of the 7 unmarked | 4 | 4 | 2 | 2 | $-1$ |
| $\lvert101\rangle$ (marked) | 4 | $-4$ | 10 | $-10$ | 11 |
| sum of squares | 128 | 128 | 128 | 128 | 128 |

![[grover-n8-amplitudes.svg|900]]

In the oracle panels only the amber bar moves (it flips sign). In the diffusion panels every bar is reflected through the dashed mean line; the dashed outlines show the old heights.

## Probabilities and angles
| Round $k$ | marked amplitude | $P(w)$ | angle $(2k+1)\theta$ |
|---|---|---|---|
| 0 | $4c\approx0.354$ | $16/128=0.125$ | $20.7^\circ$ |
| 1 | $10c\approx0.884$ | $100/128\approx0.781$ | $62.1^\circ$ |
| 2 | $11c\approx0.972$ | $121/128\approx0.945$ | $103.5^\circ$ |
| 3 (overshoot) | n/a | $\approx0.33$ | $144.9^\circ$ |

The amplitude table and the angle table agree: $\sin62.1^\circ\approx0.884$, $\sin103.5^\circ\approx0.972$. At $k=2$ the state is already $13.5^\circ$ **past** the vertical axis and the unmarked amplitudes have turned slightly negative ($-c$). Stopping at $k=2$ is still best: $k=1$ gives $0.78$ and $k=3$ falls to $0.33$.

## Measurement
Measuring the register gives $101$ with probability $121/128\approx94.5\%$. Each wrong outcome has probability $1/128$ (that is $(-c)^2$), seven of them, totaling $7/128\approx5.5\%$. Since the oracle can verify any answer, a failure is cheap: rerun.

> [!note] Global sign from the circuit
> The diffusion block as drawn equals $-D$, so after each round the state carries an extra global sign. This changes no probability and no later step, so the numbers above are unaffected.

## Comparison with a classical search
Classical: about $4.5$ guesses on average. Grover: $2$ oracle calls, $94.5\%$ success. At this tiny size the gain is modest; the point of $\sqrt N$ scaling is large $N$ (about $785$ vs $500{,}000$ calls at $N=10^6$).

---
Previous: [[13 The Grover Circuit]] · Next: [[15 Exercises and Quick Answers]]
