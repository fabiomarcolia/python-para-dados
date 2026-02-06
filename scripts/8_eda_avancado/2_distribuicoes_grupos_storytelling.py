"""02 — EDA avançado: distribuições, grupos e storytelling

Execute na raiz do repo:
    python scripts/07_eda_avancado/02_distribuicoes_grupos_storytelling.py

Saídas:
- dados/output/insights_07_02.md
- dados/output/eda07_02_monthly.png
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
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
    customers["signup_date"] = pd.to_datetime(customers["signup_date"])

    df = sales.merge(customers, on="customer_id", how="left")

    # Monthly revenue plot
    monthly = (
        df.assign(month=df["date"].dt.to_period("M").dt.to_timestamp())
          .groupby("month", as_index=False)["revenue"].sum()
          .sort_values("month")
    )

    out_dir = data / "output"
    out_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(monthly["month"], monthly["revenue"])
    ax.set_title("Revenue total por mês")
    ax.set_xlabel("mês")
    ax.set_ylabel("revenue")
    plt.xticks(rotation=30)
    fig.tight_layout()
    fig.savefig(out_dir / "eda07_02_monthly.png", dpi=160)
    plt.close(fig)

    # Simple insights
    insights = []
    top_cat = df.groupby("category")["revenue"].sum().sort_values(ascending=False).head(1)
    top_reg = df.groupby("region")["revenue"].sum().sort_values(ascending=False).head(1)
    insights.append({"pergunta": "Categoria líder?", "insight": f"{top_cat.index[0]} ({top_cat.iloc[0]:.2f})"})
    insights.append({"pergunta": "Região líder?", "insight": f"{top_reg.index[0]} ({top_reg.iloc[0]:.2f})"})

    insights_df = pd.DataFrame(insights)
    (out_dir / "insights_07_02.md").write_text(insights_df.to_markdown(index=False), encoding="utf-8")

    print("OK! Saídas em:", out_dir)


if __name__ == "__main__":
    main()
