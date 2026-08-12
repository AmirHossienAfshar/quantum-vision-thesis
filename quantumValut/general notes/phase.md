
# Relative Phase and the Bloch Sphere Representation of a Qubit

## 1. General form of a qubit state

A pure single-qubit quantum state is written as
$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle,
\quad \alpha,\beta \in \mathbb{C},
\quad |\alpha|^2 + |\beta|^2 = 1.
$$

The quantities (|\alpha|^2) and (|\beta|^2) represent measurement probabilities in the computational basis.

---

## 2. Insufficiency of probabilities alone

Different quantum states may share the same measurement probabilities while remaining physically distinct. For example,
$$
\frac{|0\rangle + |1\rangle}{\sqrt{2}},
\quad
\frac{|0\rangle - |1\rangle}{\sqrt{2}},
\quad
\frac{|0\rangle + i|1\rangle}{\sqrt{2}}
$$
all yield identical probabilities in the computational basis, yet they behave differently under quantum operations and measurements in other bases.

This demonstrates that **probabilities alone do not fully characterize a quantum state**.

---

## 3. Global phase vs relative phase

### Global phase

Two states differing only by an overall complex phase,
$$
|\psi\rangle \sim e^{i\gamma}|\psi\rangle,
$$
are physically indistinguishable. The global phase (e^{i\gamma}) has no observable effect.

---

### Relative phase

A phase difference between amplitudes,
$$
|\psi\rangle = \alpha |0\rangle + e^{i\theta}\beta |1\rangle,
$$
is physically meaningful. The parameter (\theta) is called the **relative phase**.

---

## 4. Why the relative phase must be (e^{i\theta})

The factor relating quantum amplitudes must satisfy two conditions:

1. **Probability preservation**
   $$
   |e^{i\theta}\beta|^2 = |\beta|^2,
   $$
   which requires (|e^{i\theta}| = 1).

2. **Linearity of quantum mechanics**, which requires complex numbers.

The only numbers satisfying both conditions are **unit-modulus complex phases**:
$$
e^{i\theta}.
$$

Thus, relative phases necessarily appear in the form (e^{i\theta}).

---

## 5. Bloch sphere parametrization

Any pure qubit state can be written as
$$
|\psi\rangle =
\cos\frac{\theta}{2},|0\rangle
+
e^{i\phi}\sin\frac{\theta}{2},|1\rangle,
\quad
0 \le \theta \le \pi,;
0 \le \phi < 2\pi.
$$

---

## 6. Interpretation of Bloch sphere angles

### Polar angle (\theta)

* Determines measurement probabilities:
  $$
  P(1) = \sin^2\frac{\theta}{2},
  \quad
  P(0) = \cos^2\frac{\theta}{2}.
  $$
* Corresponds to latitude on the Bloch sphere.

---

### Azimuthal angle (\phi)

* Represents the **relative phase** between basis states.
* Corresponds to longitude (rotation about the (Z)-axis).
* Does not affect probabilities in the computational basis, but affects interference and outcomes in other measurement bases.

---

## 7. Interference and the role of phase

When quantum amplitudes combine, measurement probabilities depend on the relative phase:
$$
|\alpha + e^{i\phi}\beta|^2
|\alpha|^2 + |\beta|^2 + 2|\alpha||\beta|\cos\phi.
$$

The final term is an **interference term**, controlled entirely by the relative phase (\phi). This effect has no analogue in classical probability theory.

---

## 8. Conceptual significance

* Probabilities describe **outcomes**.
* Relative phase describes **relationships between alternatives**.
* The geometry of the Bloch sphere captures both aspects simultaneously.
* The necessity of complex phases reflects the fundamentally non-classical structure of quantum theory.

---

## 9. Key takeaway

> A single-qubit quantum state is fully specified by both its measurement probabilities and a physically meaningful relative phase, which appears necessarily as a unit complex factor (e^{i\theta}). On the Bloch sphere, probabilities are encoded by the polar angle, while relative phase is encoded by the azimuthal angle.

---
