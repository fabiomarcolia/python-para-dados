#---------------------------------------------------

#PROMPT: ​Crie um script em Python que carregue um conjunto de dados, lide com valores ausentes e gere estatísticas descritivas para análise exploratória.

#💡 O que esse script faz?
#✅ Carrega um arquivo .csv

#✅ Exibe estrutura do DataFrame

#✅ Trata valores ausentes com estratégias adequadas

#✅ Gera resumo estatístico para dados numéricos e categóricos

#✅ Exporta os dados limpos para um novo .csv

#📌 Requisitos:
#Arquivo .csv com colunas variadas

#Instalar o Pandas:

#---------------------------------------------------

import pandas as pd

# 1. Carregando o conjunto de dados (altere o caminho do arquivo se necessário)
file_path = 'seu_arquivo.csv'  # Substitua pelo seu arquivo real
df = pd.read_csv(file_path)

# 2. Exibir as primeiras linhas
print("\n📌 Primeiras 5 linhas do conjunto de dados:")
print(df.head())

# 3. Verificar tipos de dados e valores nulos
print("\n📌 Informações do DataFrame:")
print(df.info())

print("\n📌 Quantidade de valores ausentes por coluna:")
print(df.isnull().sum())

# 4. Lidando com valores ausentes

# Estratégia: preencher colunas numéricas com a média
for coluna in df.select_dtypes(include=['float64', 'int64']).columns:
    if df[coluna].isnull().any():
        media = df[coluna].mean()
        df[coluna].fillna(media, inplace=True)

# Estratégia: preencher colunas categóricas com o valor mais frequente (moda)
for coluna in df.select_dtypes(include=['object']).columns:
    if df[coluna].isnull().any():
        moda = df[coluna].mode()[0]
        df[coluna].fillna(moda, inplace=True)

# 5. Verificar novamente os valores ausentes
print("\n📌 Após tratamento, valores ausentes por coluna:")
print(df.isnull().sum())

# 6. Estatísticas descritivas
print("\n📌 Estatísticas descritivas (variáveis numéricas):")
print(df.describe())

print("\n📌 Estatísticas descritivas (variáveis categóricas):")
print(df.describe(include=['object']))

# 7. Salvar o DataFrame tratado (opcional)
df.to_csv('dados_tratados.csv', index=False)
print("\n✅ Arquivo tratado salvo como 'dados_tratados.csv'")
