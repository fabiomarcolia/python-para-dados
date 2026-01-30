# Strings em Python
'''
O que são Strings?
Strings são sequências de caracteres em Python. Elas são usadas para representar texto
e são um dos tipos de dados mais comuns e úteis na programação. Em Python, strings são
imutáveis, o que significa que não podem ser alteradas após a criação.
'''

print("=== STRINGS EM PYTHON ===\n")

# 1. Criando Strings
print("1. CRIANDO STRINGS")
print("Strings podem ser criadas usando aspas simples, duplas ou triplas.")

string1 = 'String com aspas simples'
string2 = "String com aspas duplas"
string3 = '''String com aspas 
triplas que pode ocupar 
múltiplas linhas'''
string4 = """Outra string 
com aspas triplas duplas"""

print(f"string1: {string1}")
print(f"string2: {string2}")
print(f"string3: {string3}")
print(f"string4: {string4}")

# 2. Acessando caracteres em Strings
print("\n2. ACESSANDO CARACTERES EM STRINGS")
print("Strings são sequências indexadas, começando em 0.")

texto = "Python"
print(f"texto: {texto}")
print(f"texto[0]: {texto[0]}")    # P
print(f"texto[1]: {texto[1]}")    # y
print(f"texto[-1]: {texto[-1]}")  # n (índice negativo: conta a partir do final)
print(f"texto[-2]: {texto[-2]}")  # o

# 3. Fatiamento (Slicing) de Strings
print("\n3. FATIAMENTO (SLICING) DE STRINGS")
print("Podemos obter partes de uma string usando a sintaxe [início:fim:passo].")

mensagem = "Aprendendo Python"
print(f"mensagem: {mensagem}")
print(f"mensagem[0:10]: {mensagem[0:10]}")      # Aprendendo
print(f"mensagem[11:]: {mensagem[11:]}")        # Python
print(f"mensagem[:10]: {mensagem[:10]}")        # Aprendendo
print(f"mensagem[::2]: {mensagem[::2]}")        # Arned yhn (pula 2 caracteres)
print(f"mensagem[::-1]: {mensagem[::-1]}")      # nohtyP odnednerpA (inverte a string)

# 4. Propriedades das Strings
print("\n4. PROPRIEDADES DAS STRINGS")

# Comprimento (length)
print(f"len(mensagem): {len(mensagem)}")        # 17

# Imutabilidade
print("Strings são imutáveis (não podem ser alteradas depois de criadas)")
try:
    mensagem[0] = 'a'  # Isso causará um erro
except TypeError as e:
    print(f"Erro ao tentar modificar a string: {e}")

# 5. Métodos de Strings
print("\n5. MÉTODOS DE STRINGS")
print("Python oferece muitos métodos úteis para manipular strings.")

texto = "  Python é uma Linguagem de Programação  "
print(f"texto original: '{texto}'")

# Métodos de transformação
print(f"\nMétodos de transformação:")
print(f"texto.upper(): '{texto.upper()}'")          # Converte para maiúsculas
print(f"texto.lower(): '{texto.lower()}'")          # Converte para minúsculas
print(f"texto.strip(): '{texto.strip()}'")          # Remove espaços em branco no início e fim
print(f"texto.replace('Python', 'Java'): '{texto.replace('Python', 'Java')}'") # Substitui texto

# Métodos de divisão e junção
print(f"\nMétodos de divisão e junção:")
palavras = texto.strip().split(' ')  # Divide a string em uma lista de palavras
print(f"texto.split(' '): {palavras}")
print(f"'-'.join(['a', 'b', 'c']): {''.join(['a', 'b', 'c'])}")  # Junta strings com um separador

# Métodos de busca
print(f"\nMétodos de busca:")
print(f"texto.find('Python'): {texto.find('Python')}")  # Retorna o índice ou -1 se não encontrar
print(f"texto.count('a'): {texto.count('a')}")          # Conta ocorrências
print(f"'Python' in texto: {'Python' in texto}")        # Verifica se contém

# Métodos de verificação
print(f"\nMétodos de verificação:")
print(f"'123'.isdigit(): {'123'.isdigit()}")                 # Verifica se só tem dígitos
print(f"'abc'.isalpha(): {'abc'.isalpha()}")                 # Verifica se só tem letras
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")           # Verifica se só tem letras e números
print(f"'Python'.startswith('Py'): {'Python'.startswith('Py')}")  # Verifica se começa com
print(f"'Python'.endswith('on'): {'Python'.endswith('on')}")      # Verifica se termina com

# 6. Formatação de Strings
print("\n6. FORMATAÇÃO DE STRINGS")
print("Python oferece várias formas de formatar strings.")

nome = "Ana"
idade = 25

# Método format()
print("\nUsando método format():")
mensagem = "Olá, {}! Você tem {} anos.".format(nome, idade)
print(mensagem)

# Com f-strings (a partir do Python 3.6)
print("\nUsando f-strings:")
mensagem = f"Olá, {nome}! Você tem {idade} anos."
print(mensagem)

# Formatação avançada com f-strings
preco = 49.99
print(f"Preço: R$ {preco:.2f}")  # Formata com 2 casas decimais
print(f"Temperatura: {23.5:.1f}°C")  # Formata com 1 casa decimal

# 7. Operações com Strings
print("\n7. OPERAÇÕES COM STRINGS")

# Concatenação
print("\nConcatenação:")
primeiro_nome = "João"
sobrenome = "Silva"
nome_completo = primeiro_nome + " " + sobrenome
print(f"primeiro_nome + ' ' + sobrenome: {nome_completo}")

# Repetição
print("\nRepetição:")
simbolo = "-="
linha = simbolo * 10
print(f"simbolo * 10: {linha}")

# 8. Escape Characters (Caracteres de Escape)
print("\n8. CARACTERES DE ESCAPE")
print("São caracteres especiais precedidos por \\.")

print("Nova linha: Linha 1\\nLinha 2")
print("Nova linha: Linha 1\nLinha 2")

print("Tabulação: Item 1\\tItem 2")
print("Tabulação: Item 1\tItem 2")

print("Aspas dentro de aspas: \"Python\"")
print("Aspas dentro de aspas: \"Python\"")

print("Barra invertida: C:\\Usuarios\\Nome")
print("Barra invertida: C:\\Usuarios\\Nome")

# 9. Convertendo entre Strings e outros tipos
print("\n9. CONVERTENDO ENTRE STRINGS E OUTROS TIPOS")

# String para número
numero_texto = "42"
numero_inteiro = int(numero_texto)
print(f"int('42'): {numero_inteiro} (tipo: {type(numero_inteiro)})")

numero_texto = "3.14"
numero_float = float(numero_texto)
print(f"float('3.14'): {numero_float} (tipo: {type(numero_float)})")

# Número para string
idade = 30
idade_texto = str(idade)
print(f"str(30): {idade_texto} (tipo: {type(idade_texto)})")

# 10. Raw Strings
print("\n10. RAW STRINGS")
print("Strings que ignoram caracteres de escape.")

caminho_normal = "C:\\Pasta\\Arquivo.txt"
caminho_raw = r"C:\Pasta\Arquivo.txt"

print(f"String normal: {caminho_normal}")
print(f"Raw string: {caminho_raw}")

# 11. Unicode e caracteres especiais
print("\n11. UNICODE E CARACTERES ESPECIAIS")

print("Símbolos: ♥ ★ ● ◆ ◉")
print("Emojis: 😀 🐍 🚀 🎉")
print("Acentos: áéíóú ãẽĩõũ âêîôû ç")