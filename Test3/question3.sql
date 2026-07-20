create DATABASE Products;
use Products;
create table Product(ProductID int,ProductName varchar(100),Category varchar(100),Price int);
insert into Product values(1,"Mouse","Electronics",800),(2,"Laptop","Electronics",65000),(3,"Chair","Furniture",4500),(4,"Keyboard","Electronics",1200);
--Write SQL queries to:
--1. Display products costing more than ₹1000.
select ProductName from Product where Price > 1000;
--2. Display all Electronics products.
select * from Product where Category="Electronics";
--3. Display the Laptop record.
select * from Product where ProductName ="Laptop";