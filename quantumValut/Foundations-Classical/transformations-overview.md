---
tags: [classical-cv, transformations, foundations, overview]
status: foundation
related:
  - "[[linear-transformation]]"
  - "[[affine-transformation]]"
  - "[[projective-transformation]]"
  - "[[RANSAC]]"
  - "[[feature-matching-SIFT-ORB]]"
---

# Transformations — Bird's-Eye View

> This note is the map. It doesn't derive any matrix in detail — [[linear-transformation]], [[affine-transformation]], and [[projective-transformation]] each do that for their own case. This note exists to show how they relate to each other and to the bigger picture of "what is an image operation."

## Where transformations sit in the bigger picture: filtering vs. warping

From Shree K. Nayar's *First Principles of Computer Vision* course — a genuinely useful framing, since it cleanly separates two categories of image operation that are easy to blur together.

**Image Filtering — changes the range** (i.e. the pixel *values*, brightness/color):

$$
g(x,y) = T_r\big(f(x,y)\big)
$$

The coordinates $(x,y)$ themselves don't move — only what's *stored* at each coordinate changes. Brightening, contrast adjustment, blurring, sharpening — all of these are $T_r$-type operations.

**Image Warping — changes the domain** (i.e. *where* each pixel's content ends up):

$$
g(x,y) = f\big(T_d(x,y)\big)
$$

Here $T_d$ is explicitly a **coordinate-changing operator** — it doesn't touch pixel values directly at all; it decides which input coordinate's value gets placed at each output coordinate. **Everything in this vault's transformations family — linear, affine, projective — is a specific choice of what $T_d$ is allowed to be.** They differ only in how flexible that choice is.

Worth remembering as a mental checkpoint when reading other notes: [[normalized-cross-correlation]] and [[feature-matching-SIFT-ORB]] operate on pixel *values* at fixed positions (closer to the $T_r$ side of the world, in the sense that they read values rather than move them), while everything about *finding where a template moved to* is fundamentally a $T_d$/warping question. Keeping these two categories distinct helps clarify which problem a given method is actually solving.

## Naming hierarchy: Linear → Affine → Projective

**Is a 2×2 transformation called "affine"? No** — it has its own, separate name, and the distinction matters, both mathematically and for getting vocabulary right in front of my professor.

Straight out of the course's own "Projective Transformation" slide, the properties in the last three columns are worth tracking explicitly across every tier, since they're exactly what changes (and doesn't) as you move up the hierarchy:

| Transform | Matrix form | DOF | What it can do | Straight lines stay straight? | Parallel lines stay parallel? | Origin maps to origin? | Note page |
|---|---|---|---|---|---|---|---|
| **Linear** | $2\times 2$, applied alone (no added translation) | 4 | rotation, scaling, shear, reflection | Yes | Yes | **Yes, always** | [[linear-transformation]] |
| **Affine** | $2\times 2$ **+ a separate translation vector**, or equivalently a $3\times3$ homogeneous matrix with bottom row fixed at $[0,0,1]$ | 6 | everything linear can do, **plus** translation | Yes | **Yes** | No | [[affine-transformation]] |
| **Projective / Homography** | $3\times 3$ homogeneous matrix, **bottom row free** ($[h_{31}, h_{32}, h_{33}]$, not fixed) | 8 | everything affine can do, **plus** perspective convergence | **Yes** | **Not necessarily** | **Not necessarily** | [[projective-transformation]] |

A few things worth being explicit about, since the names encode real mathematical containment, not just vocabulary:

- **Linear transformations are a strict subset of affine ones.** Set $t_x = t_y = 0$ in an affine matrix and it collapses back into a plain linear transformation. This is *why* a 2×2 matrix alone can never be called "affine": affine's defining feature, by name and definition, is that it includes translation, and a bare 2×2 matrix structurally cannot represent translation at all — see [[linear-transformation]] for exactly why not.
- **Affine transformations are a strict subset of projective ones.** Set the bottom row to $[0,0,1]$ in a general 3×3 projective matrix and it collapses into an affine transform — see [[affine-transformation]] and [[projective-transformation]] for the mechanics of that boundary.
- So the containment chain is: **Linear $\subset$ Affine $\subset$ Projective**. Each step widens what's allowed by unfreezing exactly one more constraint (first "must fix the origin," then "bottom row must be $[0,0,1]$").
- The course's phrase **"3×3 transformations are called projective transformations"** is really shorthand for "a fully general 3×3 homogeneous matrix, with no constraints on the bottom row." Both affine and linear transforms *can* be written in 3×3 homogeneous form too, but they're special/constrained cases of that general 3×3 form, not what the name "projective" refers to on its own. The name is reserved for the unconstrained version — the one that actually needs that bottom row to do something.
- The two properties that actually change as you go from affine to projective are the interesting ones to remember: **straightness survives every single tier** (it's the one thing that never breaks, all the way up to full projective — a huge reason lines are the natural feature to match on in [[feature-matching-SIFT-ORB]] / [[RANSAC]]-style pipelines), but **parallelism only survives through affine** and is exactly what projective is willing to sacrifice in exchange for representing perspective convergence. See [[projective-transformation]] for the full worked explanation of *why* parallel lines stop being preserved — it's the same $w'$-division mechanism covered there.
