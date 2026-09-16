---
tags: [quantum-computing, quantum-annealing, linear-algebra, thesis-core, beginner-friendly]
status: foundation
related:
  - "[[quantum-hamiltonian]]"
  - "[[ising-model-and-qubo]]"
  - "[[quantum-annealing-overview]]"
  - "[[adiabatic-theorem]]"
  - "[[annealing-hardware-details]]"
---

# QUBO — An Introduction

> This note builds QUBO up from a plain scheduling example, no physics needed, before touching Ising spins or hardware at all. [[ising-model-and-qubo]] covers the *physical* side (bias fields, couplers, the double-well diagrams) — this note is the standalone math/intuition companion, and the one to start with if QUBO itself still feels abstract.

## 1. What is QUBO?

**QUBO** stands for **Quadratic Unconstrained Binary Optimization**. It's a way of writing certain optimization problems so they can be solved by classical optimization algorithms, simulated annealing, quantum annealing, or gate-based quantum algorithms like QAOA.

The name tells us almost everything, one letter at a time:

- **Q — Quadratic:** the objective function contains terms up to degree 2, such as $x_ix_j$.
- **U — Unconstrained:** the basic formulation has no separate constraints like $x_1+x_2=1$. Constraints get folded in indirectly, via penalty terms (Section 7 and 14).
- **B — Binary:** every decision variable is binary, $x_i \in \{0,1\}$.
- **O — Optimization:** we want the *best* assignment of variables, by minimizing or maximizing an objective.

$$
\boxed{\min_{\mathbf{x}\in\{0,1\}^n} \mathbf{x}^T Q\mathbf{x}}
$$

**Worth flagging early, since it'll save confusion later:** different books and software packages use slightly different conventions for the $Q$ matrix — especially whether the factor of 2 on off-diagonal terms is stored explicitly. Always check which convention a given source or library is using before comparing numbers across sources.

## 2. Before QUBO — what is an optimization problem?

Start somewhere familiar, no binary variables yet. A university has **four talks** (A, B, C, D) and **two time slots** (Morning, Afternoon). Several students each want to attend a *pair* of talks, but only if those talks land in different slots:

- Student 1 wants A and B.
- Student 2 wants B and C.
- Student 3 wants C and D.
- Student 4 wants A and D.

**Goal:** schedule the four talks so that as many students as possible can attend both of their preferred talks. Many possible schedules exist, and we want the best one — that's what makes this an optimization problem.

## 3. Turning decisions into binary variables

Introduce one binary variable per talk:

$$
x_A, x_B, x_C, x_D \in \{0,1\}, \qquad x_i = \begin{cases} 0 & \text{talk } i \text{ is in the morning} \\ 1 & \text{talk } i \text{ is in the afternoon} \end{cases}
$$

For example, $(x_A,x_B,x_C,x_D)=(0,1,0,1)$ means:

| Talk | Time |
|---|---|
| A | Morning |
| B | Afternoon |
| C | Morning |
| D | Afternoon |

Every variable being restricted to $\{0,1\}$ is the **B (Binary)** in QUBO.

## 4. How do we mathematically describe "different"?

This is the key trick the whole formulation rests on. A student wanting talks $A$ and $B$ can attend both if $x_A \neq x_B$. We want an expression giving $0$ when they're on the same day and $1$ when they're on different days. For binary variables, this expression does exactly that:

$$
\boxed{x_A + x_B - 2x_Ax_B}
$$

Check all four possibilities:

| $x_A$ | $x_B$ | $x_A+x_B-2x_Ax_B$ | Different? |
|---:|---:|---:|---|
| 0 | 0 | 0 | No |
| 0 | 1 | 1 | Yes |
| 1 | 0 | 1 | Yes |
| 1 | 1 | 0 | No |

This is effectively **XOR** for binary variables — it tells us whether two decisions differ.

## 5. Building the objective function

Apply the XOR trick to every student's pair:

$$
F(\mathbf{x}) = (x_A+x_B-2x_Ax_B) + (x_B+x_C-2x_Bx_C) + (x_C+x_D-2x_Cx_D) + (x_A+x_D-2x_Ax_D)
$$

Goal: $\boxed{\max F(\mathbf{x})}$ — maximize the number of satisfied students. This is already a quadratic binary optimization problem.

## 6. Why is it "quadratic"?

Look at $x_A+x_B-2x_Ax_B$ — the highest-degree term is $x_Ax_B$, a product of two variables: **degree 2**. There are no terms like $x_Ax_Bx_C$ or $x_A^3$. That's the whole reason for the name — the highest degree present is 2.

A general quadratic binary objective looks like:

$$
F(\mathbf{x}) = c + \sum_i a_i x_i + \sum_{i<j} b_{ij}x_ix_j
$$

containing a constant $c$, linear terms $a_ix_i$, and pairwise terms $b_{ij}x_ix_j$.

## 7. Why "Unconstrained"?

Our talk-scheduling story clearly has a rule ("every talk goes to morning or afternoon") — but that rule is already handled by the variable *domain* itself, $x_i \in \{0,1\}$; we never need a separate equation enforcing it. A basic QUBO has the form $\min_{\mathbf{x}\in\{0,1\}^n} f(\mathbf{x})$ with no separate constraints like $A\mathbf{x}=\mathbf{b}$ — that's the **U**.

This does **not** mean QUBO can't represent problems that originally *do* have constraints, though. We convert constraints into the objective using **penalty terms**. Example: if exactly one of two items must be selected, $x_1+x_2=1$, add $P(x_1+x_2-1)^2$ to the objective. Zero penalty when satisfied, a growing penalty when violated. This is one of the most important techniques for turning a real-world problem into a QUBO — see Section 14 for a fuller worked example.

## 8. Why "Binary"?

$x_i \in \{0,1\}$ — only two possible states. The interpretation of $0$ and $1$ depends entirely on the problem:

```text
x = 0  →  do not select
x = 1  →  select
```
```text
x = 0  →  correspondence rejected
x = 1  →  correspondence selected
```

That second example isn't arbitrary — it's exactly the encoding this vault has already been using for consensus maximization; see Section 22.

## 9. Why "Optimization"?

Because we're not just evaluating a function once — we want the assignment giving the *best* value. $F(0,0,0,0)=0$ might be a bad schedule; $F(0,1,0,1)=4$ could be much better. We want $\mathbf{x}^* = \arg\max_{\mathbf{x}} F(\mathbf{x})$. With $n$ binary variables, there are $2^n$ possible assignments — checkable exhaustively for small $n$, but quickly impractical for large $n$. That's exactly where optimization algorithms (classical or quantum) become interesting.

## 10. Converting maximization into minimization

Most QUBO formulations are written as minimization: $\boxed{\min_{\mathbf{x}} E(\mathbf{x})}$. If the original problem is $\max_{\mathbf{x}} F(\mathbf{x})$, define $E(\mathbf{x}) = -F(\mathbf{x})$ — then maximizing $F$ is equivalent to minimizing $-F$. This flip is especially convenient once the objective gets reinterpreted as a physical *energy* (see [[ising-model-and-qubo]]) — energy minimization is the natural framing for annealing hardware.

## 11. The QUBO matrix — worked all the way through

Collect coefficients into a matrix: $E(\mathbf{x}) = \mathbf{x}^TQ\mathbf{x}$. For the four-talk problem, expand $F(\mathbf{x})$ fully:

$$
F(\mathbf{x}) = 2x_A+2x_B+2x_C+2x_D - 2x_Ax_B - 2x_Bx_C - 2x_Cx_D - 2x_Ax_D
$$

So the minimization objective is:

$$
E(\mathbf{x}) = -2x_A-2x_B-2x_C-2x_D + 2x_Ax_B+2x_Bx_C+2x_Cx_D+2x_Ax_D
$$

Using the convention $\mathbf{x}^TQ\mathbf{x} = \sum_i Q_{ii}x_i + 2\sum_{i<j}Q_{ij}x_ix_j$, one valid QUBO matrix (ordering $A,B,C,D$) is:

$$
Q = \begin{pmatrix} -2 & 1 & 0 & 1 \\ 1 & -2 & 1 & 0 \\ 0 & 1 & -2 & 1 \\ 1 & 0 & 1 & -2 \end{pmatrix}
$$

The exact matrix can look different under another convention, but the resulting objective is the same — a direct, concrete instance of the convention-dependence flagged back in Section 1.

## 12. What does the matrix actually mean?

The **diagonal** holds the linear terms — e.g. $Q_{AA}=-2$. The **off-diagonal** entries represent interactions between pairs of variables — e.g. $Q_{AB}=1$ represents the $A$-$B$ interaction. A QUBO isn't a mysterious matrix; it describes the individual costs/rewards of decisions and the interactions between pairs of decisions:

```text
variable A ───── variable B
      │               │
      └──── interaction
```

## 13. A tiny QUBO example, from scratch

Choose between two projects, $A$ and $B$, with $x_A,x_B\in\{0,1\}$. Selecting $A$ gives reward 5, selecting $B$ gives reward 3: $F(\mathbf{x})=5x_A+3x_B$. No quadratic terms yet — this is technically still a valid QUBO, since a quadratic function is allowed to have zero quadratic coefficients.

Now add a penalty of 10 if *both* are selected: $F(\mathbf{x})=5x_A+3x_B-10x_Ax_B$. A genuine interaction term. Check $(x_A,x_B)=(1,1)$: $F=5+3-10=-2$ — worse than selecting just $A$ alone ($F=5$), so the optimizer avoids picking both. This is the core idea to hold onto: 

**linear terms describe individual decisions; quadratic terms describe relationships between decisions.**

## 14. Constraints through penalties — a fuller example

Three projects, must select **exactly two**: $x_1+x_2+x_3=2$. Add penalty $P(x_1+x_2+x_3-2)^2$. If the original objective is to maximize $5x_1+4x_2+3x_3$, convert to minimization ($-5x_1-4x_2-3x_3$) and add the penalty:

$$
E(\mathbf{x}) = -5x_1-4x_2-3x_3 + P(x_1+x_2+x_3-2)^2
$$

The optimizer is now encouraged toward selecting exactly two projects. This is how a genuinely **constrained** problem becomes an **unconstrained** QUBO. The penalty weight $P$ needs care: large enough to discourage invalid solutions, but not so large it drowns out the real objective and makes the optimizer numerically insensitive to which *valid* solution is best.

## 15. QUBO and graphs

Many QUBO problems have a natural graph interpretation — each binary variable is a node, and an edge between two variables means a quadratic interaction exists:

```text
      x1
     /  \
   x2----x3
     \
      x4
```

This "choose a subset of nodes optimizing total reward plus pairwise compatibility" framing shows up across Max-Cut, graph partitioning, scheduling, portfolio optimization, clustering, facility location, assignment problems, feature selection, **correspondence selection**, and routing.

## 16. Why QUBO is interesting for quantum computing

A QUBO is a **classical mathematical optimization formulation** — QUBO itself is not inherently quantum. This distinction matters. You can solve a QUBO with brute force, classical optimization, simulated annealing, tabu search, classical Ising solvers, [[quantum-annealing-overview|quantum annealing]], QAOA, and more. QUBO shows up so often in quantum computing because it maps naturally onto an **Ising Hamiltonian** ([[ising-model-and-qubo]]), which can then be represented using qubits and Pauli operators:

```text
Real-world optimization problem
              ↓
       Binary variables
              ↓
             QUBO
              ↓
       Ising formulation
              ↓
      Quantum Hamiltonian
              ↓
    Quantum optimization
       (e.g. QAOA)
              ↓
       Binary solution
```

## 17. From binary variables to spin variables
 
Quantum formulations often use $s_i \in \{-1,+1\}$ instead of $x_i \in \{0,1\}$. The transformation used in this particular source is:
 
$$
\boxed{x_i = \frac{1-s_i}{2}} \qquad \text{or equivalently} \qquad \boxed{s_i = 1-2x_i}
$$
 
| Binary $x_i$ | Spin $s_i$ |
|---:|---:|
| 0 | +1 |
| 1 | −1 |
 
> **Worth being precise about this step, since it's easy to mentally file it as "the quantum step":** this relabeling is **100% classical.** $s_i$ is still just a plain number, $+1$ or $-1$ — no qubit, no superposition, no operator, nothing quantum has entered yet. It's the exact same move as rewriting a temperature in Celsius instead of Fahrenheit: a different numbering convention for the same underlying classical fact ("talk A is in the morning"). The actual transition to quantum mechanics doesn't happen until Section 18 below — worth holding that boundary firmly, because conflating "we switched to $\pm1$" with "we went quantum" is a very natural but incorrect inference, and it's exactly what's being untangled in this revision.
 
> **Convention gotcha, worth flagging explicitly:** [[ising-model-and-qubo]] uses the *opposite* sign convention, $s_i = 2x_i - 1$ (mapping $0\to-1$, $1\to+1$) — literally flipped relative to this note's $s_i=1-2x_i$. Both are valid, self-consistent conventions; they just assign $-1$/$+1$ to $0$/$1$ oppositely. When comparing a QUBO/Ising formulation from two different papers, always re-derive which convention each one uses rather than assuming they match.
 
## 18. From spins to qubits — where quantum mechanics genuinely enters
 
This section answers a question worth stating explicitly, because it's the right question to ask: **spin sounds like it should be a quantum *state* — something like $|\psi\rangle$, that can be $|0\rangle$, $|1\rangle$, or a superposition of both. So why does the note say "replace $s_i$ with the Pauli-Z *operator* $Z_i$" — an operator, not a state? That seems backwards.**
 
It isn't backwards, but the reason takes some unpacking. Two genuinely different objects are involved, and neither is optional:
 
- **The quantum *state*** — call it $|\psi\rangle$ — is the actual physical thing a qubit *is*. It lives in a 2-dimensional space spanned by the basis states $|0\rangle$ and $|1\rangle$, and can be either of those, or any superposition $\alpha|0\rangle+\beta|1\rangle$. This is the "$|\psi\rangle$" you were picturing.
- **The quantum *operator*** — here, $Z$ — is a mathematical machine (a matrix) that *acts on* a state and extracts information from it. It is never itself "the qubit's condition"; it's the tool used to ask a question of a state (specifically: "what's your energy/spin along this axis?") and get a number back.
**We are not claiming $Z_i$ "is" the spin.** We're using $Z_i$ to *build a new object* — a Hamiltonian, an energy operator (see [[quantum-hamiltonian]]) — such that when this operator is applied to the *right state*, it hands back exactly the classical energy that configuration would have had. Here's the full mechanism, worked through concretely rather than just asserted:
 
### Step 1 — pick the encoding: which state stands for which classical spin?
 
We need a rule connecting a physical qubit state to a classical spin value. The natural choice — and precisely why $Z$ was picked, not some arbitrary operator — is to let each qubit's own computational basis states directly stand for the two classical spin values:
 
$$
|0\rangle \;\longleftrightarrow\; s = +1, \qquad |1\rangle \;\longleftrightarrow\; s = -1
$$
 
This isn't a coincidence dressed up after the fact — the Pauli-Z matrix is *defined* as
 
$$
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$
 
and its eigenvalue equation is exactly $Z|0\rangle = (+1)|0\rangle$ and $Z|1\rangle = (-1)|1\rangle$ (see [[quantum-hamiltonian]] for this worked in full). $Z$ was chosen specifically *because* its two eigenvalues are exactly $+1$ and $-1$ — the same two numbers a classical spin is allowed to take. That match is the whole reason it's the right tool for this job, not an arbitrary substitution.
 
### Step 2 — build the Hamiltonian by literally swapping $s_i \to Z_i$ in the formula
 
Take the classical Ising energy and mechanically replace every $s_i$ with $Z_i$:
 
$$
E(\mathbf{s}) = h\,s_1 \quad\longrightarrow\quad H = h\,Z_1
$$
 
**Check that this actually works, one spin at a time:**
 
$$
H|0\rangle = hZ_1|0\rangle = h(+1)|0\rangle = h|0\rangle
$$
 
$$
H|1\rangle = hZ_1|1\rangle = h(-1)|1\rangle = -h|1\rangle
$$
 
Compare to the classical values directly: $E(s=+1) = h$, and $E(s=-1) = -h$. **They match exactly** — $H$'s eigenvalue on $|0\rangle$ equals $E(+1)$, and its eigenvalue on $|1\rangle$ equals $E(-1)$, precisely because of the encoding chosen in Step 1 and $Z$'s own eigenvalues chosen in Step 2. This is the eigenvalue equation from [[quantum-hamiltonian]], $H|\psi_n\rangle = E_n|\psi_n\rangle$, showing up concretely: the *state* is $|0\rangle$ or $|1\rangle$ (exactly the $|\psi\rangle$ you were picturing), and the *operator* $H$ (built from $Z$) is what produces the right energy number when applied to that state.
 
### Step 3 — the two-spin case, to see why tensor products enter
 
For a coupling term $E(s_1,s_2) = J\,s_1s_2$, the substitution is $J\,s_1s_2 \to J\,Z_1Z_2$, where $Z_1Z_2$ means the **tensor product** of the two single-qubit operators, acting on the combined 2-qubit space (basis states $|00\rangle,|01\rangle,|10\rangle,|11\rangle$). A joint eigenstate's eigenvalue under a tensor product of operators is just the *product* of each factor's own eigenvalue — so:
 
$$
Z_1Z_2|00\rangle = (+1)(+1)|00\rangle = +1|00\rangle \quad\Rightarrow\quad H|00\rangle = J|00\rangle
$$
 
$$
Z_1Z_2|01\rangle = (+1)(-1)|01\rangle = -1|01\rangle \quad\Rightarrow\quad H|01\rangle = -J|01\rangle
$$
 
Check against the classical formula directly: $|00\rangle$ encodes $(s_1,s_2)=(+1,+1)$, giving $E=J(+1)(+1)=J$ — matches $H|00\rangle$'s eigenvalue exactly. $|01\rangle$ encodes $(s_1,s_2)=(+1,-1)$, giving $E=J(+1)(-1)=-J$ — matches too. The pattern holds for all four basis states, which is exactly the general rule stated in the full formula below.
 
### Step 4 — why go to all this trouble instead of just trying each configuration directly?
 
This is the actual payoff, and it's worth stating plainly since it's the entire point of building an *operator* rather than just picking one state at a time. If all we wanted was to evaluate $E(\mathbf{s})$ for one specific guess, we wouldn't need any of this — just plug numbers into the classical formula. The reason to build $H$ as an operator is that **a single quantum state can be a superposition across *every* basis state simultaneously** — one state, $|\psi\rangle = \sum_{\mathbf{s}} c_{\mathbf{s}} |\mathbf{s}\rangle$, with a piece corresponding to every possible classical configuration at once. Because $H$ was built by the substitution above, it correctly assigns the right energy eigenvalue to *every one* of those basis components simultaneously, through the same single operator — it doesn't need to be separately re-evaluated per configuration. That's what lets quantum dynamics (interference in QAOA, physical evolution in annealing) work across the whole configuration space at once, rather than one guess at a time the way classical brute force would.
 
**One-sentence summary to hold onto:** $s_i \to Z_i$ isn't "turning a number into a state" — it's "encoding an entire classical cost function into a single quantum operator, engineered so that its eigenvalues on the computational basis states exactly reproduce that cost function's values," which is precisely what makes the ground-state-finding machinery of [[adiabatic-theorem|annealing]] or the measurement-based machinery of VQE/QAOA (see [[quantum-hamiltonian]]) applicable to the original classical optimization problem at all.
 
### Checking the big picture against a plain-language summary
 
A natural way to summarize all of Sections 17–18: *"we take the QUBO, convert to $\pm1$ spins, turn $F(\mathbf{s})$ into a function that measures energy, then test different inputs (brute force, optimization, etc.) to see which one has the least energy — that's the answer."*
 
Most of this is exactly right, and worth confirming piece by piece: yes, the goal genuinely is to find the configuration with minimum (or maximum) energy, and yes, that configuration — the [[quantum-hamiltonian|ground state]] — *is* the answer to the original problem. That part of the picture is correct.
 
**One word is worth sharpening, though: "test different inputs."** That phrase describes exactly what *classical* methods do — brute force literally evaluates $F(\mathbf{s})$ for each candidate one at a time; classical optimization (simulated annealing, tabu search, gradient-based heuristics) is smarter about which candidates to try next, but it's still fundamentally evaluating one configuration, then another, then another. Nothing in Sections 17–18 was required to do *that* — plain classical code can minimize $F(\mathbf{s})$ directly, with no qubits, no $Z$ operators, no Hamiltonian at all.
 
**The entire reason to go to the trouble of building $H$ as a quantum operator (rather than just optimizing $F(\mathbf{s})$ classically) is specifically to *avoid* one-at-a-time testing** — this is exactly what Step 4 above was pointing at. A quantum state can hold a superposition across every candidate configuration simultaneously, and because $H$ was built so its eigenvalues match $F$ on every basis state at once, the door is open to strategies that never inspect configurations individually:
- **Annealing** ([[adiabatic-theorem]]): the physical system evolves continuously toward $H$'s ground state — there's no loop stepping through candidates one by one; it's one continuous physical process across the whole landscape at once.
- **QAOA / VQE** ([[quantum-hamiltonian]]): a superposed state gets measured, and interference between the superposed components (not sequential testing) is what concentrates probability onto low-energy configurations over repeated rounds.
So the corrected one-line version: *we build $H$ so that its eigenvalues reproduce every classical configuration's energy at once; the ground state is the answer; and the reason to bother with quantum mechanics here at all is that annealing and QAOA can search for that ground state without literally testing configurations one at a time the way classical brute force or classical optimization does.*
 
## 19. Where QAOA fits
 
**QAOA — Quantum Approximate Optimization Algorithm** — one gate-model algorithm commonly paired with QUBO problems (this is alternative to [[quantum-annealing-overview|annealing hardware]] if staying in the gate-model paradigm from e.g. Jiang et al., Tezuka et al.).
 
1. Create a quantum state representing many possible configurations.
2. Construct a **cost Hamiltonian** from the QUBO.
3. Apply parameterized quantum operations encoding the cost.
4. Measure the qubits.
5. Use a classical optimizer to update the parameters.
6. Repeat.
7. Eventually, high-quality solutions should be sampled with high probability.
```text
QUBO
  ↓
Cost Hamiltonian
  ↓
Quantum circuit
  ↓
Measurement
  ↓
Classical optimizer
  ↺
```
 
QUBO is the **problem formulation**. QAOA is one possible **algorithm for attacking that formulation** — don't confuse the two (see Section 20).
 
## 20. An important misconception
 
It's tempting to say "QUBO is a quantum algorithm." **It is not.** QUBO is a mathematical formulation of an optimization problem: $\min_{\mathbf{x}\in\{0,1\}^n}\mathbf{x}^TQ\mathbf{x}$. Once you have that formulation, you *choose* how to solve it:
 
```text
                  QUBO
                    │
          ┌─────────┼─────────┐
          ↓         ↓         ↓
      Classical   Quantum   Hybrid
       methods    methods    methods
          │         │         │
     SA / tabu     QAOA     classical
     / exact       / QA     optimizer
```
 
## 21. Why QUBO can be powerful
 
Many complicated-looking problems reduce to binary decisions, individual rewards/costs, and pairwise interactions: $E(\mathbf{x}) = \text{constant} + \text{linear terms} + \text{quadratic terms}$. Once in that form, many optimization techniques (classical or quantum) can work with it directly. The hard part is usually **not** running the optimizer — it's **finding a good QUBO formulation of the original problem** in the first place. That's where most of the actual problem-specific modeling work happens, and it's the part a thesis genuinely has to design, not just look up.
 
## 22. Connection to correspondence selection
 
This is directly the encoding this vault's [[RANSAC]] discussion has been circling. Suppose an image matcher (SIFT/ORB) produces $N$ candidate correspondences. For each, define:
 
$$
x_i = \begin{cases} 1 & \text{correspondence } i \text{ is selected (kept as inlier)} \\ 0 & \text{correspondence } i \text{ is rejected (outlier)} \end{cases}
$$
 
Two correspondences can be geometrically compatible or incompatible under a shared transform — assign a pairwise compatibility score $C_{ij}$. A possible objective:
 
$$
\boxed{E(\mathbf{x}) = -\sum_i w_i x_i - \sum_{i<j} C_{ij}x_ix_j}
$$
 
where $w_i$ is the quality/confidence of correspondence $i$, $C_{ij}$ is pairwise geometric compatibility, and the $x_ix_j$ product activates the pairwise term only when *both* correspondences are selected. This has exactly the QUBO structure: linear terms + quadratic pairwise terms.
 
**Important honesty note, worth keeping front and center:** this does *not* automatically mean it's the best formulation for homography estimation specifically. The compatibility score $C_{ij}$, any constraints, scaling of $w_i$ vs. $C_{ij}$, and the relationship to actual [[projective-transformation|homography]] geometry all need real design and experimental validation — this is exactly the "finding a good QUBO formulation" work flagged as the hard part in Section 21. But mathematically, this is the same basic idea as the scheduling example this whole note started with — worth holding onto that continuity when the notation starts looking intimidating in an actual paper.
 
## 23. The central idea to remember
 
$$
\boxed{\min_{\mathbf{x}\in\{0,1\}^n}\left(c+\sum_i a_ix_i+\sum_{i<j}b_{ij}x_ix_j\right)}
$$
 
Three pieces: the **individual decision** term $a_ix_i$ ("what happens if I select decision $i$?"), the **pairwise interaction** term $b_{ij}x_ix_j$ ("what happens if I select both $i$ and $j$?"), and **optimization** — find the binary assignment making the total as good as possible.
 
## 24. One mental model
 
```text
                 THE PROBLEM
                      │
          "What decisions can I make?"
                      ↓
             Binary variables
             x₁ x₂ x₃ ... xₙ
                      │
                      ↓
        "What is good/bad about
         each decision?"
                      ↓
              Linear terms
                  aᵢxᵢ
                      │
                      ↓
        "How do decisions interact?"
                      ↓
             Quadratic terms
                 bᵢⱼxᵢxⱼ
                      │
                      ↓
                   QUBO
                      │
                      ↓
          Choose an optimizer
             /            \
       Classical         Quantum
                         (e.g. QAOA)
```
 
The quantum computer is **not discovering what your variables mean.** You, as the problem designer, formulate the problem. The quantum algorithm then works on the mathematical optimization problem you gave it — worth remembering whenever a paper's results sound more "magical" than they are.
 
## 25. QUBO vocabulary
 
| Term               | Meaning                                                                       |
| ------------------ | ----------------------------------------------------------------------------- |
| QUBO               | Quadratic Unconstrained Binary Optimization                                   |
| Binary variable    | Variable restricted to 0 or 1                                                 |
| Objective function | Function we want to minimize/maximize                                         |
| Linear term        | $a_ix_i$                                                                      |
| Quadratic term     | $b_{ij}x_ix_j$                                                                |
| QUBO matrix        | Matrix containing objective coefficients                                      |
| Constraint         | A rule solutions must satisfy                                                 |
| Penalty            | Extra objective cost for violating a constraint                               |
| Ising model        | Equivalent formulation using spins $\{-1,+1\}$ — see [[ising-model-and-qubo]] |
| Hamiltonian        | Quantum operator representing the cost/energy                                 |
| QAOA               | Quantum Approximate Optimization Algorithm                                    |
| QUBO solver        | Any method that attempts to find a good QUBO solution                         |
|                    |                                                                               |
 
## 26. Final picture
 
$$
\boxed{\text{Real-world problem} \rightarrow \text{binary decisions} \rightarrow \text{quadratic objective} \rightarrow \text{QUBO}}
$$
 
and, to use a quantum computer:
 
$$
\boxed{\text{QUBO} \rightarrow \text{Ising model} \rightarrow \text{Hamiltonian} \rightarrow \text{quantum algorithm}}
$$
 
The most important conceptual distinction: **QUBO is the formulation. QAOA (or quantum annealing) is an algorithm that can be used to solve the formulation.** Once this is clear, most "quantum optimization" papers become much easier to read — including Chin & Suter's robust-fitting line of work on my reading list, which is, underneath everything, "here's our QUBO formulation" plus "here's the hardware we solved it on."
 
