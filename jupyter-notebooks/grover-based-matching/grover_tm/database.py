"""Sliding-window database: big image -> one entry per window position."""
from __future__ import annotations

import numpy as np
from .encoders import BaseEncoder


class WindowExtractor:
    """Cuts every (stride-spaced) window out of a 2-D image."""

    def __init__(self, window_shape: tuple[int, int], stride: int = 1):
        self.window_shape = tuple(window_shape)
        self.stride = stride

    def extract(self, image: np.ndarray):
        h, w = image.shape
        wh, ww = self.window_shape
        positions, windows = [], []
        for r in range(0, h - wh + 1, self.stride):
            for c in range(0, w - ww + 1, self.stride):
                positions.append((r, c))
                windows.append(image[r:r + wh, c:c + ww])
        return windows, positions


class WindowDatabase:
    """Holds the windows of one image and their encoded vectors.

    The database vector has the paper's structure
        |database> ~ sum_k |data(k)>_D |k>_I
    stored with integer layout  x = k * N_D + j  (data register = low qubits,
    index register = high qubits, matching Qiskit's little-endian ordering).
    Index slots k >= number of windows (padding up to a power of two) and
    windows with an all-zero encoding have amplitude 0.
    """

    def __init__(self, image: np.ndarray, extractor: WindowExtractor, encoder: BaseEncoder,
                 positions: list[tuple[int, int]] | None = None):
        """If `positions` is given, only those window origins (row, col) are loaded
        (used by the pyramid to search just the neighbourhood of coarse candidates)."""
        self.image = np.asarray(image)
        self.extractor = extractor
        self.encoder = encoder
        if positions is None:
            self.windows, self.positions = extractor.extract(self.image)
        else:
            wh, ww = extractor.window_shape
            self.positions = [tuple(p) for p in positions]
            self.windows = [self.image[r:r + wh, c:c + ww] for r, c in self.positions]
        self.n_windows = len(self.windows)
        self.n_index_qubits = max(1, int(np.ceil(np.log2(self.n_windows))))
        self.data_vectors = np.array([encoder.encode(w) for w in self.windows])
        self.vector = self._build_vector()

    @property
    def n_data_qubits(self) -> int:
        return self.encoder.n_qubits

    @property
    def n_total_qubits(self) -> int:
        return self.n_data_qubits + self.n_index_qubits

    def _build_vector(self) -> np.ndarray:
        n_d, n_i = self.encoder.dimension, 2 ** self.n_index_qubits
        vec = np.zeros(n_i * n_d)
        for k, d in enumerate(self.data_vectors):
            vec[k * n_d:(k + 1) * n_d] = d
        norm = np.linalg.norm(vec)
        if norm == 0:
            raise ValueError("every window encodes to the zero vector")
        return vec / norm

    def classical_overlaps(self, query_vector: np.ndarray) -> np.ndarray:
        """<query|data(k)> for every window (classical reference)."""
        return self.data_vectors @ query_vector

    def position_of(self, index: int) -> tuple[int, int]:
        return self.positions[index]
