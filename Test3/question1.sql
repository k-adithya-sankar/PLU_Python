create database company;
--Question 1
--A company wants to store employee information.
--Create the following table.
use company;
create table Employee(EmployeeID int PRIMARY KEY ,EmployeeName varchar(100),Department varchar(50),Salary int,JoiningDate DATE)
