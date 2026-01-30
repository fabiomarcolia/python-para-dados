# ============================================
# Tópico: Manipulação de Data e Hora em Python
# Módulo: datetime
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# Importando o módulo datetime
# --------------------------------------------
import datetime

# --------------------------------------------
# 1. Obter data e hora atual
# --------------------------------------------
agora = datetime.datetime.now()
print("Data e hora atual:", agora)

# Somente a data
print("Data atual:", agora.date())

# Somente a hora
print("Hora atual:", agora.time())

# --------------------------------------------
# 2. Criar uma data/hora específica
# --------------------------------------------
data_especifica = datetime.datetime(2023, 12, 25, 15, 30)
print("Data específica:", data_especifica)

# --------------------------------------------
# 3. Adicionar ou subtrair dias, horas, etc. (timedelta)
# --------------------------------------------
amanha = agora + datetime.timedelta(days=1)
print("Amanhã:", amanha)

ontem = agora - datetime.timedelta(days=1)
print("Ontem:", ontem)

duas_horas_antes = agora - datetime.timedelta(hours=2)
print("Duas horas atrás:", duas_horas_antes)

# --------------------------------------------
# 4. Formatando datas com strftime()
# --------------------------------------------
print("Data formatada (dia/mês/ano):", agora.strftime("%d/%m/%Y"))
print("Hora formatada:", agora.strftime("%H:%M:%S"))
print("Formato completo:", agora.strftime("%d/%m/%Y %H:%M:%S"))

# --------------------------------------------
# 5. Convertendo string para data (strptime)
# --------------------------------------------
data_str = "20/04/2025 18:30"
data_convertida = datetime.datetime.strptime(data_str, "%d/%m/%Y %H:%M")
print("Data convertida de string:", data_convertida)

# --------------------------------------------
# 6. Comparação de datas
# --------------------------------------------
hoje = datetime.date.today()
data_futura = datetime.date(2025, 12, 31)

if data_futura > hoje:
    print("A data futura ainda vai chegar.")
else:
    print("A data futura já passou.")

# --------------------------------------------
# 7. Extras úteis
# --------------------------------------------
print("Dia da semana (0=Seg, 6=Dom):", hoje.weekday())
print("Nome do mês:", agora.strftime("%B"))
print("Nome do dia da semana:", agora.strftime("%A"))

# --------------------------------------------
# Desafio: calcular diferença de dias entre duas datas
# --------------------------------------------
nascimento = datetime.date(1990, 1, 1)
dias_vividos = (hoje - nascimento).days
print("Dias desde 01/01/1990:", dias_vividos)
