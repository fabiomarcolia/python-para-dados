# ============================================
# Tópico: Estatística Básica em Python
# Biblioteca: statistics
# Autor: Fabio Marçolia
# ============================================

import statistics

# --------------------------------------------
# 1. Conjunto de dados para análise
# --------------------------------------------
dados = [10, 12, 15, 18, 18, 21, 25, 25, 25, 30]

# --------------------------------------------
# 2. Média (mean)
# --------------------------------------------
media = statistics.mean(dados)
print("Média:", media)

# --------------------------------------------
# 3. Mediana (median)
# --------------------------------------------
mediana = statistics.median(dados)
print("Mediana:", mediana)

# --------------------------------------------
# 4. Moda (mode)
# --------------------------------------------
moda = statistics.mode(dados)
print("Moda:", moda)

# --------------------------------------------
# 5. Desvio padrão (standard deviation)
# --------------------------------------------
desvio_padrao = statistics.stdev(dados)
print("Desvio padrão:", round(desvio_padrao, 2))

# --------------------------------------------
# 6. Variância
# --------------------------------------------
variancia = statistics.variance(dados)
print("Variância:", round(variancia, 2))

# --------------------------------------------
# 7. Média Harmônica
# --------------------------------------------
media_harmonica = statistics.harmonic_mean(dados)
print("Média Harmônica:", round(media_harmonica, 2))

# --------------------------------------------
# 8. Média Geométrica (com math.prod em Python >= 3.8)
# --------------------------------------------
import math

produto = math.prod(dados)
media_geometrica = produto ** (1 / len(dados))
print("Média Geométrica:", round(media_geometrica, 2))

# --------------------------------------------
# 9. Medidas adicionais (mínimo, máximo, amplitude)
# --------------------------------------------
minimo = min(dados)
maximo = max(dados)
amplitude = maximo - minimo

print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Amplitude:", amplitude)

# --------------------------------------------
# Desafio: Crie uma função que receba uma lista de valores
# e retorne um dicionário com as principais estatísticas
# --------------------------------------------
def resumo_estatistico(lista):
    return {
        "média": statistics.mean(lista),
        "mediana": statistics.median(lista),
        "moda": statistics.mode(lista),
        "mínimo": min(lista),
        "máximo": max(lista),
        "amplitude": max(lista) - min(lista),
        "desvio padrão": round(statistics.stdev(lista), 2),
        "variância": round(statistics.variance(lista), 2)
    }

resumo = resumo_estatistico(dados)
print("\nResumo estatístico:", resumo)
