"""03 — Feature Engineering: RFM + Parquet

Execute na raiz do repo:
    python scripts/07_eda_avancado/03_feature_engineering_rfm_parquet.py

Saídas:
- dados/processed/rfm_features.parquet
- dados/processed/rfm_features.csv
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
    data = root / "data"

    sales = pd.read_csv(data / "sample" / "sales.csv")
    customers = pd.read_csv(data / "sample" / "customers.csv")
    sales["date"] = pd.to_datetime(sales["date"])
    customers["signup_date"] = pd.to_datetime(customers["signup_date"])

    df = sales.merge(customers, on="customer_id", how="left")
    as_of = df["date"].max() + pd.Timedelta(days=1)

    rfm = (
        df.groupby("customer_id")
          .agg(
              last_purchase=("date", "max"),
              frequency=("order_id", "nunique"),
              monetary=("revenue", "sum"),
              avg_order_value=("revenue", "mean"),
              category_nunique=("category", "nunique"),
              region_nunique=("region", "nunique"),
              segment=("segment", "first"),
              signup_date=("signup_date", "first"),
          )
          .reset_index()
    )
    rfm["recency_days"] = (as_of - rfm["last_purchase"]).dt.days

    thr = rfm["monetary"].quantile(0.80)
    rfm["is_vip"] = (rfm["monetary"] >= thr).astype(int)

    out_dir = data / "processed"
    out_dir.mkdir(parents=True, exist_ok=True)

    rfm.to_parquet(out_dir / "rfm_features.parquet", index=False)
    rfm.to_csv(out_dir / "rfm_features.csv", index=False)

    print("OK! Features salvas em:", out_dir)


if __name__ == "__main__":
    main()
