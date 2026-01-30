-- ============================================
-- Criação do Banco de Dados
-- ============================================

-- ✅ Esse arquivo faz:
-- Cria o banco de dados chamado testepython
-- Cria a tabela clientes com:
-- id como chave primária (auto incremento)
-- nome, idade, cidade
-- Insere dados iniciais para teste
-- Faz uma consulta final para visualizar os dados
-- Cria Procedure

-- ============================================
-- 📥 Para usar:
-- Abra o MySQL Workbench ou outro cliente de banco de dados.
-- Copie esse conteúdo ou importe o arquivo .sql ou cole o conteúdo abaixo.
-- Execute.



CREATE DATABASE IF NOT EXISTS testepython;
USE testepython;

-- ============================================
-- Criação da Tabela clientes
-- ============================================

CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    idade INT,
    cidade VARCHAR(50)
);

-- ============================================
-- Inserção de Dados Exemplo
-- ============================================

INSERT INTO clientes (nome, idade, cidade) VALUES 
('Ana', 30, 'SP'),
('Bruno', 25, 'RJ'),
('Carlos', 28, 'MG');

-- ============================================
-- Consulta para verificar
-- ============================================

SELECT * FROM clientes;


-- ============================================
-- Criação da Stored Procedure
-- ============================================

DELIMITER $$

CREATE PROCEDURE BuscarClientesPorCidade(IN cidade_param VARCHAR(50))
BEGIN
    SELECT id, nome, idade
    FROM clientes
    WHERE cidade = cidade_param;
END$$

DELIMITER ;
-- ✅ Essa procedure chamada BuscarClientesPorCidade recebe um parâmetro (cidade_param) e retorna os clientes da cidade informada.
