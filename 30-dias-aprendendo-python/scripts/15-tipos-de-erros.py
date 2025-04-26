# ============================================
# Tópico: Tipos de Erros em Python (Exceptions)
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# O que são erros (exceções)?
# --------------------------------------------
# São interrupções que ocorrem durante a execução do código
# causadas por problemas como divisão por zero, tipo errado, etc.

# Vamos explorar os erros mais comuns:

# --------------------------------------------
# 1. ZeroDivisionError
# --------------------------------------------
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero!")

# --------------------------------------------
# 2. NameError
# --------------------------------------------
try:
    print(nome)
except NameError:
    print("Erro: Variável 'nome' não definida!")

# --------------------------------------------
# 3. TypeError
# --------------------------------------------
try:
    resultado = "10" + 5
except TypeError:
    print("Erro: Tipos incompatíveis (str + int)!")

# --------------------------------------------
# 4. ValueError
# --------------------------------------------
try:
    numero = int("abc")
except ValueError:
    print("Erro: Valor inválido para conversão!")

# --------------------------------------------
# 5. IndexError
# --------------------------------------------
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError:
    print("Erro: Índice fora do alcance da lista!")

# --------------------------------------------
# 6. KeyError
# --------------------------------------------
try:
    dicionario = {"nome": "Fabio"}
    print(dicionario["idade"])
except KeyError:
    print("Erro: Chave inexistente no dicionário!")

# --------------------------------------------
# 7. FileNotFoundError
# --------------------------------------------
try:
    with open("arquivo_inexistente.txt", "r") as f:
        conteudo = f.read()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")

# --------------------------------------------
# 8. ImportError
# --------------------------------------------
try:
    import modulo_inexistente
except ImportError:
    print("Erro: Módulo não encontrado!")

# --------------------------------------------
# Bloco completo: try + except + else + finally
# --------------------------------------------
try:
    numero = int("10")
    print("Conversão bem-sucedida!")
except ValueError:
    print("Erro ao converter.")
else:
    print("Tudo certo no else (sem erro).")
finally:
    print("Finalizando a execução com finally.")

# --------------------------------------------
# Raise: Lançar erros manualmente
# --------------------------------------------
def dividir(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b

try:
    dividir(10, 0)
except ValueError as erro:
    print(f"Erro lançado manualmente: {erro}")

# --------------------------------------------
# Dicas finais:
# - Use try/except para capturar exceções previsíveis
# - Use else para blocos que devem rodar apenas se não houve erro
# - Use finally para executar algo sempre (ex: fechar conexões)
# - Nunca ignore exceções silenciosamente (boa prática: logar ou tratar)
