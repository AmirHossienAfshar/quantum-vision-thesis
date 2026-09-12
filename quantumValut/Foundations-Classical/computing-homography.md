---
tags: [classical-cv, transformations, linear-algebra, thesis-core]
status: foundation
related:
  - "[[projective-transformation]]"
  - "[[RANSAC]]"
  - "[[feature-matching-SIFT-ORB]]"
  - "[[transformations-overview]]"
---

# Computing Homography

> This is the derivation [[projective-transformation]] points to under "Estimating a homography (the pipeline)," step 3 (DLT). That note treats it as a black box; this note opens the box.

## The setup

We have $n$ point correspondences from [[feature-matching-SIFT-ORB]]: source points $(x_s^{(i)}, y_s^{(i)})$ on $\Pi_1$ matched to destination points $(x_d^{(i)}, y_d^{(i)})$ on $\Pi_2$, for $i = 1, \dots, n$. We want the $3\times3$ homography $H$ (9 entries, $h_{11}$ through $h_{33}$) satisfying $\tilde{\mathbf{p}}_d \equiv H\tilde{\mathbf{p}}_s$ for every correspondence — using $\equiv$ deliberately, since [[projective-transformation]] already established this only holds **up to scale**, not as an exact equality.

## Step 1 — turning one correspondence into two linear equations

$\tilde{\mathbf{p}}_d \equiv H\tilde{\mathbf{p}}_s$ means $H\tilde{\mathbf{p}}_s$ and $\tilde{\mathbf{p}}_d$ point in the same direction but not necessarily the same length — so there's some unknown nonzero scale factor $\lambda$ connecting them:

$$
\begin{bmatrix} h_{11}x_s + h_{12}y_s + h_{13} \\ h_{21}x_s + h_{22}y_s + h_{23} \\ h_{31}x_s + h_{32}y_s + h_{33} \end{bmatrix} = \lambda \begin{bmatrix} x_d \\ y_d \\ 1 \end{bmatrix}
$$

(dropping the $(i)$ superscripts for a moment — this is per-correspondence). The third row directly tells us what $\lambda$ *is*: $\lambda = h_{31}x_s + h_{32}y_s + h_{33}$. Substituting that into the first two rows eliminates the unknown $\lambda$ entirely:

$$
h_{11}x_s + h_{12}y_s + h_{13} - x_d(h_{31}x_s + h_{32}y_s + h_{33}) = 0
$$
$$
h_{21}x_s + h_{22}y_s + h_{23} - y_d(h_{31}x_s + h_{32}y_s + h_{33}) = 0
$$

Regrouping to explicitly show every $h_{ij}$ as a coefficient (some coefficients are just $0$):

$$
x_s h_{11} + y_s h_{12} + h_{13} + 0\cdot h_{21} + 0\cdot h_{22} + 0\cdot h_{23} - x_d x_s\, h_{31} - x_d y_s\, h_{32} - x_d\, h_{33} = 0
$$
$$
0\cdot h_{11} + 0\cdot h_{12} + 0\cdot h_{13} + x_s h_{21} + y_s h_{22} + h_{23} - y_d x_s\, h_{31} - y_d y_s\, h_{32} - y_d\, h_{33} = 0
$$

This is exactly the two-row pattern in the slide's matrix — **one correspondence gives exactly 2 linear equations in the 9 unknowns $h_{11},\dots,h_{33}$**, not 3, because the third equation ($\lambda$'s definition) was used up eliminating $\lambda$ rather than contributing an independent constraint.

## Step 2 — stacking every correspondence into one matrix equation

Every correspondence contributes its own two rows, all sharing the same 9 unknowns. Stack all $n$ correspondences and collect the unknowns into a single vector $\mathbf{h} = [h_{11}, h_{12}, h_{13}, h_{21}, h_{22}, h_{23}, h_{31}, h_{32}, h_{33}]^T$:

$$
A\mathbf{h} = \mathbf{0}
$$

Written out in full — this is the exact matrix from the slide, and it's worth actually looking at rather than just knowing it exists, since the repeating two-row block per correspondence is what makes the whole structure click:

$$
\underbrace{\begin{bmatrix}
x_s^{(1)} & y_s^{(1)} & 1 & 0 & 0 & 0 & -x_d^{(1)}x_s^{(1)} & -x_d^{(1)}y_s^{(1)} & -x_d^{(1)} \\
0 & 0 & 0 & x_s^{(1)} & y_s^{(1)} & 1 & -y_d^{(1)}x_s^{(1)} & -y_d^{(1)}y_s^{(1)} & -y_d^{(1)} \\
& & & & \vdots & & & & \\
x_s^{(i)} & y_s^{(i)} & 1 & 0 & 0 & 0 & -x_d^{(i)}x_s^{(i)} & -x_d^{(i)}y_s^{(i)} & -x_d^{(i)} \\
0 & 0 & 0 & x_s^{(i)} & y_s^{(i)} & 1 & -y_d^{(i)}x_s^{(i)} & -y_d^{(i)}y_s^{(i)} & -y_d^{(i)} \\
& & & & \vdots & & & & \\
x_s^{(n)} & y_s^{(n)} & 1 & 0 & 0 & 0 & -x_d^{(n)}x_s^{(n)} & -x_d^{(n)}y_s^{(n)} & -x_d^{(n)} \\
0 & 0 & 0 & x_s^{(n)} & y_s^{(n)} & 1 & -y_d^{(n)}x_s^{(n)} & -y_d^{(n)}y_s^{(n)} & -y_d^{(n)}
\end{bmatrix}}_{A \text{ (known — every entry comes from matched pixel coordinates)}}
\begin{bmatrix} h_{11} \\ h_{12} \\ h_{13} \\ h_{21} \\ h_{22} \\ h_{23} \\ h_{31} \\ h_{32} \\ h_{33} \end{bmatrix}
=
\begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ 0 \\ \vdots \\ 0 \\ 0 \end{bmatrix}
$$

Two things worth actually noticing by looking at this, rather than just the compact $A\mathbf{h}=\mathbf{0}$ form:

- **$A$ is $2n \times 9$** — every correspondence adds exactly the same two-row template shown above, just with that correspondence's own $(x_s, y_s, x_d, y_d)$ plugged in. This is why $n=4$ correspondences give a $8\times9$ matrix — 8 equations for 9 unknowns (9, not 8, because the scale ambiguity hasn't been removed yet at this stage — that happens in Step 3).
- **$\mathbf{h}$ never appears inside $A$** — every single entry of $A$ is a known number the moment you have your matched points; $\mathbf{h}$ is the only unknown in the whole equation, which is exactly what makes this a *linear* system, solvable with the machinery below, rather than something needing iterative nonlinear optimization.

$A$ is the "(Known)" label directly from the slide. $\mathbf{h}$ is what we're solving for.

## Step 3 — why we can't just solve $A\mathbf{h}=\mathbf{0}$ directly, and where the constraint comes from

$A\mathbf{h} = \mathbf{0}$ is a **homogeneous** linear system, and homogeneous systems always have the trivial solution $\mathbf{h} = \mathbf{0}$ — which is useless here, since $H = \mathbf{0}$ isn't a valid transform at all. We need to explicitly exclude it.

This is the *exact same scale-ambiguity fact* already established in [[projective-transformation]]'s "why 8 parameters, not 9" section: since $H$ and $kH$ represent the identical transformation for any $k \neq 0$, if $\mathbf{h}$ solves $A\mathbf{h}=\mathbf{0}$, so does $k\mathbf{h}$ for *any* $k$ — including $k=0$, which is exactly the trivial solution sneaking back in. So we need to pin down one specific representative, exactly as before — and the slide picks the same convention already flagged there: **fix $\|\mathbf{h}\|^2 = 1$.**

## Step 4 — Constrained Least Squares

In practice, with real (noisy) matched points, $A\mathbf{h}=\mathbf{0}$ typically has **no exact nontrivial solution** at all once $n > 4$ (more equations than unknowns, and measurement noise means they won't be perfectly consistent). So instead of solving it exactly, we look for the $\mathbf{h}$ that gets *closest* to satisfying it, in a least-squares sense, while still respecting the unit-norm constraint:

$$
\min_{\mathbf{h}} \|A\mathbf{h}\|^2 \quad \text{such that} \quad \|\mathbf{h}\|^2 = 1
$$

Expand both pieces algebraically (this is just how squared-norms of vectors expand as a quadratic form):

$$
\|A\mathbf{h}\|^2 = (A\mathbf{h})^T(A\mathbf{h}) = \mathbf{h}^T A^T A\, \mathbf{h}, \qquad \|\mathbf{h}\|^2 = \mathbf{h}^T\mathbf{h} = 1
$$

So the problem becomes: $\min_{\mathbf{h}} \left(\mathbf{h}^T A^T A\, \mathbf{h}\right)$ subject to $\mathbf{h}^T\mathbf{h} = 1$.

## Step 5 — solving the constraint via Lagrange multipliers

Constrained optimization → introduce a Lagrange multiplier $\lambda$ and fold the constraint into a single loss function:

$$
L(\mathbf{h}, \lambda) = \mathbf{h}^T A^T A\, \mathbf{h} - \lambda(\mathbf{h}^T\mathbf{h} - 1)
$$

At a minimum, the derivative of $L$ with respect to $\mathbf{h}$ must vanish. Using the standard matrix-calculus identities $\frac{\partial}{\partial \mathbf{h}}(\mathbf{h}^T M \mathbf{h}) = 2M\mathbf{h}$ (for symmetric $M$, and $A^TA$ is always symmetric) and $\frac{\partial}{\partial \mathbf{h}}(\mathbf{h}^T\mathbf{h}) = 2\mathbf{h}$:

$$
\frac{\partial L}{\partial \mathbf{h}} = 2A^TA\,\mathbf{h} - 2\lambda\mathbf{h} = 0 \quad\Longrightarrow\quad A^TA\,\mathbf{h} = \lambda\mathbf{h}
$$

**This is exactly an eigenvalue problem.** $\mathbf{h}$ must be an eigenvector of the $9\times9$ matrix $A^TA$, with $\lambda$ its corresponding eigenvalue — this is precisely your own instinct, confirmed by the derivative.

## Step 6 — why the *smallest* eigenvalue specifically

This is the part worth not skating past, since it's not just "eigenvectors are the answer, done" — you have to know *which* eigenvector out of nine.

At any eigenvector solution, plug $A^TA\,\mathbf{h} = \lambda\mathbf{h}$ back into the original objective:

$$
\mathbf{h}^T A^T A\, \mathbf{h} = \mathbf{h}^T(\lambda\mathbf{h}) = \lambda(\mathbf{h}^T\mathbf{h}) = \lambda \cdot 1 = \lambda
$$

So **the value of the thing we're trying to minimize is literally just $\lambda$ itself**, at every eigenvector solution. Since $A^TA$ is a $9\times9$ symmetric matrix, it has (up to) 9 real eigenvalues, each with its own eigenvector — and each one is a valid *critical point* of the constrained problem, but only one of them actually *minimizes* it: whichever has the **smallest** $\lambda$. That eigenvector is $\mathbf{h}$; reshape its 9 entries back into a $3\times3$ matrix (row-major: first three entries become row 1, and so on) and that's your estimated $H$.

**A sanity-check worth internalizing:** $A^TA$ is always symmetric positive semi-definite (any matrix of the form $M^TM$ is), so every eigenvalue is real and $\geq 0$ — the smallest eigenvalue is never negative, which is reassuring since a negative "closest-fit error" wouldn't make sense here. In the ideal noiseless case with exactly 4 correspondences, the smallest eigenvalue comes out to exactly $0$ — meaning a perfect exact fit exists and $\mathbf{h}$ is a genuine null-space vector of $A$, recovering the un-constrained $A\mathbf{h}=\mathbf{0}$ case as the special "no noise" limit of this more general method.

## A practical implementation note — SVD instead of eigendecomposition

In practice (OpenCV, most implementations), this is computed via the **Singular Value Decomposition** of $A$ directly, $A = U\Sigma V^T$, rather than explicitly forming $A^TA$ and eigendecomposing it. The two are mathematically equivalent — the eigenvectors of $A^TA$ are exactly the columns of $V$, and the eigenvalues of $A^TA$ are the squared singular values in $\Sigma$ — but computing $A^TA$ explicitly squares the matrix's condition number, which can amplify numerical error. Taking the SVD of $A$ directly and picking the column of $V$ corresponding to the *smallest singular value* gives the identical answer with better numerical stability. Worth knowing the equivalence even if a library call hides the eigendecomposition from you.

## How many correspondences do you actually need?

Each correspondence contributes 2 equations; there are 8 unknowns after fixing scale — so **4 correspondences** (giving exactly 8 equations) is the minimum for an exact solution, provided no 3 of the 4 points are collinear (collinear points make $A$ rank-deficient, i.e. degenerate). This is exactly the "4 points" [[RANSAC]] samples on each iteration — RANSAC's per-iteration model-fit step *is* this exact DLT computation, just run on a minimal 4-point sample each time. Once RANSAC identifies its best inlier set, this same eigenvector method gets rerun using **all** the inliers (now $n \gg 4$, an overdetermined, least-squares regime) for the final refined $H$ — this is the "optional refinement" step mentioned at the end of [[projective-transformation]]'s estimation pipeline.
