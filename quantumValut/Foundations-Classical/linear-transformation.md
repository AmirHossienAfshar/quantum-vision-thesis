---
tags: [classical-cv, transformations, foundations, linear-algebra]
status: foundation
related:
  - "[[transformations-overview]]"
  - "[[affine-transformation]]"
---

# Linear Transformation

## One-line definition
A 2×2-matrix mapping of the plane that always fixes the origin — it can rotate, scale, shear, or reflect, but it can **never** translate.

## The math

$$
\begin{bmatrix} x' \\ y' \end{bmatrix} =
\begin{bmatrix} a & b \\ c & d \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}
$$

**4 free parameters**: $a, b, c, d$. No translation term at all — this is the whole story of what separates this note from [[affine-transformation]].

## Why it's called "linear" — the actual mathematical definition

This is worth pinning down properly, since "linear" isn't just a vague synonym for "simple" — it's a precise property from linear algebra, and it's the reason translation is excluded by definition, not by accident.

A transformation $T$ is called **linear** if it satisfies two properties, for any vectors $\vec{u}, \vec{v}$ and any scalar $k$:

1. **Additivity:** $T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v})$
2. **Homogeneity (scaling):** $T(k\vec{v}) = k \cdot T(\vec{v})$

Any transform expressible as "multiply by a matrix" automatically satisfies both — that's a general fact about matrix multiplication, not specific to 2×2. So "linear transformation" and "transformation representable by a plain matrix multiplication, no added constant" are the same thing.

**Why translation breaks this, concretely:** take homogeneity with $k=0$. It requires $T(0 \cdot \vec{v}) = 0 \cdot T(\vec{v})$, i.e. $T(\vec{0}) = \vec{0}$ — **every linear transformation must send the origin to itself.** But a translation by $(t_x, t_y) \neq (0,0)$ sends $(0,0) \to (t_x, t_y) \neq (0,0)$. So translation directly violates the defining property of linearity — it's not that a 2×2 matrix is *too small* to fit translation in; it's that translation is *structurally incompatible* with what "linear" means. This is exactly the fact [[affine-transformation]] leans on when it explains why a bare 2×2 matrix can't do the job and homogeneous coordinates are needed instead.

## The 4 parameters, in isolation

Same method as the affine note: hold everything else at its "do nothing" value, vary one thing at a time, and note that the identity transform is $a=1, b=0, c=0, d=1$.

### $a$ and $d$ — scaling along each axis

$$
\begin{bmatrix} x' \\ y' \end{bmatrix} =
\begin{bmatrix} a & 0 \\ 0 & d \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}
\quad\Rightarrow\quad
x' = a\cdot x, \quad y' = d \cdot y
$$

**Example — $a=2, d=1$, applied to $(3, 4)$:**

$$
\begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} 3 \\ 4 \end{bmatrix} =
\begin{bmatrix} 6 \\ 4 \end{bmatrix}
$$

$(3,4) \rightarrow (6,4)$ — doubled horizontally. Notice $(0,0)$ would map to $(0,0)$ under this same matrix — the origin never moves, no matter what $a$ and $d$ are.

### $b$ and $c$ — shear

$$
\begin{bmatrix} x' \\ y' \end{bmatrix} =
\begin{bmatrix} 1 & b \\ c & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}
\quad\Rightarrow\quad
x' = x + b\cdot y, \quad y' = y + c\cdot x
$$

**Example — $b=0.5, c=0$, applied to $(0, 10)$:**

$$
\begin{bmatrix} 1 & 0.5 \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} 0 \\ 10 \end{bmatrix} =
\begin{bmatrix} 5 \\ 10 \end{bmatrix}
$$

$(0,10) \rightarrow (5,10)$ — same shear behavior as the affine case, since shear doesn't need translation to exist; it's already a purely linear effect.

### Rotation — again, a combination, not a single parameter

$$
\begin{bmatrix} x' \\ y' \end{bmatrix} =
\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}
$$

**Example — $\theta=90°$, applied to $(10,0)$:**

$$
\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
\begin{bmatrix} 10 \\ 0 \end{bmatrix} =
\begin{bmatrix} 0 \\ 10 \end{bmatrix}
$$

$(10,0) \rightarrow (0,10)$ — identical result to the affine note's rotation example, because rotation never needed translation in the first place; rotation about the *origin* is already a purely linear operation. (Rotation about any *other* point does need translation — see [[affine-transformation]]'s "center of rotation" discussion — which is itself a nice demonstration of exactly where linear transformations stop being enough.)

### Reflection — a case linear transformations handle that's worth naming explicitly

$$
\begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}
=
\begin{bmatrix} -x \\ y \end{bmatrix}
$$

Mirrors every point across the $y$-axis. Reflections are linear (they fix the origin, and satisfy additivity/homogeneity), which is worth knowing since it's easy to mentally file "reflection" under "weird edge case" rather than recognizing it as an ordinary member of this same family (it's just a scaling matrix with a negative entry, as already shown in [[affine-transformation]]'s scaling section).

## What's identical to, and different from, [[affine-transformation]]

- **Identical:** scaling, shear, rotation, and reflection are all *already* fully linear — nothing about them requires translation. Every worked example above matches the corresponding affine example exactly, minus the padded $1$/$3\times3$ bookkeeping.
- **Different:** linear transformations always fix the origin; affine transformations don't have to. This is the *entire* difference — affine is not "a different kind of transform," it's "linear transform, plus the one thing linear transforms structurally cannot do."
