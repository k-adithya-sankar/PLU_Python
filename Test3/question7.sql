create database employeees;
use employeees;
create table employee(employeeid int,name varchar(100),department varchar(100),salary int);
insert into employee values(1,"rahul","it",65000),(2,"priya","hr",45000),(3,"aman","it",70000);
create view highsalaryemployee where salary >60000;