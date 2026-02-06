"""04 — ML: tuning + interpretabilidade (Permutation Importance)

Execute na raiz do repo:
    python scripts/08_machine_learning/04_tuning_interpretabilidade.py

Saídas:
- dados/output/ml/model_rf_tuned.joblib
- dados/output/ml/tuning_rf.json
- dados/output/ml/feature_importance_permutation.csv
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.inspection import permutation_importance
import joblib


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

    rfm_path = data / "processed" / "rfm_features.parquet"
    if not rfm_path.exists():
        raise FileNotFoundError("Gere primeiro o rfm_features.parquet (módulo 07).")

    rfm = pd.read_parquet(rfm_path)

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

    pipe = Pipeline([
        ("prep", preprocess),
        ("model", RandomForestClassifier(random_state=42, class_weight="balanced")),
    ])

    param_grid = {
        "model__n_estimators": [200, 500],
        "model__max_depth": [None, 8, 12],
        "model__min_samples_leaf": [1, 3, 5],
    }

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    gs = GridSearchCV(pipe, param_grid=param_grid, scoring="roc_auc", cv=cv, n_jobs=-1, refit=True)
    gs.fit(X_train, y_train)

    best = gs.best_estimator_
    proba = best.predict_proba(X_test)[:, 1]
    test_auc = float(roc_auc_score(y_test, proba))

    perm = permutation_importance(best, X_test, y_test, n_repeats=20, random_state=42, scoring="roc_auc")
    imp = pd.DataFrame({
        "feature": X_test.columns,
        "importance_mean": perm.importances_mean,
        "importance_std": perm.importances_std,
    }).sort_values("importance_mean", ascending=False)

    out_dir = data / "output" / "ml"
    out_dir.mkdir(parents=True, exist_ok=True)

    joblib.dump(best, out_dir / "model_rf_tuned.joblib")
    (out_dir / "feature_importance_permutation.csv").write_text(imp.to_csv(index=False), encoding="utf-8")

    payload = {
        "best_score_cv_auc": float(gs.best_score_),
        "best_params": gs.best_params_,
        "test_auc": test_auc,
    }
    (out_dir / "tuning_rf.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print("OK! Test AUC:", round(test_auc, 4))
    print("Saídas em:", out_dir)


if __name__ == "__main__":
    main()
