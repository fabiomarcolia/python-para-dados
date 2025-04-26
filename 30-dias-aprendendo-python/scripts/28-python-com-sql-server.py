
# ============================================
# Tópico: Python com SQL Server
# Biblioteca: pyodbc
# Autor: Fabio Marçolia
# ============================================

# Você vai aprender:    
# -Conexão com o banco
# -Criação de tabela
# -Inserção, leitura, atualização e exclusão de dados
# -Leitura com pandas
# -Boas práticas
# -Usar com Procedures

# ============================================



import pyodbc
import pandas as pd

# --------------------------------------------
# 1. Conectar ao SQL Server
# --------------------------------------------
conexao = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"  # ou IP ou hostname
    "DATABASE=teste_python;"
    "Trusted_Connection=yes;"
)

cursor = conexao.cursor()
print("Conexão estabelecida!")

# --------------------------------------------
# 2. Criar tabela (se não existir)
# --------------------------------------------
cursor.execute("""
IF OBJECT_ID('clientes', 'U') IS NULL
CREATE TABLE clientes (
    id INT PRIMARY KEY IDENTITY(1,1),
    nome VARCHAR(50),
    idade INT,
    cidade VARCHAR(50)
)
""")
conexao.commit()

# --------------------------------------------
# 3. Inserir dados
# --------------------------------------------
cursor.execute("INSERT INTO clientes (nome, idade, cidade) VALUES (?, ?, ?)", ("Ana", 30, "SP"))
cursor.execute("INSERT INTO clientes (nome, idade, cidade) VALUES (?, ?, ?)", ("Bruno", 25, "RJ"))
conexao.commit()

# --------------------------------------------
# 4. Consultar dados
# --------------------------------------------
cursor.execute("SELECT * FROM clientes")
for linha in cursor.fetchall():
    print(linha)

# --------------------------------------------
# 5. Usar pandas para leitura
# --------------------------------------------
df = pd.read_sql("SELECT * FROM clientes", conexao)
print("\nLeitura com Pandas:")
print(df)

# --------------------------------------------
# 6. Atualizar dados
# --------------------------------------------
cursor.execute("UPDATE clientes SET idade = ? WHERE nome = ?", (35, "Ana"))
conexao.commit()

# --------------------------------------------
# 7. Deletar registros
# --------------------------------------------
cursor.execute("DELETE FROM clientes WHERE nome = ?", ("Bruno",))
conexao.commit()

# --------------------------------------------
# 8. Filtros com parâmetros
# --------------------------------------------
nome_busca = "Ana"
cursor.execute("SELECT * FROM clientes WHERE nome = ?", (nome_busca,))
print("\nFiltro WHERE nome = 'Ana':")
print(cursor.fetchone())

# --------------------------------------------
# 9. Fechar conexão
# --------------------------------------------
cursor.close()
conexao.close()
print("\nConexão encerrada.")



# --------------------------------------------
# Exemplo de JOIN, GROUP BY, ORDER BY com pandas
# --------------------------------------------


import pandas as pd

# ============================================
# Tabelas simuladas (como em SQL)
# ============================================

# Tabela de clientes
clientes = pd.DataFrame({
    "cliente_id": [1, 2, 3],
    "nome": ["Ana", "Bruno", "Carlos"],
    "cidade": ["SP", "RJ", "SP"]
})

# Tabela de pedidos
pedidos = pd.DataFrame({
    "pedido_id": [101, 102, 103, 104],
    "cliente_id": [1, 2, 1, 3],
    "produto": ["Notebook", "Mouse", "Teclado", "Monitor"],
    "valor": [2500, 150, 300, 1200]
})

# ============================================
# JOIN (equivalente ao INNER JOIN em SQL)
# ============================================
# SELECT * FROM clientes JOIN pedidos ON cliente_id

df_join = pd.merge(clientes, pedidos, on="cliente_id", how="inner")

print("\nJOIN entre clientes e pedidos:")
print(df_join)

# ============================================
# GROUP BY (ex: total gasto por cliente)
# ============================================
# SELECT nome, SUM(valor) FROM ... GROUP BY nome

df_group = df_join.groupby("nome")["valor"].sum().reset_index()
df_group = df_group.rename(columns={"valor": "total_gasto"})

print("\nGROUP BY - Total gasto por cliente:")
print(df_group)

# ============================================
# ORDER BY (ordenar por total gasto, decrescente)
# ============================================
# SELECT ... ORDER BY total_gasto DESC

df_sorted = df_group.sort_values(by="total_gasto", ascending=False)

print("\nORDER BY - Total gasto decrescente:")
print(df_sorted)

# ============================================
# Uso de stored procedures com parâmetros
# ============================================

import pyodbc

# ============================================
# Conexão com SQL Server
# ============================================
conexao = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=teste_python;"
    "Trusted_Connection=yes;"
)
cursor = conexao.cursor()

# ============================================
# Exemplo: Procedure no SQL Server
# ============================================
# Suponha que no banco de dados, temos a SP:

"""
CREATE PROCEDURE BuscarClientePorCidade
    @Cidade VARCHAR(50)
AS
BEGIN
    SELECT nome, idade FROM clientes WHERE cidade = @Cidade
END
"""

# ============================================
# Chamar a Stored Procedure com parâmetro
# ============================================

cidade = "SP"
cursor.execute("EXEC BuscarClientePorCidade @Cidade = ?", (cidade,))

# Obter resultados
print("\nResultado da Stored Procedure:")
for linha in cursor.fetchall():
    print(linha)

# ============================================
# Outra forma: procedure com múltiplos parâmetros
# ============================================

"""
CREATE PROCEDURE InserirCliente
    @Nome VARCHAR(50),
    @Idade INT,
    @Cidade VARCHAR(50)
AS
BEGIN
    INSERT INTO clientes (nome, idade, cidade)
    VALUES (@Nome, @Idade, @Cidade)
END
"""

# Chamada com 3 parâmetros:
cursor.execute("EXEC InserirCliente @Nome=?, @Idade=?, @Cidade=?", ("Lucas", 27, "MG"))
conexao.commit()
print("\nCliente inserido com sucesso.")

# ============================================
# Encerrar
# ============================================
cursor.close()
conexao.close()
