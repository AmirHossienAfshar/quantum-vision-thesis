"""Loaders: real vector -> state-preparation circuit.

ExactStatePrepLoader uses Qiskit's generic (exponential-depth) preparation.
To reproduce the paper's AAE, add a subclass of BaseLoader whose `load` trains
a hardware-efficient ansatz and returns the trained circuit; nothing else in
the package has to change.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import StatePreparation


class BaseLoader(ABC):
    @abstractmethod
    def load(self, vector: np.ndarray) -> QuantumCircuit:
        """Return a circuit V with V|0...0> ~ vector."""


class ExactStatePrepLoader(BaseLoader):
    def load(self, vector: np.ndarray) -> QuantumCircuit:
        vector = np.asarray(vector, dtype=float)
        n = int(np.log2(len(vector)))
        if 2 ** n != len(vector):
            raise ValueError("vector length must be a power of two")
        if not np.isclose(np.linalg.norm(vector), 1.0):
            raise ValueError("vector must be normalised")
        qc = QuantumCircuit(n, name="load")
        qc.append(StatePreparation(vector), range(n))
        return qc
