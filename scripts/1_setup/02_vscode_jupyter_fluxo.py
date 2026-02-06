"""02 — VS Code + Jupyter (fluxo de trabalho)

Este script é só um checklist executável para você validar o ambiente.
"""

from __future__ import annotations

from pathlib import Path


def find_repo_root(start: Path | None = None) -> Path:
    cur = (start or Path.cwd()).resolve()
    for _ in range(10):
        if (cur / "README.md").exists() and (cur / "data").exists():
            return cur
        cur = cur.parent
    return Path.cwd().resolve()


def main() -> None:
    root = find_repo_root()
    print("ROOT:", root)

    # sanity checks
    req = root / "requirements.txt"
    sample_sales = root / "data" / "sample" / "sales.csv"

    print("requirements.txt exists:", req.exists())
    print("sample sales exists:", sample_sales.exists())

    print("\nAgora rode:")
    print("1) python scripts/03_pandas/02_groupby_pivot_agg.py")
    print("2) abra notebooks/04_visualizacao/03_plotly_interativo.ipynb e execute")


if __name__ == "__main__":
    main()
