"""01 — Polars: expressões + Lazy

Execute na raiz do repo:
    python scripts/05_polars/01_polars_expressions_lazy.py
"""

from __future__ import annotations

from pathlib import Path

import polars as pl


def find_repo_root(start: Path | None = None) -> Path:
    cur = (start or Path.cwd()).resolve()
    for _ in range(10):
        if (cur / "README.md").exists() and (cur / "data").exists():
            return cur
        cur = cur.parent
    return Path.cwd().resolve()


def main() -> None:
    root = find_repo_root()
    sample = root / "data" / "sample" / "sales.csv"

    sales_pl = pl.read_csv(sample).with_columns((pl.col("qty") * pl.col("unit_price")).alias("revenue_calc"))

    by_region = (
        sales_pl.group_by("region")
        .agg(
            [
                pl.col("revenue_calc").sum().alias("revenue_total"),
                pl.col("order_id").n_unique().alias("pedidos"),
            ]
        )
        .sort("revenue_total", descending=True)
    )

    print(by_region)

    lazy = pl.scan_csv(sample)
    result = (
        lazy.with_columns((pl.col("qty") * pl.col("unit_price")).alias("revenue_calc"))
        .group_by(["region", "category"])
        .agg(pl.col("revenue_calc").sum().alias("revenue_total"))
        .sort("revenue_total", descending=True)
        .collect()
    )

    print(result.head(10))


if __name__ == "__main__":
    main()
