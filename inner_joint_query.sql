create database lodha;
use lodha;
create table sam(id int,nav varchar(20),age int,city varchar(20));
insert into sam values(100,'kambale',20,'pune'),
(101,'jadhav',21,'mumbai'),
(102,'mule',22,'pune');

select * from sam;

create table mayur(id int ,age int);
insert into mayur values(101,25),
(102,30),
(100,45);

select * from mayur;


select sam.id,sam.nav,mayur.age from sam
inner join mayur
on sam.id=mayur.id;