"""03 — Visualização: Plotly (interativo)

Execute na raiz do repo:
    python scripts/04_visualizacao/03_plotly_interativo.py
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px


def find_repo_root(start: Path | None = None) -> Path:
    cur = (start or Path.cwd()).resolve()
    for _ in range(10):
        if (cur / "README.md").exists() and (cur / "data").exists():
            return cur
        cur = cur.parent
    return Path.cwd().resolve()


def main() -> None:
    root = find_repo_root()
    sales = pd.read_csv(root / "data" / "sample" / "sales.csv")
    sales["date"] = pd.to_datetime(sales["date"])

    daily = sales.groupby("date", as_index=False).agg(revenue=("revenue", "sum"))
    fig = px.line(daily, x="date", y="revenue", title="Receita diária (interativo)")

    out_dir = root / "data" / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    html_path = out_dir / "receita_diaria_plotly.html"
    fig.write_html(html_path)

    print("saved:", html_path)


if __name__ == "__main__":
    main()
