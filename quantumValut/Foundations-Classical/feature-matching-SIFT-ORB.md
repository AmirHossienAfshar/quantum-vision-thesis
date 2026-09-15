---
tags: [classical-cv, feature-matching, foundations]
status: foundation
related:
  - "[[projective-transformation]]"
  - "[[RANSAC]]"
  - "[[normalized-cross-correlation]]"
---

# Feature Matching (SIFT / ORB)

## One-line definition
Instead of comparing every possible image window (like [[normalized-cross-correlation]]), detect a sparse set of *distinctive* keypoints in each image, describe each one with a vector, and match keypoints between images by comparing those descriptor vectors.

## The pipeline (4 steps)

1. **Keypoint detection** — find points in the image that are distinctive and likely to be found again in another view of the same scene (corners, blobs, high-contrast regions). Good keypoints are stable under rotation, scale, and some lighting change.
2. **Descriptor extraction** — for each keypoint, compute a vector that numerically summarizes the local neighborhood around it, designed so that the *same* physical point in a different image produces a *similar* vector.
3. **Descriptor matching** — for each keypoint in image A, find its nearest neighbor (by descriptor distance) in image B. This gives a set of **candidate correspondences** — includes correct matches and wrong ones.
4. **Geometric verification** — fit a global transform ([[projective-transformation]] or affine) via [[RANSAC]] to reject correspondences that don't fit any consistent transform.

## SIFT vs. ORB

| | SIFT | ORB |
|---|---|---|
| Full name | Scale-Invariant Feature Transform | Oriented FAST and Rotated BRIEF |
| Descriptor type | Floating-point gradient histograms | Binary string |
| Speed | Slower | Much faster |
| Matching distance metric | Euclidean | Hamming distance (bitwise, very fast) |
| Patent status | Historically patented, now expired/free to use | Always free/open |
| Typical use case | Accuracy-critical, offline processing | Real-time applications |

Both are designed to be invariant (or near-invariant) to rotation and, to some degree, scale — which is exactly what [[normalized-cross-correlation]] is *not*, and is the main reason feature-based matching scales so much better to real-world unknown-orientation scenarios.

## Rejecting ambiguous matches

Not every nearest-neighbor descriptor match is trustworthy. Two common filtering strategies before even getting to RANSAC:
- **Ratio test (Lowe's ratio test)**: compare the distance to the best match vs. the second-best match; if they're too close together, the match is ambiguous and gets discarded.
- **Symmetry check**: only keep a match if A→B's best match is also B→A's best match (mutual nearest neighbors).

## Why feature-based matching beats brute-force NCC for this project

- Only compares a **sparse** set of distinctive points, not every possible window position/orientation/scale — massively cheaper.
- Naturally invariant (mostly) to rotation and scale — no need to brute-force sweep those parameters, unlike naive [[normalized-cross-correlation]].
- Directly produces the point correspondences that [[projective-transformation]] estimation needs as input.
