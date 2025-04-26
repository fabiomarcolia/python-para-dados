# Listas em Python
'''
O que são Listas?
Listas são estruturas de dados em Python que armazenam coleções ordenadas de itens.
Elas são mutáveis (podem ser modificadas após a criação) e podem conter elementos
de diferentes tipos, incluindo outras listas. Listas são uma das estruturas de dados
mais versáteis e utilizadas em Python.
'''

print("=== LISTAS EM PYTHON ===\n")

# 1. Criando Listas
print("1. CRIANDO LISTAS")
print("Há várias formas de criar listas em Python.")

# Lista vazia
lista_vazia = []
print(f"Lista vazia: {lista_vazia}")

# Lista com elementos
numeros = [1, 2, 3, 4, 5]
print(f"Lista de números: {numeros}")

# Lista com diferentes tipos de dados
lista_mista = [1, "Python", 3.14, True, [10, 20]]
print(f"Lista com diferentes tipos: {lista_mista}")

# Criando lista com a função list()
caracteres = list("Python")
print(f"Lista a partir de uma string: {caracteres}")

# Criando lista com range
sequencia = list(range(1, 6))
print(f"Lista com range: {sequencia}")

# Compreensão de lista (List Comprehension)
quadrados = [x**2 for x in range(1, 6)]
print(f"Lista de quadrados com compreensão: {quadrados}")

# 2. Acessando Elementos de uma Lista
print("\n2. ACESSANDO ELEMENTOS DE UMA LISTA")

frutas = ["maçã", "banana", "laranja", "uva", "manga"]
print(f"Lista de frutas: {frutas}")

# Acessando pelo índice (começa em 0)
print(f"frutas[0]: {frutas[0]}")  # Primeiro elemento
print(f"frutas[2]: {frutas[2]}")  # Terceiro elemento

# Índices negativos (contam a partir do final)
print(f"frutas[-1]: {frutas[-1]}")  # Último elemento
print(f"frutas[-2]: {frutas[-2]}")  # Penúltimo elemento

# 3. Fatiamento (Slicing) de Listas
print("\n3. FATIAMENTO (SLICING) DE LISTAS")
print("Podemos obter partes de uma lista usando a sintaxe [início:fim:passo].")

print(f"frutas[1:4]: {frutas[1:4]}")    # Do segundo ao quarto elemento
print(f"frutas[:3]: {frutas[:3]}")      # Do início até o terceiro elemento
print(f"frutas[2:]: {frutas[2:]}")      # Do terceiro elemento até o final
print(f"frutas[::2]: {frutas[::2]}")    # Elementos em posições pares
print(f"frutas[::-1]: {frutas[::-1]}")  # Lista invertida

# 4. Modificando Listas
print("\n4. MODIFICANDO LISTAS")
print("Listas são mutáveis, o que significa que podem ser alteradas após a criação.")

numeros = [1, 2, 3, 4, 5]
print(f"Lista original: {numeros}")

# Alterando um elemento
numeros[2] = 30
print(f"Após numeros[2] = 30: {numeros}")

# Alterando vários elementos com slicing
numeros[1:4] = [20, 30, 40]
print(f"Após numeros[1:4] = [20, 30, 40]: {numeros}")

# 5. Métodos de Listas
print("\n5. MÉTODOS DE LISTAS")
print("Python oferece vários métodos para trabalhar com listas.")

lista = [3, 1, 4, 1, 5, 9]
print(f"Lista original: {lista}")

# Adicionando elementos
print("\nAdicionando elementos:")
lista.append(6)  # Adiciona ao final
print(f"Após lista.append(6): {lista}")

lista.insert(2, 10)  # Insere na posição especificada
print(f"Após lista.insert(2, 10): {lista}")

lista.extend([7, 8])  # Adiciona vários elementos
print(f"Após lista.extend([7, 8]): {lista}")

# Removendo elementos
print("\nRemovendo elementos:")
removido = lista.pop()  # Remove e retorna o último elemento
print(f"Elemento removido com lista.pop(): {removido}")
print(f"Lista após pop(): {lista}")

removido = lista.pop(2)  # Remove e retorna o elemento na posição 2
print(f"Elemento removido com lista.pop(2): {removido}")
print(f"Lista após pop(2): {lista}")

lista.remove(5)  # Remove a primeira ocorrência do valor
print(f"Após lista.remove(5): {lista}")

# Organizando listas
print("\nOrganizando listas:")
lista.sort()  # Ordena a lista in-place
print(f"Após lista.sort(): {lista}")

lista.reverse()  # Inverte a lista in-place
print(f"Após lista.reverse(): {lista}")

# Outros métodos úteis
print("\nOutros métodos úteis:")
print(f"lista.count(1): {lista.count(1)}")  # Conta ocorrências do valor
print(f"lista.index(4): {lista.index(4)}")  # Retorna a posição da primeira ocorrência

copia = lista.copy()  # Cria uma cópia rasa da lista
print(f"copia = lista.copy(): {copia}")

lista.clear()  # Remove todos os elementos
print(f"Após lista.clear(): {lista}")

# 6. Operações com Listas
print("\n6. OPERAÇÕES COM LISTAS")

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Concatenação
concatenada = lista1 + lista2
print(f"lista1 + lista2: {concatenada}")

# Repetição
repetida = lista1 * 3
print(f"lista1 * 3: {repetida}")

# Verificar se um elemento está na lista
print(f"2 in lista1: {2 in lista1}")
print(f"7 in lista1: {7 in lista1}")

# Comprimento da lista
print(f"len(lista1): {len(lista1)}")

# 7. Listas Multidimensionais
print("\n7. LISTAS MULTIDIMENSIONAIS")
print("Listas podem conter outras listas, criando estruturas multidimensionais.")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriz 3x3:")
for linha in matriz:
    print(linha)

# Acessando elementos da matriz
print(f"matriz[1][2]: {matriz[1][2]}")  # Elemento na 2ª linha, 3ª coluna

# 8. Compreensão de Listas (List Comprehension)
print("\n8. COMPREENSÃO DE LISTAS (LIST COMPREHENSION)")
print("Uma forma concisa de criar listas baseadas em sequências existentes.")

# Forma básica
numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros]
print(f"Quadrados: {quadrados}")

# Com condição
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Números pares de 1 a 10: {pares}")

# Mais complexa
matriz = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Matriz de produtos:")
for linha in matriz:
    print(linha)

# 9. Funções Úteis para Listas
print("\n9. FUNÇÕES ÚTEIS PARA LISTAS")

numeros = [5, 2, 8, 1, 9]
print(f"Lista: {numeros}")

print(f"sum(numeros): {sum(numeros)}")    # Soma dos elementos
print(f"max(numeros): {max(numeros)}")    # Maior valor
print(f"min(numeros): {min(numeros)}")    # Menor valor
print(f"sorted(numeros): {sorted(numeros)}")  # Retorna uma nova lista ordenada
print(f"sorted(numeros, reverse=True): {sorted(numeros, reverse=True)}")  # Ordem decrescente

# 10. Desempacotamento de Listas
print("\n10. DESEMPACOTAMENTO DE LISTAS")
print("Atribuir elementos de uma lista a variáveis individuais.")

coordenadas = [10, 20, 30]
x, y, z = coordenadas
print(f"coordenadas: {coordenadas}")
print(f"x: {x}, y: {y}, z: {z}")

# Desempacotamento com *
primero, *meio, ultimo = [1, 2, 3, 4, 5]
print(f"primeiro: {primero}, meio: {meio}, último: {ultimo}")

# 11. Cópias de Listas
print("\n11. CÓPIAS DE LISTAS")
print("Existem diferentes formas de copiar listas em Python.")

original = [1, [2, 3], 4]
print(f"Lista original: {original}")

# Referência (não é uma cópia)
referencia = original
referencia[0] = 100
print(f"Após modificar a referência: original = {original}, referencia = {referencia}")

# Cópia rasa
original = [1, [2, 3], 4]
copia_rasa = original.copy()  # ou list(original) ou original[:]
copia_rasa[0] = 100
print(f"Após modificar cópia rasa[0]: original = {original}, copia_rasa = {copia_rasa}")

copia_rasa[1][0] = 200  # Modifica o objeto aninhado
print(f"Após modificar copia_rasa[1][0]: original = {original}, copia_rasa = {copia_rasa}")

# Cópia profunda
import copy
original = [1, [2, 3], 4]
copia_profunda = copy.deepcopy(original)
copia_profunda[1][0] = 200
print(f"Após modificar copia_profunda[1][0]: original = {original}, copia_profunda = {copia_profunda}")

# 12. Listas vs. Tuplas
print("\n12. LISTAS VS. TUPLAS")
print("Enquanto listas são mutáveis, tuplas são imutáveis.")

lista = [1, 2, 3]
tupla = (1, 2, 3)

print(f"Lista: {lista}")
print(f"Tupla: {tupla}")

# Modificando lista
lista[0] = 10
print(f"Após modificar: {lista}")

# Tentando modificar tupla
try:
    tupla[0] = 10
except TypeError as e:
    print(f"Erro ao tentar modificar tupla: {e}")