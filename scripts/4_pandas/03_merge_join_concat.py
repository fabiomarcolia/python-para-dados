"""03 — Pandas: merge/join/concat

Execute na raiz do repo:
    python scripts/03_pandas/03_merge_join_concat.py
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
    customers = pd.read_csv(root / "data" / "sample" / "customers.csv")

    df = sales.merge(customers, on="customer_id", how="left")
    missing_segment = int(df["segment"].isna().sum())

    df1 = sales.copy()
    df1["periodo"] = "P1"
    df2 = sales.sample(frac=0.2, random_state=42).copy()
    df2["periodo"] = "P2"
    stacked = pd.concat([df1, df2], ignore_index=True)

    print("missing_segment:", missing_segment)
    print("period counts:")
    print(stacked["periodo"].value_counts())


if __name__ == "__main__":
    main()
