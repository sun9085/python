CREATE DATABASE MANAPUARAM;
 use MANAPUARAM ;

create table ACTOR( id int, nav varchar(20), number int);
insert into ACTOR values(1,"SHARUKH",75000),
(2,"SALMAN",45000),
(3,"AMIR",25000);

select * from ACTOR;
create table FILMS (items varchar (20), price int, city varchar(20));
insert into FILMS values ("DON",200,"pune"),
("BAJRANGI",50,"solapur");


select*from FILMS;

select  ACTOR.id,ACTOR.nav,ACTOR.number from ACTOR Cross join FILMS;
