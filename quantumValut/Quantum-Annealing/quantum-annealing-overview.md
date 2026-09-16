---
tags: [quantum-computing, quantum-annealing, foundations, thesis-core]
status: foundation
related:
  - "[[ising-model-and-qubo]]"
  - "[[qubo-explained]]"
  - "[[adiabatic-theorem]]"
  - "[[annealing-hardware-details]]"
---

# Quantum Annealing — Overview

## One-line definition
A physics-based, hardware-native method for solving **optimization** problems by letting a real quantum system physically evolve toward its lowest-energy configuration — not a general-purpose computer, and not built from a sequence of discrete logic gates the way [[projective-transformation|classical algorithms]] or gate-model quantum circuits are.

## What problem it actually solves

Quantum annealing is built to solve exactly one shape of problem: **"find the configuration of variables that minimizes some cost/energy function."** That's it. It's not universal — see the comparison below. But that one shape covers a huge amount of ground, because combinatorial optimization, consensus maximization ([[RANSAC]]'s actual objective), and constraint satisfaction all reduce to exactly this form once expressed as [[ising-model-and-qubo|QUBO]].

## How it differs from gate-model quantum computing


|                      | Gate-based                                                                                                                                                                                                        | Quantum annealing                                                                                              |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Universal?           | Yes — any algorithm, in principle                                                                                                                                                                                 | **No** — only energy-minimization / QUBO-style optimization                                                    |
| What you write       | A circuit (explicit gate sequence)                                                                                                                                                                                | An energy function ([[ising-model-and-qubo\|QUBO/Ising matrix]])                                               |
| Current scale        | Tens to low hundreds of noisy qubits (NISQ)                                                                                                                                                                       | Thousands of qubits (D-Wave Advantage: ~5,000)                                                                 |
| Proven speedup?      | Yes, for specific structured problems (Grover: quadratic; Shor: exponential)                                                                                                                                      | No general proof — a physics-based heuristic; often fast in practice, no guarantee (see [[adiabatic-theorem]]) |
| Companies / hardware | IBM (superconducting), Google Quantum AI (superconducting), IonQ & Quantinuum (trapped-ion), Rigetti (superconducting), PsiQuantum & Xanadu (photonic), IQM, PASQAL/QuEra (neutral atom), Microsoft (topological) | D-Wave (dominant commercial player; also branching into gate-model as of 2025)                                 |
| Papers using it      | Jiang et al., Tezuka et al., the 2024 gate-quantum robust-fitting paper (IonQ)                                                                                                                                    | Q-Match, CCuantuMM, Chin & Suter's 2020/2022 robust-fitting papers (D-Wave)                                    |


**A useful metaphor:** gate-based computing is like following a precise recipe, step by step, to arrive at a dish. Quantum annealing is like shaping a landscape and dropping a marble in — you don't control its path, you just trust physics to roll it down into the lowest valley, which you've engineered in advance to be the answer.

## What a "qubit" physically looks like in an annealer

This is worth grounding concretely, since "qubit" can otherwise stay an abstract word. In D-Wave-style hardware, a qubit is physically realized as a tiny **superconducting loop carrying a persistent electrical current**, which can circulate in one of two directions — clockwise or counterclockwise. These two directions correspond to two distinct, stable, low-energy configurations, conventionally labeled $0$ and $1$:

![[double-well-potential-basic.png]]

The curve here isn't a metaphor — it's the qubit's **actual physical potential energy**, plotted against its state. Notice the shape: two wells (two stable low-energy configurations, $0$ and $1$) separated by a hump (an energy barrier) in between. A classical bit sitting in a double-well potential like this would just settle into whichever well it started in and stay there. A **quantum** system, sitting in the same landscape, behaves differently — it can be in superposition across both wells simultaneously, and can even move between them by **quantum tunneling straight through the barrier** rather than needing enough energy to climb over it. That tunneling mechanism is central enough to deserve its own full treatment — see [[annealing-hardware-details]].

## The overall annealing process, in one paragraph

Every qubit starts in a symmetric, easy-to-prepare superposition state, and ends the anneal settled into a definite $0$ or $1$ — this happens because the landscape itself changes shape underneath it over the course of the anneal, not because the qubit is "measured early" or forced. The two diagrams below are literally the same qubit's landscape, shown at two different points in that process.

### Start of the anneal — a single well, superposition

![[single-well-superposition-state.png]]

At the very start, the barrier between what will eventually become the "$0$" and "$1$" wells is suppressed — the landscape is effectively **one single well**, not two, so there's no energetic reason yet for the qubit to prefer either side. This is exactly the state pictured: the qubit sits at the bottom of one smooth well, in a genuine superposition — not "secretly already $0$ or $1$ and we just don't know which," but actually spread across both possibilities at once, the way [[quantum-hamiltonian]] describes a general (non-eigenstate) quantum state. This is $H_{start}$ from [[adiabatic-theorem]] — engineered specifically so its ground state is this easy, symmetric, no-preference superposition.

### End of the anneal — the landscape has been tilted to favor the answer

![[double-well-potential-biased.png]]

By the end of the anneal, the hardware has slowly raised the barrier back up (splitting the single well into two) **and** tilted the landscape based on the problem's specific [[ising-model-and-qubo|bias and coupling values]] — so one well now sits measurably lower in energy than the other. This is precisely how a QUBO/Ising objective gets turned into a physical preference: the "applied magnetic field" in the diagram *is* the $h_i$ bias term made physical, tilting the landscape so the qubit has a **higher probability of settling into the lower-energy state** — exactly the label in the diagram. This is $H_{problem}$ from [[adiabatic-theorem]]: engineered so its ground state (the deeper of the two wells) is the actual answer to your optimization problem.

**Reading the two images together, in order:** superposition, no preference (Image 1) → landscape reshaped and tilted based on the problem's encoding (Image 2) → measure the qubit, and it's overwhelmingly likely to be found in whichever well the tilt favored. Do this across every qubit simultaneously, with couplers ([[annealing-hardware-details]]) linking them according to the problem's $J_{ij}$ terms, and the whole chip's final readout is your QUBO solution. *Why* this slow reshaping process is expected to land on the true minimum, and exactly when that expectation breaks down, is the subject of [[adiabatic-theorem]].
