create database if not exists bdloja;
use bdloja;



create table if not exists Produtos(
	ProdutoID int primary key auto_increment,
	NomeProduto varchar(20),
	Quantidade int,
	Preco float
);

insert into Produtos (NomeProduto,Quantidade,Preco) values
("leite",100,7.99),
("café",500,19.99),
("ovo",300,29.99);

SELECT * FROM bdloja.Produtos;

