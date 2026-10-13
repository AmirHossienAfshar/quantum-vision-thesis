"""Grover template matcher (paper: Tezuka et al., arXiv:2108.10854, Sec. II).

Pipeline
--------
  U   = (B^dagger on data register) . A          -> |Psi> = U|0>
  G_o = 1 - 2 |0..0><0..0|_data (x) 1_index       (no knowledge of the answer!)
  G_d = U (2|0><0| - 1) U^dagger                  (reflection about |Psi>)
  G   = G_d G_o,   |Psi_t> = G^t |Psi>
Read-out: measure all qubits, keep shots whose data register is all zeros,
histogram the index register.

Qubit layout: data register = qubits 0..n_D-1, index register = qubits n_D..n-1,
so a basis state has integer x = k * N_D + j  (k = index, j = data).
"""
from __future__ import annotations

from dataclasses import dataclass, field
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

from .database import WindowDatabase
from .loaders import BaseLoader, ExactStatePrepLoader


def optimal_iterations_from_s2(s2: float) -> int:
    """t* = round( arccos(s) / (2 arcsin(s)) ), s = sqrt(s2)   (paper Eq. 18)."""
    s = np.sqrt(min(max(float(s2), 1e-12), 1.0))
    return max(0, int(round(np.arccos(s) / (2 * np.arcsin(s)))))


@dataclass
class MatchResult:
    """Outcome of one sampled run."""
    num_iterations: int
    shots: int
    index_counts: dict = field(default_factory=dict)   # k -> count (post-selected)
    n_index_slots: int = 0

    @property
    def post_selected(self) -> int:
        return sum(self.index_counts.values())

    @property
    def success_rate(self) -> float:
        return self.post_selected / self.shots

    @property
    def index_probabilities(self) -> np.ndarray:
        """Histogram over index k, normalised over post-selected shots."""
        p = np.zeros(self.n_index_slots)
        for k, c in self.index_counts.items():
            p[k] = c
        return p / p.sum() if p.sum() > 0 else p

    @property
    def best_index(self) -> int:
        return int(np.argmax(self.index_probabilities))


class GroverTemplateMatcher:
    def __init__(self, database: WindowDatabase, template: np.ndarray,
                 loader: BaseLoader | None = None):
        self.db = database
        self.loader = loader or ExactStatePrepLoader()
        self.query_vector = database.encoder.encode(template)
        if not np.any(self.query_vector):
            raise ValueError("template encodes to the zero vector (flat template?)")

        self.n_d = database.n_data_qubits
        self.n_i = database.n_index_qubits
        self.n = self.n_d + self.n_i
        self.data_qubits = list(range(self.n_d))

        self.A = self.loader.load(database.vector)        # database operator
        self.B = self.loader.load(self.query_vector)      # query operator
        self.U = self._build_U()
        self.G = self._build_grover_operator()

    # ---------- circuit construction ----------
    @staticmethod
    def _flip_all_zero(num_qubits: int) -> QuantumCircuit:
        """1 - 2|0..0><0..0| on `num_qubits` qubits (sign flip of the all-zero state)."""
        qc = QuantumCircuit(num_qubits)
        qc.x(range(num_qubits))
        if num_qubits == 1:
            qc.z(0)
        else:
            qc.h(num_qubits - 1)
            qc.mcx(list(range(num_qubits - 1)), num_qubits - 1)
            qc.h(num_qubits - 1)
        qc.x(range(num_qubits))
        return qc

    def _build_U(self) -> QuantumCircuit:
        qc = QuantumCircuit(self.n, name="U")
        qc.compose(self.A, qubits=range(self.n), inplace=True)
        qc.compose(self.B.inverse(), qubits=self.data_qubits, inplace=True)
        return qc

    def oracle(self) -> QuantumCircuit:
        qc = QuantumCircuit(self.n, name="G_o")
        qc.compose(self._flip_all_zero(self.n_d), qubits=self.data_qubits, inplace=True)
        return qc

    def diffusion(self) -> QuantumCircuit:
        qc = QuantumCircuit(self.n, name="G_d")
        qc.compose(self.U.inverse(), inplace=True)
        qc.compose(self._flip_all_zero(self.n), inplace=True)
        qc.compose(self.U, inplace=True)
        qc.global_phase += np.pi          # 2|0><0| - 1 = -(1 - 2|0><0|)
        return qc

    def _build_grover_operator(self) -> QuantumCircuit:
        qc = QuantumCircuit(self.n, name="G")
        qc.compose(self.oracle(), inplace=True)
        qc.compose(self.diffusion(), inplace=True)
        return qc

    def build_circuit(self, num_iterations: int, measure: bool = False) -> QuantumCircuit:
        qc = self.U.copy()
        for _ in range(num_iterations):
            qc.compose(self.G, inplace=True)
        if measure:
            qc.measure_all()
        return qc

    # ---------- exact (noise-free, shot-free) analysis ----------
    def _joint_from_state(self, psi: Statevector) -> np.ndarray:
        """P(data = 0..0, index = k) for every k."""
        amp = psi.data.reshape(2 ** self.n_i, 2 ** self.n_d)
        return np.abs(amp[:, 0]) ** 2

    def exact_joint(self, num_iterations: int) -> np.ndarray:
        psi = Statevector(self.U)
        for _ in range(num_iterations):
            psi = psi.evolve(self.G)
        return self._joint_from_state(psi)

    def exact_scan(self, max_iterations: int) -> np.ndarray:
        """Matrix [t, k] of P(data=0, index=k) for t = 0..max_iterations."""
        psi = Statevector(self.U)
        rows = [self._joint_from_state(psi)]
        for _ in range(max_iterations):
            psi = psi.evolve(self.G)
            rows.append(self._joint_from_state(psi))
        return np.array(rows)

    def initial_success_probability(self, shots: int | None = None,
                                    backend=None, seed: int | None = None) -> float:
        """s^2 = P(data register reads 0..0) at t = 0 (exact, or estimated from shots)."""
        if shots is None:
            return float(self.exact_joint(0).sum())
        return self.run(0, shots, backend, seed).success_rate

    def optimal_iterations(self, s2: float | None = None) -> int:
        """t* = round( arccos(s) / (2 arcsin(s)) )   (paper Eq. 18)."""
        s2 = self.initial_success_probability() if s2 is None else s2
        return optimal_iterations_from_s2(s2)

    # ---------- sampled execution ----------
    def run(self, num_iterations: int, shots: int = 4096, backend=None,
            seed: int | None = None) -> MatchResult:
        qc = self.build_circuit(num_iterations, measure=True)
        if backend is None:
            # Aer cannot execute Qiskit's high-level state-preparation blocks directly,
            # so compile explicitly down to {u, cx}.
            backend = AerSimulator()
            tqc = transpile(qc, basis_gates=["u", "cx", "measure"],
                            optimization_level=1, seed_transpiler=seed)
        else:
            tqc = transpile(qc, backend, optimization_level=1, seed_transpiler=seed)
        counts = backend.run(tqc, shots=shots, seed_simulator=seed).result().get_counts()
        n_d_mask = 2 ** self.n_d - 1
        index_counts: dict[int, int] = {}
        for key, c in counts.items():
            x = int(key.replace(" ", ""), 2)
            if x & n_d_mask == 0:                       # post-selection on data = 0..0
                k = x >> self.n_d
                index_counts[k] = index_counts.get(k, 0) + c
        return MatchResult(num_iterations, shots, index_counts, 2 ** self.n_i)

    # ---------- resources ----------
    def resource_summary(self, num_iterations: int) -> dict:
        """Depth / gate counts after compiling to {u, cx}."""
        qc = transpile(self.build_circuit(num_iterations), basis_gates=["u", "cx"],
                       optimization_level=1, seed_transpiler=0)
        ops = qc.count_ops()
        return {"qubits": self.n, "depth": qc.depth(), "cx": ops.get("cx", 0),
                "single_qubit": ops.get("u", 0)}
