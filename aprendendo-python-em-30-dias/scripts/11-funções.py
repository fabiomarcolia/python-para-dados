# ============================================
# Tópico: Funções em Python
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# O que são funções?
# --------------------------------------------
# Funções são blocos de código reutilizáveis que executam
# uma tarefa específica. Evitam repetição e organizam melhor o código.

# --------------------------------------------
# Exemplo 1: Definindo e chamando uma função
# --------------------------------------------
def saudacao():
    print("Olá! Seja bem-vindo(a).")

# Chamando a função
saudacao()
print("Fim do exemplo 1.\n")

# --------------------------------------------
# Exemplo 2: Função com parâmetros
# --------------------------------------------
def exibir_nome(nome):
    print(f"Olá, {nome}!")

exibir_nome("Fabio")
exibir_nome("Maria")
print("Fim do exemplo 2.\n")

# --------------------------------------------
# Exemplo 3: Função com retorno (return)
# --------------------------------------------
def dobrar_numero(numero):
    return numero * 2

resultado = dobrar_numero(10)
print("Resultado:", resultado)
print("Fim do exemplo 3.\n")

# --------------------------------------------
# Exemplo 4: Função com múltiplos parâmetros
# --------------------------------------------
def soma(a, b):
    return a + b

print("Soma de 5 + 3 =", soma(5, 3))
print("Fim do exemplo 4.\n")

# --------------------------------------------
# Exemplo 5: Parâmetros com valor padrão
# --------------------------------------------
def mensagem(texto="Olá, mundo!"):
    print(texto)

mensagem()
mensagem("Python é incrível!")
print("Fim do exemplo 5.\n")

# --------------------------------------------
# Exemplo 6: Função que retorna múltiplos valores
# --------------------------------------------
def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    return soma, subtracao

resultado_soma, resultado_sub = operacoes(10, 5)
print("Soma:", resultado_soma)
print("Subtração:", resultado_sub)
print("Fim do exemplo 6.\n")

# --------------------------------------------
# Exemplo 7: Funções com *args e **kwargs
# --------------------------------------------
def somar_tudo(*args):
    return sum(args)

print("Soma com *args:", somar_tudo(1, 2, 3, 4))

def mostrar_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_info(nome="Fabio", idade=30, linguagem="Python")
print("Fim do exemplo 7.\n")

# --------------------------------------------
# Boas práticas:
# - Nome da função deve ser claro (usar verbos)
# - Documente usando docstrings (três aspas)
# - Evite funções muito longas
# - Uma função = uma responsabilidade
# --------------------------------------------
