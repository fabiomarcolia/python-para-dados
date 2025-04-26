
# ============================================
# ✅ O que você aprende com esse script:

# Como identificar, contar, remover e preencher valores nulos

# Como fazer merge (joins) entre DataFrames: inner, left, outer

# Como montar uma tabela dinâmica (pivot table) com pivot_table()

# Como aplicar funções de agregação (sum, mean, etc.)
# ============================================


import pandas as pd


# ============================================
# 1. Tratamento de NULOS
# ============================================

# Criar DataFrame com valores nulos
df_nulos = pd.DataFrame({
    "nome": ["Ana", "Bruno", None, "Carlos"],
    "idade": [25, None, 30, 28],
    "cidade": ["SP", "RJ", "RJ", None]
})

print("DataFrame com nulos:")
print(df_nulos)

# Verificar nulos
print("\nVerificar valores nulos:")
print(df_nulos.isnull())

# Contar nulos por coluna
print("\nContagem de nulos:")
print(df_nulos.isnull().sum())

# Remover linhas com nulo
df_sem_nulos = df_nulos.dropna()
print("\nRemover linhas com nulo:")
print(df_sem_nulos)

# Preencher nulos com valor padrão
df_preenchido = df_nulos.fillna({
    "nome": "Desconhecido",
    "idade": df_nulos["idade"].mean(),
    "cidade": "Indefinido"
})
print("\nPreenchimento de nulos:")
print(df_preenchido)

# ============================================
# 2. Merge (Junção de DataFrames)
# ============================================

# Dois DataFrames com coluna comum "id"
clientes = pd.DataFrame({
    "id": [1, 2, 3],
    "nome": ["Ana", "Bruno", "Carlos"]
})

compras = pd.DataFrame({
    "id": [1, 2, 4],
    "produto": ["Notebook", "Mouse", "Teclado"]
})

# Merge (join) pela coluna "id"
df_merge = pd.merge(clientes, compras, on="id", how="inner")
print("\nMerge (INNER JOIN):")
print(df_merge)

# Merge com LEFT JOIN
df_merge_left = pd.merge(clientes, compras, on="id", how="left")
print("\nMerge (LEFT JOIN):")
print(df_merge_left)

# Merge com OUTER JOIN (todos os dados)
df_merge_outer = pd.merge(clientes, compras, on="id", how="outer")
print("\nMerge (OUTER JOIN):")
print(df_merge_outer)

# ============================================
# 3. Pivot Table (Tabela Dinâmica)
# ============================================

# Criar um DataFrame com dados repetidos
vendas = pd.DataFrame({
    "vendedor": ["Ana", "Ana", "Bruno", "Carlos", "Carlos"],
    "produto": ["Notebook", "Mouse", "Notebook", "Mouse", "Notebook"],
    "valor": [2500, 150, 2700, 160, 2300]
})

print("\nDataFrame de vendas:")
print(vendas)

# Tabela dinâmica: soma dos valores por vendedor e produto
pivot = vendas.pivot_table(
    index="vendedor",
    columns="produto",
    values="valor",
    aggfunc="sum",
    fill_value=0
)

print("\nPivot Table (total vendido por vendedor/produto):")
print(pivot)
