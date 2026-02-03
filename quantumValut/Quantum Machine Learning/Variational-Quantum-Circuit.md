## Variational Quantum Circutes
 
 ### The Neural Network Analogy

Think of a single layer in a simple neural network. It takes an input vector, multiplies it by a **weight matrix (W)**, adds a **bias vector (b)**, and applies an activation function.

`output = activation(W * input + b)`

The "learning" process is all about adjusting the values in `W` and `b` to make the output match your goal. These weights and biases are the **trainable parameters**.

### What is a Variational Circuit?

A **variational quantum circuit** is the quantum equivalent of that neural network layer. It's a quantum circuit that has **tunable, classical parameters** built into it.

1.  **The Circuit Structure:** This is the fixed architecture of your quantum model. It's a predefined sequence of quantum gates. You design this structure upfront. It's analogous to choosing the type of layer in your neural network (e.g., a Dense layer vs. a Convolutional layer).

2.  **The Variational Parameters:** These are the classical parameters that you can change or "vary." In quantum circuits, these are almost always the **rotation angles** of specific gates. For example, a gate might rotate a qubit around the Y-axis by an angle `θ`. This `θ` is your trainable parameter.

    *   **Classical NN:** Trainable parameters are weights and biases (e.g., `W`, `b`).
    *   **Variational Circuit:** Trainable parameters are gate angles (e.g., `θ₁`, `θ₂`, ...).

3.  **The Goal (The "Cost Function"):** The circuit is part of a larger process to compute a value. In QML, this value is usually a **cost function** (or loss function). You run the circuit, measure the result, and calculate how "wrong" it is compared to the desired outcome.

---

1.  **Quantum Part:** You run the variational circuit with a given set of parameters `θ`.
2.  **Classical Part:** A classical computer takes the measurement from the circuit, calculates the cost function, and then—just like in classical machine learning—uses an optimizer (like Adam or SGD) to figure out a better set of parameters `θ'` for the next step.
3.  **Repeat:** You repeat this process, updating the parameters `θ` in each iteration, until the cost is minimized.


[read more here.](https://pennylane.ai/qml/glossary/variational_circuit)