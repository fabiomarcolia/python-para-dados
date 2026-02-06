"""03_pandas/01_pandas_intro_limpeza.py

Objetivo:
- Carregar um dataset (via dados/source/)
- Inspeção rápida e checks de qualidade
"""

from pathlib import Path
import pandas as pd
import numpy as np

BASE = Path("data")
SOURCE = BASE / "source" / "bases-dados-analytics-powerbi-ml"

# 1) Descobrir arquivos
csvs = list(SOURCE.rglob("*.csv"))
print(f"CSVs encontrados: {len(csvs)}")
if not csvs:
    print("Dica: adicione o submodule/clone em dados/source (ver README).")
    raise SystemExit

path = csvs[0]  # ajuste para o dataset desejado
print("Usando:", path)

# 2) Ler
df = pd.read_csv(path)

# 3) Inspeção
print("shape:", df.shape)
print(df.head(3))

# 4) Qualidade
null_rate = df.isna().mean().sort_values(ascending=False)
print("\nTop 10 colunas com mais nulos:")
print(null_rate.head(10))

dup = df.duplicated().sum()
print("\nDuplicados:", int(dup))
