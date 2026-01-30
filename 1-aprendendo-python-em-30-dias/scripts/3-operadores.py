# Operadores em Python
'''
O que são operadores?
Operadores são símbolos especiais em Python que realizam operações com variáveis e valores.
Python oferece diversos tipos de operadores que permitem realizar operações aritméticas,
de comparação, lógicas, de atribuição, entre outras.
'''

print("=== OPERADORES EM PYTHON ===\n")

# 1. Operadores Aritméticos
print("1. OPERADORES ARITMÉTICOS")
print("Estes operadores são usados para realizar operações matemáticas básicas.")

a = 10
b = 3

print(f"Valores: a = {a}, b = {b}")
print(f"Adição (a + b): {a + b}")           # 13
print(f"Subtração (a - b): {a - b}")        # 7
print(f"Multiplicação (a * b): {a * b}")    # 30
print(f"Divisão (a / b): {a / b}")          # 3.3333...
print(f"Divisão inteira (a // b): {a // b}")# 3
print(f"Módulo/Resto (a % b): {a % b}")     # 1
print(f"Exponenciação (a ** b): {a ** b}")  # 1000

print("\n2. OPERADORES DE COMPARAÇÃO")
print("Usados para comparar valores e retornam True ou False.")

print(f"Igual (a == b): {a == b}")          # False
print(f"Diferente (a != b): {a != b}")      # True
print(f"Maior que (a > b): {a > b}")        # True
print(f"Menor que (a < b): {a < b}")        # False
print(f"Maior ou igual (a >= b): {a >= b}") # True
print(f"Menor ou igual (a <= b): {a <= b}") # False

print("\n3. OPERADORES LÓGICOS")
print("Usados para combinar expressões condicionais.")

x = True
y = False

print(f"Valores: x = {x}, y = {y}")
print(f"AND (x and y): {x and y}")  # False (verdadeiro apenas se ambos forem verdadeiros)
print(f"OR (x or y): {x or y}")     # True (verdadeiro se pelo menos um for verdadeiro)
print(f"NOT (not x): {not x}")      # False (inverte o valor booleano)
print(f"NOT (not y): {not y}")      # True

print("\n4. OPERADORES DE ATRIBUIÇÃO")
print("Usados para atribuir valores a variáveis.")

c = 10
print(f"Valor inicial: c = {c}")

c += 5      # Equivalente a: c = c + 5
print(f"Após c += 5: {c}")     # 15

c -= 3      # Equivalente a: c = c - 3
print(f"Após c -= 3: {c}")     # 12

c *= 2      # Equivalente a: c = c * 2
print(f"Após c *= 2: {c}")     # 24

c /= 4      # Equivalente a: c = c / 4
print(f"Após c /= 4: {c}")     # 6.0

c //= 2     # Equivalente a: c = c // 2
print(f"Após c //= 2: {c}")    # 3.0

c %= 2      # Equivalente a: c = c % 2
print(f"Após c %= 2: {c}")     # 1.0

d = 2
d **= 3     # Equivalente a: d = d ** 3
print(f"d = 2, após d **= 3: {d}")  # 8

print("\n5. OPERADORES DE IDENTIDADE")
print("Usados para comparar objetos na memória.")

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(f"lista1 = {lista1}, lista2 = {lista2}, lista3 = lista1")
print(f"lista1 is lista2: {lista1 is lista2}")  # False (objetos diferentes na memória)
print(f"lista1 is lista3: {lista1 is lista3}")  # True (mesmo objeto na memória)
print(f"lista1 is not lista2: {lista1 is not lista2}")  # True

print("\n6. OPERADORES DE ASSOCIAÇÃO")
print("Usados para verificar se um valor existe em uma sequência.")

frutas = ['maçã', 'banana', 'laranja', 'uva']
print(f"Lista de frutas: {frutas}")

print(f"'banana' in frutas: {'banana' in frutas}")          # True
print(f"'abacaxi' in frutas: {'abacaxi' in frutas}")        # False
print(f"'melancia' not in frutas: {'melancia' not in frutas}")  # True

print("\n7. OPERADORES BIT A BIT")
print("Operam em nível de bits e são usados para operações binárias.")

x = 10  # 1010 em binário
y = 7   # 0111 em binário

print(f"Valores: x = {x} (binário: {bin(x)[2:]}), y = {y} (binário: {bin(y)[2:]})")
print(f"AND bit a bit (x & y): {x & y}")       # 2 (0010 em binário)
print(f"OR bit a bit (x | y): {x | y}")        # 15 (1111 em binário)
print(f"XOR bit a bit (x ^ y): {x ^ y}")       # 13 (1101 em binário)
print(f"NOT bit a bit (~x): {~x}")             # -11 (inverte todos os bits + 1)
print(f"Deslocamento à esquerda (x << 1): {x << 1}")  # 20 (10100 em binário)
print(f"Deslocamento à direita (x >> 1): {x >> 1}")  # 5 (0101 em binário)

print("\n8. PRECEDÊNCIA DE OPERADORES")
print("A ordem em que as operações são executadas.")

resultado = 10 + 5 * 2
print(f"10 + 5 * 2 = {resultado}")  # 20, pois a multiplicação é executada antes da adição

resultado = (10 + 5) * 2
print(f"(10 + 5) * 2 = {resultado}")  # 30, pois os parênteses têm precedência mais alta

# Exemplo mais complexo
expressao = 5 + 3 * 2 ** 2 - 4 // 2
print(f"5 + 3 * 2 ** 2 - 4 // 2 = {expressao}")  # 15

print("\n9. TABELA DE PRECEDÊNCIA (da mais alta para a mais baixa):")
print("1. Parênteses e colchetes: (), []")
print("2. Exponenciação: **")
print("3. Complemento bit a bit: ~")
print("4. Multiplicação, divisão, divisão inteira, módulo: *, /, //, %")
print("5. Adição e subtração: +, -")
print("6. Deslocamentos bit a bit: <<, >>")
print("7. Operações bit a bit: &, ^, |")
print("8. Comparações: ==, !=, <, >, <=, >=")
print("9. Operações lógicas: not, and, or")
print("10. Operadores de atribuição: =, +=, -=, etc.")