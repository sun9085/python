create database store_keeper;
use store_keeper;
create table dukandar1( id int, nav varchar(20), number int);
insert into dukandar1 values(1,"manilal",1),
(2,"shah",2),
(3,"ghanekar",3),
(4,"deshmukh",4);
select * from dukandar1;
create table dukandar2 (items varchar (20), price int, city varchar(20));
insert into dukandar2 values ("wheat",200,"pune"),
("bajri",50,"solapur"),
("sugar",38,"nagar"),
("besan",45,"rantangiri");
select*from dukandar2;

select  dukandar1.id,dukandar1.nav,dukandar1.number from dukandar1 Cross join dukandar2;
;