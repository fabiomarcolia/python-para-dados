"""03 — ML: pipeline + comparação de modelos

Execute na raiz do repo:
    python scripts/08_machine_learning/03_pipeline_comparacao_modelos.py

Saídas:
- dados/output/ml/model_pipeline_best.joblib
- dados/output/ml/scores_cv.json
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
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
    raise FileNotFoundError("Gere primeiro o rfm_features.parquet (módulo 07).")


def main() -> None:
    root = find_repo_root()
    data = root / "data"

    rfm = load_rfm(data)

    target = "is_vip"
    num_features = ["recency_days", "frequency", "monetary", "avg_order_value", "category_nunique", "region_nunique"]
    cat_features = ["segment"]

    X = rfm[num_features + cat_features].copy()
    y = rfm[target].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    preprocess = ColumnTransformer(
        transformers=[
            ("num", Pipeline([("scaler", StandardScaler())]), num_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features),
        ]
    )

    models = {
        "logreg": LogisticRegression(max_iter=400, class_weight="balanced", random_state=42),
        "rf": RandomForestClassifier(n_estimators=300, random_state=42, class_weight="balanced"),
    }

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    scores = []
    for name, clf in models.items():
        pipe = Pipeline([("prep", preprocess), ("model", clf)])
        aucs = cross_val_score(pipe, X_train, y_train, cv=cv, scoring="roc_auc")
        scores.append({"model": name, "auc_mean": float(aucs.mean()), "auc_std": float(aucs.std())})

    scores_df = pd.DataFrame(scores).sort_values("auc_mean", ascending=False)
    best_name = scores_df.iloc[0]["model"]
    best_model = models[best_name]

    final_pipe = Pipeline([("prep", preprocess), ("model", best_model)])
    final_pipe.fit(X_train, y_train)

    out_dir = data / "output" / "ml"
    out_dir.mkdir(parents=True, exist_ok=True)

    joblib.dump(final_pipe, out_dir / "model_pipeline_best.joblib")
    (out_dir / "scores_cv.json").write_text(json.dumps(scores, indent=2), encoding="utf-8")

    print("OK! Best:", best_name)
    print("Saídas em:", out_dir)


if __name__ == "__main__":
    main()
