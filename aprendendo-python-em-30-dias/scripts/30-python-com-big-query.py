# ============================================
# Tópico: Python com Google BigQuery
# Biblioteca: google-cloud-bigquery
# Autor: Fabio Marçolia
# ============================================

#Pré-requisitos:
# 1-Ter uma conta no Google Cloud (GCP)
# 2-Criar um Projeto no GCP
# 3-Ativar a API do BigQuery no projeto
# 4-Criar uma chave de serviço (Service Account JSON)
# 5-Instalar a biblioteca Python oficial: pip install google-cloud-bigquery

from google.cloud import bigquery

# --------------------------------------------
# 1. Conexão com o BigQuery
# --------------------------------------------

# Caminho para o seu arquivo de credenciais JSON
credenciais_json = "caminho/para/seu_arquivo_credenciais.json"

# Inicializar cliente
client = bigquery.Client.from_service_account_json(credenciais_json)

# Definir projeto e dataset
project_id = "seu-projeto-gcp"
dataset_id = "testepython"  # Dataset será criado se não existir

# --------------------------------------------
# 2. Criar Dataset (se não existir)
# --------------------------------------------

dataset_ref = bigquery.Dataset(f"{project_id}.{dataset_id}")
dataset_ref.location = "US"

try:
    client.get_dataset(dataset_ref)  # Verifica se existe
except Exception:
    client.create_dataset(dataset_ref)  # Cria se não existir
    print(f"Dataset '{dataset_id}' criado com sucesso.")

# --------------------------------------------
# 3. Criar Tabela clientes (se não existir)
# --------------------------------------------

table_id = f"{project_id}.{dataset_id}.clientes"

schema = [
    bigquery.SchemaField("id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("nome", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("idade", "INTEGER"),
    bigquery.SchemaField("cidade", "STRING"),
]

table = bigquery.Table(table_id, schema=schema)

try:
    client.get_table(table)  # Verifica se existe
except Exception:
    client.create_table(table)
    print(f"Tabela 'clientes' criada com sucesso.")

# --------------------------------------------
# 4. Inserir Dados
# --------------------------------------------

rows_to_insert = [
    {u"id": 1, u"nome": u"Ana", u"idade": 30, u"cidade": u"SP"},
    {u"id": 2, u"nome": u"Bruno", u"idade": 25, u"cidade": u"RJ"},
    {u"id": 3, u"nome": u"Carlos", u"idade": 35, u"cidade": u"MG"},
]

errors = client.insert_rows_json(table_id, rows_to_insert)

if errors == []:
    print("Dados inseridos com sucesso!")
else:
    print("Erros ao inserir dados:", errors)

# --------------------------------------------
# 5. Consultar Dados
# --------------------------------------------

query = f"""
SELECT id, nome, idade, cidade
FROM `{table_id}`
WHERE cidade = 'SP'
"""

query_job = client.query(query)

print("\nClientes de SP:")
for row in query_job:
    print(dict(row))

# --------------------------------------------
# 6. Atualizar Dados (usando SQL)
# --------------------------------------------

query_update = f"""
UPDATE `{table_id}`
SET idade = idade + 1
WHERE cidade = 'SP'
"""

update_job = client.query(query_update)
update_job.result()  # Aguarda execução
print("\nAtualização concluída.")

# --------------------------------------------
# 7. Deletar Dados (usando SQL)
# --------------------------------------------

query_delete = f"""
DELETE FROM `{table_id}`
WHERE nome = 'Bruno'
"""

delete_job = client.query(query_delete)
delete_job.result()
print("\nRegistro de 'Bruno' deletado.")

# --------------------------------------------
# 8. Fechar sessão (opcional no BigQuery client)
# --------------------------------------------

# Não é necessário fechar explicitamente o cliente BigQuery


# --------------------------------------------
# Chamar um Procedure
# --------------------------------------------

from google.cloud import bigquery

# Conectar
client = bigquery.Client.from_service_account_json("caminho/para/credenciais.json")

# Chamar a stored procedure
cidade = "SP"
query = f"CALL `seu-projeto.testepython.BuscarClientesPorCidade`('{cidade}')"

query_job = client.query(query)

for row in query_job:
    print(dict(row))
    
    
# Chamar Função
from google.cloud import bigquery

# 1. Conectar ao BigQuery
client = bigquery.Client.from_service_account_json("caminho/para/credenciais.json")

# 2. Escrever uma consulta que usa a função
query = """
SELECT 
  nome,
  idade,
  `seu-projeto.testepython.CategorizarIdade`(idade) AS categoria
FROM
  `seu-projeto.testepython.clientes`
"""

# 3. Executar a consulta
query_job = client.query(query)

# 4. Obter e exibir os resultados
print("\nResultados usando função BigQuery:")
for row in query_job:
    print(f"Nome: {row['nome']}, Idade: {row['idade']}, Categoria: {row['categoria']}")


# -Funções no BigQuery devem ser referenciadas sempre com o path completo:→ projeto.dataset.funcao
# A consulta (query) é normal como qualquer SELECT, apenas chamando a função.
