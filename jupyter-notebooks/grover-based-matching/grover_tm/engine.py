"""Search engines: how a database + template is turned into a MatchResult.

CircuitEngine   - builds the real Qiskit circuits (matcher.py). Exact but only
                  feasible up to roughly 10-12 qubits with exact state loading.
AnalyticEngine  - uses the paper's closed form (Eq. 17) for the ideal circuit:
                      P_k(t) = P_k(0) * ( sin((2t+1)θ) / sinθ )^2,   P_k(0) = |<query|data(k)>|^2 / N
                  so large databases can be simulated instantly. It is validated
                  against CircuitEngine in the notebook.
Both return the same EngineReport, so the pyramid code does not care which is used.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
import numpy as np

from .database import WindowDatabase
from .loaders import BaseLoader
from .matcher import GroverTemplateMatcher, MatchResult, optimal_iterations_from_s2


@dataclass
class EngineReport:
    result: MatchResult          # post-selected index histogram
    num_iterations: int          # Grover iterations t used
    s2_estimate: float           # estimated initial success probability
    n_qubits: int                # n_D + n_I
    n_windows: int


class BaseEngine(ABC):
    @abstractmethod
    def search(self, db: WindowDatabase, template: np.ndarray, shots: int,
               seed: int | None = None, s2_shots: int = 2000,
               max_iterations: int = 200) -> EngineReport:
        ...


class AnalyticEngine(BaseEngine):
    def joint_probabilities(self, db: WindowDatabase, template: np.ndarray, t: int) -> np.ndarray:
        """P(data = 0..0, index = k) after t iterations, length 2**n_I."""
        q = db.encoder.encode(template)
        r = db.classical_overlaps(q)
        n_valid = np.count_nonzero(np.linalg.norm(db.data_vectors, axis=1))
        p0 = r ** 2 / n_valid
        s2 = p0.sum()
        theta = np.arcsin(np.sqrt(min(s2, 1.0)))
        factor = (np.sin((2 * t + 1) * theta) / np.sin(theta)) ** 2
        joint = np.zeros(2 ** db.n_index_qubits)
        joint[: db.n_windows] = p0 * factor
        return joint

    def search(self, db, template, shots, seed=None, s2_shots=2000, max_iterations=200):
        rng = np.random.default_rng(seed)
        s2_true = self.joint_probabilities(db, template, 0).sum()
        s2_hat = rng.binomial(s2_shots, min(s2_true, 1.0)) / s2_shots      # estimated like on hardware
        s2_hat = max(s2_hat, 1.0 / (s2_shots + 1))
        t = min(optimal_iterations_from_s2(s2_hat), max_iterations)

        joint = self.joint_probabilities(db, template, t)
        success = float(joint.sum())
        n_ps = rng.binomial(shots, min(success, 1.0))
        counts = rng.multinomial(n_ps, joint / success) if n_ps > 0 else np.zeros(len(joint), int)
        result = MatchResult(t, shots, {int(k): int(c) for k, c in enumerate(counts) if c > 0},
                             2 ** db.n_index_qubits)
        return EngineReport(result, t, float(s2_hat), db.n_total_qubits, db.n_windows)


class CircuitEngine(BaseEngine):
    def __init__(self, loader: BaseLoader | None = None, backend=None):
        self.loader, self.backend = loader, backend

    def search(self, db, template, shots, seed=None, s2_shots=2000, max_iterations=200):
        m = GroverTemplateMatcher(db, template, self.loader)
        s2_hat = max(m.initial_success_probability(s2_shots, self.backend, seed), 1.0 / (s2_shots + 1))
        t = min(optimal_iterations_from_s2(s2_hat), max_iterations)
        result = m.run(t, shots, self.backend, seed)
        return EngineReport(result, t, float(s2_hat), db.n_total_qubits, db.n_windows)
