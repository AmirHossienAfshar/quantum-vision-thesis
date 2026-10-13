"""Data encoders: classical patch -> unit-norm real vector of length 2**n_qubits.

An encoder only produces the *vector*. Turning that vector into a quantum
circuit is the job of a loader (see loaders.py). This split lets you swap the
encoding (NEQR, NCC-amplitude, FRQI, ...) without touching the Grover part.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
import numpy as np


class BaseEncoder(ABC):
    """Interface every encoder must follow."""

    def __init__(self, patch_shape: tuple[int, int]):
        self.patch_shape = tuple(patch_shape)
        self.n_pixels = int(np.prod(self.patch_shape))
        # qubits needed to address the pixel positions
        self.n_position_qubits = int(np.ceil(np.log2(self.n_pixels)))

    @property
    @abstractmethod
    def n_qubits(self) -> int:
        """Number of qubits of the data register (n_D in the paper)."""

    @property
    def dimension(self) -> int:
        return 2 ** self.n_qubits

    @abstractmethod
    def encode(self, patch: np.ndarray) -> np.ndarray:
        """Return a real vector of length 2**n_qubits (unit norm, or all zeros
        if the patch carries no usable information)."""

    def _check(self, patch: np.ndarray) -> np.ndarray:
        patch = np.asarray(patch)
        if patch.shape != self.patch_shape:
            raise ValueError(f"expected patch of shape {self.patch_shape}, got {patch.shape}")
        return patch.reshape(-1)


class NEQREncoder(BaseEncoder):
    """Basis encoding used in the paper's demo (NEQR).

    State: 1/sqrt(N_P) * sum_p |g_p>_C |p>_P, i.e. a colour register holding the
    intensity of every pixel, entangled with the pixel-position register.
    For binary images n_color_bits = 1 (where NEQR == FRQI, as in the paper).
    Integer layout of the data register:  j = g * N_P + p.
    Overlap of two such states = (fraction of pixels with identical colour).
    """

    def __init__(self, patch_shape: tuple[int, int], n_color_bits: int = 1):
        super().__init__(patch_shape)
        self.n_color_bits = n_color_bits

    @property
    def n_qubits(self) -> int:
        return self.n_color_bits + self.n_position_qubits

    def encode(self, patch: np.ndarray) -> np.ndarray:
        pixels = self._check(patch).astype(int)
        if pixels.min() < 0 or pixels.max() >= 2 ** self.n_color_bits:
            raise ValueError("pixel values outside [0, 2**n_color_bits - 1]")
        n_p = 2 ** self.n_position_qubits
        vec = np.zeros(self.dimension)
        colors = np.zeros(n_p, dtype=int)       # padded positions get colour 0
        colors[: self.n_pixels] = pixels
        vec[colors * n_p + np.arange(n_p)] = 1.0 / np.sqrt(n_p)
        return vec


class AmplitudeNCCEncoder(BaseEncoder):
    """Amplitude encoding of the (optionally mean-subtracted) patch.

    With zero_mean=True the overlap of two encoded patches is exactly their
    normalised cross-correlation (NCC) at zero shift. Flat patches (zero
    variance) have an undefined NCC and are encoded as the zero vector, which
    means they simply do not take part in the superposition.
    """

    def __init__(self, patch_shape: tuple[int, int], zero_mean: bool = True, eps: float = 1e-12):
        super().__init__(patch_shape)
        self.zero_mean = zero_mean
        self.eps = eps

    @property
    def n_qubits(self) -> int:
        return self.n_position_qubits

    def encode(self, patch: np.ndarray) -> np.ndarray:
        pixels = self._check(patch).astype(float)
        if self.zero_mean:
            pixels = pixels - pixels.mean()
        vec = np.zeros(self.dimension)
        vec[: self.n_pixels] = pixels           # zero padding AFTER mean removal
        norm = np.linalg.norm(vec)
        return vec / norm if norm > self.eps else np.zeros(self.dimension)
