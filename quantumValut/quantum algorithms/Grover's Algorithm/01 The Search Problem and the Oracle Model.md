---
tags: [quantum, grover]
---
# 01 The Search Problem and the Oracle Model

## The problem
We have a function $f$ on $n$-bit strings, so $N = 2^n$ possible inputs. It returns $1$ for the **marked** input $w$ and $0$ for everything else:

$$
f(x) = \begin{cases} 1 & x = w\\ 0 & x \neq w\end{cases}
$$

We want to find $w$. For now assume there is exactly one marked item (see [[08 Multiple Solutions and Unknown M]] for the general case).

## The oracle model
We cannot read the internals of $f$. We can only **query** it, like a black box (the *oracle*). The cost of an algorithm is the **number of queries**.

- Classically, the best strategy is to try inputs one by one: about $N/2$ queries on average, about $N$ in the worst case.
- Grover's algorithm needs about $\frac{\pi}{4}\sqrt{N}$ queries.

## Is the oracle part of the hypothesis?
Yes. The query model assumes we are handed a black box that **evaluates** $f$. The $\sqrt{N}$ vs $N$ claim is about the *query count*.

The oracle does **not** hand us $w$. It only **recognizes** a correct answer when shown one, like a password checker that accepts or rejects a guess without revealing the password. If we could read $w$ out of it, there would be nothing to search for.

This fits problems where **verifying is easy but finding is hard**: SAT, puzzles, checking a key. In practice you build the oracle from the *verification* circuit, which does not need to know $w$.

> [!example] Toy oracle
> Find $x \in \{0,\dots,7\}$ with $x^2 = 9$ ($n = 3$, $N = 8$). The oracle squares $x$, compares to $9$, and outputs $1$ on a match. Only $x = 3$ (binary $011$) passes, so $w = 011$. (This is only a format example: you could just compute $\sqrt 9$.)

> [!warning] Two honest caveats
> 1. If building the oracle required already knowing $w$, the whole thing would be circular.
> 2. The gate cost of implementing the oracle is **not** counted in the $\sqrt{N}$, so the real speedup depends on how cheap $f$ is to compute. See [[09 Limits of the Speedup]].

---
Next: [[02 The Uniform Superposition]]
