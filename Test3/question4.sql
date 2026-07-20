create database Customers;
use Customers;
--Tasks
--1. Create the table.
--2. Make CustomerID the Primary Key.
--==============================================
create table customer(customerid int PRIMARY KEY,customername varchar(100),city varchar(50),mobile varchar(15));
--3. Explain why Primary Keys are important
-- primary key is the key where it contains unique values,in one table there will be only one primary 
-- with primary key we can use it for indexing where we can access a particular row for updating it or deleting 
