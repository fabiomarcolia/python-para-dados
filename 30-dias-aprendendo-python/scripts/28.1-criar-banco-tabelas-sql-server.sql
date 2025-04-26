-- ============================================
-- Criação do Banco de Dados
-- ============================================

IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'testepython')
BEGIN
    CREATE DATABASE testepython;
END
GO

USE testepython;
GO

-- ============================================
-- Criação da Tabela clientes
-- ============================================

IF OBJECT_ID('clientes', 'U') IS NOT NULL
    DROP TABLE clientes;
GO

CREATE TABLE clientes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(50) NOT NULL,
    idade INT,
    cidade NVARCHAR(50)
);
GO

-- ============================================
-- Criação da Tabela pedidos
-- ============================================

IF OBJECT_ID('pedidos', 'U') IS NOT NULL
    DROP TABLE pedidos;
GO

CREATE TABLE pedidos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    cliente_id INT,
    produto NVARCHAR(100),
    valor DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
GO

-- ============================================
-- Inserção de Dados na Tabela clientes
-- ============================================

INSERT INTO clientes (nome, idade, cidade) VALUES
('Ana', 30, 'SP'),
('Bruno', 25, 'RJ'),
('Carlos', 35, 'MG');
GO

-- ============================================
-- Inserção de Dados na Tabela pedidos
-- ============================================

INSERT INTO pedidos (cliente_id, produto, valor) VALUES
(1, 'Notebook', 2500.00),
(1, 'Mouse', 150.00),
(2, 'Teclado', 200.00),
(3, 'Monitor', 1200.00);
GO

-- ============================================
-- Verificação rápida
-- ============================================

SELECT * FROM clientes;
SELECT * FROM pedidos;


-- ============================================
-- Criar Procedure para Praticar
-- Banco: testepython
-- Tabelas: clientes e pedidos
-- Chamar no Python Exemplo:

--    cursor.execute("EXEC BuscarPedidosPorCliente @ClienteNome = ?", ("Ana",))
--      for linha in cursor.fetchall():
--       print(linha)

-- ============================================

USE testepython;
GO

-- Excluir se já existir
IF OBJECT_ID('BuscarPedidosPorCliente', 'P') IS NOT NULL
    DROP PROCEDURE BuscarPedidosPorCliente;
GO

-- Criar a Stored Procedure
CREATE PROCEDURE BuscarPedidosPorCliente
    @ClienteNome NVARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT c.nome, p.produto, p.valor
    FROM clientes c
    INNER JOIN pedidos p ON c.id = p.cliente_id
    WHERE c.nome = @ClienteNome;
END;
GO
