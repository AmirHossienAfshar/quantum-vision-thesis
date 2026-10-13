"""Toy 'Where is Waldo?' scene generator (binary pixel images)."""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass
class Scene:
    image: np.ndarray
    waldo: np.ndarray
    waldo_position: tuple[int, int]
    decoys: list            # [(position, n_flipped_pixels), ...]


class SceneGenerator:
    DEFAULT_WALDO = np.array([[0, 1, 1, 0],
                              [1, 0, 0, 1],
                              [1, 0, 0, 1],
                              [0, 1, 1, 0]])

    def __init__(self, scene_shape=(8, 8), waldo: np.ndarray | None = None,
                 noise_density: float = 0.25, seed: int = 7):
        self.scene_shape = scene_shape
        self.waldo = self.DEFAULT_WALDO.copy() if waldo is None else np.asarray(waldo)
        self.noise_density = noise_density
        self.seed = seed

    def make(self, waldo_position=(4, 3), decoys=(((0, 0), 2),)) -> Scene:
        """Random binary background + one exact Waldo + optional near-miss decoys
        (Waldo copies with a few flipped pixels). Re-draws the background until
        Waldo's pattern occurs exactly once."""
        wh, ww = self.waldo.shape
        for attempt in range(200):
            rng = np.random.default_rng(self.seed + attempt)
            img = (rng.random(self.scene_shape) < self.noise_density).astype(int)
            for (r, c), flips in decoys:
                patch = self.waldo.copy().reshape(-1)
                idx = rng.choice(patch.size, size=flips, replace=False)
                patch[idx] = 1 - patch[idx]
                img[r:r + wh, c:c + ww] = patch.reshape(wh, ww)
            r, c = waldo_position
            img[r:r + wh, c:c + ww] = self.waldo
            if self._count_exact(img) == 1:
                return Scene(img, self.waldo, tuple(waldo_position), list(decoys))
        raise RuntimeError("could not generate a scene with a unique Waldo")

    def _count_exact(self, img: np.ndarray) -> int:
        wh, ww = self.waldo.shape
        H, W = img.shape
        return sum(np.array_equal(img[r:r + wh, c:c + ww], self.waldo)
                   for r in range(H - wh + 1) for c in range(W - ww + 1))


@dataclass
class TexturedScene:
    image: np.ndarray
    waldo: np.ndarray                 # clean template
    waldo_position: tuple[int, int]
    decoys: list                      # [(name, position), ...]


class TexturedSceneGenerator:
    """Harder scene: smooth random texture + Gaussian noise + look-alike decoys,
    and Waldo itself is pasted with a different brightness / contrast
    (the template stays clean). NCC is invariant to that gain/offset change."""

    def __init__(self, scene_shape=(64, 64), template_size: int = 16, noise_std: float = 0.15,
                 gain: float = 0.8, offset: float = 0.15, seed: int = 0):
        self.scene_shape, self.s = scene_shape, template_size
        self.noise_std, self.gain, self.offset, self.seed = noise_std, gain, offset, seed

    # ---- building blocks ----
    @staticmethod
    def make_waldo(s: int = 16, seed: int = 12345) -> np.ndarray:
        """Fixed random 4x4 grid of grey blocks (distinctive, and it survives pooling)."""
        blocks = np.random.default_rng(seed).random((4, 4))
        return np.kron(blocks, np.ones((s // 4, s // 4)))

    @staticmethod
    def _box_blur(img: np.ndarray, k: int) -> np.ndarray:
        pad = k // 2
        p = np.pad(img, pad, mode="reflect")
        out = np.zeros_like(img)
        for dr in range(k):
            for dc in range(k):
                out += p[dr:dr + img.shape[0], dc:dc + img.shape[1]]
        return out / k ** 2

    def _background(self, rng) -> np.ndarray:
        H, W = self.scene_shape
        coarse = rng.random((H // 8, W // 8))
        bg = np.kron(coarse, np.ones((8, 8)))
        return 0.5 * self._box_blur(bg, 7)

    def _decoy(self, kind: str, waldo: np.ndarray, rng) -> np.ndarray:
        s = self.s
        if kind == "mirrored":                         # left-right flipped Waldo
            return np.fliplr(waldo).copy()
        if kind == "half_blocks":                      # half of the 4x4 blocks replaced
            d = waldo.copy(); b = s // 4
            for k in rng.permutation(16)[:8]:
                i, j = divmod(int(k), 4)
                d[i * b:(i + 1) * b, j * b:(j + 1) * b] = rng.random()
            return d
        if kind == "corrupted":                        # 35% of the pixels replaced by random values
            d = waldo.copy(); m = rng.random(d.shape) < 0.35
            d[m] = rng.random(m.sum()); return d
        raise ValueError(kind)

    # ---- public ----
    def make(self, waldo_position=(37, 23),
             decoys=(("half_blocks", (4, 40)), ("mirrored", (40, 2)), ("corrupted", (6, 4)))) -> TexturedScene:
        rng = np.random.default_rng(self.seed)
        waldo = self.make_waldo(self.s)
        img = self._background(rng)
        for kind, (r, c) in decoys:
            img[r:r + self.s, c:c + self.s] = self._decoy(kind, waldo, rng)
        r, c = waldo_position
        img[r:r + self.s, c:c + self.s] = self.gain * waldo + self.offset
        img = img + rng.normal(0.0, self.noise_std, img.shape)
        return TexturedScene(img, waldo, tuple(waldo_position), [(k, tuple(p)) for k, p in decoys])
