create database truck_driver;
use truck_driver;
create table emp10 (id int, nav varchar(20),mobile int(50));
insert into emp10 values(1,"kambale",98655898),
(2,"sutar",989566),
(3,"more",865654784),
(4,"sane",895645122);

select * from emp10;

create table epm55 (id int , age varchar(20),city varchar(50));
insert into emp55 values(1,20,"pune"),
(2,21,"delhi"),
(3,22,"panjab"),
(4,23,"mp"),
(5,24,"hp"),
(6,25,"uk"),
(7,26,"hr");
select * from emp55;

select emp10.id,emp10.nav,emp10.mobile,emp55.age,emp55.city from emp10
right join emp55
on emp10.id=emp55.id;



