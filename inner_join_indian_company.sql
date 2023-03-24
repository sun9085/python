create database indian_company;
use indian_company;
create table emp1(id int,name varchar(20));
insert into emp1 values(1,"sunny"),
(2,"ramesh"),
(3,"datta"),
(4,"mita"),
(5,"arnav");
select * from emp1;

create table emp2(id int,age int,address varchar(20),emp_salary int);
insert into emp2 values(1,20,"pune",2000),
(2,45,"nashik",4000),
(3,60,"satara",8000),
(4,75,"thane",800000),
(5,65,"loni",700000),
(6,78,"solapur",12000),
(7,85,"nagar",14000),
(8,65,"bima",5000);
select * from emp2;

select emp1.id,emp1.name ,emp2.age,emp2.address,emp2.emp_salary from emp1
inner join emp2
on emp1.id=emp2.id;