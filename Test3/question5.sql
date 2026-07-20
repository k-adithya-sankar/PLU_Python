create database hr;
use hr;
create table employee(employeeid int,name varchar(100),departmentid int);
insert into employee values(1,"Rahul",101),(2,"Priya",102),(3,"Aman",103);
create table Department(departmentid int,departmentname varchar(100));
insert into Department values(101,"It"),(102,"Hr");

-- Write an SQL query to display
-- * Employee Name
-- * Department Name
-- using an INNER JOIN.

select e.name,d.departmentname from employee as e inner join Department as d on d.departmentid=e.departmentid;