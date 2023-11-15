Funções de Datas

- SQL
 Treine online: https://onecompiler.com/mysql/3zte5xx3m
  
-- Converter uma string em data é importante 
-- para facilitar calculos e uso de funções específicas
SELECT DATE('2022-10-01') Data; -- Ano/Mês/Dia


---- Retorna data e Hora atual
SELECT NOW() DataNow, CURRENT_TIMESTAMP() DataSTAMP;

---- Retorna a data atual no formato YYYY-MM-DD
SELECT CURDATE() DataAtual, CURDATE() -10  as 'Voltar 10 dias';

---- Retorna a hora no formato HH:MM:SS
SELECT CURTIME() HoraAtual;

---- Retorna o ano de uma data
SELECT YEAR(NOW()) AnoDoNOW, YEAR('2022-10-01') AnoDeData;

---- Retorna o mês de uma data
SELECT MONTH(NOW()) MêsDoNOW, MONTH('2023-10-01') MêsDeData;

---- Retorna o dia de uma data
SELECT DAY(NOW()) DiaDoNOW, DAY('2023-10-01') DiaDeData;

---- Retorna a hora e o minuto de uma data/hora
SELECT HOUR(Now()) Hora ,MINUTE(Now()) Minuto;

---- Retorna a diferença em dias entre duas datas
---- Parametros é a data inicial e a final
SELECT DATEDIFF(now(),'2022-10-01');

---- Adiciona dias, mês ou anos em um data
---- Paramentros data e INTERVAL [valor] DAY|MONTH|YEAR
SELECT DATE_ADD('2022-10-01', INTERVAL 10 YEAR);

---- Remove dias, mês ou anos em um data
---- Paramentros data e INTERVAL [valor] DAY|MONTH|YEAR
SELECT DATE_SUB('2022-10-01', INTERVAL 10 YEAR);

########################################################

- PANDAS
Treine online: https://onecompiler.com/python/3ztgr9xh2	
print("Hello, World!")

## Usaremos a função print() para mostrar os resultados

import pandas as pd

## Converter String para Data
## Isso é importante para usar funções e realizar cálculos
StringParaData = (pd.to_datetime("2022-01-01"));
print("Data Atual: " + str(StringParaData));

## Data e Hora Atual
DataHoraAtual = pd.Timestamp.now();
print("Data Hora Atual: " + str(StringParaData));

## Hora Atual
Hora = pd.Timestamp.now().time();
print("Hora Atual: " + str(Hora));

## Extrair Ano de Data
Ano = pd.to_datetime("2022-01-01").year;
print("Extrair Ano de Data: " + str(Ano));

## Extrair Mês de Data
Mês= pd.to_datetime("2022-12-01").month;
print("Extrair Mês de Data: " + str(Mês));

## Extrair dia de Data
Dia= pd.to_datetime("2022-12-01").day
print("Extrair Dia de Data: " + str(Dia));

## Extrair hora de Data
Hora = pd.to_datetime(DataHoraAtual).hour
print("Extrair Hora de Data: " + str(Hora));

## Extrair minuto de Data
Minuto = pd.to_datetime(StringParaData).minute
print("Extrair Hora de Data: " + str(Minuto));

## Calcular a diferenças de dias entre datas
## Nagativos dias no futuro, positivo passado
## Só funciona com subtração
DiffDias = pd.to_datetime(StringParaData) - pd.to_datetime("2010-12-01")
print("Difença de Dias entre datas: " + str(DiffDias));

## Acrescentrar Data
## Para subtrair da data, só trocar o Sinal
dt='2022-02-25'
print(" Add Dia: " + str(pd.Timestamp(dt)+pd.DateOffset(day=15)));
print(" Add Mês: " + str(pd.Timestamp(dt)+pd.DateOffset(months=15)));
print(" Add Ano: " + str(pd.Timestamp(dt)+pd.DateOffset(years=15)));
