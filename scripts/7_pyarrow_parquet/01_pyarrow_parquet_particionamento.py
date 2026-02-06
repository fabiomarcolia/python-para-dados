"""01 — PyArrow + Parquet: schema e particionamento

Execute na raiz do repo:
    python scripts/06_pyarrow_parquet/01_pyarrow_parquet_particionamento.py
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.dataset as ds
import pyarrow.parquet as pq


def find_repo_root(start: Path | None = None) -> Path:
    cur = (start or Path.cwd()).resolve()
    for _ in range(10):
        if (cur / "README.md").exists() and (cur / "data").exists():
            return cur
        cur = cur.parent
    return Path.cwd().resolve()


def main() -> None:
    root = find_repo_root()
    sample = root / "data" / "sample" / "sales.csv"

    df = pd.read_csv(sample)
    table = pa.Table.from_pandas(df)

    out_dir = root / "data" / "output"
    out_dir.mkdir(parents=True, exist_ok=True)

    parquet_path = out_dir / "sales_arrow.parquet"
    pq.write_table(table, parquet_path)

    partition_dir = out_dir / "sales_partitioned"
    partition_dir.mkdir(parents=True, exist_ok=True)

    ds.write_dataset(
        data=table,
        base_dir=str(partition_dir),
        format="parquet",
        partitioning=["region"],
        existing_data_behavior="overwrite_or_ignore",
    )

    dataset = ds.dataset(str(partition_dir), format="parquet")
    filtered = dataset.to_table(filter=ds.field("region") == "Sudeste")
    print("filtered rows:", filtered.num_rows)


if __name__ == "__main__":
    main()
