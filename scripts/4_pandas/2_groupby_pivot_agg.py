"""02 — Pandas: groupby, pivot, agregações

Execute na raiz do repo:
    python scripts/03_pandas/02_groupby_pivot_agg.py
"""

from __future__ import annotations

from pathlib import Path

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

    rev_by_region = (
        sales.groupby("region", as_index=False)
        .agg(revenue_total=("revenue", "sum"), pedidos=("order_id", "nunique"))
        .sort_values("revenue_total", ascending=False)
    )

    pivot = pd.pivot_table(
        sales,
        index="region",
        columns="category",
        values="revenue",
        aggfunc="sum",
        fill_value=0,
    )

    print(rev_by_region.head())
    print("\nPivot:")
    print(pivot)


if __name__ == "__main__":
    main()
