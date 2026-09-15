---
tags: [classical-cv, robust-estimation, foundations]
status: foundation
related:
  - "[[projective-transformation]]"
  - "[[feature-matching-SIFT-ORB]]"
  - "[[affine-transformation]]"
  - "[[computing-homography]]"
---

# RANSAC (Random Sample Consensus)

## One-line definition
A robust-fitting algorithm that finds the best-supported model (e.g. a [[projective-transformation]]) from a set of data points that contains both correct data and outliers — without needing to know in advance which points are which.

Originally from Fischler & Bolles (1981), "Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography" — the original use case really was cartography/image analysis.
## Why it's needed

After [[feature-matching-SIFT-ORB]], the set of candidate point correspondences between two images always contains **outliers** — wrong matches caused by repetitive textures, ambiguous descriptors, or noise. A direct least-squares fit of a [[projective-transformation]] to *all* candidate matches (including the wrong ones) would be badly skewed by even a small number of bad points. RANSAC is the fix.

## The algorithm (loop)

1. **Randomly sample** a minimal subset of correspondences needed to compute the model — for homography, that's **4 point pairs** (the minimum needed to solve the 8-parameter system via [[computing-homography|DLT]]).
2. **Fit** a candidate homography to just that minimal sample.
3. **Score** the candidate: check every *other* correspondence against this candidate homography, and count how many fall within some error tolerance (these are the "inliers" for this candidate).
4. **Keep the best**: repeat steps 1–3 many times (fixed number of iterations, or until a good-enough model is found), and keep whichever candidate model had the most inlier support.
5. **(Optional) Refine**: re-fit the model using least-squares over *all* the inliers of the winning candidate, for a more accurate final result.

## Why "minimal sample" matters

RANSAC deliberately fits on the *smallest possible* subset each round (4 points for homography), not a large random subset. This is the key design insight: the smaller the sample, the higher the chance that a single random draw is entirely outlier-free, and thus produces a correct candidate model purely by chance — you just need to try enough rounds for that to happen at least once, then let the inlier-counting step recognize it as the winner.

## Inlier Ratio — how "success" gets measured

A 2026 comparative study on satellite imagery evaluated SIFT and ORB feature matching using exactly this idea: **Inlier Ratio**, the fraction of correspondences consistent with the estimated homography, as the core quality metric.

## Key parameters to know

- **Number of iterations**: how many random minimal samples to try. More iterations = higher chance of finding the true best model, at the cost of compute time.
- **Inlier threshold**: how close a point needs to be to the candidate model's prediction to count as an inlier. Too tight → too few inliers, unstable fit. Too loose → wrong matches sneak in as "inliers."

Framing worth keeping for later:
- **RANSAC** = randomized classical search over a continuous parameter space, guided by inlier-counting as the "goodness" signal.
- **Grover-based quantum matching** = structured search over a discretized/quantized parameter space, guided by an oracle that marks "good" states for amplitude amplification.
