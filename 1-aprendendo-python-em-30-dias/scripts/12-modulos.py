# ============================================
# MÓDULOS EM PYTHON
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# O que são módulos?
# --------------------------------------------
# Módulos são arquivos Python (.py) que contêm funções, classes ou variáveis.
# Eles servem para organizar melhor o código, reaproveitar funções
# e manter tudo mais limpo em projetos maiores.

# Podemos usar:
# - Módulos internos (criados por você)
# - Módulos embutidos no Python (ex: math, random, os)
# - Módulos externos (instalados via pip, como pandas, requests)

# --------------------------------------------
# EXEMPLO 1: Usando módulos embutidos
# --------------------------------------------
import math
import random

print("Raiz quadrada de 16:", math.sqrt(16))
print("Número aleatório entre 1 e 100:", random.randint(1, 100))

# --------------------------------------------
# EXEMPLO 2: Criando e usando módulos personalizados
# --------------------------------------------
# Suponha que temos dois arquivos no mesmo diretório:
# ├── modulos_em_python.py
# ├── calculadora.py
# └── saudacoes.py

# 📄 calculadora.py
# def somar(a, b):
#     return a + b
# def dividir(a, b):
#     return a / b if b != 0 else "Erro"

# 📄 saudacoes.py
# def bom_dia(nome):
#     print(f"Bom dia, {nome}!")

# Importando tudo do módulo calculadora
import calculadora

# Importando função específica do módulo saudacoes
from saudacoes import bom_dia

print("Soma com módulo calculadora:", calculadora.somar(5, 3))
bom_dia("Fabio")

# --------------------------------------------
# EXEMPLO 3: Usando __name__ == '__main__'
# --------------------------------------------
# Isso serve para definir se o arquivo está sendo executado
# diretamente ou está sendo apenas importado como módulo.
# Veja como usar no seu próprio módulo (ex: calculadora.py):

# if __name__ == '__main__':
#     print("Executando diretamente calculadora.py")
#     print(somar(2, 2))

# No arquivo principal (modulos_em_python.py), isso não será executado
# ao importar o módulo — somente quando o módulo for rodado diretamente.

# --------------------------------------------
# RESUMO:
# - Crie arquivos separados para funções reutilizáveis
# - Importe módulos com `import` ou `from ... import ...`
# - Use `__name__ == '__main__'` para testes locais
# - Explore os módulos padrão do Python (https://docs.python.org/3/library/)
