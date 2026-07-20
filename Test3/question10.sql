create database studentsss;
use studentsss;
create table student(studentid int,name varchar(100),courseid int);
insert into student values(1,"Rahul",201),(2,"Priya",202),(3,"Aman",101);
create table course(courseid int,coursename varchar(100));
insert into course values(201,"Python"),(202,"Java");
-- Write SQL queries to:
-- 1. Display Student Name and Course Name using an INNER JOIN.
select s.name,c.coursename from student as s inner join course as c on s.courseid=c.courseid;
-- 2. Display only students enrolled in the Python course using the WHERE
-- clause.
select s.name from student as s left join course as c on s.courseid=c.courseid where c.coursename="Python";
-- 3. Create a view named 'PythonStudents' for students enrolled in the Python
-- course.
