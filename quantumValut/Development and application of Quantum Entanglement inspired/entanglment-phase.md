### **Entanglement Step in QEPSO (Step-by-Step)**

* Each **particle** is represented as a **Q-bit matrix** of size (D \times n),
  where:

  * rows ((D)) correspond to **dimensions / decision variables**
  * columns ((n)) correspond to **Q-bit orders** (sign, integer bits, fractional bits)

* The **entanglement step** is applied to **one particle at a time**.

* A probability $ \rho $ determines:

  * whether entanglement occurs
  * whether **dimensional entanglement** or **ordered entanglement** is selected

---

### **Dimensional Entanglement (Row-wise)**

* Randomly select two different dimensions (d_i) and (d_j)
* Copy the entire Q-bit vector of dimension (d_j) to dimension (d_i):
  $$
  x_i^k \leftarrow x_j^k \quad \forall k = 1,\dots,n
  $$
* This enforces equality between the two dimensions
* Inspired by the $|\phi_{00}\rangle$ Bell state (only identical states allowed)

---

### **Ordered Entanglement (Column-wise)**

* Randomly select two different orders $k_i$ and $k_j$
* Copy all Q-bits of order $k_j$ to order $k_i$ across all dimensions:
  $$
  x_d^{k_i} \leftarrow x_d^{k_j} \quad \forall d = 1,\dots,D
  $$
* This enforces dependency between bit positions (orders) across dimensions
* Also inspired by the $|\phi_{00}\rangle$ Bell state

---

### **Acceptance Criterion**

* Decode the modified Q-bit matrix into real-valued variables
* Evaluate the particle’s fitness
* If fitness improves:

  * keep the entangled particle
* Else:

  * discard all entanglement changes

---

### **Key Insight**

* Entanglement in QEPSO is a **structure-copying operation**, not a quantum process
* It enforces **perfect correlation** between selected dimensions or bit orders
* Helps handle **dimensional dependency** and **bit-level dependency** in optimization problems
