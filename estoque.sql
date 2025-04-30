CREATE DATABASE IF NOT EXISTS bdloja;
USE bdloja;


CREATE TABLE IF NOT EXISTS Produtos (
    ProdutoID INT PRIMARY KEY AUTO_INCREMENT,
    NomeProduto VARCHAR(20),
    Quantidade INT,
    Preco FLOAT
);


INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES
("leite", 100, 7.99),
("café", 500, 19.99),
("ovo", 300, 29.99);


CREATE TABLE IF NOT EXISTS Fornecedores (
    FornecedorID INT PRIMARY KEY AUTO_INCREMENT,
    NomeFornecedor VARCHAR(50)
);


INSERT INTO Fornecedores (NomeFornecedor) VALUES
("Fornecedor A"),
("Fornecedor B");


CREATE TABLE IF NOT EXISTS Estoque (
    EstoqueID INT PRIMARY KEY AUTO_INCREMENT,
    ProdutoID INT,
    FornecedorID INT,
    Quantidade INT NOT NULL,
    DataEntrada DATE NOT NULL,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);

ALTER TABLE Estoque
ADD DataValidade DATE;


INSERT INTO Estoque (ProdutoID, FornecedorID, Quantidade, DataEntrada, DataValidade) VALUES
(1, 1, 50, '2025-04-15', '2025-05-15'), -- leite do Fornecedor A
(2, 2, 200, '2025-04-10', NULL),        -- café do Fornecedor B
(3, 1, 100, '2025-04-12', '2025-04-30'), -- ovo do Fornecedor A
(1, 2, 25, '2025-04-18', '2025-05-18');  -- leite do Fornecedor B


SELECT *
FROM Produtos
LEFT JOIN Estoque ON Produtos.ProdutoID = Estoque.ProdutoID

UNION

SELECT *
FROM Produtos
RIGHT JOIN Estoque ON Produtos.ProdutoID = Estoque.ProdutoID;


SELECT ProdutoID, SUM(Quantidade) AS TotalEstocado
FROM Estoque
GROUP BY ProdutoID;
