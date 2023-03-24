create database factory;
use factory ;
create table wk1 (id int,nav varchar(20),salary int);
insert into wk1 values(1,"sharma",15000),
(2,"khurana",20000),
(3,"pandit",12000);
select * from wk1;
create table wk2(age int, mobile int,lang varchar(20),wk_id int);
insert into wk2 values(20,89856,"panjabi",3),
(45,568956,"bihari",2),
(50,451254,"asami",1);
select * from wk2;
select wk1.id as new_id,wk1.nav as name_worker,wk1.salary as new_salary,wk2.age as new_age
,wk2.mobile as mb_no,wk2.wk_id as w_id from wk1 ,wk2 
where wk1.id = wk2.wk_id;
