# ============================================
# Tópico: Python com MySQL
# Biblioteca: mysql.connector
# Autor: Fabio Marçolia
# ============================================

# Você vai aprender
# -Conexão com o banco
# -Criação de tabela
# -Inserção, leitura, atualização e exclusão de dados
# -Leitura com pandas
# -Filtros e boas práticas

# ============================================

# 💡 Pré-requisitos:
# 1-MySQL instalado e rodando
# 2-Criar banco de dados testepython
# 3-Instalar o driver: pip install mysql-connector-python

# ============================================

# Instale no terminal: pip install mysql-connector-python

import mysql.connector
import pandas as pd

# --------------------------------------------
# 1. Conectar ao MySQL
# --------------------------------------------
conexao = mysql.connector.connect(
    host="localhost",
    user="root",         # ou outro usuário
    password="sua_senha",
    database="testepython"
)

cursor = conexao.cursor()
print("Conexão com MySQL estabelecida!")

# --------------------------------------------
# 2. Criar tabela (se não existir)
# --------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    idade INT,
    cidade VARCHAR(50)
)
""")

# --------------------------------------------
# 3. Inserir dados
# --------------------------------------------
cursor.execute("INSERT INTO clientes (nome, idade, cidade) VALUES (%s, %s, %s)", ("Ana", 30, "SP"))
cursor.execute("INSERT INTO clientes (nome, idade, cidade) VALUES (%s, %s, %s)", ("Bruno", 25, "RJ"))
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
print("\nLeitura com pandas:")
print(df)

# --------------------------------------------
# 6. Atualizar dados
# --------------------------------------------
cursor.execute("UPDATE clientes SET idade = %s WHERE nome = %s", (35, "Ana"))
conexao.commit()

# --------------------------------------------
# 7. Deletar dados
# --------------------------------------------
cursor.execute("DELETE FROM clientes WHERE nome = %s", ("Bruno",))
conexao.commit()

# --------------------------------------------
# 8. Consultar com filtro
# --------------------------------------------
cursor.execute("SELECT * FROM clientes WHERE cidade = %s", ("SP",))
print("\nClientes de SP:")
for linha in cursor.fetchall():
    print(linha)

# --------------------------------------------
# 9. Fechar conexão
# --------------------------------------------
cursor.close()
conexao.close()
print("\nConexão encerrada.")


# --------------------------------------------
# Trabalhando com Store Procedure
# Veja o arquivo SQL para criar o Banco e Procedure: criar-banco-procedure-mysql.sql
# --------------------------------------------

import mysql.connector

# Conectar ao MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",         # Trocar se necessário
    password="sua_senha",
    database="testepython"
)

cursor = conexao.cursor()

# Executar a stored procedure
cidade_busca = "SP"

cursor.callproc('BuscarClientesPorCidade', [cidade_busca])

# A resposta vem dentro de cursor.stored_results()
print("\nClientes da cidade:", cidade_busca)
for resultado in cursor.stored_results():
    for linha in resultado.fetchall():
        print(linha)

# Encerrar conexão
cursor.close()
conexao.close()
