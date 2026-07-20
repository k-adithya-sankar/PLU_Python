create database students;
use students;
create table student(studentid int,name varchar(100),courseid int);
insert into student values(1,"Rahul",201),(2,"Priya",202),(3,"Aman",NULL);
create table course(courseid int,coursename varchar(100));
insert into course values(201,"Python"),(202,"Sql");

-- Write an SQL query to display all students along with their course names
-- using a LEFT JOIN.
select s.name,c.coursename from student as s left join course as c on s.courseid=c.courseid;