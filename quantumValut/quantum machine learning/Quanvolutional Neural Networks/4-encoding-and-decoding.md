# 4 — Encoding & decoding (Sections 3.3–3.5)

## Encoding: classical patch -> initial qubit states

Simplest possible scheme (their choice, not the only option):

- Apply a threshold (they used `0`) to each pixel
- pixel `>` threshold -> qubit initialized to `|1>`
- pixel `<=` threshold -> qubit initialized to `|0>`

3x3 patch -> 9 classical bits -> 9 qubits' initial states.

## Decoding: quantum output -> single scalar

Goal: match the "one scalar out" contract of a classical conv filter.

Steps:
1. Run the circuit, get the **full probability distribution** over all `2^9 = 512` possible joint 9-bit outcomes
2. Take the **single most likely** bitstring (argmax over the 512 probabilities) — not a simulated measurement, a deterministic "peak of the distribution" pick
3. **Count how many of those 9 bits are `1`** -> integer in `[0, 9]`
4. That integer is `f_x`, the filter's output for that patch

### Why 512, not 9 numbers

Naive first guess: 9 qubits -> 9 independent probabilities. Wrong once entangling gates are involved — entangled qubits aren't independent, so you need a probability for **every joint combination** of all 9 bits together: `2^9 = 512` numbers, summing to 1.

### Why "most likely state," not real measurement

Real hardware: no access to the full distribution, only actual measurement samples (shots) — repeated runs, statistical estimate, always some noise. Simulation: full state vector computable exactly, so they can skip sampling entirely and just take the analytic argmax. Deterministic, same patch -> same output every time. **This exact decoding method is flagged by the authors as infeasible on real hardware** — future work would need a
shots-based version instead.

### Lookup table (computational shortcut, simulation-only)

Because encoding is binary/threshold, the input domain is finite: exactly `2^9 = 512` possible patches. So: precompute the full input -> output mapping **once per filter**, then applying the filter to real data is just a dictionary lookup, not a re-run of the quantum circuit. This is purely a classical-simulation trick — wouldn't help on real hardware, since you can't precompute all 512 "true" measurement outcomes without infinite shots per input anyway.