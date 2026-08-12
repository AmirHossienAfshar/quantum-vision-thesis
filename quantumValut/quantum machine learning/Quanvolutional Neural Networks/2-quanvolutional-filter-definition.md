# 2 — Quanvolutional filter definition (Section 3.1)

## The formal pipeline

For a single quanvolutional filter `Q`, applied to a local patch `u_x` of the input:

```
i_x = e(u_x)        encoding:  patch -> initial quantum state
o_x = q(i_x)         circuit:   fixed random quantum circuit q applied to i_x
f_x = d(o_x)         decoding:  quantum output -> scalar

f_x = Q(u_x, e, q, d)
```

- `u_x`: an `n x n` local patch of the input (`n > 1`); paper uses `n = 3`
- `e`: the encoding function — one fixed choice per filter
- `q`: a **random quantum circuit** in BQP (bounded-error quantum polynomial time) — this is the "quantum" part, and it's fixed/untrained
- `d`: the decoding function, reducing the quantum output to a single scalar (so it slots into a CNN-style feature map, same shape as a classical conv filter's output)

## Why this shape specifically

It's deliberately built to be a **drop-in replacement for a classical convfilter**: same "patch in, scalar out" contract, so the rest of the CNN architecture doesn't need to change at all. All the quantum-specific machinery is hidden inside `e`/`q`/`d`.

## Complexity note (important, easy to miss)

- Classical conv filter over input from dataset `u`: `O(n^2)` — squarely in **P**
- `Q` (the quanvolutional transform): **#P-hard**, per Huang et al. 2018 — this hardness comes specifically from simulating `q`, the random quantum circuit; `e` and `d` are both still efficiently classical

This is the practical cost of the "richer function class" bet from [[1-design-motivations|design motivations]]: whatever expressive power you gain, you pay for in classical simulation cost if you don't have real
quantum hardware.
