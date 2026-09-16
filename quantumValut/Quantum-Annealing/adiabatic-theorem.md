---
tags: [quantum-computing, quantum-annealing, physics, thesis-core]
status: foundation
related:
  - "[[quantum-hamiltonian]]"
  - "[[quantum-annealing-overview]]"
  - "[[ising-model-and-qubo]]"
  - "[[qubo-explained]]"
  - "[[annealing-hardware-details]]"
---

# The Adiabatic Theorem

## The theorem itself

A real result from quantum physics (Born & Fock, 1928 — predates quantum computing entirely). Informally:

> If a quantum system starts in its **ground state** (lowest-energy configuration available to it), and its Hamiltonian (its energy landscape) is changed **slowly enough**, the system stays in the ground state the entire time — even as that ground state itself moves and changes shape underneath it.

The word doing all the work is "slowly enough," and it's not vague — it's precisely governed by the **energy gap** between the ground state and the first excited state, at every point during the change.

## How annealing is literally built on this

Quantum annealing doesn't use two separate energy functions compared against each other — it uses **one single Hamiltonian that gets smoothly morphed** from an easy starting point into the hard problem you actually want solved:

$$
H(t) = A(s)\, H_{start} + B(s)\, H_{problem}, \qquad s = t/T \in [0,1]
$$

where $T$ is the total anneal time, $s$ is the normalized progress through the anneal (0 at the start, 1 at the end), and $A(s), B(s)$ are schedule functions controlled by the hardware — $A(s)$ starts large and shrinks to $0$, $B(s)$ starts at $0$ and grows large, so the system smoothly hands control from $H_{start}$ over to $H_{problem}$. (The simplest version of this idea is a plain linear interpolation $H(t) = (1-s)H_{start} + s\,H_{problem}$ — real hardware schedules are usually more specific curves than a straight line, worth checking D-Wave's own documentation for the exact functions used on whichever system a paper ran on.)

- **$H_{start}$**: engineered so its ground state is trivial to prepare — conceptually, every qubit in an equal superposition, not yet preferring $0$ or $1$. This is the strong-tunneling, barrier-suppressed regime from [[quantum-annealing-overview]]'s first diagram.
- **$H_{problem}$**: engineered so its ground state **is** the answer to your [[ising-model-and-qubo|QUBO/Ising problem]] — the biased, barrier-raised landscape from that same note's second diagram, where the applied field has tilted the wells toward the correct answer.

If the interpolation from $H_{start}$ to $H_{problem}$ happens slowly enough — relative to the smallest energy gap encountered anywhere along that path — the adiabatic theorem guarantees the system ends up in the ground state of $H_{problem}$: the true minimum of your QUBO.

## The minimum gap — why "slowly enough" is the whole catch

Define $\Delta(s)$ as the energy gap between the ground state and the first excited state at progress point $s$, and $\Delta_{min} = \min_s \Delta(s)$ — the smallest gap encountered anywhere along the entire path. The (simplified, qualitative form of the) adiabatic condition is roughly:

$$
T \gg \frac{\max_s \left|\frac{dH}{ds}\right|}{\Delta_{min}^2}
$$

The dependence on $\Delta_{min}^2$ in the denominator is the important part to internalize: **the smaller the minimum gap, the longer the anneal has to run** to keep the guarantee — and the relationship is not gentle, it's roughly inverse-square.

## Why real hardware doesn't get the "guaranteed" version

This is the correction worth having fully settled, since it directly explains why annealing is a heuristic rather than a provably-correct solver in practice. For many genuinely hard optimization problems, $\Delta_{min}$ can shrink **exponentially** as the problem size grows. Plugging an exponentially small gap into the condition above means the required anneal time $T$ would *also* have to grow exponentially to keep the theorem's guarantee. Real annealing hardware runs on a fixed, practical timescale (microseconds, not "however long the theorem demands") — far shorter than what would be needed for a guarantee on hard instances. So in practice, real annealers behave as a strong **heuristic**: often fast, often good, but without the theorem's guarantee once the problem is hard enough to have a tiny minimum gap somewhere along its path.

This is exactly the gap Chin & Suter's 2022 CVPR paper addresses directly — their contribution is squeezing a rigorous **error bound** out of this otherwise-unguaranteed process, which plain RANSAC can't offer either. Both methods end up heuristic in different ways; their paper's specific value is making the annealing version's uncertainty quantifiable.

## Why this matters for the thesis

This is the theoretical backbone that makes sense of every practical claim in the annealing papers on my reading list — when they report "found the optimal solution in N runs" or discuss failure rates, this gap-dependent, no-universal-guarantee behavior is the underlying reason results are usually reported statistically (success probability over many anneal runs) rather than as a single deterministic guarantee.

## Open questions / things to verify
- [ ] Find and record D-Wave's actual published $A(s)$, $B(s)$ schedule curves for whichever specific system (Advantage, etc.) the papers on my reading list used — the linear approximation above is a simplification.
- [ ] Look for a concrete, small worked example (even a 2-qubit toy problem) showing the energy gap shrinking as a function of problem size, to make "$\Delta_{min}$ can shrink exponentially" less abstract.
