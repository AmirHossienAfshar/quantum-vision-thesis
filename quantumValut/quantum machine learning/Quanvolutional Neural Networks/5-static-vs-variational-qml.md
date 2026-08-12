# 5 — Static vs. variational QML (Section 2.2 positioning)

## The key distinguishing sentence

> "Another key difference in the QNN approach revolves around the **lack of
> variational tuning of the quantum components of the model.**"

This paper's quantum circuit `q` is **never trained** — no gradient updates, no parameter optimization inside the circuit, ever. It's generated once (see [[3-filter-generation-methodology|note 3]]) and stays fixed for the life of the model.

## What it's explicitly contrasted against

Other QML approaches at the time *do* train the quantum part — **variational quantum circuits**: tunable rotation angles optimized via a hybrid classical-quantum training loop (cited: Bergholm et al. 2018, Crooks 2018, Schuld et al. 2018).

Paper's own description of its choice: **"the static feature methodology"** — extending the QRC methodology rather than the variational-circuit trend.

## The "quantum advantage" argument despite no training

Argument mirrors Havlíček et al. (2019) on quantum kernel methods: even a fixed/untrained quantum circuit can act as a kernel function mapping data into a high-dimensional Hilbert space that's classically hard to replicate. So the claim isn't "we optimized the quantum part better" — it's "even *random* quantum circuits might access a useful kernel space that's inaccessible (efficiently) to classical computation."

## Related concept to look up later

quantum kernel methods / quantum-enhanced feature spaces (Havlíček et al. 2019) — cited as the direct precedent for this paper's advantage argument.
