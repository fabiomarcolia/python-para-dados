"""02 — Visualização: Seaborn para EDA

Execute na raiz do repo:
    python scripts/04_visualizacao/02_seaborn_eda.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


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

    plt.figure(figsize=(8, 4))
    sns.histplot(sales["revenue"], bins=30, kde=True)
    plt.title("Distribuição de revenue")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
