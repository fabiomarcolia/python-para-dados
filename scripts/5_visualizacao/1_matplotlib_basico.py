"""01 — Visualização: Matplotlib (o básico bem feito)

Execute na raiz do repo:
    python scripts/04_visualizacao/01_matplotlib_basico.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
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
    sales = pd.read_csv(root / "data" / "sample" / "sales.csv")
    sales["date"] = pd.to_datetime(sales["date"])

    daily = sales.groupby("date", as_index=False).agg(revenue=("revenue", "sum"))

    out_dir = root / "data" / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    fig_path = out_dir / "receita_diaria.png"

    plt.figure(figsize=(10, 4))
    plt.plot(daily["date"], daily["revenue"])
    plt.title("Receita diária")
    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    plt.close()

    print("saved:", fig_path)


if __name__ == "__main__":
    main()
