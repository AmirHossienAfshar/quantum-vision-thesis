**Source:** "Formal Methods for Quantum Programs: A Survey"  
**Chapter:** Overview of Formal Methods in Quantum Computing

---

## Main Formal Methods

### 1. Type Checking

A static, compile-time technique that ensures expressions, functions, and data structures follow the rules of a type system.

Type checking is like a **grammar checker for data**.

**It ensures:**

- You don't add numbers to strings.
- You don't call a function with the wrong inputs.
- You only access fields that belong to an object.
- You follow the language's structural rules.

---

### 2. Model Checking

Automatic exploration of _all possible states_ of a system to verify that it satisfies a formal specification (usually in temporal logic).

Model checking exhaustively checks _all possible states_ of a system.

**Process:**

1. You describe the system as a **state machine**.
2. You write properties to check, like:
    - "It never deadlocks."
    - "If button pressed, door eventually opens."
3. The model checker explores _all possible paths_.

---

### 3. Abstract Interpretation

- It analyzes the program _without running it_ by building an **approximate mathematical model** of all possible values.
- It allows analysis of huge programs because it simplifies behavior without losing safety.
- Static analysis that approximates the behavior of a quantum program using mathematical abstractions.

**Purpose:**  
Analyze large quantum programs by replacing exact state evolution with safe over-approximations.

**Examples of abstractions:**

- Entanglement tracking
- Alias analysis for qubits
- Resource usage (depth, qubits)

---

### 4. Deductive Verification (First-order reasoning)

It proves that **actual code** satisfies **mathematical specifications**.

It uses **preconditions**, **postconditions**, **loop invariants**, etc.

Uses Hoare-style logic to prove that a program satisfies formal specifications.

**Purpose:**  
Prove correctness with:

- Preconditions
- Postconditions
- Loop invariants (if classical control present)

---

### 5. Interactive Proof Systems (Second-order reasoning)

This is _full mathematical proof_ about software or hardware.

You construct proofs step-by-step:

- define data types
- state theorems
- write lemmas
- use tactics like "induction", "rewrite", "apply"

The assistant checks every inference.

It's like doing real mathematics, but about code.

Manual, step-by-step construction of mathematical proofs about quantum programs using proof assistants (Coq, Isabelle, Lean).

**Purpose:**  
Build complete correctness proofs for quantum algorithms or protocols.

**Characteristics:**

- Most expressive method
- Most work-intensive
- Supports second-order reasoning (over operators, states, semantics)

---

## Relationships Between the Methods

- **Type checking** ⟶ ensures well-formedness before deeper analysis.
- **Abstract interpretation** ⟶ scalable static analysis.
- **Model checking** ⟶ automatic state exploration, but limited by quantum state-space size.
- **Deductive verification** ⟶ precise but needs strong specifications.
- **Interactive proving** ⟶ most expressive; proves algorithm-level correctness.