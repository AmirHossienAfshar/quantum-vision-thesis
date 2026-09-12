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

**9 matrix entries, but only 8 independent parameters** — the matrix is only defined up to overall scale (multiplying every entry by the same constant gives the same transform), so by convention we fix $h_{33} = 1$ and solve for the remaining 8.

This division step is the whole story of *why* homography can do what [[affine-transformation]] can't: that $w'$ denominator is what's absent in the affine case (affine's bottom row is fixed at $[0,0,1]$, so $w'$ is always exactly 1, and the division does nothing). Letting $w'$ vary with position is exactly what creates convergence toward a vanishing point — i.e., perspective distortion. This is also the exact spot where the [[transformations-overview]] hierarchy's "each tier unfreezes one more constraint" idea plays out concretely: affine froze the bottom row at $[0,0,1]$; projective unfreezes it.

## When does homography exactly (not approximately) apply?

Two, and only two, situations:
1. **The imaged surface is planar** (a flat wall, a book cover, a printed page, a sports field).
2. **The camera only rotates between the two shots — no translation** (this is why panorama stitching works even when photographing a 3D scene like a landscape: pivoting a camera on a tripod is pure rotation).

If neither condition holds (e.g. a 3D scene, photographed from two different positions), a single global homography won't be exactly correct — you'd need per-plane local homographies, or a different model (epipolar geometry / fundamental matrix) entirely. Worth remembering as a limitation, not a universal tool.

## Estimating a homography (the pipeline)

1. Detect features in both images ([[feature-matching-SIFT-ORB]]).
2. Match descriptors → candidate correspondences (includes wrong matches).
3. **DLT (Direct Linear Transform)**: given ≥4 point correspondences, set up a linear system and solve for the 8 unknown parameters (typically via SVD).
4. **RANSAC** wraps step 3 in a robust loop: repeatedly sample minimal point sets, compute a candidate homography, count inliers, keep the best. See [[RANSAC]].
5. (Optional) refine the final homography with least-squares over all inliers.

## Where this sits in the hierarchy

| Transform | DOF | Can represent perspective convergence? | Note |
|---|---|---|---|
| [[linear-transformation]] | 4 | No | fixes the origin too |
| [[affine-transformation]] | 6 | No | preserves parallel lines |
| **Projective / Homography** | **8** | **Yes** | this note |

