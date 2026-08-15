# Dense qubit encoding

A concrete method for the **encode** step of the [[encode-classify-decode-pipeline|encode → classify → decode pipeline]] — a way to map classical data into a quantum state.

## Starting point: a qubit holds more than one number's worth of "room"

A single qubit's state can be fully described by **two real-valued parameters** — visualize it as a point on the surface of the Bloch sphere (a qubit's state as an arrow pointing somewhere on a sphere; a point on a sphere needs two angles, like latitude/longitude, to pin down). This means a single qubit can, in principle, hold **two independent classical numbers**, not just one.

## The trick: two rotations around different axes

To pack two numbers into one qubit, apply two rotations:
- A rotation around the Bloch sphere's **x-axis**, angle controlled by one input number
- A rotation around the **y-axis**, angle controlled by the other input number

Since the axes are different, the rotations don't collapse into redundancy — together they can reach any point on the sphere. So each qubit ends up encoding a *pair* of classical values $x_j = (x_{j1}, x_{j2})$.

## The formula

$$|\phi(x_j)\rangle = e^{-i\frac{x_{j2}}{2}\sigma_y} \, e^{-i\frac{x_{j1}}{2}\sigma_x} \, |0\rangle$$

Read right to left (application order):
1. Start in default state $|0\rangle$
2. Rotate around x-axis by an angle set by $x_{j1}$
3. Rotate around y-axis by an angle set by $x_{j2}$

Result: a single-qubit state that has "absorbed" both numbers into where it points on the Bloch sphere.

## Scaling up (encoding a full vector)

For an N-dimensional classical vector $x = (x_1, ..., x_N)$, since each qubit holds two values, you only need **N/2 qubits** (half as many as a one-value-per-qubit scheme). Each qubit gets a different pair from the input vector; the individual qubit states are tensored (⊗) together into the full N/2-qubit encoded state.

## Why "dense"

Roughly **2x more qubit-efficient** than a one-classical-value-per-qubit encoding — same information, half the qubits.

## Design choice: which values get paired

There's freedom in choosing *which two values* land in the same qubit. E.g., pairing $x_j$ with $x_{N/2+j}$ (opposite halves of the vector) vs. pairing neighbors $x_{2j-1}$ with $x_{2j}$ (consecutive values). Both are valid; the choice may affect how well the encoding preserves useful structure in the data — see [[encode-classify-decode-pipeline]] for why encoding choice matters for downstream classification performance.

## Where this shows up

- [[Quantum Convolutional NN for Classical Data Classification/0-about-paper|QCNN for Classical Data Classification]] — used as the encoding step (Eq. 4) before data is passed into the QCNN classifier.