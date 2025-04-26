# ============================================
# Tópico: Expressões Regulares (RegEx) em Python
# Módulo: re
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# O que são expressões regulares?
# --------------------------------------------
# São padrões para busca e manipulação de strings.
# Usadas para validar, extrair ou substituir partes de textos.

import re

# --------------------------------------------
# 1. Procurar um padrão simples com search()
# --------------------------------------------
texto = "Meu e-mail é fabio.marcolia@gmail.com"
padrao = r"\w+@\w+\.\w+"

resultado = re.search(padrao, texto)
if resultado:
    print("Exemplo 1 - E-mail encontrado:", resultado.group())

# --------------------------------------------
# 2. Encontrar todos os padrões com findall()
# --------------------------------------------
texto2 = "Os CEPs são 12345-678 e 98765-432"
ceps = re.findall(r"\d{5}-\d{3}", texto2)
print("Exemplo 2 - CEPs encontrados:", ceps)

# --------------------------------------------
# 3. Substituir parte do texto com sub()
# --------------------------------------------
texto3 = "CPF: 111.222.333-44"
texto_oculto = re.sub(r"\d{3}\.\d{3}\.\d{3}-\d{2}", "***.***.***-**", texto3)
print("Exemplo 3 - Texto com CPF ocultado:", texto_oculto)

# --------------------------------------------
# 4. Validar formatos (e-mails, senhas, etc.)
# --------------------------------------------
email = "usuario123@gmail.com"
padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(padrao_email, email):
    print("Exemplo 4 - E-mail válido!")
else:
    print("E-mail inválido!")

# --------------------------------------------
# 5. Dividir string com split()
# --------------------------------------------
frase = "Palavras,separadas;por:diversos|delimitadores"
palavras = re.split(r"[ ,;:|]+", frase)
print("Exemplo 5 - Palavras divididas:", palavras)

# --------------------------------------------
# 6. Grupos com parênteses
# --------------------------------------------
data = "Data de nascimento: 20/04/1990"
match = re.search(r"(\d{2})/(\d{2})/(\d{4})", data)

if match:
    dia, mes, ano = match.groups()
    print(f"Exemplo 6 - Dia: {dia}, Mês: {mes}, Ano: {ano}")

# --------------------------------------------
# Dicionário rápido dos símbolos mais usados:
# \d  → qualquer dígito (0-9)
# \w  → qualquer caractere alfanumérico (a-z, A-Z, 0-9, _)
# \s  → qualquer espaço em branco
# .   → qualquer caractere (exceto nova linha)
# +   → uma ou mais ocorrências
# *   → zero ou mais ocorrências
# ?   → zero ou uma ocorrência
# ^   → início da string
# $   → fim da string
# []  → conjunto de caracteres
# ()  → grupos

# --------------------------------------------
# Desafio: Valide uma senha com pelo menos:
# - 8 caracteres
# - Uma letra maiúscula
# - Um número

senha = "Senha123"
padrao_senha = r"^(?=.*[A-Z])(?=.*\d).{8,}$"

if re.match(padrao_senha, senha):
    print("Desafio - Senha válida!")
else:
    print("Desafio - Senha inválida!")
