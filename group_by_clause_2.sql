create database saraswati;
use saraswati;

create table teacher1( t_id int ,t_name varchar(20),t_salary int,t_address varchar(20));
insert into teacher1 values(1,"deshmukh",75000,"vimaknnagar"),
(2,"gaikwad ",80000,"camp"),
(3,"jadhav",75000,"devli"),
(4,"kane",45000,"mumbai"),
(5,"shivtanre",50000,"pune");

select * from teacher1;

# wrtite teachers name min salary  use  group by clause?

select t_id ,min(t_salary)as min_salary from teacher1 group by t_id;

# write qurey min salary from given table using group by clause?

select t_address , min(t_salary) as min_sal from teacher1 group by t_address;

# write query all agareecate functions using group by clause?

select t_address ,min(t_salary)as mini_s,max(t_salary)as max_s,avg(t_salary)as avg_s 
from teacher1 group by t_address;

















#drop database saraswati;
