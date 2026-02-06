# ============================================
# Tópico: Usando MongoDB com Python
# Biblioteca: pymongo
# Autor: Fabio Marçolia
# ============================================

# instale no terminal: pip install pymongo

from pymongo import MongoClient

# --------------------------------------------
# 1. Conectar ao MongoDB
# --------------------------------------------

# Se estiver rodando localmente:
client = MongoClient("mongodb://localhost:27017/")

# Criar banco de dados (será criado ao inserir dados)
db = client["meu_banco"]

# Criar coleção (tabela)
colecao = db["clientes"]

# --------------------------------------------
# 2. Inserir documentos
# --------------------------------------------

cliente = {"nome": "Ana", "idade": 28, "cidade": "SP"}
colecao.insert_one(cliente)  # inserir um

clientes = [
    {"nome": "Bruno", "idade": 32, "cidade": "RJ"},
    {"nome": "Carlos", "idade": 25, "cidade": "BH"},
]
colecao.insert_many(clientes)  # inserir vários

# --------------------------------------------
# 3. Consultar documentos
# --------------------------------------------

# Encontrar todos
for doc in colecao.find():
    print(doc)

# Filtrar por campo
print("\nClientes de SP:")
for doc in colecao.find({"cidade": "SP"}):
    print(doc)

# Buscar um só
cliente = colecao.find_one({"nome": "Carlos"})
print("\nBusca por nome Carlos:", cliente)

# --------------------------------------------
# 4. Atualizar documento
# --------------------------------------------
colecao.update_one(
    {"nome": "Ana"},
    {"$set": {"idade": 29}}  # atualiza apenas o campo idade
)

# --------------------------------------------
# 5. Remover documentos
# --------------------------------------------
colecao.delete_one({"nome": "Carlos"})  # remove um
# colecao.delete_many({})  # cuidado: remove todos

# --------------------------------------------
# 6. Contar documentos
# --------------------------------------------
print("\nTotal de clientes:", colecao.count_documents({}))

# --------------------------------------------
# 7. Criar índice (opcional)
# --------------------------------------------
colecao.create_index("nome")

# --------------------------------------------
# Observação:
# É necessário ter o MongoDB instalado localmente ou usar um cluster no MongoDB Atlas (cloud)
# MongoDB Atlas: https://www.mongodb.com/cloud/atlas

# Exemplo para conexão remota:
# client = MongoClient("mongodb+srv://usuario:senha@cluster0.mongodb.net/?retryWrites=true&w=majority")


# Operações mais avançadas

# from pymongo import MongoClient

# ============================================
# CONEXÃO
# ============================================

client = MongoClient("mongodb://localhost:27017/")
db = client["empresa"]
clientes = db["clientes"]
pedidos = db["pedidos"]

# ============================================
# DADOS DE EXEMPLO
# ============================================

# Limpar as coleções
clientes.delete_many({})
pedidos.delete_many({})

# Inserir clientes
clientes.insert_many([
    {"_id": 1, "nome": "Ana", "idade": 30, "cidade": "SP"},
    {"_id": 2, "nome": "Bruno", "idade": 22, "cidade": "RJ"},
    {"_id": 3, "nome": "Carlos", "idade": 35, "cidade": "SP"},
])

# Inserir pedidos
pedidos.insert_many([
    {"cliente_id": 1, "produto": "Notebook", "valor": 2500},
    {"cliente_id": 1, "produto": "Mouse", "valor": 150},
    {"cliente_id": 2, "produto": "Teclado", "valor": 200},
    {"cliente_id": 3, "produto": "Monitor", "valor": 1200},
])

# ============================================
# CONSULTAS BÁSICAS
# ============================================

print("\nTodos os clientes:")
for doc in clientes.find():
    print(doc)

print("\nClientes de SP com idade > 25:")
for doc in clientes.find({"cidade": "SP", "idade": {"$gt": 25}}):
    print(doc)

print("\nClientes com nome começando com 'B':")
for doc in clientes.find({"nome": {"$regex": "^B"}}):
    print(doc)

print("\nClientes de SP ou RJ:")
for doc in clientes.find({"cidade": {"$in": ["SP", "RJ"]}}):
    print(doc)

# ============================================
# PROJEÇÃO DE CAMPOS
# ============================================

print("\nSomente nomes e cidades (sem _id):")
for doc in clientes.find({}, {"nome": 1, "cidade": 1, "_id": 0}):
    print(doc)

# ============================================
# ORDENAÇÃO
# ============================================

print("\nClientes ordenados por idade (desc):")
for doc in clientes.find().sort("idade", -1):
    print(doc)

# ============================================
# AGREGAÇÃO: TOTAL DE PEDIDOS POR CLIENTE
# ============================================

print("\nTotal de pedidos por cliente:")
pipeline = [
    {"$group": {
        "_id": "$cliente_id",
        "total_pedidos": {"$sum": 1},
        "valor_total": {"$sum": "$valor"},
        "valor_medio": {"$avg": "$valor"}
    }}
]
for doc in pedidos.aggregate(pipeline):
    print(doc)

# ============================================
# JOIN COM $lookup: Clientes + Pedidos
# ============================================

print("\nJoin (lookup) entre clientes e pedidos:")
pipeline = [
    {
        "$lookup": {
            "from": "pedidos",
            "localField": "_id",
            "foreignField": "cliente_id",
            "as": "compras"
        }
    }
]
for doc in clientes.aggregate(pipeline):
    print(doc)

# ============================================
# ATUALIZAÇÃO CONDICIONAL
# ============================================

print("\nAtualizar idade +5 de quem mora em SP:")
clientes.update_many(
    {"cidade": "SP"},
    {"$inc": {"idade": 5}}
)
for doc in clientes.find({"cidade": "SP"}):
    print(doc)

# ============================================
# CONTAR DOCUMENTOS
# ============================================

print("\nTotal de clientes com idade > 30:", clientes.count_documents({"idade": {"$gt": 30}}))
