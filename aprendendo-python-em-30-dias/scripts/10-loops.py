# ============================================
# Tópico: Loops em Python (for e while)
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# O que são loops?
# --------------------------------------------
# Loops permitem repetir um bloco de código várias vezes.
# Python tem dois principais tipos de loop: for e while.

# --------------------------------------------
# Exemplo 1: Loop FOR com range()
# --------------------------------------------
print("Exemplo 1: Contando de 1 a 5")
for i in range(1, 6):
    print(i)
print("Fim do exemplo 1.\n")

# --------------------------------------------
# Exemplo 2: Iterando sobre uma lista
# --------------------------------------------
print("Exemplo 2: Percorrendo uma lista")
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(f"Eu gosto de {fruta}")
print("Fim do exemplo 2.\n")

# --------------------------------------------
# Exemplo 3: FOR com enumerate()
# --------------------------------------------
print("Exemplo 3: Listando com índice")
for indice, fruta in enumerate(frutas):
    print(f"{indice + 1} - {fruta}")
print("Fim do exemplo 3.\n")

# --------------------------------------------
# Exemplo 4: WHILE - repete enquanto a condição for verdadeira
# --------------------------------------------
print("Exemplo 4: Contando com while")
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1
print("Fim do exemplo 4.\n")

# --------------------------------------------
# Exemplo 5: Break e Continue
# --------------------------------------------
print("Exemplo 5: Usando break e continue")
for numero in range(1, 6):
    if numero == 3:
        print("Número 3 encontrado! Pulando...")
        continue  # Pula o restante do loop e vai pro próximo
    if numero == 5:
        print("Parando o loop no número 5.")
        break  # Interrompe o loop
    print(f"Número: {numero}")
print("Fim do exemplo 5.\n")

# --------------------------------------------
# Exemplo 6: Loop em função para somar lista
# --------------------------------------------
def somar_lista(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma

numeros = [10, 20, 30]
print("Exemplo 6: Soma =", somar_lista(numeros), "\n")

# --------------------------------------------
# Dica Extra:
# --------------------------------------------
# Use loops para processar dados, ler arquivos, repetir ações,
# fazer buscas, aplicar cálculos e muito mais!

# Experimente modificar os valores e adicionar mais exemplos!
