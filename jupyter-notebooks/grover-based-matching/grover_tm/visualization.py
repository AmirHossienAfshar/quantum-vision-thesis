"""Plotting helpers (matplotlib only)."""
from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from .database import WindowDatabase


class MatchVisualizer:
    @staticmethod
    def show_scene(scene, ax=None, title="Scene (red box = Waldo)"):
        ax = ax or plt.gca()
        ax.imshow(scene.image, cmap="gray_r", vmin=0, vmax=1)
        r, c = scene.waldo_position
        wh, ww = scene.waldo.shape
        ax.add_patch(Rectangle((c - .5, r - .5), ww, wh, fill=False, ec="red", lw=2))
        for (dr, dc), _ in scene.decoys:
            ax.add_patch(Rectangle((dc - .5, dr - .5), ww, wh, fill=False, ec="orange", lw=1.5, ls="--"))
        ax.set_title(title); ax.set_xticks([]); ax.set_yticks([])

    @staticmethod
    def show_template(waldo, ax=None, title="Template"):
        ax = ax or plt.gca()
        ax.imshow(waldo, cmap="gray_r", vmin=0, vmax=1)
        ax.set_title(title); ax.set_xticks([]); ax.set_yticks([])

    @staticmethod
    def index_histogram(db: WindowDatabase, probs, ax=None, highlight=None, title=""):
        ax = ax or plt.gca()
        k = np.arange(db.n_windows)
        colors = ["tab:red" if i == highlight else "tab:blue" for i in k]
        ax.bar(k, np.asarray(probs)[: db.n_windows], color=colors)
        ax.set_xticks(k)
        ax.set_xticklabels([f"{db.position_of(i)}" for i in k], rotation=90, fontsize=7)
        ax.set_xlabel("window position (row, col)"); ax.set_ylabel("probability")
        ax.set_title(title)

    @staticmethod
    def position_heatmap(db: WindowDatabase, probs, ax=None, title="", mark=None):
        ax = ax or plt.gca()
        rows = sorted({p[0] for p in db.positions}); cols = sorted({p[1] for p in db.positions})
        grid = np.full((len(rows), len(cols)), np.nan)
        for k, (r, c) in enumerate(db.positions):
            grid[rows.index(r), cols.index(c)] = probs[k]
        im = ax.imshow(grid, cmap="viridis")
        if mark is not None:
            ax.plot(cols.index(mark[1]), rows.index(mark[0]), "r*", ms=14)
        ax.set_xticks(range(len(cols))); ax.set_xticklabels(cols)
        ax.set_yticks(range(len(rows))); ax.set_yticklabels(rows)
        ax.set_xlabel("window col"); ax.set_ylabel("window row"); ax.set_title(title)
        plt.colorbar(im, ax=ax, fraction=0.046)

    @staticmethod
    def iteration_scan(scan: np.ndarray, target_index: int, ax=None, title=""):
        """scan[t, k] = P(data=0, index=k). Plots success prob and target prob vs t."""
        ax = ax or plt.gca()
        t = np.arange(scan.shape[0])
        ax.plot(t, scan.sum(axis=1), "o-", label="total success  P(data=0)")
        ax.plot(t, scan[:, target_index], "s-", color="tab:red", label="target window (joint)")
        ax.set_xlabel("Grover iterations t"); ax.set_ylabel("probability")
        ax.set_title(title); ax.legend()


class PyramidVisualizer:
    @staticmethod
    def show_pyramid(pyramid, axes):
        for l, ax in enumerate(axes):
            ax.imshow(pyramid.images[l], cmap="gray"); ax.set_xticks([]); ax.set_yticks([])
            ax.set_title(f"level {l}: image {pyramid.images[l].shape}, template {pyramid.templates[l].shape}", fontsize=8)

    @staticmethod
    def show_level(level_report, image, template_shape, true_pos=None, ax=None):
        """Searched windows as dots (size ~ probability), chosen candidates boxed."""
        ax = ax or plt.gca()
        db = level_report.db
        ax.imshow(image, cmap="gray"); ax.set_xticks([]); ax.set_yticks([])
        h, w = template_shape
        probs = level_report.report.result.index_probabilities[: db.n_windows]
        pos = np.array(db.positions)
        ax.scatter(pos[:, 1] + w / 2, pos[:, 0] + h / 2, s=2 + 600 * probs / max(probs.max(), 1e-9),
                   c=probs, cmap="autumn_r", alpha=.7)
        for (r, c), _ in level_report.candidates:
            ax.add_patch(Rectangle((c - .5, r - .5), w, h, fill=False, ec="cyan", lw=1.5))
        if true_pos is not None:
            ax.add_patch(Rectangle((true_pos[1] - .5, true_pos[0] - .5), w, h, fill=False, ec="lime", lw=1.5, ls="--"))
        ax.set_title(f"level {level_report.level}: {db.n_windows} windows, {level_report.n_qubits} qubits, "
                     f"t={level_report.report.num_iterations}", fontsize=8)
