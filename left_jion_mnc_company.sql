create database mnc_company;
use mnc_company;
create table emp4 (id int ,nave varchar(20),address varchar(20));
insert into emp4 values(1,"ramesh","pune"),
(2,"mahesh","delhi"),
(3,"satish","mumbai"),
(4,"kumar","nashik"),
(5,"rajesh","bihar"),
(6,"sunny","wadki");
select * from emp4;

create table emp5(id int,age varchar(20),company varchar(20),department varchar(20));
insert into emp5 values(1,20,"tcs","hr"),
(2,25,"wipro","account"),
(3,35,"google","maintenace"),
(4,45,"amazon","packing"),
(5,50,"hyndai","marketing"),
(12,55,"suzuki","service"),
(20,90,"uber","auto");
select * from emp5;

select emp4.id,emp4.nave,emp4.address,emp5.age,emp5.company,emp5.department from emp4
left join emp5
on emp4.id= emp5.id;


