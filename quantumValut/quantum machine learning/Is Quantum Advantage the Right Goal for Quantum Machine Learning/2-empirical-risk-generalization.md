# Empirical Risk, Generalization, and the Deep Learning Puzzle

## The practical workaround: empirical risk
Since true risk can't be computed, ML uses a proxy: test the model against the finite labeled data you actually have, and use that average error as a stand-in. This is **empirical risk** — "how many mistakes did the model make on the data I collected."

**The catch:** doing well on your specific training batch doesn't guarantee doing well on new, unseen emails. Maybe your training set happened to have lots of "URGENT ACT NOW" spam, so the filter gets great at catching that pattern specifically — but fails on a sneakier newsletter-disguised spam it's never seen.

## Generalization: the gap between the two
**Generalization** = "if my model does well on training emails, how confident can I be it'll do well on brand-new ones?"

- 100% training accuracy that fails on new data = memorization, not learning (like a student memorizing exact exam answers instead of understanding the material).
- **Generalization theory** is the branch of research asking: how much data do I need, and under what conditions does good training performance actually predict good real-world performance?

## The old assumption: "fitting too well" = bad
Classic example from the paper: if every "harmful" image in a training set coincidentally has a black pixel in one position, a model might "learn" that black pixel = harmful — a spurious pattern that happens to fit the sample but is nonsense in general.

For decades the fix was: **prevent the model from fitting training data too perfectly** — keep model class simple, add regularization penalties, stop training early. All under the assumption that zero training error = memorized coincidences = bad generalization.

## The deep learning surprise
Modern deep networks often have *more parameters than training examples* — by the old logic they should massively overfit. But empirically, many fit training data with **zero errors** and still generalize excellently to new data. This directly contradicts the old assumption, and there's still no fully satisfying theoretical explanation (sometimes called "benign overfitting").

## Why the old theory isn't enough anymore
The old theory mainly asked: *what function class F are you choosing from?* Deep learning shows that's insufficient — two more things matter enormously:
1. **The training algorithm itself** (not just which functions are allowed — how you optimize matters)
2. **The data distribution p(x) itself** (the actual structure of real data, not just the abstract space of possibilities)

A viable theory now has to juggle all three moving parts together, and each is already hard to analyze alone.

> **Why this matters for QML:** classical ML theory is *actively being rebuilt* to explain deep learning, and already struggles with three interacting moving parts (model class, algorithm, data). Quantum ML wants to add a **fourth** moving part — "quantumness" (entanglement, interference) — on top of a foundation that isn't even settled yet.