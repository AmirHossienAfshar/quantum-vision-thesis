---
tags: [quantum, deutsch-algorithm]
---
# 02 Making Any Function Reversible

Previous: [[01 Reversible Functions]] | Next: [[03 The Quantum Oracle]]

## The construction
Keep the inputs and add one extra bit $C$ that receives the answer:

$$(A,B,C)\;\longrightarrow\;(A,\,B,\,C\oplus f(A,B))$$

$\oplus$ is XOR (addition mod 2). For $f=\text{AND}$ this is the **Toffoli gate**.

With $C=0$ we get $C\oplus f(A,B)=f(A,B)$, so the third output bit is the AND we wanted. The inputs $00,01,10$ now give $(0,0,0),(0,1,0),(1,0,0)$, which are all different, because $A$ and $B$ are carried along. (Setting $C=0$ is just how we *read off* $f$. The gate itself is defined for both values of $C$.)

## What is "the oracle" here?
The oracle is the **whole gate** $U_f$, and its output is the **whole triple** $(A,B,C\oplus f(A,B))$, not $f$ alone. $f$ by itself is not reversible, so it cannot be the oracle. $f$ is *hidden inside* $U_f$ in the third bit. "Calling the oracle" means applying $U_f$ to the whole register.

## Why this works for every $f$
Apply it twice:

$$(A,B,C)\to(A,B,C\oplus f(A,B))\to(A,B,C\oplus f(A,B)\oplus f(A,B))=(A,B,C)$$

Two ingredients, neither depends on what $f$ is:
1. **The inputs pass through untouched.** The second application sees the same $A,B$, so it computes the *same* $f(A,B)$.
2. **XOR cancels itself**, since $x\oplus x=0$.

Ingredient 2 only works because of ingredient 1. If the gate changed $A$ or $B$, the second $f$ could differ and the cancellation would fail.

So $U_f$ applied twice is the identity: $U_f$ is **its own inverse**, hence reversible, hence no two inputs collide.

## Recap
Classical functions lose information. Keep the inputs, XOR $f$ of them into an extra bit, and you get a reversible $U_f$ for **any** $f$.

For Deutsch's algorithm $f$ takes one bit, so the oracle is $(x,y)\mapsto(x,\,y\oplus f(x))$.

## Do we have to do this construction ourselves?
No. In Deutsch's problem the reversible oracle $U_f$ is **given to us as a ready-made box**. We never make it reversible while running the algorithm.

The construction answers a different question: *is it fair to assume such a box exists for any $f$?* Yes, because anyone with a classical circuit for $f$ can build the box by keeping the inputs and XOR-ing $f(x)$ into the extra bit. That is why the standard oracle is **defined** as $U_f|x\rangle|y\rangle=|x\rangle|y\oplus f(x)\rangle$ and not as "$x$ goes in, $f(x)$ comes out". The XOR form is a modeling choice that makes the oracle a legal quantum gate.

There is no separate "take $f$, then apply XOR" stage on our side. The XOR is already part of the box.
