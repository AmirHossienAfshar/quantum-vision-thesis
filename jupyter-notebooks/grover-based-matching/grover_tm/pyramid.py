"""Coarse-to-fine (image pyramid) template matching.

Why a pyramid?  At full resolution the database has one entry per window
(thousands) and each entry is a long vector (many data qubits). On a 2x2-pooled
copy of the image both numbers shrink: fewer windows (smaller index register)
and a shorter template (smaller data register). So:

  1. search ALL windows at the coarsest level (cheap, low resolution),
  2. keep the top-k candidate positions,
  3. go one level finer and search only a small neighbourhood around each
     candidate (positions 2p + d, |d| <= radius),
  4. repeat until level 0; the best window there is the answer.

Each level is one Grover run (pairs with any engine from engine.py).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from itertools import product
import numpy as np

from .database import WindowDatabase, WindowExtractor
from .encoders import AmplitudeNCCEncoder, BaseEncoder
from .engine import BaseEngine, EngineReport


class ImagePyramid:
    """Box-filter (2x2 average) pyramid of the image AND of the template."""

    def __init__(self, image: np.ndarray, template: np.ndarray, num_levels: int = 3):
        self.images = [np.asarray(image, float)]
        self.templates = [np.asarray(template, float)]
        for _ in range(num_levels - 1):
            self.images.append(self.pool2(self.images[-1]))
            self.templates.append(self.pool2(self.templates[-1]))

    @staticmethod
    def pool2(a: np.ndarray) -> np.ndarray:
        h, w = a.shape
        if h % 2 or w % 2:
            raise ValueError(f"cannot pool a {a.shape} array by 2")
        return a.reshape(h // 2, 2, w // 2, 2).mean(axis=(1, 3))

    @property
    def num_levels(self) -> int:
        return len(self.images)


@dataclass
class LevelReport:
    level: int
    db: WindowDatabase
    report: EngineReport
    candidates: list            # [(position, probability), ...] best first

    @property
    def n_qubits(self) -> int:
        return self.db.n_total_qubits


@dataclass
class PyramidResult:
    position: tuple[int, int]               # best window origin at level 0
    levels: list = field(default_factory=list)   # coarse -> fine

    @property
    def max_qubits(self) -> int:
        return max(l.n_qubits for l in self.levels)

    @property
    def total_iterations(self) -> int:
        return sum(l.report.num_iterations for l in self.levels)

    @property
    def total_windows(self) -> int:
        return sum(l.db.n_windows for l in self.levels)


class PyramidMatcher:
    def __init__(self, engine: BaseEngine, encoder_factory=None, top_k: int = 3,
                 radius: int = 2, shots: int = 4096, s2_shots: int = 2000):
        self.engine = engine
        self.encoder_factory = encoder_factory or (lambda shape: AmplitudeNCCEncoder(shape))
        self.top_k, self.radius = top_k, radius
        self.shots, self.s2_shots = shots, s2_shots

    @staticmethod
    def _expand(candidates, image_shape, template_shape, radius):
        """Candidate positions of the coarser level -> positions to search one level finer."""
        (H, W), (h, w) = image_shape, template_shape
        out = set()
        for r, c in candidates:
            for dr, dc in product(range(-radius, radius + 1), repeat=2):
                rr, cc = 2 * r + dr, 2 * c + dc
                if 0 <= rr <= H - h and 0 <= cc <= W - w:
                    out.add((rr, cc))
        return sorted(out)

    def run(self, pyramid: ImagePyramid, seed: int | None = None) -> PyramidResult:
        levels, candidates = [], None
        for level in reversed(range(pyramid.num_levels)):          # coarsest first
            img, tpl = pyramid.images[level], pyramid.templates[level]
            encoder: BaseEncoder = self.encoder_factory(tpl.shape)
            extractor = WindowExtractor(tpl.shape, stride=1)
            positions = None if candidates is None else self._expand(
                candidates, img.shape, tpl.shape, self.radius)
            db = WindowDatabase(img, extractor, encoder, positions=positions)
            rep = self.engine.search(db, tpl, self.shots, s2_shots=self.s2_shots,
                                     seed=None if seed is None else seed * 100 + level)
            probs = rep.result.index_probabilities[: db.n_windows]
            order = [i for i in np.argsort(-probs)[: (self.top_k if level > 0 else 1)] if probs[i] > 0]
            if not order:
                raise RuntimeError(f"no post-selected shots at level {level}")
            cand = [(db.position_of(int(i)), float(probs[i])) for i in order]
            candidates = [p for p, _ in cand]
            levels.append(LevelReport(level, db, rep, cand))
        return PyramidResult(position=levels[-1].candidates[0][0], levels=levels)
