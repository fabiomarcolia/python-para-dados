# Tuplas em Python
'''
O que são Tuplas?
Tuplas são estruturas de dados em Python que armazenam coleções ordenadas de itens,
semelhantes às listas. No entanto, ao contrário das listas, as tuplas são imutáveis,
ou seja, não podem ser modificadas após a criação. Tuplas são usadas para dados que
não devem ser alterados, como coordenadas, configurações ou valores de retorno de funções.
'''

print("=== TUPLAS EM PYTHON ===\n")

# 1. Criando Tuplas
print("1. CRIANDO TUPLAS")
print("Existem várias maneiras de criar tuplas em Python.")

# Tupla vazia
tupla_vazia = ()
print(f"Tupla vazia: {tupla_vazia}")

# Tupla com elementos
numeros = (1, 2, 3, 4, 5)
print(f"Tupla de números: {numeros}")

# Tupla com um único elemento (precisa da vírgula)
tupla_unica = (10,)  # A vírgula é necessária!
print(f"Tupla com um elemento: {tupla_unica}")
print(f"Tipo de (10,): {type((10,))}")
print(f"Tipo de (10): {type((10))}")  # Sem a vírgula, não é uma tupla

# Tupla com diferentes tipos de dados
tupla_mista = (1, "Python", 3.14, True, (10, 20))
print(f"Tupla com diferentes tipos: {tupla_mista}")

# Criando tupla sem parênteses (packing)
tupla_sem_parenteses = 1, 2, 3, 4, 5
print(f"Tupla sem parênteses: {tupla_sem_parenteses}")

# Criando tupla com a função tuple()
caracteres = tuple("Python")
print(f"Tupla a partir de uma string: {caracteres}")

# 2. Acessando Elementos de uma Tupla
print("\n2. ACESSANDO ELEMENTOS DE UMA TUPLA")

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho")
print(f"Tupla de meses: {meses}")

# Acessando pelo índice (começa em 0)
print(f"meses[0]: {meses[0]}")  # Primeiro elemento
print(f"meses[3]: {meses[3]}")  # Quarto elemento

# Índices negativos (contam a partir do final)
print(f"meses[-1]: {meses[-1]}")  # Último elemento
print(f"meses[-2]: {meses[-2]}")  # Penúltimo elemento

# 3. Fatiamento (Slicing) de Tuplas
print("\n3. FATIAMENTO (SLICING) DE TUPLAS")
print("Podemos obter partes de uma tupla usando a sintaxe [início:fim:passo].")

print(f"meses[1:4]: {meses[1:4]}")    # Do segundo ao quarto elemento
print(f"meses[:3]: {meses[:3]}")      # Do início até o terceiro elemento
print(f"meses[3:]: {meses[3:]}")      # Do quarto elemento até o final
print(f"meses[::2]: {meses[::2]}")    # Elementos em posições pares
print(f"meses[::-1]: {meses[::-1]}")  # Tupla invertida

# 4. Imutabilidade das Tuplas
print("\n4. IMUTABILIDADE DAS TUPLAS")
print("Tuplas são imutáveis, ou seja, não podem ser modificadas após a criação.")

coordenadas = (10, 20, 30)
print(f"Tupla original: {coordenadas}")

# Tentando modificar um elemento (causará erro)
try:
    coordenadas[0] = 100
except TypeError as e:
    print(f"Erro ao tentar modificar a tupla: {e}")

# No entanto, se um elemento da tupla for um objeto mutável, o objeto em si pode ser modificado
tupla_com_lista = (1, 2, [3, 4])
print(f"Tupla com lista: {tupla_com_lista}")

tupla_com_lista[2][0] = 30  # Modificando a lista dentro da tupla
print(f"Após modificar a lista dentro da tupla: {tupla_com_lista}")

# 5. Operações com Tuplas
print("\n5. OPERAÇÕES COM TUPLAS")

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenação
concatenada = tupla1 + tupla2
print(f"tupla1 + tupla2: {concatenada}")

# Repetição
repetida = tupla1 * 3
print(f"tupla1 * 3: {repetida}")

# Verificar se um elemento está na tupla
print(f"2 in tupla1: {2 in tupla1}")
print(f"7 in tupla1: {7 in tupla1}")

# Comprimento da tupla
print(f"len(tupla1): {len(tupla1)}")

# 6. Métodos de Tuplas
print("\n6. MÉTODOS DE TUPLAS")
print("Tuplas têm poucos métodos, devido à sua imutabilidade.")

numeros = (5, 2, 8, 2, 1, 8, 9)
print(f"Tupla: {numeros}")

# Método count() - conta ocorrências de um valor
print(f"numeros.count(2): {numeros.count(2)}")

# Método index() - retorna a posição da primeira ocorrência
print(f"numeros.index(8): {numeros.index(8)}")

# Com início e fim opcionais
print(f"numeros.index(8, 3): {numeros.index(8, 3)}")  # Procura a partir do índice 3

# 7. Conversão entre Tuplas e Listas
print("\n7. CONVERSÃO ENTRE TUPLAS E LISTAS")

# Tupla para lista
tupla = (1, 2, 3, 4)
lista = list(tupla)
print(f"Tupla: {tupla}")
print(f"Convertida para lista: {lista}")

# Lista para tupla
lista = [5, 6, 7, 8]
tupla = tuple(lista)
print(f"Lista: {lista}")
print(f"Convertida para tupla: {tupla}")

# 8. Desempacotamento de Tuplas
print("\n8. DESEMPACOTAMENTO DE TUPLAS")
print("Atribuir elementos de uma tupla a variáveis individuais.")

coordenadas = (10, 20, 30)
x, y, z = coordenadas
print(f"coordenadas: {coordenadas}")
print(f"x: {x}, y: {y}, z: {z}")

# Desempacotamento com *
primeiro, *meio, ultimo = (1, 2, 3, 4, 5)
print(f"primeiro: {primeiro}, meio: {meio}, último: {ultimo}")

# 9. Tuplas em Loops
print("\n9. TUPLAS EM LOOPS")

cores = ("vermelho", "verde", "azul", "amarelo")

print("Iterando sobre uma tupla:")
for cor in cores:
    print(f"  - {cor}")

print("\nIterando com índice e valor:")
for i, cor in enumerate(cores):
    print(f"  {i}: {cor}")

# 10. Tuplas como Retorno de Funções
print("\n10. TUPLAS COMO RETORNO DE FUNÇÕES")

def minmax(numeros):
    """Retorna o valor mínimo e máximo de uma sequência"""
    return min(numeros), max(numeros)

valores = [23, 45, 12, 67, 89, 34]
minimo, maximo = minmax(valores)
print(f"Lista: {valores}")
print(f"Mínimo: {minimo}, Máximo: {maximo}")

# 11. Named Tuples (Tuplas Nomeadas)
print("\n11. TUPLAS NOMEADAS (NAMEDTUPLES)")
print("Uma extensão de tuplas onde os campos podem ser acessados por nome.")

from collections import namedtuple

# Definindo uma tupla nomeada
Pessoa = namedtuple('Pessoa', ['nome', 'idade', 'cidade'])

# Criando instâncias
p1 = Pessoa('Maria', 30, 'São Paulo')
p2 = Pessoa('João', 25, 'Rio de Janeiro')

print(f"p1: {p1}")
print(f"p2: {p2}")

# Acessando por índice
print(f"p1[0]: {p1[0]}")

# Acessando por nome
print(f"p1.nome: {p1.nome}")
print(f"p1.idade: {p1.idade}")
print(f"p1.cidade: {p1.cidade}")

# Desempacotando
nome, idade, cidade = p1
print(f"Desempacotado: nome={nome}, idade={idade}, cidade={cidade}")

# 12. Vantagens das Tuplas sobre Listas
print("\n12. VANTAGENS DAS TUPLAS SOBRE LISTAS")
print("Por que usar tuplas em vez de listas?")

print("  1. Imutabilidade: garantia que os dados não serão alterados")
print("  2. Performance: tuplas são geralmente mais rápidas que listas")
print("  3. Podem ser usadas como chaves em dicionários (listas não podem)")
print("  4. Segurança: dados que não devem ser alterados")
print("  5. Clareza: indica para outros programadores que os dados são fixos")

# Exemplo: tupla como chave de dicionário
try:
    dicionario = {(1, 2): "tupla como chave"}
    print(f"Dicionário com tupla como chave: {dicionario}")
    
    dicionario[[1, 2]] = "lista como chave"  # Isso causará erro
except TypeError as e:
    print(f"Erro ao usar lista como chave: {e}")

# 13. Tuplas vs. Listas: Quando Usar Cada Uma
print("\n13. TUPLAS VS. LISTAS: QUANDO USAR CADA UMA")

print("Use tuplas quando:")
print("  - Os dados não devem mudar (ex: coordenadas, configurações)")
print("  - Quer garantir que os dados não sejam alterados acidentalmente")
print("  - Precisa de uma coleção que possa ser usada como chave de dicionário")
print("  - Retornar múltiplos valores de uma função")

print("\nUse listas quando:")
print("  - Os dados precisam ser modificados (adicionados, removidos ou alterados)")
print("  - Precisa de muitos métodos para manipulação (sort, append, etc.)")
print("  - Está trabalhando com uma coleção homogênea que muda com frequência")