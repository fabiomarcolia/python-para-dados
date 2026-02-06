"""03 — Exceções, validação e logging (padrão de projeto)

Execute na raiz do repo:
    python scripts/01_fundamentos/03_excecoes_logging_validacao.py
"""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd


def find_repo_root(start: Path | None = None) -> Path:
    cur = (start or Path.cwd()).resolve()
    for _ in range(10):
        if (cur / "README.md").exists() and (cur / "data").exists():
            return cur
        cur = cur.parent
    return Path.cwd().resolve()


logger = logging.getLogger("mentoria")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(handler)


def load_sales(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    df = pd.read_csv(path)

    required = {"date", "region", "category", "revenue"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Colunas faltando: {sorted(missing)}")

    return df


def safe_load_sales(path: Path) -> pd.DataFrame | None:
    try:
        df = load_sales(path)
        logger.info("OK: %s linhas, %s colunas", len(df), len(df.columns))
        return df
    except Exception as e:
        logger.error("Falhou ao carregar: %s", e)
        return None


def main() -> None:
    root = find_repo_root()
    sample = root / "data" / "sample" / "sales.csv"

    logger.info("Carregando sales.csv...")
    df = safe_load_sales(sample)
    _ = safe_load_sales(root / "data" / "sample" / "nao_existe.csv")

    if df is None:
        return

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    report = {
        "nulos_total": int(df.isna().sum().sum()),
        "duplicadas_order_id": int(df.duplicated("order_id").sum()),
        "revenue_negativa": int((df["revenue"] < 0).sum()),
        "datas_invalidas": int(df["date"].isna().sum()),
    }

    logger.info("report: %s", report)


if __name__ == "__main__":
    main()
