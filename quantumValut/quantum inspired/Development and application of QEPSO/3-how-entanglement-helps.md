## What PSO actually does (strip it to essentials)

PSO iteratively:

1. proposes candidate solutions
2. evaluates them
3. biases future proposals toward better regions

Anything that:

* reduces useless randomness
* increases meaningful structure

**helps PSO**.

---

## What entanglement *becomes* inside PSO

When they “simulate entanglement”, they are doing this:

> **They restrict the space of allowed candidates.**

Instead of:

```
bit₁ ∈ {0,1}
bit₂ ∈ {0,1}
(all 4 combinations allowed)
```

They enforce:

```
(bit₁, bit₂) ∈ {(0,0), (1,1)}
```

So the search space shrinks:

* from 4 possibilities → 2 possibilities

This is the **core benefit**.

