# ============================================
# Tópico: Condicionais em Python (if, elif, else)
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# O que são condicionais?
# --------------------------------------------
# Condicionais são estruturas que permitem que o programa
# tome decisões com base em condições. Usamos "if", "elif" e "else".

# Exemplo 1: Usando IF
idade = 20

if idade >= 18:
    print("Você é maior de idade.")  # Esse bloco será executado
print("Fim do exemplo 1.\n")

# --------------------------------------------
# Exemplo 2: IF e ELSE
# --------------------------------------------
nota = 6

if nota >= 7:
    print("Aprovado!")
else:
    print("Reprovado.")
print("Fim do exemplo 2.\n")

# --------------------------------------------
# Exemplo 3: IF, ELIF e ELSE
# --------------------------------------------
temperatura = 30

if temperatura < 15:
    print("Está frio.")
elif temperatura < 25:
    print("Clima agradável.")
else:
    print("Está calor.")
print("Fim do exemplo 3.\n")

# --------------------------------------------
# Exemplo 4: Condicional com múltiplas condições (AND, OR)
# --------------------------------------------
usuario_logado = True
tem_permissao = False

if usuario_logado and tem_permissao:
    print("Acesso autorizado.")
else:
    print("Acesso negado.")
print("Fim do exemplo 4.\n")

# --------------------------------------------
# Exemplo 5: Usando condicional dentro de uma função
# --------------------------------------------
def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

print("Exemplo 5:", verificar_par_ou_impar(7), "\n")

# --------------------------------------------
# Exemplo 6: Expressão condicional em uma linha (ternário)
# --------------------------------------------
idade = 16
mensagem = "Pode dirigir." if idade >= 18 else "Não pode dirigir."
print("Exemplo 6:", mensagem)

# --------------------------------------------
# Dica Extra:
# --------------------------------------------
# Tome cuidado com a indentação! O Python usa indentação
# (espaços/tabs) para definir blocos de código.

# Experimente mudar os valores e observar os resultados!
