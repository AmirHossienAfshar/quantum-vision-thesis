---
created: 2025-12-31
first_encounter: 2025-12-31
last_updated: 2025-12-31
status: evolving
---

## 1. The idea phase (1980s): “Classical computers are not enough”

**Problem noticed:**  
Simulating quantum systems on classical computers scales exponentially.
### Key moments

- **1981 – Richard Feynman**
    
    - Says: _“Nature isn’t classical, so why should our computers be?”_
    - Proposes a computer that itself obeys quantum mechanics.
        
- **1985 – David Deutsch**
    
    - Formalizes the **quantum Turing machine**
    - Introduces the idea of **universal quantum computation**

## 2. Algorithms ignite the field (1990s)

Quantum computing becomes _useful_, not just philosophical.
### Breakthroughs

- **1994 – Peter Shor** 
    - Polynomial-time factoring algorithm
    - Threatens RSA cryptography
        
- **1996 – Lov Grover**
    - Quadratic speedup for unstructured search

Impact:

- Governments and industry start paying attention

## 3. First physical qubits (late 1990s – 2000s)

People try to **physically realize** qubits.

### Early platforms

- Nuclear Magnetic Resonance (NMR)
- Ion traps

Reality check:
- Decoherence shows up immediately
- Qubits die fast
- Noise dominates

## 4. decoherence is unavoidable

Quantum systems **cannot be perfectly isolated**.
Two consequences:
1. Long algorithms are impossible without protection
2. Quantum computing needs **error correction**

But error correction seems impossible because:
> “You can’t copy a quantum state” (no-cloning theorem)

## 5. Quantum error correction is discovered (mid–late 1990s)

This is the _turning point_.
### Key results
- **1995 – Peter Shor**
    - First quantum error-correcting code    
- **1996 – Steane**
    - CSS codes
- **Late 1990s**
    - Fault-tolerant quantum computation theory emerges
Core idea:
- You don’t copy quantum information
- You **encode it non-locally**
- Measure errors _without measuring the state_

 This is where **logical qubits** are born (theoretically).

## 6. The long gap: theory ahead of hardware (2000–2015)

For ~15 years:
- Error correction exists on paper
- Hardware is nowhere near good enough

Why?
- Error rates too high
- Too few qubits
- Too much noise

Quantum computing survives mainly in:
- Universities
- National labs

## 7. The NISQ era begins (≈2016)

John Preskill coins the term **NISQ**:
> _Noisy Intermediate-Scale Quantum_

Characteristics:
- 50–1000 physical qubits
- No full error correction
- Short circuits only
    
Milestones:
- Google’s “quantum supremacy” experiment (2019)
- IBM publishes public roadmaps
- Cloud quantum computers appear

---

# Keywords

**Foundations**
- Richard Feynman quantum computer
- David Deutsch quantum Turing machine
- Shor’s algorithm factoring
- Grover’s algorithm

**Noise & limits**
- Quantum decoherence
- T1 T2 coherence times
- No-cloning theorem

**Error correction**
- Quantum error correction codes
- Shor code
- Steane code
- CSS codes
- Fault-tolerant quantum computation

**Modern era**
- NISQ quantum computing
- Surface code logical qubits
- Quantum error threshold theorem
- Logical vs physical qubits
- 
- Fault-tolerant quantum gates

**Industry**
- IBM quantum roadmap
- Google logical qubit experiment
- Trapped ion quantum computing coherence