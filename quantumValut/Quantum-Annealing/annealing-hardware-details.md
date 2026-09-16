---
tags: [quantum-computing, quantum-annealing, hardware, thesis-core]
status: foundation
related:
  - "[[quantum-annealing-overview]]"
  - "[[ising-model-and-qubo]]"
  - "[[qubo-explained]]"
  - "[[adiabatic-theorem]]"
---

# Quantum Annealing — Hardware Details: Tunneling and Couplers

## Quantum tunneling — the actual escape mechanism

Look again at the double-well potential from [[quantum-annealing-overview]]: two low-energy wells ($0$ and $1$) separated by an energy barrier. A **classical** system sitting in one well is stuck there unless it gets enough thermal energy to climb *over* the barrier — this is exactly how **classical simulated annealing** (a much older, purely classical optimization heuristic with a similar-sounding name) escapes local minima: by injecting controlled random thermal noise, occasionally kicking the system over a barrier it would otherwise be trapped behind.

A **quantum** system has a second, genuinely different option: its wavefunction extends into the classically forbidden region *inside* the barrier itself, with a nonzero (if small) probability of being found on the other side — meaning the system can move from one well to the other by **tunneling straight through** the barrier, without ever having the energy to go over the top. This is quantum tunneling, and it's the actual physical mechanism — not a metaphor — that gives quantum annealing a genuinely different escape route out of local minima than classical simulated annealing has, despite the similar name.

## Couplers — how $J_{ij}$ gets physically implemented

[[ising-model-and-qubo]] introduced $J_{ij}$, the coupling term between a pair of spins — this section is about what that actually *is* in hardware, not just in the equation.

A **coupler** is a physical circuit element (itself typically a small superconducting loop, similar in spirit to the qubit loops themselves) placed at the junction between two specific qubits, whose coupling strength is individually programmable before the anneal begins. Setting a coupler's strength is literally how you "write" one entry of your $J_{ij}$ (or QUBO $Q_{ij}$) matrix into the physical hardware:

- A coupler programmed **ferromagnetic** (positive $J_{ij}$, in the sign convention from [[ising-model-and-qubo]]) energetically favors its two qubits ending up **aligned** (both $0$ or both $1$).
- A coupler programmed **antiferromagnetic** (negative $J_{ij}$) favors them ending up **opposite**.

Together with each qubit's individually programmable **bias** $h_i$ (implemented via that qubit's own local applied field — literally the "applied magnetic field" arrows in [[ising-model-and-qubo]]'s second diagram), the full set of biases and couplers *is* how an entire QUBO/Ising problem gets loaded onto the chip before the anneal starts. Programming the problem is a one-time setup step (set every $h_i$ and $J_{ij}$); the anneal itself is then just letting physics run.

## A practical constraint worth flagging now, before it becomes a surprise later

Real annealing hardware does **not** have a coupler between every possible pair of qubits — the physical chip layout only wires up a sparse, fixed set of qubit-to-qubit connections (D-Wave's chip topologies have specific names, e.g. Pegasus, Chimera). If your problem's QUBO needs a coupling between two qubits that aren't physically adjacent on the chip, you can't just set $J_{ij}$ directly — you need **minor embedding**: representing one logical variable in your problem as a *chain* of several physically-connected qubits, forced (via strong internal couplings within the chain) to always agree with each other, so the chain collectively behaves as one variable that can now reach further across the chip.

This has real practical cost — chains use up multiple physical qubits per logical variable, reducing how large a problem actually fits on the hardware, and a chain that "breaks" (its qubits disagree at readout) is a real source of error distinct from the annealing process itself. This is a genuine, concrete bottleneck worth anticipating for the thesis, not an abstract footnote — if the consensus-maximization QUBO for homography ends up densely connected (many correspondence pairs interacting), minor embedding overhead could be a real practical limit on how many feature correspondences can be handled on real hardware at once.

