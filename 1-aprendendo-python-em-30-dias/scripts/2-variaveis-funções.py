# Variáveis em Python

'''
O que são variáveis?
Variáveis são espaços na memória utilizados para armazenar dados. Em Python, as variáveis 
são criadas quando atribuímos um valor a elas. Não precisamos declarar o tipo de variável
previamente, pois Python é uma linguagem de tipagem dinâmica.

Algumas regras para nomear variáveis em Python:
- Podem conter letras, números e underscore (_)
- Não podem começar com um número
- Não podem ser palavras reservadas (como 'if', 'for', 'while', etc.)
- São sensíveis a maiúsculas e minúsculas (case-sensitive)
'''


primeiro_nome = 'Fabio'
sobrenome = 'Marçolia'
pais = 'Brasil'
cidade = 'São Paulo'
idade = 120
casado = True
habilidades = ['SQL', 'Python', 'Power BI', 'Modelagem', 'Cloud', 'IA']
info_pessoa = {
    'Formação':'Análise de Sistema', 
    'MBA':'Big Data Aplicado ao Marketing', 
    'Instituição':'ESPM',
    'Linkedin':'https://www.linkedin.com/in/fabiomarcolia/'
    }
# Imprimindo os valores armazenados nas variáveis
print('Nome:', primeiro_nome)
print('Tamanho do nome:', len(primeiro_nome))
print('Sobrenome:', sobrenome)
print('Tamanho do sobrenome:', len(sobrenome))
print('País:', pais)
print('Cidade:', cidade)
print('Idade:', idade)
print('Casado:', casado)
print('Habilidades:', habilidades)
print('Informações da pessoa:', info_pessoa)

# Declarando múltiplas variáveis em uma linha
primeiro_nome, sobrenome, pais, idade, casado = 'Asabeneh', 'Yetayeh', 'Helsinki', 250, True
print(primeiro_nome, sobrenome, pais, idade, casado)
print('Nome:', primeiro_nome)
print('Sobrenome:', sobrenome)
print('País:', pais)
print('Idade:', idade)
print('Casado:', casado)


'''
Funções Embutidas (Built-in Functions) em Python

Python possui várias funções embutidas que estão sempre disponíveis para uso.
Algumas das principais funções embutidas são:
'''

# print() - Exibe informações na tela
print("\n--- Exemplos de funções embutidas ---")
print("Esta é a função print() em ação!")

# len() - Retorna o tamanho (número de itens) de um objeto
texto = "Python"
minha_lista = [1, 2, 3, 4, 5]
print(f"Tamanho do texto '{texto}': {len(texto)}")
print(f"Tamanho da lista {minha_lista}: {len(minha_lista)}")

# type() - Retorna o tipo de um objeto
print(f"Tipo de {texto}: {type(texto)}")
print(f"Tipo de {idade}: {type(idade)}")
print(f"Tipo de {casado}: {type(casado)}")
print(f"Tipo de {habilidades}: {type(habilidades)}")

# int(), float(), str() - Conversão entre tipos
numero_str = "10"
print(f"Convertendo string para int: {numero_str} → {int(numero_str)}")
print(f"Convertendo int para float: {idade} → {float(idade)}")
print(f"Convertendo int para string: {idade} → {str(idade)}")

# input() - Recebe entrada do usuário (comentado para não interromper a execução)
# nome_usuario = input("Digite seu nome: ")
# print(f"Olá, {nome_usuario}!")

# min(), max() - Retorna o valor mínimo e máximo
numeros = [10, 5, 23, 7, 42, 3]
print(f"Valor mínimo da lista {numeros}: {min(numeros)}")
print(f"Valor máximo da lista {numeros}: {max(numeros)}")

# sum() - Soma todos os itens de uma sequência
print(f"Soma dos valores da lista {numeros}: {sum(numeros)}")

# sorted() - Retorna uma nova lista ordenada
print(f"Lista ordenada: {sorted(numeros)}")
print(f"Lista ordenada decrescente: {sorted(numeros, reverse=True)}")

# round() - Arredonda um número
pi = 3.14159
print(f"Arredondando {pi} para 2 casas decimais: {round(pi, 2)}")

# abs() - Retorna o valor absoluto
negativo = -42
print(f"Valor absoluto de {negativo}: {abs(negativo)}")

# range() - Cria uma sequência de números
print("Range de 5 números:", list(range(5)))
print("Range de 2 a 8:", list(range(2, 8)))
print("Range de 1 a 10 com passo 2:", list(range(1, 10, 2)))

# help() - Fornece ajuda sobre um objeto
# Descomente para ver a ajuda sobre a função print
# help(print)

# dir() - Lista os atributos de um objeto
print(f"Alguns métodos disponíveis para strings: {dir(texto)[:5]}")

# isinstance() - Verifica se um objeto é de um determinado tipo
print(f"'texto' é uma string? {isinstance(texto, str)}")
print(f"'idade' é um float? {isinstance(idade, float)}")