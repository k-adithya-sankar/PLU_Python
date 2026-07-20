create database books;
use books;
create table book(bookid int,bookname varchar(100),author varchar(100),price int);
insert into book values(1,"pythonbasics","john",500),(2,"learningsql","david",700);
delimiter//
create procedure getbooks
    @booksr VARCHAR(100)
as
begin
    select *
    from book
    where bookname = @booksr;
end //
delimiter ;