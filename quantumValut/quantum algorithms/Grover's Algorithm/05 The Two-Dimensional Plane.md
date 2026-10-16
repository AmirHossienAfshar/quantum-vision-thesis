---
tags: [quantum, grover, geometry]
---
# 05 The Two-Dimensional Plane

Although the state lives in $N$ dimensions, the whole algorithm happens inside a **2D plane**.

## The two axes
- $\lvert w\rangle$: the marked state (vertical axis).
- $\lvert w^\perp\rangle = \frac{1}{\sqrt{N-1}}\sum_{x\neq w}\lvert x\rangle$: the **uniform mix of all unmarked states** (horizontal axis). It is one specific vector, not "all the orthogonal ones".

These two are orthogonal.

## Where the decomposition comes from
Start from $\lvert s\rangle = \frac{1}{\sqrt N}\sum_x\lvert x\rangle$. Pull out the $x = w$ term and keep the rest together:

$$
\lvert s\rangle = \frac1{\sqrt N}\lvert w\rangle + \frac1{\sqrt N}\sum_{x\neq w}\lvert x\rangle
$$

Since $\sum_{x\neq w}\lvert x\rangle = \sqrt{N-1}\,\lvert w^\perp\rangle$:

$$
\lvert s\rangle = \frac{1}{\sqrt N}\lvert w\rangle + \sqrt{\frac{N-1}{N}}\,\lvert w^\perp\rangle
$$

## Why $\sin\theta = 1/\sqrt N$
It is a **definition**: choose $\theta$ so its sine is the coefficient on $\lvert w\rangle$. This is allowed because

$$
\left(\frac1{\sqrt N}\right)^2 + \left(\sqrt{\tfrac{N-1}{N}}\right)^2 = \frac1N+\frac{N-1}N = 1
$$

Any two numbers whose squares sum to $1$ can be written as $\sin\theta$ and $\cos\theta$. So

$$
\boxed{\lvert s\rangle = \sin\theta\,\lvert w\rangle + \cos\theta\,\lvert w^\perp\rangle,\qquad \sin\theta = \frac1{\sqrt N}}
$$

For large $N$, $\theta\approx 1/\sqrt N$: $\lvert s\rangle$ sits almost on top of $\lvert w^\perp\rangle$, far from the answer.

## Why bother with $\theta$
Any unit vector in this plane is described by **one angle** $\varphi$:

$$
\lvert\psi\rangle = \cos\varphi\,\lvert w^\perp\rangle + \sin\varphi\,\lvert w\rangle
$$

So the whole $N$-amplitude state becomes a single number. At the start $\varphi = \theta$. The success probability is

$$
P(w) = \sin^2\varphi
$$

so "make $P(w)$ close to $1$" becomes "push $\varphi$ up to $90^\circ$". The payoff: each round adds exactly $2\theta$ to $\varphi$ ([[06 Two Reflections Make a Rotation]]), giving a clean formula for any round.

## Why the plane is enough
$O$ and $D$ only ever combine $\lvert w\rangle$, $\lvert s\rangle$ and each other, so the state never leaves the span of $\lvert w\rangle$ and $\lvert w^\perp\rangle$.

## The circle picture
All states visited lie on the unit circle in this plane. $\lvert s\rangle$ is a **fixed vector**, the starting point. After $k$ rounds the state is $G^k\lvert s\rangle$, a different vector further along the circle.

*Grover's algorithm starts the state near $\lvert w^\perp\rangle$ (far from the answer) and rotates it, step by step, toward $\lvert w\rangle$ (the answer).*

## The picture
![[grover-2d-plane.svg|680]]

Read it as: the horizontal axis is $\lvert w^\perp\rangle$, the vertical axis is $\lvert w\rangle$, the purple arrow is the start state $\lvert s\rangle$ at angle $\theta$, the gray arrow is the state after the oracle (reflected to $-\theta$), and the amber arrow is the state after diffusion at $3\theta$. The dashed connectors are perpendicular to the mirror line. Why this works is the topic of [[06 Two Reflections Make a Rotation]].

## Example: $N = 4$
$\sin\theta = \tfrac12$, so $\theta = 30^\circ$. The state starts $30^\circ$ above $\lvert w^\perp\rangle$, i.e. $60^\circ$ away from $\lvert w\rangle$.

---
Previous: [[04 The Diffusion Operator]] · Next: [[06 Two Reflections Make a Rotation]]
