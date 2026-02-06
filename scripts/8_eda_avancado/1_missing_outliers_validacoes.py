"""01 — EDA avançado: missingness, outliers e validações

Execute na raiz do repo:
    python scripts/07_eda_avancado/01_missing_outliers_validacoes.py
"""

from __future__ import annotations

import json
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
    df = pd.read_csv(root / "data" / "sample" / "sales.csv")
    df["date"] = pd.to_datetime(df["date"])

    report = {
        "rows": int(len(df)),
        "duplicated_order_id": int(df.duplicated("order_id").sum()),
        "revenue_le_zero": int((df["revenue"] <= 0).sum()),
        "unit_price_le_zero": int((df["unit_price"] <= 0).sum()),
    }

    out_dir = root / "data" / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "eda_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print("report:", report)


if __name__ == "__main__":
    main()
