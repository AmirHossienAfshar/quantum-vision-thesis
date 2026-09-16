---
tags: [quantum-computing, quantum-annealing, linear-algebra, thesis-core]
status: foundation
related:
  - "[[quantum-hamiltonian]]"
  - "[[qubo-explained]]"
  - "[[quantum-annealing-overview]]"
  - "[[adiabatic-theorem]]"
  - "[[annealing-hardware-details]]"
  - "[[RANSAC]]"
---

# The Ising Model

> The full QUBO derivation, worked examples, and the correspondence-selection application now live in [[qubo-explained]] — a standalone, beginner-friendly build-up starting from a plain scheduling problem, no physics required. This note stays focused on the Ising model specifically: the physics side, and its direct connection to the two double-well diagrams from [[quantum-annealing-overview]].

## The Ising model — physics first

The Ising model is a real, much older piece of statistical physics (originally for modeling magnetism), and it's the native mathematical language of annealing hardware. Every variable is a **spin** $s_i \in \{-1, +1\}$ (physically: which way a tiny magnetic moment points), and the total energy of a configuration of spins is:

$$
E(\mathbf{s}) = -\sum_{i<j} J_{ij}\, s_i s_j - \sum_i h_i\, s_i
$$

Two kinds of terms, each with a direct physical meaning worth holding onto:

- **$h_i$ — the bias** on spin $i$ alone. This is literally an externally applied field pulling that one spin toward $+1$ or $-1$. This is exactly what's pictured below:

![[double-well-potential-biased.png]]

Compare this to [[quantum-annealing-overview]]'s first diagram — same double-well shape, but now an **applied magnetic field** has been added, tilting the landscape so one well sits lower than the other. That asymmetry is $h_i$ made physically visible: a nonzero bias literally deforms the qubit's potential so one state becomes more probable at the end of the anneal. A large positive $h_i$ tilts it hard toward $-1$; a large negative $h_i$ tilts it hard toward $+1$ (sign convention depends on how the hardware defines "up").
- **$J_{ij}$ — the coupling** between a *pair* of spins $i$ and $j$. This doesn't touch either spin individually — it rewards or penalizes specific *relationships* between them. $J_{ij} > 0$ favors the two spins being aligned (both $+1$ or both $-1$) — physically, a "ferromagnetic" coupling. $J_{ij} < 0$ favors them being opposite — "antiferromagnetic." The physical hardware element that implements this is a **coupler**, covered in [[annealing-hardware-details]].

## Converting between Ising and QUBO — worked derivation

QUBO ([[qubo-explained]]) is mathematically the *same* structure as the Ising model above, just using $0/1$ variables instead of $\pm1$ spins. The two are connected by one linear substitution. **This note uses $s_i = 2x_i - 1$** (maps $x_i=0 \to s_i=-1$ and $x_i=1 \to s_i=+1$):

$$
J_{ij}\, s_i s_j = J_{ij}(2x_i - 1)(2x_j - 1) = J_{ij}\left(4x_ix_j - 2x_i - 2x_j + 1\right)
$$

Expanding this out and collecting terms shows a single Ising coupling term $J_{ij}s_is_j$ becomes a **quadratic term** ($4J_{ij}\,x_ix_j$) *plus* two **linear terms** ($-2J_{ij}\,x_i$ and $-2J_{ij}\,x_j$) once switched to binary variables. Doing this substitution across the whole sum is mechanical but slightly tedious — the important takeaway is that **Ising and QUBO are the same problem wearing different variable conventions**, and any hardware/software built for one can solve the other via this substitution.

> **Convention gotcha:** [[qubo-explained]] (Section 17) uses the *opposite* convention, $s_i = 1-2x_i$ (mapping $0\to+1$, $1\to-1$) — quoted straight from that source, since it's how the material I adapted it from wrote it. Both conventions are internally valid; they just assign $\pm1$ to $0/1$ oppositely. This is a real, live example of the "always check the convention" warning [[qubo-explained]] opens with — worth resolving into one house convention before doing any original derivation that depends on the sign.
