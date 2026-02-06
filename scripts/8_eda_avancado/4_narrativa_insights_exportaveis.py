"""04 — EDA: narrativa e insights exportáveis

Execute na raiz do repo:
    python scripts/07_eda_avancado/04_narrativa_insights_exportaveis.py

Saídas:
- dados/output/insights_07_04.md
- dados/output/pareto_produtos.png
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


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

    df = sales.merge(customers, on="customer_id", how="left")

    seg = (
        df.groupby("segment")
          .agg(revenue_total=("revenue", "sum"), orders=("order_id", "nunique"))
          .assign(avg_ticket=lambda x: x["revenue_total"] / x["orders"])
          .sort_values("avg_ticket", ascending=False)
    )

    prod = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
    pareto = (prod.cumsum() / prod.sum()).reset_index()
    pareto.columns = ["product", "cum_share"]
    k = int((pareto["cum_share"] <= 0.80).sum())

    out_dir = data / "output"
    out_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(range(1, len(pareto) + 1), pareto["cum_share"])
    ax.axhline(0.8, linestyle="--")
    ax.set_title("Pareto: share acumulado de receita por produto")
    ax.set_xlabel("rank do produto")
    ax.set_ylabel("share acumulado")
    fig.tight_layout()
    fig.savefig(out_dir / "pareto_produtos.png", dpi=160)
    plt.close(fig)

    insights = [
        {
            "pergunta": "Ticket médio difere entre segmentos?",
            "insight": f"Segmento líder: {seg.index[0]} (avg_ticket={seg['avg_ticket'].iloc[0]:.2f}).",
            "evidencia": "Tabela seg + gráfico de ticket médio"
        },
        {
            "pergunta": "Quantos produtos fazem ~80% da receita?",
            "insight": f"~{k} produtos acumulam aproximadamente 80% da receita.",
            "evidencia": "Curva de Pareto"
        },
    ]

    insights_df = pd.DataFrame(insights)
    (out_dir / "insights_07_04.md").write_text(insights_df.to_markdown(index=False), encoding="utf-8")

    print("OK! Saídas em:", out_dir)


if __name__ == "__main__":
    main()
