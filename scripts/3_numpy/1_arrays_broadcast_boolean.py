"""01 — Numpy: arrays, broadcasting e boolean indexing

Execute na raiz do repo:
    python scripts/02_numpy/01_arrays_broadcast_boolean.py
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
    qty = sales["qty"].to_numpy()
    unit_price = sales["unit_price"].to_numpy()

    discount = 0.10
    revenue_discounted = qty * unit_price * (1 - discount)

    mask = revenue > 300
    high_revenue = revenue[mask]

    stats = {
        "count": int(revenue.size),
        "sum": float(revenue.sum()),
        "mean": float(revenue.mean()),
        "median": float(np.median(revenue)),
        "p90": float(np.percentile(revenue, 90)),
    }

    print("high_revenue_count:", int(high_revenue.size))
    print("stats:", stats)


if __name__ == "__main__":
    main()
