"""02 — Pathlib e I/O (CSV, JSON, Parquet)

Objetivo: dominar leitura/escrita e organização de pastas para projetos de dados.
Tempo sugerido: ~25 min

Execute na raiz do repo:
    python scripts/01_fundamentos/02_pathlib_io_csv_json_parquet.py
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
    sample_dir = root / "data" / "sample"

    raw = root / "data" / "raw"
    processed = root / "data" / "processed"
    output = root / "data" / "output"

    for p in (raw, processed, output):
        p.mkdir(parents=True, exist_ok=True)

    sales = pd.read_csv(sample_dir / "sales.csv")
    sales["date"] = pd.to_datetime(sales["date"])

    # CSV
    csv_out = output / "sales_export.csv"
    sales.to_csv(csv_out, index=False)

    # JSON summary
    summary = {
        "rows": int(len(sales)),
        "columns": list(sales.columns),
        "date_min": str(sales["date"].min().date()),
        "date_max": str(sales["date"].max().date()),
        "revenue_total": float(sales["revenue"].sum()),
    }
    (output / "sales_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    # Parquet
    pq_out = output / "sales.parquet"
    sales.to_parquet(pq_out, index=False)
    _ = pd.read_parquet(pq_out)

    print("ok:", csv_out, pq_out)


if __name__ == "__main__":
    main()
