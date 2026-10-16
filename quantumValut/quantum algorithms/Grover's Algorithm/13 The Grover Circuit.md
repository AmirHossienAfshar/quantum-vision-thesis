---
tags: [quantum, grover, circuits]
---
# 13 The Grover Circuit

Three register qubits $q_2q_1q_0$ plus one ancilla, marked item $w=101$, $k=2$ rounds ($N=8$).

```
q2 : ───────H─────────●─────────H────X────●────X────H────M──
                      │                   │
q1 : ───────H────X────●────X────H────X────●────X────H────M──
                      │                   │
q0 : ───────H─────────●─────────H────X────●────X────H────M──
                      │
anc: ──X────H─────────⊕─────────────────────────────────────
```

The block from the first $X$ on $q_1$ through the last $H$ is **repeated twice** (the same gates each round). The three $\bullet$ on the diffusion block form a CCZ.

## Reading it left to right
- **Prepare.** $H$ on each register qubit builds $\lvert s\rangle$. On the ancilla, $X$ then $H$ builds $\lvert-\rangle$ (this is what turns the oracle's bit flip into a sign flip).
- **Oracle** ([[10 Building the Oracle from Gates]]). $X$ on $q_1$ because $w=101$ has a $0$ there. The three dots with $\oplus$ on the ancilla are the triple-controlled NOT: it flips the ancilla only when $q_2=q_1=q_0=1$, which by phase kickback puts a $-1$ on $\lvert101\rangle$. The second $X$ on $q_1$ undoes the first.
- **Diffusion** ([[12 Building the Diffusion Operator]]). $H$, $X$, CCZ, $X$, $H$ on all three register qubits. The $X$'s move the special state between $\lvert000\rangle$ and $\lvert111\rangle$; the outer $H$'s move $\lvert s\rangle$ to $\lvert000\rangle$ and back. Overall this is $D$ up to a global sign.
- **Repeat** twice.
- **Measure** $q_2q_1q_0$. You get $101$ with probability $121/128\approx94.5\%$. The ancilla is never measured; it stays in $\lvert-\rangle$.

## Gate bookkeeping
| Block | Gates |
|---|---|
| Prepare | $3\times H$ (register), $X$ and $H$ (ancilla) |
| Oracle | $2\times X$, one $C^3X$ |
| Diffusion | $6\times H$, $6\times X$, one CCZ |

$C^3X$ and CCZ are not native on real hardware; a compiler breaks each into Toffolis/CNOTs and single-qubit gates ([[11 CNOT and Toffoli Gates]]).

The numbers at each step are in [[14 Worked Example N=8]].

---
Previous: [[12 Building the Diffusion Operator]] · Next: [[14 Worked Example N=8]]
