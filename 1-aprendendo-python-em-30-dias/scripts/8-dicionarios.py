# Dicionários em Python
# Um dicionário é uma estrutura de dados que armazena pares de chave-valor
# Características:
# - Mutável (pode ser modificado)
# - Não ordenado (antes do Python 3.7)
# - Indexado por chaves (não por posição)
# - Chaves devem ser únicas e imutáveis (strings, números, tuplas)

# Criando um dicionário vazio
dicionario_vazio = {}
dicionario_vazio2 = dict()

# Criando dicionários com elementos
pessoa = {
    "nome": "João",
    "idade": 28,
    "profissao": "Desenvolvedor"
}

carro = dict(marca="Toyota", modelo="Corolla", ano=2020)

# Acessando valores
print(pessoa["nome"])  # Saída: João
print(carro.get("modelo"))  # Saída: Corolla

# Acessando com get() evita erros se a chave não existir
print(pessoa.get("endereco"))  # Saída: None
print(pessoa.get("endereco", "Não informado"))  # Saída: Não informado

# Modificando valores
pessoa["idade"] = 29
carro.update({"ano": 2021, "cor": "Prata"})
print(pessoa)  # Saída: {'nome': 'João', 'idade': 29, 'profissao': 'Desenvolvedor'}
print(carro)   # Saída: {'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2021, 'cor': 'Prata'}

# Adicionando novos pares chave-valor
pessoa["email"] = "joao@exemplo.com"
carro["quilometragem"] = 15000
print(pessoa)  # Saída: {'nome': 'João', 'idade': 29, 'profissao': 'Desenvolvedor', 'email': 'joao@exemplo.com'}

# Removendo itens
idade = pessoa.pop("idade")  # Remove e retorna o valor
print(f"Idade removida: {idade}")  # Saída: Idade removida: 29
print(pessoa)  # Saída: {'nome': 'João', 'profissao': 'Desenvolvedor', 'email': 'joao@exemplo.com'}

# Removendo o último item adicionado (Python 3.7+)
ultimo_item = carro.popitem()  # Retorna uma tupla (chave, valor)
print(f"Último item removido: {ultimo_item}")  # Saída: Último item removido: ('quilometragem', 15000)

# Removendo um item específico
del carro["cor"]
print(carro)  # Saída: {'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2021}

# Verificando se uma chave existe
if "nome" in pessoa:
    print("A chave 'nome' existe!")  # Esta linha será executada

# Iterando sobre dicionários
print("\nIterando sobre chaves:")
for chave in pessoa:
    print(chave)

print("\nIterando sobre valores:")
for valor in pessoa.values():
    print(valor)

print("\nIterando sobre pares chave-valor:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Copiando dicionários
pessoa_copia = pessoa.copy()
pessoa_copia2 = dict(pessoa)

# Dicionários aninhados (nested dictionaries)
contatos = {
    "João": {
        "email": "joao@exemplo.com",
        "telefone": "1234-5678"
    },
    "Maria": {
        "email": "maria@exemplo.com",
        "telefone": "8765-4321",
        "endereco": "Rua das Flores, 123"
    }
}

print("\nEmail da Maria:", contatos["Maria"]["email"])  # Saída: maria@exemplo.com

# Limpando um dicionário
carro.clear()
print("Dicionário carro após clear():", carro)  # Saída: {}

# Métodos úteis
pessoa_keys = list(pessoa.keys())
print("Chaves:", pessoa_keys)  # Saída: ['nome', 'profissao', 'email']

pessoa_values = list(pessoa.values())
print("Valores:", pessoa_values)  # Saída: ['João', 'Desenvolvedor', 'joao@exemplo.com']

# Exemplo de uso prático: contando frequência de palavras
texto = "Python é uma linguagem de programação Python é muito utilizada em ciência de dados"
palavras = texto.lower().split()

frequencia = {}
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print("\nFrequência de palavras:")
for palavra, contagem in frequencia.items():
    print(f"{palavra}: {contagem}")

# Usando dict.fromkeys() para criar dicionário com valores padrão
frutas = ["maçã", "banana", "laranja"]
estoque = dict.fromkeys(frutas, 0)
print("\nEstoque inicial:", estoque)  # Saída: {'maçã': 0, 'banana': 0, 'laranja': 0}

# Usando setdefault() para adicionar uma chave se não existir
pessoa.setdefault("website", "www.joao.com")  # Adiciona porque não existe
pessoa.setdefault("nome", "Roberto")  # Não altera porque a chave já existe
print("\nDepois de setdefault:", pessoa)  # nome continua sendo João