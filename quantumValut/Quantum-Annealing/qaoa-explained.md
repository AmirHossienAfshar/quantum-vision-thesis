---
tags: [quantum-computing, gate-model, optimization, thesis-core, beginner-friendly]
status: foundation
related:
  - "[[qubo-explained]]"
  - "[[ising-model-and-qubo]]"
  - "[[quantum-hamiltonian]]"
  - "[[quantum-annealing-overview]]"
  - "[[adiabatic-theorem]]"
  - "[[RANSAC]]"
---

# QAOA — A Beginner-Friendly Introduction

> Small but important correction before starting: **QAOA does not formalize a QUBO.** The QUBO ([[qubo-explained]]) is the mathematical formulation of the optimization problem; **QAOA is a quantum algorithm that can be used to approximately solve that formulation.** The clean mental pipeline for the whole cluster of notes so far:
>
> $$
> \boxed{\text{Problem} \rightarrow \text{QUBO} \rightarrow \text{Hamiltonian} \rightarrow \text{QAOA} \rightarrow \text{Solution}}
> $$

## 1. What is QAOA?

**QAOA** stands for **Quantum Approximate Optimization Algorithm**. It's a **hybrid quantum-classical algorithm** for finding good solutions to combinatorial optimization problems — including anything already written as a [[qubo-explained|QUBO]]:

$$
\min_{\mathbf{x}\in\{0,1\}^n} f(\mathbf{x})
$$

The important word is **Approximate**. QAOA doesn't guarantee a gate-model quantum computer will immediately find the exact global optimum. Instead, it prepares a quantum state from which **good solutions can be sampled with high probability**, while a classical optimizer tunes the circuit to keep improving those odds.

## 2. The big picture

We already know how to build a QUBO — the hard, problem-specific modeling work is [[qubo-explained|done separately]]. Now we want to use a gate-model quantum computer to actually search it:

```text
              Original problem
                    │
                    ▼
                  QUBO
             min xᵀQx
                    │
                    ▼
             Ising / Hamiltonian
                    │
                    ▼
              QAOA circuit
                    │
          ┌─────────┴─────────┐
          │                   │
       Quantum             Classical
       computer             optimizer
          │                   │
          └─────────┬─────────┘
                    │
                    ↺
              repeat / optimize
                    │
                    ▼
              measured bitstring
                    │
                    ▼
                 solution
```

This back-and-forth between the quantum computer and a classical optimizer is exactly why QAOA is called **hybrid**.

## 3. Reusing the scheduling problem

Recall [[qubo-explained]]'s four-talk scheduling example: talks $A,B,C,D$, each $x_i\in\{0,1\}$ meaning morning or afternoon, and a QUBO objective $E(\mathbf{x})=\mathbf{x}^TQ\mathbf{x}$ built from which students want which pairs of talks on different days. The classical optimization problem was:

$$
\boxed{\min_{\mathbf{x}\in\{0,1\}^4} E(\mathbf{x})}
$$

Now we want QAOA to search for a good $\mathbf{x}$.

## 4. Quantum computers don't directly understand QUBO matrices

A QUBO is written with classical binary variables $x_i\in\{0,1\}$. Quantum computers work with qubits and quantum operators. So the QUBO first gets transformed into the [[ising-model-and-qubo|Ising formulation]] — spin variables $s_i\in\{-1,+1\}$, via $s_i=1-2x_i$ or $x_i=\frac{1-s_i}{2}$ — giving $E(\mathbf{s}) = C + \sum_i h_is_i + \sum_{i<j}J_{ij}s_is_j$. This part is pure classical algebra, already fully worked through in [[qubo-explained]] Section 17 — nothing new to derive here.

## 5. From Ising model to Hamiltonian — the cost Hamiltonian

Now the genuinely quantum part enters (worked in full, with 1- and 2-spin examples, in [[qubo-explained]] Section 18): replace each spin $s_i$ with the Pauli-Z operator, $s_i \rightarrow Z_i$, giving the **cost Hamiltonian**:

$$
\boxed{H_C = CI + \sum_i h_iZ_i + \sum_{i<j}J_{ij}Z_iZ_j}
$$

This is the quantum representation of the objective function — see [[quantum-hamiltonian]] for what a Hamiltonian formally is and why this substitution works.

## 6. What the Hamiltonian actually does

For a computational-basis state like $|0101\rangle$ (corresponding to $\mathbf{x}=(0,1,0,1)$), the cost Hamiltonian assigns it an energy:

$$
H_C|0101\rangle = E(0101)|0101\rangle
$$

Every possible binary solution corresponds to a quantum basis state, and $H_C$ assigns that state an energy equal to the objective value:

```text
|0000⟩  → energy =  0
|0001⟩  → energy = -2
|0010⟩  → energy = -2
|0101⟩  → energy = -8   ← very good
|1111⟩  → energy =  0
```

(the exact numbers depend on the specific QUBO — this is illustrative). The principle: $\boxed{\text{better solution} \leftrightarrow \text{lower energy}}$ for a minimization problem, so ideally $\boxed{\text{ground state} = \text{optimal solution}}$ — exactly the eigenvalue-equation idea from [[quantum-hamiltonian]], now applied concretely across an entire solution space at once.

## 7. So why not just prepare the lowest-energy state directly?

Because we don't know which state that is — that's the entire optimization problem. With $n$ binary variables there are $2^n$ possibilities: for $n=5$, that's $32$, trivial; for $n=50$, that's $\approx 1.13\times10^{15}$ — nobody wants to check each one explicitly. QAOA's strategy: use a quantum state that represents many possible configurations at once, and **steer the probability toward good configurations** rather than checking them one at a time.

## 8. The starting state — equal superposition

QAOA begins by putting every qubit into superposition. For one qubit, $|+\rangle = \frac{|0\rangle+|1\rangle}{\sqrt2}$; for $n$ qubits:

$$
|+\rangle^{\otimes n} = \frac{1}{\sqrt{2^n}}\sum_{\mathbf{x}}|\mathbf{x}\rangle
$$

For three variables, explicitly: $|+\rangle^{\otimes3} = \frac{1}{\sqrt8}\left(|000\rangle+|001\rangle+|010\rangle+|011\rangle+|100\rangle+|101\rangle+|110\rangle+|111\rangle\right)$ — equal-amplitude superposition across **every** binary solution simultaneously.

## 9. Superposition alone doesn't solve anything

Worth stating explicitly, since it's a genuine and common misconception: merely having $|000\rangle+|001\rangle+\cdots+|111\rangle$ does **not** mean the problem is solved. The state needs to be steered so good solutions become likelier than bad ones — that's the job of the cost Hamiltonian, next.

## 10. The cost layer

QAOA applies a unitary built from the cost Hamiltonian:

$$
\boxed{U_C(\gamma) = e^{-i\gamma H_C}}
$$

with $\gamma$ a tunable real parameter — this is the **cost unitary** (sometimes called the phase-separation operator). It doesn't simply "delete bad solutions and keep good ones" — instead, it changes the quantum amplitudes/phases of each basis component according to that configuration's objective value, in a way that, combined with the next layer, can increase the probability of eventually measuring good solutions.

## 11. The mixer layer

If the cost layer encodes "what's good," something else is needed to let the state actually explore different candidates. QAOA uses a **mixer Hamiltonian**, standardly:

$$
\boxed{H_M = \sum_i X_i}
$$

($X_i$ the Pauli-X operator on qubit $i$), with mixer unitary $\boxed{U_M(\beta)=e^{-i\beta H_M}}$. The intuitive split:

```text
Cost Hamiltonian  → "What solutions are good?"
Mixer Hamiltonian → "Explore different solutions."
```

This interplay between evaluation and exploration is the heart of QAOA.

## 12–13. Layers and depth

One QAOA layer is $U_M(\beta)U_C(\gamma)$, applied to the starting superposition: $|\psi(\gamma,\beta)\rangle = U_M(\beta)U_C(\gamma)|+\rangle^{\otimes n}$. This can be repeated $p$ times — $p$ is the **QAOA depth**:

$$
|\psi_p(\boldsymbol\gamma,\boldsymbol\beta)\rangle = \prod_{k=1}^{p} U_M(\beta_k)U_C(\gamma_k)\,|+\rangle^{\otimes n}
$$

For $p=2$: $|\psi\rangle = U_M(\beta_2)U_C(\gamma_2)U_M(\beta_1)U_C(\gamma_1)|+\rangle^{\otimes n}$, and so on.

## 14–15. Where the classical computer enters

The best values of $\gamma_1,\dots,\gamma_p$ and $\beta_1,\dots,\beta_p$ aren't known in advance — a **classical optimizer** finds them:

```text
Choose γ and β → Run quantum circuit → Measure / estimate energy →
Classical optimizer → Choose better γ, β → Run circuit again → ...
```

Specifically, the classical optimizer minimizes the expectation value (see [[quantum-hamiltonian]] for what an expectation value is and why it needs many repeated shots, not one measurement):

$$
\boxed{\langle H_C\rangle = \langle\psi_p(\boldsymbol\gamma,\boldsymbol\beta)|H_C|\psi_p(\boldsymbol\gamma,\boldsymbol\beta)\rangle}
$$

The loop continues until the optimizer stops finding improvement.

## 16. What "measurement" actually means here

After optimization, the state might look roughly like $|\psi\rangle = 0.05|0000\rangle+0.03|0001\rangle+\cdots+0.80|0101\rangle+\cdots$ — those coefficients are amplitudes, not probabilities of getting "the whole answer." Measuring gives **one bitstring**, e.g. $0101$. Repeating the measurement many times builds a distribution:

```text
0000 →  1%
0001 →  2%
0010 →  1%
...
0101 → 75%
...
```

The goal is for good solutions to dominate this distribution. QAOA is, at its core, a **sampling-based** optimization method.

## 17. Why "Approximate"?

QAOA doesn't necessarily return the exact optimum. If the true optimum is $E^*=-20$ but optimization converges to $E=-19$, that's a very good but not exact answer — and depending on the problem and circuit depth, results can sometimes be considerably worse. More layers $p$ generally means more expressive power, but a deeper, harder-to-run circuit. Hence: **Approximate** Optimization Algorithm.

## 18. Why QAOA is a hybrid algorithm

The **quantum computer** does: state preparation, parameterized gates, evolution, measurement. The **classical computer** does: choose parameters, evaluate the measured objective, optimize the parameters, repeat.

$$
\boxed{\text{QAOA} = \text{Quantum circuit} + \text{Classical optimization loop}}
$$

## 19. A tiny worked example

Two binary variables, $x_1,x_2$, objective $E(\mathbf{x}) = -x_1-x_2+2x_1x_2$:

| $x_1$ | $x_2$ | $E(\mathbf{x})$ |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | −1 |
| 1 | 0 | −1 |
| 1 | 1 | 0 |

Optimum: $(0,1)$ or $(1,0)$, both giving $E=-1$. QAOA doesn't test these four one after another — it starts from $\frac12(|00\rangle+|01\rangle+|10\rangle+|11\rangle)$, the cost layer encodes the differences in $E$ between configurations, the mixer allows exploration, and the classical optimizer tunes $\gamma,\beta$ so that eventually $P(01)+P(10)$ becomes large — making an optimal answer likely on measurement.

## 20. QAOA is *not* "trying every solution simultaneously"

A common but misleading beginner explanation: *"the quantum computer tries all possible solutions simultaneously."* The quantum state does contain amplitudes for many candidate solutions at once — but **measurement gives only one result**. The actual power of the algorithm comes from manipulating amplitudes so desirable solutions become *more likely* to be the one you measure — which is exactly why the cost and mixer layers matter, rather than superposition alone (Section 9) being sufficient.

## 21. QAOA vs. brute force

With $n$ variables and $2^n$ possibilities: **brute force** explicitly evaluates every single one, $000\ldots0$ through $111\ldots1$. **QAOA** prepares a quantum state over the whole solution space and uses the Hamiltonian plus parameterized evolution to bias the measurement distribution toward good solutions — without inspecting each one individually. This does **not** guarantee QAOA beats brute force on every problem; proving practical quantum advantage for QAOA on genuinely useful problems remains an open research question, not a settled fact.

## 22. QAOA vs. QUBO — don't conflate these

$$
\text{QUBO: "What problem are we solving?"} \qquad \text{QAOA: "How do we search for it on a gate-model computer?"}
$$

```text
QUBO         "What is the optimization problem?"
   ↓
Hamiltonian  "How is that objective represented quantum mechanically?"
   ↓
QAOA         "How do we use a quantum circuit to search for
              a low-energy solution?"
```

## 23. QAOA vs. quantum annealing — the comparison worth getting precise

These solve the *same kind* of problem (anything expressible as a [[qubo-explained|QUBO]]/[[ising-model-and-qubo|Ising model]]) but via genuinely different mechanisms — and the relationship between them is closer and more principled than "two unrelated options," so it's worth building up properly rather than just listing differences.

**The core problem gate-model computers face, that annealing doesn't:** [[quantum-annealing-overview|Annealing hardware]] *physically is* a system that naturally evolves according to the Schrödinger equation — set up $H_{start}$ and $H_{problem}$, and the [[adiabatic-theorem]] governs a continuous morph between them, done automatically by physics. A gate-based computer has no such continuous physical process available — it only knows how to apply a sequence of discrete gates. QAOA is what you get when you try to *approximate* that same continuous adiabatic journey using only discrete gate operations.

**The direct correspondence, piece by piece:**

| Annealing ([[quantum-annealing-overview]]) | QAOA |
|---|---|
| $H_{start}$ (easy superposition ground state) | Initial state $|+\rangle^{\otimes n}$ (Section 8) — same role, same state |
| $H_{problem}$ (ground state = answer) | Cost Hamiltonian $H_C$ (Section 5) — the identical mathematical object |
| Continuous interpolation $H(t)=A(s)H_{start}+B(s)H_{problem}$ | Discrete alternating layers $U_M(\beta_k)U_C(\gamma_k)$ (Sections 10–13) |
| Physical evolution, governed by the [[adiabatic-theorem|adiabatic theorem]] | **Trotterization** — a standard technique for approximating continuous time-evolution under a changing Hamiltonian using a sequence of small discrete steps |
| One continuous run; read out once | An explicit outer loop: run, measure, classically adjust $\gamma,\beta$, repeat (Sections 14–15) |
| Dedicated annealing hardware (D-Wave) | General-purpose gate-model hardware (IBM, IonQ, etc.) |

**Why this connection matters, not just as trivia:** QAOA is, formally, a Trotterized approximation of the same adiabatic passage annealing performs physically. **The more layers $p$ used, the closer QAOA approximates true adiabatic evolution** — this is a real, provable statement, not just a loose analogy. But more layers also means a deeper circuit, and real (NISQ) gate-model hardware accumulates more error as circuits get deeper — which is the actual, concrete reason practical QAOA experiments today typically stick to small $p$ (often just 1–3 layers). Annealing hardware doesn't face this particular trade-off the same way, since it performs the "full continuous version" as one physical process rather than building it up from discrete approximating steps — though annealing has its own honest limitations, covered in [[adiabatic-theorem]] (the real-hardware anneal-time vs. minimum-gap problem) and [[annealing-hardware-details]] (tunneling, limited connectivity, minor embedding overhead).

**One more structural difference worth naming:** annealing's mixer-equivalent (the transverse field driving $H_{start}$) is baked into the continuous hardware process itself, with no separate "mixer step" to design — whereas QAOA's mixer $H_M=\sum_iX_i$ is an explicit, separately chosen design decision (Section 11), and different mixer choices are an active area of QAOA research (constrained-problem-aware mixers, for instance) with no equivalent design freedom on annealing hardware.

**The one-sentence version to hold onto:** *annealing and QAOA are two different physical/algorithmic realizations of the exact same underlying idea — start in an easy superposition, gradually favor the low-energy configuration of a problem-specific Hamiltonian, read out the answer — but annealing does it as one continuous physical process on dedicated hardware, while QAOA does it as a finite, parameterized gate circuit tuned by an outer classical optimization loop, on general-purpose gate-model hardware.*

```text
                  QUBO
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
 Quantum annealing          QAOA
 (continuous physical      (discrete gate circuit,
  evolution, dedicated      general-purpose hardware,
  hardware, no outer loop)  outer classical loop)
```

## 24. The important equations, collected

| Object | Equation |
|---|---|
| Initial state | $\lvert\psi_0\rangle = \lvert+\rangle^{\otimes n}$ |
| Cost Hamiltonian | $H_C$ — represents the optimization problem |
| Mixer Hamiltonian | $H_M = \sum_i X_i$ (standard choice) |
| Cost unitary | $U_C(\gamma) = e^{-i\gamma H_C}$ |
| Mixer unitary | $U_M(\beta) = e^{-i\beta H_M}$ |
| QAOA state, depth $p$ | $\lvert\psi_p(\boldsymbol\gamma,\boldsymbol\beta)\rangle = \prod_{k=1}^p U_M(\beta_k)U_C(\gamma_k)\lvert\psi_0\rangle$ |
| Objective (classical optimizer minimizes) | $E(\boldsymbol\gamma,\boldsymbol\beta) = \langle\psi_p\rvert H_C\lvert\psi_p\rangle$ |
| Parameter search | $(\boldsymbol\gamma^*,\boldsymbol\beta^*) = \arg\min_{\boldsymbol\gamma,\boldsymbol\beta} E(\boldsymbol\gamma,\boldsymbol\beta)$ |

## 25. A final mental model

Think of QAOA as a game between two operations, with the classical optimizer as coach:

- **Cost layer:** "I know what a good solution looks like" — uses $H_C$.
- **Mixer layer:** "Let's explore other possible solutions" — uses $H_M$.
- **Classical optimizer:** "Try different strengths for those two operations until the measured solutions become good."

$$
\boxed{\text{Cost} \leftrightarrow \text{Explore} \leftrightarrow \text{Optimize parameters}}
$$

repeated over and over.

## 26. Connecting this to the thesis

This is where the QUBO/QAOA distinction becomes directly useful for the correspondence-selection direction already sketched in [[qubo-explained]] Section 22 and [[RANSAC]]. One binary variable $x_i$ per candidate correspondence, pairwise geometric-compatibility terms $C_{ij}x_ix_j$ — that's the QUBO. Feeding it through $\text{QUBO} \rightarrow \text{Ising Hamiltonian} \rightarrow \text{QAOA}$ is the gate-model alternative to the annealing route Chin & Suter's papers took:

```text
Feature matching
      ↓
Candidate correspondences
      ↓
Geometric compatibility
      ↓
     QUBO
      ↓
Cost Hamiltonian
      ↓
     QAOA
      ↓
Selected correspondences
      ↓
Homography estimation
```

Once QUBO is understood, QAOA stops being mysterious — the question shifts from *"what is this strange quantum circuit doing?"* to *"how is this circuit trying to minimize the energy corresponding to the QUBO I constructed?"* — the central idea of this whole note.
