

> Multi-qubit gates can be made from simpler single-qubit gates using tensor products.  
> And the combined gate performs the predictable job:  
> **each qubit gets the gate that was tensored for it.**


---

# **Example to confirm**

Suppose you build:

$$
A \otimes B.  
$$

This is a **2-qubit gate** whose job is:

- Apply **A** to the **first** qubit
    
- Apply **B** to the **second** qubit
    

This is predictable and guaranteed.

Example:

$$
I \otimes X  
$$

- first qubit unchanged
    
- second qubit flipped
    

And you saw that clearly in examples like:

$$
(I\otimes X)|10\rangle = |11\rangle.  
$$

---

# **This generalizes to any number of qubits**

For 3 qubits:

$$
H \otimes I \otimes Z  
$$

means:

- qubit 1 → apply Hadamard
    
- qubit 2 → do nothing
    
- qubit 3 → apply Z
    

For n qubits:

$$
G_1 \otimes G_2 \otimes \cdots \otimes G_n  
$$

means each qubit gets its own gate independently.

---

# But keep in mind

Only **independent** multi-qubit gates are tensor products.

If a gate creates correlations or entanglement (CNOT, CZ, SWAP, Toffoli…), then it **cannot** be written as a simple tensor product — but it _can_ be built using tensor products _and_ outer products.

---
