# ============================================
# Tópico: Tratamento de Exceções em Python
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# 1. O que é uma exceção?
# --------------------------------------------
# É um erro que ocorre durante a execução do programa
# e pode ser tratado para evitar que o programa pare inesperadamente.

# --------------------------------------------
# 2. Estrutura básica do try/except
# --------------------------------------------
try:
    numero = int(input("Digite um número inteiro: "))
    print("Você digitou:", numero)
except ValueError:
    print("Erro: Valor inválido! Digite um número inteiro.")

# --------------------------------------------
# 3. Vários tipos de exceção (multiplos excepts)
# --------------------------------------------
try:
    a = int("abc")        # ValueError
    b = 10 / 0            # ZeroDivisionError
except ValueError:
    print("Erro: Conversão inválida.")
except ZeroDivisionError:
    print("Erro: Divisão por zero.")
except Exception as e:
    print("Erro genérico:", e)

# --------------------------------------------
# 4. Usando else e finally
# --------------------------------------------
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Erro ao dividir.")
else:
    print("Divisão realizada com sucesso:", resultado)
finally:
    print("Finalizando a execução do bloco try/except.\n")

# --------------------------------------------
# 5. Capturando o erro como variável
# --------------------------------------------
try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError as erro:
    print("Erro de índice:", erro)

# --------------------------------------------
# 6. Criando e lançando exceções com raise
# --------------------------------------------
def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

try:
    print(dividir(10, 0))
except ValueError as erro:
    print("Erro capturado com raise:", erro)

# --------------------------------------------
# 7. Criando sua própria exceção personalizada
# --------------------------------------------
class ErroNegativo(Exception):
    """Exceção lançada quando o valor é negativo."""
    pass

def validar_positivo(x):
    if x < 0:
        raise ErroNegativo("Número negativo não permitido.")
    return x

try:
    validar_positivo(-5)
except ErroNegativo as erro:
    print("Erro personalizado:", erro)

# --------------------------------------------
# Dicas de boas práticas:
# - Use exceções específicas sempre que possível
# - Nunca capture erros sem tratar: evite "except:" sozinho
# - Use "finally" para fechar arquivos, conexões, etc.
# - Evite esconder erros silenciosamente

# --------------------------------------------
# Desafio:
# Crie uma função que abre um arquivo e leia seu conteúdo
# Trate: FileNotFoundError e erros genéricos
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Arquivo não encontrado!"
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"
    finally:
        print("Tentativa de leitura concluída.")

print("\nDesafio:", ler_arquivo("inexistente.txt"))
