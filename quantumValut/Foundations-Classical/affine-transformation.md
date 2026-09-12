---
tags: [classical-cv, transformations, foundations]
status: foundation
related:
  - "[[transformations-overview]]"
  - "[[linear-transformation]]"
  - "[[projective-transformation]]"
  - "[[RANSAC]]"
  - "[[feature-matching-SIFT-ORB]]"
---

# Affine Transformation

## One-line definition
A 2D transformation that maps points using a linear transformation plus a translation, and **always preserves parallel lines**.

> Where this fits in the bigger picture — filtering vs. warping, and the full Linear → Affine → Projective naming hierarchy — now lives in [[transformations-overview]]. Short version: this note picks up exactly where [[linear-transformation]] leaves off, adding the one capability a bare 2×2 matrix structurally cannot have — translation.

## The math

An affine transform maps a point $(x, y)$ to $(x', y')$ via:

$$
\begin{bmatrix} x' \\ y' \end{bmatrix} =
\begin{bmatrix} a & b \\ c & d \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix} +
\begin{bmatrix} t_x \\ t_y \end{bmatrix}
$$

Or, in the common **homogeneous coordinates** form (this is the form that matters — it's what makes affine a special case of [[projective-transformation]]):

$$
\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} =
\begin{bmatrix} a & b & t_x \\ c & d & t_y \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
$$

**6 free parameters**: $a, b, c, d, t_x, t_y$.

## Homogeneous Coordinates — the formal definition

The earlier sections used the padded-$(x,y,1)$ trick without formally defining what homogeneous coordinates actually *are*. Worth doing properly, since it's a genuinely general concept (used well beyond just affine transforms), and it's what makes the "up to scale" language in [[projective-transformation]] make real sense later rather than sounding like a throwaway remark.

**The formal definition** (this is from Shree K. Nayar's *First Principles of Computer Vision* course): the homogeneous representation of a 2D point $\mathbf{p} = (x, y)$ is a **3D point** $\tilde{\mathbf{p}} = (\tilde x, \tilde y, \tilde z)$, where the third coordinate $\tilde z \neq 0$ is **fictitious** — it doesn't correspond to any real physical dimension, it's purely a bookkeeping device — such that:

$$
x = \frac{\tilde x}{\tilde z}, \qquad y = \frac{\tilde y}{\tilde z}
$$

**The key idea — this is an equivalence class, not a single representation:**

$$
\mathbf{p} \equiv \begin{bmatrix} x \\ y \\ 1 \end{bmatrix} \equiv \begin{bmatrix} \tilde z x \\ \tilde z y \\ \tilde z \end{bmatrix} \equiv \begin{bmatrix} \tilde x \\ \tilde y \\ \tilde z \end{bmatrix} = \tilde{\mathbf{p}}
$$

In plain words: **every scalar multiple of a homogeneous coordinate represents the exact same 2D point.** $(2, 4, 2)$, $(3, 6, 3)$, and $(1, 2, 1)$ all represent the single 2D point $(1, 2)$, because dividing each by its own third coordinate recovers $(1,2)$ every time. 

**Geometric picture:** think of the 3D point $\tilde{\mathbf{p}}=(\tilde x, \tilde y, \tilde z)$ as sitting somewhere on a line $L$ that passes through the origin. **Every point on that line except the origin itself** represents the *same* 2D point $\mathbf{p}$ — because every point on a line through the origin is some scalar multiple of every other point on it, and scalar multiples are exactly what the equivalence class above says don't matter. To recover the actual, concrete 2D coordinates, you intersect line $L$ with the plane $\tilde z = 1$ — that intersection point is exactly $(x, y, 1)$, the normalized representative this whole vault has been using directly. This is a genuinely useful mental image: a 2D point isn't one 3D point, it's an entire ray of them, and $(x,y,1)$ is just where that ray happens to cross the convenient reference plane.

**Why "fictitious" is the right word for $\tilde z$:** it isn't measuring anything real (not a depth, not a height) — it only exists to make the representation *homogeneous*, meaning every coordinate scales together consistently, which is precisely the property that lets a single matrix multiplication represent translation (covered next) and, more generally, is exactly the same "defined up to overall scale" property [[projective-transformation]] relies on when it says a homography has 9 matrix entries but only 8 independent parameters — that scale ambiguity is this equivalence class, just applied to the transformation matrix instead of to a point.

## Why a 3×3 matrix at all? Why the $[0,0,1]$ bottom row?

This is worth being precise about, because it's the single idea that makes everything downstream (RANSAC, homography, chaining transforms) work cleanly.

**The problem it solves:** a plain 2×2 matrix can only represent a *linear map* — rotation, scale, shear. It has no way to represent translation, because linear maps always send the origin $(0,0)$ to $(0,0)$ (multiply the zero vector by any matrix and you get the zero vector back). But translation moves the origin somewhere else. So with only a 2×2 matrix, you're stuck writing translation as a *separate* addition step, outside the matrix:

$$
\begin{bmatrix} x' \\ y' \end{bmatrix} = M \begin{bmatrix} x \\ y \end{bmatrix} + \vec{t}
$$

That's fine for a single transform, but it becomes a real problem the moment you want to **chain multiple transforms together** (e.g. "rotate, then translate, then scale" — exactly what happens when composing a sequence of image operations, or when RANSAC/DLT need to solve for a transform as one clean linear system). Matrix multiplication composes beautifully ($M_2 (M_1 \vec{x})= (M_2 M_1)\vec{x}$), but "matrix multiply, then add a vector" does **not** compose as cleanly — you end up with messy, separate bookkeeping for the linear part and the translation part at every step.

**The trick — homogeneous coordinates:** pad every 2D point with an extra coordinate fixed at $1$: $(x, y) \rightarrow (x, y, 1)$. Now embed the transform into a 3×3 matrix so that this extra coordinate is what *carries* the translation into the multiplication itself:

$$
\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} =
\begin{bmatrix} a & b & t_x \\ c & d & t_y \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
$$

Multiply this out by hand and you'll see exactly why it works:

$$
x' = a \cdot x + b \cdot y + t_x \cdot 1, \qquad y' = c \cdot x + d \cdot y + t_y \cdot 1
$$

The $t_x, t_y$ terms get pulled in *because* they're multiplied against that fixed $1$ in the third coordinate — which is the entire reason the extra coordinate was added in the first place. Translation is now baked into the matrix, not bolted on separately, so a single matrix multiplication does the whole job.

**So why is the bottom row specifically $[0, 0, 1]$, and not something else?** Two separate reasons, worth keeping distinct:

1. **The two zeros** ($0, 0$) exist so that $x$ and $y$ don't get mixed into the third output coordinate. Multiplying the bottom row against the input gives $0 \cdot x + 0 \cdot y + 1 \cdot 1 = 1$ — meaning the third coordinate of the output is *always exactly 1 again*, preserving the "point padded with a 1" format so the result can be fed right back into another transform (chaining) or reinterpreted as an ordinary 2D point $(x', y')$ with nothing further to do.
2. **This is precisely the constraint that homography removes.** [[projective-transformation]] replaces that bottom row with $[h_{31}, h_{32}, h_{33}]$ — general, non-zero values. That means the third output coordinate is no longer a guaranteed $1$; it becomes $w' = h_{31}x + h_{32}y + h_{33}$, a value that *depends on where the point is*. Recovering the real 2D point then requires dividing through: $x_{final} = x'/w'$. That position-dependent division is exactly the mechanism that creates perspective convergence — and it's completely absent here because affine's bottom row is frozen at $[0,0,1]$, which forces $w'=1$ everywhere, so the division always does nothing.

**One-sentence summary to remember:** the 3×3 form with $[0,0,1]$ on the bottom exists purely to let translation ride along inside ordinary matrix multiplication (via the padded $1$), and the frozen bottom row is exactly the thing that later gets "unfrozen" to produce homography's extra perspective power.

## Detailed breakdown of the 6 parameters

Each parameter has a specific, isolated geometric job. A good way to build intuition: set every other parameter to its "do-nothing" value and vary just one.

The **identity** transform (does nothing) has $a=1, d=1$, and everything else $0$:

$$
\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} =
\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
=
\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
$$

which is just the identity matrix — plugging any point in returns that same point unchanged, as expected.

### $t_x$ and $t_y$ — translation

$$
\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} =
\begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
\quad\Rightarrow\quad
x' = x + t_x, \quad y' = y + t_y
$$

Pure shift, no change to shape/size/orientation.

**Example — $t_x = 50,\ t_y = 0$, applied to the point $(10, 20)$:**

$$
\begin{bmatrix} 1 & 0 & 50 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} 10 \\ 20 \\ 1 \end{bmatrix} =
\begin{bmatrix} 60 \\ 20 \\ 1 \end{bmatrix}
$$

$(10,20) \rightarrow (60,20)$ — shifted 50 pixels right, height unchanged.

### $a$ and $d$ — scaling along each axis

$$
\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} =
\begin{bmatrix} a & 0 & 0 \\ 0 & d & 0 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
\quad\Rightarrow\quad
x' = a \cdot x, \quad y' = d \cdot y
$$

- $a=d$ → **uniform scaling** (image gets uniformly bigger/smaller, aspect ratio preserved).
- $a \neq d$ → **non-uniform scaling / stretch** (aspect ratio changes — e.g. image gets wider but not taller).
- Negative $a$ or $d$ → **flip/mirror** along that axis, in addition to any scaling.

**Example — $a=2, d=1$ (stretch width only), applied to $(10, 20)$:**

$$
\begin{bmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} 10 \\ 20 \\ 1 \end{bmatrix} =
\begin{bmatrix} 20 \\ 20 \\ 1 \end{bmatrix}
$$

$(10,20) \rightarrow (20,20)$ — doubled horizontally, height untouched.

**Example — $a=-1, d=1$ (horizontal mirror), applied to $(10, 20)$:**

$$
\begin{bmatrix} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} 10 \\ 20 \\ 1 \end{bmatrix} =
\begin{bmatrix} -10 \\ 20 \\ 1 \end{bmatrix}
$$

$(10,20) \rightarrow (-10,20)$ — flipped across the $y$-axis.

### $b$ and $c$ — shear (skew)

$$
\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} =
\begin{bmatrix} 1 & b & 0 \\ c & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
\quad\Rightarrow\quad
x' = x + b \cdot y, \quad y' = y + c \cdot x
$$

- $b \neq 0$: horizontal shear — how much a point's $x$-position shifts depending on its **height** ($y$). Think of pushing the top of a rectangle sideways while the bottom stays put → turns a rectangle into a parallelogram leaning left/right.
- $c \neq 0$: vertical shear — how much a point's $y$-position shifts depending on its **horizontal position** ($x$). Pushes the right side of a rectangle up or down while the left stays put.

**Example — $b=0.5, c=0$, applied to $(0, 10)$:**

$$
\begin{bmatrix} 1 & 0.5 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} 0 \\ 10 \\ 1 \end{bmatrix} =
\begin{bmatrix} 5 \\ 10 \\ 1 \end{bmatrix}
$$

$(0,10) \rightarrow (5,10)$ — the higher up a point is, the more it gets pushed sideways, which is the classic "italic text" leaning effect. A point at $y=0$ under this same matrix wouldn't move at all.

### Rotation — a combination, not a single parameter

There's no single dedicated "rotation parameter" in $a,b,c,d,t_x,t_y$ — rotation by angle $\theta$ comes from a specific *combination* of $a,b,c,d$:

$$
\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} =
\begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
$$

i.e. $a=\cos\theta,\ b=-\sin\theta,\ c=\sin\theta,\ d=\cos\theta$.

#### What exactly is $\theta$?

Worth pinning down precisely, since it's easy to get its direction backwards in practice.

- **Units:** $\theta$ is an angle, and the trig functions here expect **radians**, not degrees, in almost every programming context (NumPy, math libraries, etc.). $90°$ is $\pi/2$ radians, $180°$ is $\pi$, a full turn ($360°$) is $2\pi$. If code produces a wildly wrong-looking rotation, converting degrees→radians incorrectly (or forgetting to convert at all) is a very common cause.
- **Sign convention — counterclockwise is positive:** with the matrix written exactly as above, increasing $\theta$ from $0$ rotates points **counterclockwise** around the origin, in the standard math convention where the $x$-axis points right and the $y$-axis points **up**. This matters a lot for image work, covered next.
- **The image-coordinate gotcha:** in most image libraries (OpenCV, NumPy arrays, pixel coordinates in general), the $y$-axis points **down**, not up — row index increases as you go down the image. Flipping the direction $y$ points in effectively flips the visual sense of the rotation: a positive $\theta$ that looks counterclockwise in standard math coordinates will appear to rotate points **clockwise** when you actually render it on an image. This is a frequent source of "my rotation went the wrong way" bugs — worth testing on a real image with a known asymmetric shape (not a symmetric one like a circle, where you can't visually tell direction) to confirm which way your specific pipeline actually rotates.
- **Range:** $\theta$ is periodic — $\theta$ and $\theta + 2\pi$ (i.e. $+360°$) produce the identical matrix and identical result, since $\cos$ and $\sin$ are periodic. In practice you'd normally only ever care about $\theta \in [0, 2\pi)$ or equivalently $(-\pi, \pi]$.
- **Center of rotation:** the matrix above always rotates around the **origin** $(0,0)$ — e.g. the top-left corner of an image, in typical image coordinates. Rotating around the *center* of an image instead (the usual desired behavior) isn't a different parameter — it's done by composing three transforms: translate the center to the origin, rotate by $\theta$, then translate back. This composition is exactly why the matrix form (rather than the separate "matrix + add vector" form from the very first section) matters in practice — chaining these three steps is just multiplying three 3×3 matrices together into one combined matrix.

**A second worked example, to make the direction convention concrete — $\theta = 45°$ applied to $(1, 0)$:** $\cos 45° = \sin 45° = \tfrac{\sqrt{2}}{2} \approx 0.707$:

$$
\begin{bmatrix} 0.707 & -0.707 & 0 \\ 0.707 & 0.707 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} =
\begin{bmatrix} 0.707 \\ 0.707 \\ 1 \end{bmatrix}
$$

$(1,0) \rightarrow (0.707, 0.707)$ — the point swings halfway between the positive $x$-axis and positive $y$-axis, confirming the counterclockwise direction (in standard math coordinates) for a positive angle.

**Example — $\theta = 90°$, applied to $(10, 0)$:** since $\cos 90°=0,\ \sin 90°=1$:

$$
\begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} 10 \\ 0 \\ 1 \end{bmatrix} =
\begin{bmatrix} 0 \\ 10 \\ 1 \end{bmatrix}
$$

$(10,0) \rightarrow (0,10)$ — a quarter-turn rotation about the origin: the point swings from sitting on the positive $x$-axis onto the positive $y$-axis.

### The entangled nature of $a, b, c, d$ — worth sitting with

The "6 parameters" aren't 6 independent named effects (translate-x, translate-y, rotate, scale-x, scale-y, shear) even though that's how affine is often *described* in words — rotation, scaling, and shear are actually entangled together inside just the 4 numbers $a,b,c,d$, and only translation ($t_x, t_y$) is cleanly separate in its own matrix slot. A general affine matrix is usually some blended combination of rotation + scale + shear all at once, not one applied cleanly after another — decomposing an arbitrary $a,b,c,d$ back into "pure" rotation/scale/shear components requires matrix decomposition (e.g. SVD or QR decomposition on the 2×2 part), not just reading the four numbers off directly.

## Linearity and composability — why a chain of transforms collapses into one matrix

This is really the payoff of putting everything in the homogeneous 3×3 form in the first place, and it's worth being explicit about it rather than leaving it implicit.

**The underlying fact:** matrix multiplication is **associative**. If you apply transform $M_1$ to a point, then transform $M_2$ to the result, then $M_3$ to that result:

$$
\vec{x}' = M_3 \left( M_2 \left( M_1 \vec{x} \right) \right)
$$

associativity means you're free to group the multiplications however you like:

$$
\vec{x}' = \left( M_3 M_2 M_1 \right) \vec{x}
$$

The parenthesized product $M_{combined} = M_3 M_2 M_1$ is itself just another 3×3 matrix — computed **once**, up front, by multiplying the three matrices together — and after that, applying the *entire* three-step chain to any point is a single matrix-vector multiplication, not three separate ones.

**Why this matters practically, not just theoretically:** an image has potentially millions of pixels. If you had to cascade three separate matrix multiplications for every single pixel, that's 3× the work per pixel, for every pixel. Collapse the chain into one combined matrix first, and it's exactly one matrix-vector multiply per pixel — the "3 steps" only ever get multiplied together *once*, regardless of how many points you apply the result to. This is precisely why homogeneous coordinates are the standard representation in graphics/vision libraries rather than a mathematical curiosity — the payoff is computational, not just notational.

**Concrete case, tying back to the center-of-rotation example above:** "rotate about the image center" was built from three separate steps — translate center-to-origin ($T_1$), rotate ($R$), translate back ($T_2$). Written out:

$$
M_{combined} = T_2 \cdot R \cdot T_1
$$

Multiply those three 3×3 matrices together **one time**, and $M_{combined}$ is now a single ordinary-looking affine matrix (some new set of $a,b,c,d,t_x,t_y$ values) — indistinguishable in form from any of the single-step examples earlier in this note, even though it represents a 3-step composite operation. This is exactly why, no matter how many affine operations you chain (translate, rotate, scale, shear, in any order, any number of times), the *result* is always still expressible as a single 3×3 matrix with the same $[0,0,1]$ bottom row — chaining affine transforms can never "escape" the affine family and accidentally produce a homography, because multiplying matrices that all have a $[0,0,1]$ bottom row together always produces another matrix with a $[0,0,1]$ bottom row (the zeros and the 1 are preserved under this multiplication — worth verifying by hand once as a small proof to yourself).

**One important order-of-operations gotcha:** matrix multiplication is associative but **not commutative** — $M_2 M_1 \neq M_1 M_2$ in general, so "rotate then translate" gives a different combined matrix than "translate then rotate." The order you multiply the matrices in must match the order you conceptually want the operations to happen, read **right to left** against the point vector (the rightmost matrix is applied to the point first).

## What it can represent

Affine transforms are built from combinations of:
- **Translation** (shift)
- **Rotation**
- **Scaling** (uniform or non-uniform, i.e. stretch)
- **Shear** (skew)

## What it can NOT represent

This is the important boundary to remember: **affine transforms cannot represent perspective distortion.**

The bottom row of the matrix is always fixed at $[0, 0, 1]$. That fixed bottom row is *exactly* why parallel lines in the input always stay parallel in the output — there's no mechanism in the matrix for lines to converge toward a vanishing point.

> This is the single fact that separates affine from [[projective-transformation]]. Homography frees up that bottom row, which is what allows convergence (perspective effects) to appear.

## Visual intuition

- Take a square. Apply affine transforms → you can get any parallelogram (rotated, stretched, skewed, shifted) — but it will **never** look like a tilted rectangle viewed at an angle (a trapezoid shape). That trapezoid effect requires [[projective-transformation]].
- Real-world scenario where affine is the *correct* model (not an approximation): a flatbed scanner, or a satellite/orthographic view where the camera is effectively infinitely far away and looking straight down — no perspective convergence happens.
- Real-world scenario where affine is an *approximation* that breaks: a handheld photo of a book on a table taken at an angle. This needs full homography.

## Degrees of freedom, in context

Affine sits at **6 DOF**, exactly 2 more than [[linear-transformation]]'s 4 (the two extra being $t_x, t_y$), and exactly 2 fewer than [[projective-transformation]]'s 8. Full comparison table across every tier lives in [[transformations-overview]].
