# Fully parameterized quantum circuit (PQC)

A quantum circuit whose gates have **tunable parameters** (e.g. rotation angles) that get adjusted during training — analogous to trainable weights in a classical neural network.

"Fully" parameterized means essentially the **whole circuit is trainable**, as opposed to circuits that hard-code fixed, exact operations (e.g. circuits built to exactly replicate classical arithmetic) with no learning involved.

## Contrast

- **Exact/fixed circuits** — implement a specific classical operation exactly (e.g. classical CNN arithmetic reproduced exactly on a quantum computer). No training; likely requires fault-tolerant quantum hardware.
- **Fully parameterized circuits (PQC)** — gates are learnable; the circuit is trained like a classical model, generally more suited to near-term (noisy) quantum devices.

## Where this shows up

- The QCNN architecture in [[Quantum Convolutional NN for Classical Data Classification/0-about-paper|QCNN for Classical Data Classification]] is a PQC whose layer structure is inspired by classical CNNs — see the paper note for how convolution/pooling map onto parameterized gates.
- Compare to [[Variational-Quantum-Circuit]] — PQCs are the general category; variational quantum circuits are PQCs trained via a classical optimization loop.