# ============================================
# Tópico: Introdução ao Pandas
# Autor: Fabio Marçolia
# ============================================

# 🐼 O que é o Pandas?
# 📌 Pandas é uma biblioteca do Python voltada para análise e manipulação de dados.
# Ela fornece estruturas de dados poderosas e flexíveis, como:

# Series → uma coluna (como uma lista com rótulos)

# DataFrame → uma tabela (como uma planilha ou tabela SQL)

# ✅ Por que usar Pandas?
# Leitura de arquivos (CSV, Excel, JSON, SQL etc.)

# Limpeza e transformação de dados

# Estatísticas e agregações

# Filtros e ordenações

# Operações parecidas com SQL (groupby, join, merge, etc.)

# Integração com matplotlib, seaborn, scikit-learn e outras

# ============================================


import pandas as pd

# --------------------------------------------
# 1. Criar um DataFrame manualmente
# --------------------------------------------
dados = {
    "nome": ["Ana", "Bruno", "Carlos"],
    "idade": [25, 30, 28],
    "cidade": ["SP", "RJ", "BH"]
}

df = pd.DataFrame(dados)
print("1. DataFrame criado manualmente:")
print(df, "\n")

# --------------------------------------------
# 2. Leitura de arquivos
# --------------------------------------------
# df = pd.read_csv("arquivo.csv")
# df = pd.read_excel("arquivo.xlsx")

# --------------------------------------------
# 3. Acesso a colunas
# --------------------------------------------
print("2. Coluna 'nome':")
print(df["nome"], "\n")

# --------------------------------------------
# 4. Filtros (condições)
# --------------------------------------------
print("3. Pessoas com idade > 27:")
print(df[df["idade"] > 27], "\n")

# --------------------------------------------
# 5. Adicionar nova coluna
# --------------------------------------------
df["ano_nascimento"] = 2025 - df["idade"]
print("4. DataFrame com nova coluna:")
print(df, "\n")

# --------------------------------------------
# 6. Estatísticas descritivas
# --------------------------------------------
print("5. Estatísticas descritivas:")
print(df.describe(), "\n")

# --------------------------------------------
# 7. Agrupamento de dados
# --------------------------------------------
media_idade = df.groupby("cidade")["idade"].mean()
print("6. Média de idade por cidade:")
print(media_idade, "\n")

# --------------------------------------------
# 8. Ordenação
# --------------------------------------------
print("7. Ordenado por idade (desc):")
print(df.sort_values(by="idade", ascending=False), "\n")

# --------------------------------------------
# 9. Exportar para CSV
# --------------------------------------------
# df.to_csv("saida.csv", index=False)

# --------------------------------------------
# 10. Outras funções úteis
# --------------------------------------------
print("8. Ver as 2 primeiras linhas:")
print(df.head(2))

print("\n9. Ver as 2 últimas linhas:")
print(df.tail(2))

print("\n10. Informações do DataFrame:")
print(df.info())
