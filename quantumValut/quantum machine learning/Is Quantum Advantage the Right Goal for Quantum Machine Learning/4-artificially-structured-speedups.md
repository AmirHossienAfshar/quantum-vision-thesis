# Reason 1: Speedups Only Proven on Artificially Structured Problems

## The core claim
Proving an *exponential* quantum speed-up requires a problem specially structured to favor quantum computers — the data distribution p(x) or ground truth f\* has some hidden bias baked in that a quantum circuit happens to exploit well. Fine as pure math, but it says almost nothing about real ML problems, since real-world data doesn't come hand-crafted to suit quantum circuits.

**Important distinction (clarified via discussion):** this critique targets *theoretical, provable* exponential speed-up claims — not empirical papers that just run a quantum model on real data (e.g., MNIST-style experiments). Empirical small-scale studies get a separate critique (see note 7) about cherry-picked benchmarks and reproducibility, not "artificial structuring."

## Concrete example: the discrete logarithm classification problem
The clearest rigorous example (Liu, Arunachalam, Temme — ref [70]) builds a classification task **directly out of the discrete logarithm problem** — the same structure Shor's algorithm solves exponentially faster than any known classical algorithm.

How it works:
- Inputs aren't natural data (images, emails) — they're numbers with specific **group-theoretic, periodic structure**, the kind Shor's algorithm exploits via the quantum Fourier transform.
- Labels are defined by whether one number is the discrete logarithm of another under modular arithmetic — a problem believed classically hard, known to be quantum-easy.
- Because the periodic structure is baked directly into how data/labels are generated, a quantum circuit exploits it the same way Shor's algorithm does — and researchers can *prove*, rigorously, no classical algorithm can match it (under standard cryptographic hardness assumptions).

**Why "artificial":** nobody would encounter this exact classification task in the real world. It was constructed specifically because its structure matches what quantum computers are provably good at — reverse-engineered from "what can we prove quantum wins at," not from "what's a real ML problem people care about."

## Connection to the "no free lunch" theorem
Real-world ML success comes from being **agnostically** applied to messy problems with no known inductive bias suited to the data (unlike quantum algorithms, which pick problems with heavy, known structure). The **no free lunch theorem** states any algorithm performing well on one problem will necessarily do worse on another. So proving a win on one artificially convenient problem tells you nothing about general-purpose usefulness.

## Is there a "framework" to convert classical data into quantum-favored data?
No — and this isn't just an engineering gap waiting to be filled. Quantum speedups like Shor's exploit a *very specific* kind of hidden structure (periodicity in modular arithmetic, symmetry groups) via interference. Real datasets (spam, images, medical data) simply don't contain that kind of structure — there's nothing to inject. A universal "make any dataset quantum-favored" framework would have to fabricate structure that isn't there, meaning it would no longer be solving the *original* real-world problem. This is a structural gap, not a temporary one — it's precisely the no-free-lunch principle in action.