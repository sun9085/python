create database banking_sbi;
use banking_sbi;
create table worker1 (id int ,nave varchar(20),address varchar(20));
insert into worker1 values(1,"dinesh","pune"),
(2,"mahesh","delhi"),
(3,"amit","mumbai"),
(4,"alfaiyaj","nashik"),
(5,"sneha","bihar"),
(6,"tushar","wadki");
select * from worker1;

create table worker2(id int,age varchar(20),company varchar(20),department varchar(20));
insert into worker2 values(1,20,"tcs","hr"),
(2,25,"ACC","account"),
(3,35,"minda","maintenace"),
(4,45,"rdm","packing"),
(5,50,"nano","marketing"),
(45,55,"swiggy","service"),
(50,90,"zomato","auto");
select * from worker2;

select worker1.id,worker1.nave,worker1.address, worker2.age, worker2.company, worker2.department from worker1
left join  worker2
on worker1.id= worker2.id;