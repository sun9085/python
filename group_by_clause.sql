create database zebra;
use zebra;
create table mt( id int, name varchar(20), deptid int ,city varchar(20),salary int);
insert into mt values(1,"shubham",12,"pune",4000),
(2,"aniket",13,"satara",5000),
(3,"vishvas",12,"viraj",1400),
(4,"sagar",13,"vai",2500);

select * from mt;

select deptid,sum(salary) as new_salary from mt group by deptid;

select name,min(salary) as min_salary from mt group by name;

select city ,avg (salary) as avg_salary from mt group by city;

select id , max(salary)as max_sal,min(salary)as min_sal,avg(salary)as avg_sal from mt group by id;




#drop database zebra;