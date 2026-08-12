# 3 — Filter generation methodology (Section 3.4)

How one specific quanvolutional filter (i.e. one instance of `q`) is actually constructed.

## Setup

- Patch size `n = 3` -> `9` qubits per filter
- Qubits treated as **nodes in a graph**

## Build steps

1. **2-qubit gates (entangling structure):** for every possible pair of qubits, flip a biased coin using a fixed "connection probability" — if it hits, place a 2-qubit gate between that pair, randomly chosen from:
   - `CNOT`
   - `SWAP`
   - `SqrtSWAP
   - `ControlledU`
2. **1-qubit gates (local rotations):** sample a random count in
   `[0, 2n^2]`, each with:
	   - random target qubit
   - random gate from `{X(θ), Y(θ), Z(θ), U(θ), P, T, H}`
   - random angle `θ` where applicable
3. **Shuffle** the full combined gate list order

The result — one random, fixed circuit — **is** the filter. It's stored/used exactly as generated;  here's no further optimization step.

## What this buys structurally, vs. a classical random filter

A classical random conv filter is "random weights, same additive structure" — no matter how scrambled the weights are, the *functional form* stays a weighted sum. The 2-qubit gates above (specifically the entangling ones — CNOT, SqrtSWAP, ControlledU) let outputs depend on **joint correlations** between input qubits that can't be reduced to any weighted sum. That's the structural difference the whole paper's "richer function class" argument rests on.
