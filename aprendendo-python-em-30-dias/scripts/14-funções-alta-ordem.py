# ============================================
# Tópico: Funções de Alta Ordem (High Order Functions)
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# O que são Funções de Alta Ordem?
# --------------------------------------------
# São funções que:
# 1. Recebem outras funções como argumento
# 2. Retornam outras funções como resultado

# Exemplo simples: função que recebe outra função
def aplicar(funcao, valor):
    return funcao(valor)

def dobrar(x):
    return x * 2

print("Exemplo 1 - Função como argumento:", aplicar(dobrar, 5))

# --------------------------------------------
# Funções embutidas de alta ordem em Python
# --------------------------------------------

# --- map(funcao, iterável) ---
# Aplica uma função a cada item do iterável

numeros = [1, 2, 3, 4]

def quadrado(n):
    return n ** 2

resultado_map = list(map(quadrado, numeros))
print("Exemplo 2 - map:", resultado_map)

# --- filter(funcao, iterável) ---
# Filtra os elementos com base na função que retorna True ou False

def par(n):
    return n % 2 == 0

resultado_filter = list(filter(par, numeros))
print("Exemplo 3 - filter:", resultado_filter)

# --- reduce(funcao, iterável) ---
# Aplica a função acumulativamente aos elementos (precisa importar)

from functools import reduce

def somar(a, b):
    return a + b

resultado_reduce = reduce(somar, numeros)
print("Exemplo 4 - reduce:", resultado_reduce)

# --------------------------------------------
# Funções Lambda (anônimas) com alta ordem
# --------------------------------------------

# Mesmos exemplos usando lambda
quadrados = list(map(lambda x: x ** 2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
soma_total = reduce(lambda x, y: x + y, numeros)

print("Exemplo 5 - Lambda com map:", quadrados)
print("Exemplo 6 - Lambda com filter:", pares)
print("Exemplo 7 - Lambda com reduce:", soma_total)

# --------------------------------------------
# Exemplo avançado: Função que retorna outra função
# --------------------------------------------
def saudacao(tipo):
    def mensagem(nome):
        return f"{tipo}, {nome}!"
    return mensagem

bom_dia = saudacao("Bom dia")
boa_noite = saudacao("Boa noite")

print("Exemplo 8 - Função retornando função:", bom_dia("Fabio"))
print("Exemplo 9 - Função retornando função:", boa_noite("Ana"))

# --------------------------------------------
# Boas práticas:
# - Use funções de alta ordem para deixar o código mais expressivo
# - Combine com lambda para operações simples
# - Prefira nomear funções quando a lógica for mais complexa

# Desafio: use map + lambda para multiplicar todos os números por 10
desafio = list(map(lambda x: x * 10, numeros))
print("Desafio - Multiplicados por 10:", desafio)
