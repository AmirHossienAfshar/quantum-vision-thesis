# How "Quantum Advantage" Gets Claimed — and Publication Bias

## The many figures of merit
The field has no single agreed definition of "beating classical ML" — researchers use whichever metric fits their result:
(a) asymptotic run time, (b) whether a learning problem is solvable at all for some data distribution, (c) model expressivity, (d) number of samples needed to learn, (e) average/worst-case generalization error, (f) optimization landscape structure, (g) test error on a small benchmark.

The sheer variety is itself a flag: without one shared yardstick, "quantum wins" can mean very different (and not always comparable) things across papers.

## Positive publication bias
Quantum ML suffers the same bias as science generally: exciting positive results ("quantum is better!") get published and cited far more than negative/neutral ones. The paper quotes real abstract phrasing, e.g., claims of "rigorous quantum speed-up," "exponentially fewer experiments," "68× enhancement" — stated with high confidence.

To be fair, some areas *do* honestly report negative results too — e.g., proofs that gradients vanish in large random quantum circuits (barren plateaus), or that quantum and classical sample complexity are actually equal in certain frameworks. So it's not that the field is all hype — but published results skew toward "quantum wins," which may not reflect the true balance of evidence.

## The authors' pivot question
Given all this activity, why do the authors still think the question is unsettled? Their answer: **not more effort needed — a structural problem.** The mathematical and experimental tools quantum computing currently has aren't capable of producing evidence that generalizes to real-world usefulness, no matter how many more papers get written. This claim is unpacked across the next several notes (artificial structuring, data loading, average-case over-generalization, small-scale benchmarks).