--Question2
--
create table Student(StudentID int,Name varchar(100),Course Varchar(100),Marks int);

insert into Student values(101,"Rahul","Python",80),(102,"Priya","Java",75),(103,"Aman","Python",90),(104,"Neha","SQL",70);
--Write SQL queries to:
--1. Display all student records.
select * from Student;
--2. Display only Name and Marks.
select Name,Marks from Student;
--3. Display only the Course column.
select Course from Student;