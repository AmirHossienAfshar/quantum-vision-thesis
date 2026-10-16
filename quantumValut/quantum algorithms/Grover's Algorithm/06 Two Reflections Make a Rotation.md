---
tags: [quantum, grover, geometry]
---
# 06 Two Reflections Make a Rotation

In the plane of [[05 The Two-Dimensional Plane]], use the basis $(\lvert w^\perp\rangle, \lvert w\rangle)$, so a state at angle $\varphi$ is $(\cos\varphi,\ \sin\varphi)^T$ and $\lvert s\rangle = (\cos\theta,\ \sin\theta)^T$.

## The oracle is a reflection
$O\lvert w\rangle = -\lvert w\rangle$ and $O\lvert w^\perp\rangle = \lvert w^\perp\rangle$ (the latter contains only unmarked states). So in the plane

$$
O = \begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
O\begin{pmatrix}\cos\varphi\\\sin\varphi\end{pmatrix}=\begin{pmatrix}\cos(-\varphi)\\\sin(-\varphi)\end{pmatrix}
$$

$O$ sends angle $\varphi\to-\varphi$: a **reflection across the horizontal axis** ($\lvert w^\perp\rangle$ axis).

## The diffusion is a reflection too
Probe $D = 2\lvert s\rangle\langle s\rvert - I$ with two special vectors. These are **test vectors to find out what $D$ is**, not steps of the algorithm. $D$ is linear, so knowing its action on two independent vectors fixes its action on the whole plane.

1. $\lvert s\rangle$: $D\lvert s\rangle = 2\lvert s\rangle\underbrace{\langle s\vert s\rangle}_{1}-\lvert s\rangle = +\lvert s\rangle$.
2. $\lvert s^\perp\rangle = (-\sin\theta,\ \cos\theta)^T$ with $\langle s\vert s^\perp\rangle = 0$: $D\lvert s^\perp\rangle = -\lvert s^\perp\rangle$.

"Keep what lies along the line, flip what is perpendicular to it" is the definition of a **reflection across the line through $\lvert s\rangle$**. As a matrix:

$$
D = 2\begin{pmatrix}\cos^2\theta&\cos\theta\sin\theta\\\cos\theta\sin\theta&\sin^2\theta\end{pmatrix}-I
=\begin{pmatrix}\cos2\theta&\sin2\theta\\\sin2\theta&-\cos2\theta\end{pmatrix}
$$

General rule: reflecting across a line at angle $\alpha$ has matrix $\begin{pmatrix}\cos2\alpha&\sin2\alpha\\\sin2\alpha&-\cos2\alpha\end{pmatrix}$. For $O$ the mirror is at $\alpha = 0$, for $D$ it is at $\alpha = \theta$.

## Combine: a rotation by $2\theta$
$$
G = DO=\begin{pmatrix}\cos2\theta&\sin2\theta\\\sin2\theta&-\cos2\theta\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}
=\begin{pmatrix}\cos2\theta&-\sin2\theta\\\sin2\theta&\cos2\theta\end{pmatrix}
$$

This is the standard matrix for a **rotation by $2\theta$**. After $k$ rounds:

$$
\boxed{G^k\lvert s\rangle\ \text{sits at angle}\ (2k+1)\theta}
$$

## The picture in words
- Mirror 1 (for $O$): the horizontal axis, at angle $0$.
- Mirror 2 (for $D$): the line through $\lvert s\rangle$, at angle $\theta$.
- Two reflections in a row rotate by **twice the angle between the mirrors**: $2\theta$.

## The picture
![[grover-2d-plane.svg|680]]

- Gray dashed line from $\lvert s\rangle$ to $O\lvert s\rangle$: reflection across the horizontal axis (mirror 1).
- Gray dashed line from $O\lvert s\rangle$ to $G\lvert s\rangle$: reflection across the purple dashed line through $\lvert s\rangle$ (mirror 2). It meets that mirror at a right angle, as every reflection does.

## Following one round with angles
Start at $+\theta$.
1. $O$ reflects across angle $0$: the state goes to $-\theta$. It is now $2\theta$ **below** the $\lvert s\rangle$ mirror ($\theta-(-\theta)=2\theta$).
2. $D$ reflects across the mirror at $\theta$: the image is $2\theta$ **above** the mirror, at $\theta+2\theta=3\theta$.

Net movement: $3\theta-\theta = 2\theta$.

Algebraic version: $O\lvert s\rangle = \cos2\theta\,\lvert s\rangle-\sin2\theta\,\lvert s^\perp\rangle$, so
$$
DO\lvert s\rangle=\cos2\theta\,\lvert s\rangle+\sin2\theta\,\lvert s^\perp\rangle
$$
which is at angle $\theta+2\theta=3\theta$.

## Why $O$ must come first
$D$ never does anything useful to $\lvert s\rangle$ alone ($D\lvert s\rangle=\lvert s\rangle$). The oracle pushes the state off the $\lvert s\rangle$ line, creating a perpendicular part, and only then does $D$ have something to flip. The two operations need each other.

> [!note] A common misreading
> $D$ does not directly "lower the horizontal part". It flips the part perpendicular to the $\lvert s\rangle$ line. The net result is that the horizontal part shrinks ($\cos3\theta<\cos\theta$) and the vertical grows ($\sin3\theta>\sin\theta$), but that is a consequence, not the mechanism.

## Checks
- $N=4$, $\theta=30^\circ$: one rotation by $60^\circ$ takes $30^\circ\to90^\circ$, exactly $\lvert w\rangle$.
- $N=8$, $\theta\approx20.7^\circ$: $O\lvert s\rangle=(0.935,-0.354)$. Overlap with $\lvert s\rangle=(0.935,0.354)$ is $0.749=\cos41.4^\circ$; with $\lvert s^\perp\rangle=(-0.354,0.935)$ it is $-0.662=-\sin41.4^\circ$ (and $2\theta=41.4^\circ$).

---
Previous: [[05 The Two-Dimensional Plane]] · Next: [[07 How Many Rounds]]
