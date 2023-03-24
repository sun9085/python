use store_keeper;

create table ABC( id int, nav varchar(20), number int);
insert into ABC values(1,"manilal",100),
(2,"shah",200),
(3,"ghanekar",300);

select * from ABC;
create table PPT (items varchar (20), price int, city varchar(20));
insert into PPT values ("wheat",200,"pune"),
("bajri",50,"solapur");


select*from PPT;

select  ABC.id,ABC.nav,ABC.number from ABC Cross join PPT;
