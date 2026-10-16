---
tags: [quantum, grover]
---
# 09 Limits of the Speedup

- **Quadratic, not exponential.** $N\to\sqrt N$ is a big gain at scale, but nothing like the exponential gain of Shor's algorithm.
- **Optimal.** For unstructured search with an oracle, no quantum algorithm can do better than order $\sqrt N$ queries (Bennett, Bernstein, Brassard, Vazirani). Grover is the best possible in this model.
- **It does not make hard problems easy.** For NP-hard problems like SAT, a $\sqrt N$ speedup of an exponential search is still exponential: roughly $2^{n/2}$ instead of $2^n$.
- **The oracle's cost is separate.** We counted queries. If evaluating $f$ takes many gates, the real runtime is about (number of rounds) $\times$ (cost of the oracle).
- **Rounds are sequential and need coherence.** All $\sim\sqrt N$ rounds must run in one uninterrupted quantum computation. Noise is a serious issue, and the speedup can disappear once error-correction overhead is included. Splitting across machines helps less than in the classical case.
- **Cryptography.** Grover's attack on an $n$-bit symmetric key costs about $2^{n/2}$ queries, which is why 256-bit keys are recommended to keep roughly 128-bit security in a quantum world.

## Reference
Grover, *A fast quantum mechanical algorithm for database search*, 1996.

---
Previous: [[08 Multiple Solutions and Unknown M]] · Next: [[10 Building the Oracle from Gates]]
