create database order;
use order;
--1. Create an index on OrderID.

create table orders(orderid int PRIMARY KEY,customername varchar(100),orderdate DATE,amount int);
--Explain one benefit of creating an index
-- using index we cna access any particular row for updating or deleting or doing crud function
