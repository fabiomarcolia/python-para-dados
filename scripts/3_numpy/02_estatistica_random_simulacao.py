"""02 — Numpy: estatística + simulação (random)

Execute na raiz do repo:
    python scripts/02_numpy/02_estatistica_random_simulacao.py
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


def find_repo_root(start: Path | None = None) -> Path:
    cur = (start or Path.cwd()).resolve()
    for _ in range(10):
        if (cur / "README.md").exists() and (cur / "data").exists():
            return cur
        cur = cur.parent
    return Path.cwd().resolve()


def main() -> None:
    root = find_repo_root()
    sales = pd.read_csv(root / "data" / "sample" / "sales.csv")

    revenue = sales["revenue"].to_numpy()

    rng = np.random.default_rng(42)
    sim = rng.choice(revenue, size=(1000, 1000), replace=True)
    totals = sim.sum(axis=1)

    print("mean_total:", float(totals.mean()))
    print("p05/p50/p95:", [float(x) for x in np.percentile(totals, [5, 50, 95])])


if __name__ == "__main__":
    main()
