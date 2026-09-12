---
aliases: [Homography, Projective Transform]
tags: [classical-cv, transformations, foundations, thesis-core]
status: foundation
related:
  - "[[transformations-overview]]"
  - "[[affine-transformation]]"
  - "[[linear-transformation]]"
  - "[[RANSAC]]"
  - "[[feature-matching-SIFT-ORB]]"
  - "[[normalized-cross-correlation]]"
---

# Projective Transformation (Homography)

> Naming note: "projective transformation" is the formal linear-algebra name; **"homography"** is the term almost universally used in computer vision for the same thing. I'll use both interchangeably in this note, leaning on "homography" for the CV-specific discussion since that's what the papers I'm reading call it. See [[transformations-overview]] for exactly how this tier relates to [[linear-transformation]] and [[affine-transformation]].

## One-line definition
A 3×3 matrix that describes the projective mapping between two views of the **same planar surface**, or between two photos taken from the **same camera center** (pure rotation, no translation).

## The math

$$
\begin{bmatrix} x' \\ y' \\ w' \end{bmatrix} =
\begin{bmatrix} h_{11} & h_{12} & h_{13} \\ h_{21} & h_{22} & h_{23} \\ h_{31} & h_{32} & h_{33} \end{bmatrix}
\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
$$

To get back to actual pixel coordinates, divide through by $w'$:

$$
x_{final} = x'/w', \quad y_{final} = y'/w'
$$

**9 matrix entries, but only 8 independent parameters** — worth deriving properly rather than just stating, since it's a genuinely different reason than "affine has 6 out of a 3×3's 9 slots because 3 are frozen at $[0,0,1]$."

## Why 8 parameters, not 9? — the scale-ambiguity argument

**The core fact:** scale $H$ by any nonzero constant $k$, and it represents the *exact same* transformation:

$$
H\tilde{\mathbf{p}}_1 \equiv k H \tilde{\mathbf{p}}_1 \qquad \text{for any } k \neq 0
$$

Written out with the actual matrix:

$$
\begin{bmatrix} h_{11} & h_{12} & h_{13} \\ h_{21} & h_{22} & h_{23} \\ h_{31} & h_{32} & h_{33} \end{bmatrix}
\begin{bmatrix} \tilde x_1 \\ \tilde y_1 \\ \tilde z_1 \end{bmatrix}
\;\equiv\;
\begin{bmatrix} \tilde x_2 \\ \tilde y_2 \\ \tilde z_2 \end{bmatrix}
\;\equiv\;
k
\begin{bmatrix} h_{11} & h_{12} & h_{13} \\ h_{21} & h_{22} & h_{23} \\ h_{31} & h_{32} & h_{33} \end{bmatrix}
\begin{bmatrix} \tilde x_1 \\ \tilde y_1 \\ \tilde z_1 \end{bmatrix}
$$

**Why this is true — it traces straight back to homogeneous coordinates:** the output $(\tilde x_2, \tilde y_2, \tilde z_2)$ is itself a [[affine-transformation#Homogeneous Coordinates — the formal definition|homogeneous coordinate]], meaning it represents a 2D point as an *entire equivalence class* — $(\tilde x_2, \tilde y_2, \tilde z_2)$ and $k(\tilde x_2, \tilde y_2, \tilde z_2)$ recover the identical real 2D point once you divide through by the third coordinate. Multiplying the whole matrix $H$ by $k$ just scales every entry of the output by $k$ too — which lands you on a different representative of the *same* equivalence class, not a different point. So $H$ and $kH$ are indistinguishable as far as the actual 2D-to-2D mapping is concerned; there's a whole family (a "ray" of matrices, in the exact same sense as the point-ray picture from the homogeneous-coordinates slide) that all do the same job.

**So the raw count of 9 matrix entries overstates the real freedom by exactly one — you need to pin down which representative of the family you're using.** Two equally valid ways to do that, both of which remove exactly one degree of freedom:

1. **Fix one entry directly** — set $h_{33} = 1$ (the convention used earlier in this note) and solve for the remaining 8.
2. **Fix the overall norm** — the course slide's convention: require $\sqrt{\sum_{i,j} h_{ij}^2} = 1$ (the matrix, treated as a flat 9-entry vector, has unit length). This is a different specific representative than $h_{33}=1$, but it removes the same one degree of freedom, for the same underlying reason.

Either convention is fine, and they'll generally give numerically different-looking matrices for the same real transformation — worth remembering when comparing $H$ matrices from different tools/papers, since a mismatch in raw numbers doesn't necessarily mean a mismatch in the actual transformation, if they used different normalization conventions.

**One more property, worth keeping in mind as a checklist:**
- **Origin does not necessarily map to the origin** — unlike [[linear-transformation]] (which *always* fixes the origin) and unlike affine's translation-only origin behavior, a general homography can send $(0,0)$ anywhere, because the $w'$-division makes the mapping position-dependent in a way translation alone doesn't.
- **Lines map to lines** — straightness survives (see [[transformations-overview]]'s comparison table), a direct consequence of the ray-through-a-point construction above: a straight ray can't bend, so a straight line's image under a central projection is still straight.
- **Parallel lines do not necessarily remain parallel** — this is the flip side of the perspective-convergence behavior; see the [[transformations-overview]] table for how this compares across every tier.
- **Closed under composition** — chaining two homographies together always produces another single homography, exactly the same closure property [[affine-transformation]]'s "Linearity and composability" section proves for the affine case, just one level up the hierarchy. This is also the fact that made the earlier "one point vs. two cameras" discussion work: composing $H_{O_1}$ (object plane → photo 1) with $H_{O_2}^{-1}$ (photo 2 → object plane) still yields one valid homography $H_{1\to2}$, even though no single physical point generates it directly.

This division step is the whole story of *why* homography can do what [[affine-transformation]] can't: that $w'$ denominator is what's absent in the affine case (affine's bottom row is fixed at $[0,0,1]$, so $w'$ is always exactly 1, and the division does nothing). Letting $w'$ vary with position is exactly what creates convergence toward a vanishing point — i.e., perspective distortion. This is also the exact spot where the [[transformations-overview]] hierarchy's "each tier unfreezes one more constraint" idea plays out concretely: affine froze the bottom row at $[0,0,1]$; projective unfreezes it.

## The geometric picture: mapping one plane to another through a point

The algebra above ($\tilde{\mathbf{p}}_2 = H \tilde{\mathbf{p}}_1$, using the [[affine-transformation#Homogeneous Coordinates — the formal definition|homogeneous coordinates]] convention) has a genuinely elegant geometric story behind it, from the same course as the homogeneous-coordinates slide, and it's worth knowing because it's *the* reason this transform is called "projective" in the first place — not an arbitrary name.

**The setup:** two planes, $\Pi_1$ and $\Pi_2$, sitting in 3D space, plus a single fixed **point** somewhere between (or behind) them. For any point $\tilde{\mathbf{p}}_1$ on $\Pi_1$, draw a straight ray from it through that fixed point, and continue the ray until it hits $\Pi_2$ — wherever it lands is $\tilde{\mathbf{p}}_2$, the corresponding point. Do this for every point on $\Pi_1$ and you get a complete mapping from $\Pi_1$ to $\Pi_2$. **That mapping is exactly a homography:**

$$
\tilde{\mathbf{p}}_2 = H\tilde{\mathbf{p}}_1
$$

written out in full:

$$
\begin{bmatrix} \tilde x_2 \\ \tilde y_2 \\ \tilde z_2 \end{bmatrix} =
\begin{bmatrix} h_{11} & h_{12} & h_{13} \\ h_{21} & h_{22} & h_{23} \\ h_{31} & h_{32} & h_{33} \end{bmatrix}
\begin{bmatrix} \tilde x_1 \\ \tilde y_1 \\ \tilde z_1 \end{bmatrix}
$$

Same matrix, same equation as above — just written with subscripts for "plane 1's point" and "plane 2's point" instead of generic primes, which makes the two-planes-and-a-point picture explicit.


## When does homography exactly (not approximately) apply?

Two, and only two, situations:
1. **The imaged surface is planar** (a flat wall, a book cover, a printed page, a sports field).
2. **The camera only rotates between the two shots — no translation** (this is why panorama stitching works even when photographing a 3D scene like a landscape: pivoting a camera on a tripod is pure rotation).

If neither condition holds (e.g. a 3D scene, photographed from two different positions), a single global homography won't be exactly correct — you'd need per-plane local homographies, or a different model (epipolar geometry / fundamental matrix) entirely. Worth remembering as a limitation, not a universal tool.


