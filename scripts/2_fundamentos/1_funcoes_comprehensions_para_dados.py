"""01 — Funções e comprehensions (focado em dados)

Objetivo: revisar padrões de Python aplicáveis ao dia a dia de análise de dados.
Tempo sugerido: ~20 min

Execute no terminal (na raiz do repo):
    python scripts/01_fundamentos/01_funcoes_comprehensions_para_dados.py
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd


def find_repo_root(start: Path | None = None) -> Path:
    """Sobe diretórios até encontrar README.md + pasta data."""
    cur = (start or Path.cwd()).resolve()
    for _ in range(10):
        if (cur / "README.md").exists() and (cur / "data").exists():
            return cur
        cur = cur.parent
    return Path.cwd().resolve()


ROOT = find_repo_root()
SAMPLE_DIR = ROOT / "data" / "sample"


def safe_float(x) -> float | None:
    """Tenta converter para float; devolve None se falhar."""
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def top_n(values: Iterable[float], n: int = 5) -> list[float]:
    """Retorna os N maiores valores."""
    return sorted(values, reverse=True)[:n]


def bucket_revenue(v: float) -> str:
    """Classifica uma receita em faixa."""
    if v < 150:
        return "baixo"
    if v < 300:
        return "medio"
    return "alto"


def main() -> None:
    # Carrega dados de exemplo
    sales = pd.read_csv(SAMPLE_DIR / "sales.csv")

    # 1) Comprehensions
    rows = sales.to_dict(orient="records")

    high = [r for r in rows if r["revenue"] > 300]
    order_revenue = [(r["order_id"], r["revenue"]) for r in rows]
    revenue_by_order = {r["order_id"]: r["revenue"] for r in rows}

    print("high rows:", len(high))
    print("first tuples:", order_revenue[:3])
    print("first dict items:", list(revenue_by_order.items())[:3])

    # 2) Funções utilitárias
    print("top 5 revenue:", top_n(sales["revenue"].tolist(), 5))

    # 3) Aplicando no Pandas
    sales["ticket_faixa_apply"] = sales["revenue"].apply(bucket_revenue)

    conds = [sales["revenue"] < 150, sales["revenue"].between(150, 299.99)]
    choices = ["baixo", "medio"]
    sales["ticket_faixa_vec"] = np.select(conds, choices, default="alto")

    print("\nPreview:")
    print(sales[["revenue","ticket_faixa_apply","ticket_faixa_vec"]].head())


if __name__ == "__main__":
    main()
