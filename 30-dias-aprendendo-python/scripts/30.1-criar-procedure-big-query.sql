-- ============================================
-- Criar uma Stored Procedure no BigQuery
-- ============================================

-- No BigQuery, o conceito de Stored Procedure existe, mas é um pouco diferente do SQL Server/MySQL:

-- São chamadas de procedures (CREATE PROCEDURE) e funções (CREATE FUNCTION).

-- Você pode usar SQL Scripts e controlar fluxo (IF, LOOP, etc) dentro delas.

-- Sempre lembrar de colocar nome do projeto.dataset.nome_da_procedure no formato completo.

-- Procedures em BigQuery executam DMLs e DDLs também, não apenas SELECT.

-- Se quiser uma função (CREATE FUNCTION), seria para retornar valores diretos


-- Criando Procedure
CREATE OR REPLACE PROCEDURE `seu-projeto.testepython.BuscarClientesPorCidade`(
  cidade_param STRING
)
BEGIN
  SELECT id, nome, idade, cidade
  FROM `seu-projeto.testepython.clientes`
  WHERE cidade = cidade_param;
END;



-- Criando Função para calcular categoria de idade
-- ============================================

CREATE OR REPLACE FUNCTION `seu-projeto.testepython.CategorizarIdade`(idade INT64)
RETURNS STRING
AS (
  CASE
    WHEN idade < 18 THEN 'Menor de idade'
    WHEN idade BETWEEN 18 AND 59 THEN 'Adulto'
    ELSE 'Idoso'
  END
);

-- Como usar a função em uma consulta:

SELECT
  nome,
  idade,
  `seu-projeto.testepython.CategorizarIdade`(idade) AS categoria
FROM
  `seu-projeto.testepython.clientes`;


-- Funções não alteram dados — só transformam ou retornam valores. 
-- Você usa em SELECTs normalmente.
-- Pode chamar funções em JOINs, WHEREs, CASE WHEN, ORDER BY, etc.