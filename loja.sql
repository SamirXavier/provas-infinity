create database if not exists bdloja;

use bdloja;

create table if not exists Clientes (
	ID int primary key auto_increment,
	Nome varchar(50) not null,
	Idade int not null,
	Cidade varchar(25) not null
);

insert into Clientes (Nome,Idade,Cidade) values
("Samir",17,"Salvador"),
("Yan",18,"Salvador"),
("Alisson",18,"Salvador"),
("Antonio",18,"camaçari");
SELECT * FROM bdloja.Clientes;
