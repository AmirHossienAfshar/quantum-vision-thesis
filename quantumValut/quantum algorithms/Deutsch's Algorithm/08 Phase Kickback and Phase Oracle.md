---
tags: [quantum, deutsch-algorithm]
---
# 08 Phase Kickback and Phase Oracle

Previous: [[07 Eigenstates and Eigenvalues]] | Next: [[09 Putting It Together]]

## The oracle as "conditional X"
$U_f|x\rangle|y\rangle=|x\rangle|y\oplus f(x)\rangle$ can be read as:
- if $f(x)=0$: do nothing to the output qubit
- if $f(x)=1$: apply $X$ to the output qubit

The input qubit $|x\rangle$ is never changed.

## Same oracle, two different output states
Example $f(x)=x$.

**Output qubit starts in $|0\rangle$** (the bit version):
- $|1\rangle|0\rangle\to|1\rangle|1\rangle$ (flipped, answer 1 sits in the second qubit)
- $|0\rangle|0\rangle\to|0\rangle|0\rangle$

The second qubit **changes**.

**Output qubit starts in $|-\rangle$:**
- $|0\rangle|-\rangle\to|0\rangle|-\rangle$
- $|1\rangle|-\rangle\to|1\rangle X|-\rangle=-|1\rangle|-\rangle$

The second qubit **stays $|-\rangle$** in both cases. The only trace of the flip is a minus sign out front.

## General $f$ (phase kickback)
Because $|-\rangle$ is an eigenstate of $X$ with eigenvalue $-1$ ([[07 Eigenstates and Eigenvalues]]):
- $f(x)=0$: factor $+1$
- $f(x)=1$: factor $-1$

One formula for both:

$$\boxed{U_f\,|x\rangle|-\rangle=(-1)^{f(x)}\,|x\rangle|-\rangle}$$

**Phase kickback** = the gate acts on the output qubit, but since that qubit is an eigenstate, the eigenvalue it picks up lands as a **phase on the input side**. The answer $f(x)$ moves out of the output qubit and becomes a sign in front of $|x\rangle$.

## Phase oracle
The $|-\rangle$ qubit is unchanged ($|-\rangle$ before and after, always) and stays **separate** from the first qubit (a product state, no entanglement). So we drop it from the bookkeeping and describe the effect on the first qubit alone:

$$\boxed{|x\rangle\;\longrightarrow\;(-1)^{f(x)}\,|x\rangle}$$

This is the **phase oracle**. (The $|-\rangle$ qubit is still physically needed: it is what turns the flip into a sign.)

## Summary of the two terms
- **Phase kickback** = the *effect* (the value of $f$ jumps into a sign on the input qubit).
- **Phase oracle** = the *operator* that results (acts on the input qubit only, multiplying each $|x\rangle$ by $(-1)^{f(x)}$).
