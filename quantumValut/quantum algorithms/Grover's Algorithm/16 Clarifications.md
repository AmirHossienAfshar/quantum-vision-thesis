---
tags: [quantum, grover, faq]
---
# 16 Clarifications

Questions that came up while learning this, with short answers and pointers.

## Notation and setup

**Is the input $\lvert000\ldots0\rangle$ a bra or a ket?**
A **ket** (a state, column vector). The bra $\langle000\ldots0\rvert$ is its conjugate transpose. See [[02 The Uniform Superposition]].

**Is the sum $\sum_x$ just over $x=0$ and $x=1$?**
No. It runs over **all $N=2^n$ bit strings**. $x$ is the label, $\lvert x\rangle$ the basis ket. It equals $\{0,1\}$ only when $n=1$. See [[02 The Uniform Superposition]].

**Is it $\sqrt n$ or $\sqrt N$ in $1/\sqrt N$?**
Capital $N=2^n$, the number of states. Lowercase $n$ is the qubit count.

## The oracle

**Is the oracle's existence part of the hypothesis?**
Yes. Grover's algorithm lives in the **query model**: we are handed a black box that evaluates $f$ and we count calls. See [[01 The Search Problem and the Oracle Model]].

**Does the oracle "know $w$" and return it?**
It *recognizes* $w$ (it computes $f$, which is $1$ only at $w$), but we cannot read $w$ out of it. If we could, there would be nothing to search for.

**What does the oracle return when given $\lvert s\rangle$?**
The entire state with the same amplitudes, except $w$'s sign flipped. All $N$ basis states are still present; nothing has been "found". See [[03 The Oracle as a Phase Flip]].

## The diffusion and the "mean"

**Which mean?**
The plain average of the $N$ amplitudes, $\mu=\frac1N\sum_x\alpha_x$. The overlap $\langle s\vert\psi\rangle=\sqrt N\,\mu$, so $D=2\lvert s\rangle\langle s\rvert-I$ sends $\alpha_x\to2\mu-\alpha_x$. See [[04 The Diffusion Operator]].

**Does one round always land exactly on $w$?**
No. That is a coincidence of $N=4$. For larger $N$ each round rotates by only $2\theta$, so we repeat about $\frac\pi4\sqrt N$ times. See [[07 How Many Rounds]].

## The geometric picture

**Where does $\lvert s\rangle=\sin\theta\lvert w\rangle+\cos\theta\lvert w^\perp\rangle$ come from, and why $\sin\theta=1/\sqrt N$?**
It is just $\lvert s\rangle$'s sum split into the $x=w$ term and the rest. $\theta$ is *defined* as the angle whose sine is the coefficient on $\lvert w\rangle$; this works because the two coefficients' squares sum to $1$. See [[05 The Two-Dimensional Plane]].

**Why bother with $\theta$ at all?**
It reduces the whole $N$-amplitude state to **one angle** $\varphi$, with $P(w)=\sin^2\varphi$ and a simple rule: each round adds $2\theta$. That gives a closed formula for any round and for the best number of rounds.

**Is the horizontal axis "all the orthogonal states"?**
No: it is one specific vector, the uniform mix of all unmarked states. The state never leaves the plane spanned by it and $\lvert w\rangle$.

**Is $\lvert s\rangle$ the thing that moves toward $\lvert w\rangle$?**
$\lvert s\rangle$ is the fixed starting vector. After $k$ rounds the state is $G^k\lvert s\rangle$, further along the circle.

**Why did you apply $D$ to $\lvert s\rangle$ and $\lvert s^\perp\rangle$ in the derivation if $O$ happens first?**
Those were **test vectors** used to discover what kind of operator $D$ is (a reflection across the $\lvert s\rangle$ line). The real input to $D$ is $O\lvert s\rangle$. Probe first, then apply to the real input. See [[06 Two Reflections Make a Rotation]].

**Does $D$ simply lower the horizontal part?**
Not directly. $D$ flips the part perpendicular to the $\lvert s\rangle$ line. The oracle first creates that perpendicular part. The horizontal part shrinking is a consequence. See [[06 Two Reflections Make a Rotation]].

## Gates

**Is CCNOT an "8-bit" gate?**
No. It is a **3-qubit** gate; the $8\times8$ matrix is because $2^3=8$ basis states. See [[11 CNOT and Toffoli Gates]].

**Are big gates really stacks of smaller ones?**
Yes, like classical logic. Hardware offers a small native universal set (single-qubit gates plus CNOT or similar) and a compiler lowers Toffoli, $C^nX$, CCZ and so on into it. See [[11 CNOT and Toffoli Gates]].

---
Previous: [[15 Exercises and Quick Answers]] · Back to [[00 Grover Index]]
