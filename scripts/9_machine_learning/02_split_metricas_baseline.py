"""02 — ML: split, métricas e baseline (VIP)

Execute na raiz do repo:
    python scripts/08_machine_learning/02_split_metricas_baseline.py

Saídas:
- dados/output/ml/model_baseline.joblib
- dados/output/ml/metrics_baseline.json
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import joblib


def find_repo_root(start: Path | None = None) -> Path:
    cur = (start or Path.cwd()).resolve()
    for _ in range(10):
        if (cur / "README.md").exists() and (cur / "data").exists():
            return cur
        cur = cur.parent
    return Path.cwd().resolve()


def load_rfm(data_dir: Path) -> pd.DataFrame:
    path = data_dir / "processed" / "rfm_features.parquet"
    if path.exists():
        return pd.read_parquet(path)

    # fallback: build from sample
    sales = pd.read_csv(data_dir / "sample" / "sales.csv")
    customers = pd.read_csv(data_dir / "sample" / "customers.csv")
    sales["date"] = pd.to_datetime(sales["date"])
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
          )
          .reset_index()
    )
    rfm["recency_days"] = (as_of - rfm["last_purchase"]).dt.days
    thr = rfm["monetary"].quantile(0.80)
    rfm["is_vip"] = (rfm["monetary"] >= thr).astype(int)

    out_dir = data_dir / "processed"
    out_dir.mkdir(parents=True, exist_ok=True)
    rfm.to_parquet(out_dir / "rfm_features.parquet", index=False)
    return rfm


def main() -> None:
    root = find_repo_root()
    data = root / "data"

    rfm = load_rfm(data)

    target = "is_vip"
    features = ["recency_days", "frequency", "monetary", "avg_order_value", "category_nunique", "region_nunique"]

    X = rfm[features]
    y = rfm[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=200, class_weight="balanced", random_state=42),
    )
    model.fit(X_train, y_train)

    proba = model.predict_proba(X_test)[:, 1]
    auc = float(roc_auc_score(y_test, proba))

    out_dir = data / "output" / "ml"
    out_dir.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, out_dir / "model_baseline.joblib")
    (out_dir / "metrics_baseline.json").write_text(json.dumps({"roc_auc": auc}, indent=2), encoding="utf-8")

    print("OK! ROC AUC:", round(auc, 4))
    print("Saídas em:", out_dir)


if __name__ == "__main__":
    main()
