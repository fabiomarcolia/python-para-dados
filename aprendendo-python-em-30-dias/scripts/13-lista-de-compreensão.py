# ============================================
# Tópico: Lista de Compreensão em Python
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# O que é uma Lista de Compreensão?
# --------------------------------------------
# É uma forma concisa e elegante de criar listas a partir de iteráveis
# em uma única linha de código — com ou sem condições.

# Sintaxe:
# nova_lista = [expressão for item in iterável if condição_opcional]

# --------------------------------------------
# Exemplo 1: Criar uma lista de números ao quadrado
# --------------------------------------------
numeros = [1, 2, 3, 4, 5]
quadrados = [n ** 2 for n in numeros]
print("Exemplo 1 - Quadrados:", quadrados)

# --------------------------------------------
# Exemplo 2: Filtrar números pares
# --------------------------------------------
pares = [n for n in numeros if n % 2 == 0]
print("Exemplo 2 - Pares:", pares)

# --------------------------------------------
# Exemplo 3: Transformar texto - colocar em maiúsculas
# --------------------------------------------
nomes = ["ana", "bruno", "carla"]
maiusculos = [nome.upper() for nome in nomes]
print("Exemplo 3 - Nomes em maiúsculas:", maiusculos)

# --------------------------------------------
# Exemplo 4: Criar pares (x, y) com dois for
# --------------------------------------------
x = [1, 2, 3]
y = [4, 5]
pares = [(i, j) for i in x for j in y]
print("Exemplo 4 - Combinações entre x e y:", pares)

# --------------------------------------------
# Exemplo 5: Lista de Compreensão com if-else
# --------------------------------------------
resultados = ["par" if n % 2 == 0 else "ímpar" for n in numeros]
print("Exemplo 5 - Par ou ímpar:", resultados)

# --------------------------------------------
# Exemplo 6: Remover espaços e converter em int
# --------------------------------------------
valores_str = [" 1", " 20", "30 "]
limpos = [int(valor.strip()) for valor in valores_str]
print("Exemplo 6 - Valores convertidos:", limpos)

# --------------------------------------------
# Exemplo 7: Criar dicionário com compreensão
# --------------------------------------------
quadrados_dict = {n: n**2 for n in range(1, 6)}
print("Exemplo 7 - Dicionário de quadrados:", quadrados_dict)

# --------------------------------------------
# Exemplo 8: Lista de listas (matriz transposta)
# --------------------------------------------
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
transposta = [[linha[i] for linha in matriz] for i in range(3)]
print("Exemplo 8 - Transposta da matriz:", transposta)

# --------------------------------------------
# Dicas de boas práticas:
# - Use list comprehensions para simplificar loops pequenos
# - Evite colocar muita lógica dentro (perde a legibilidade)
# - Quando for muito complexo, prefira loops normais

# Desafio: Crie uma lista com os quadrados dos números ímpares entre 1 e 10
desafio = [n**2 for n in range(1, 11) if n % 2 != 0]
print("Desafio - Quadrados de ímpares:", desafio)
