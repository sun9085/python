create database shamitabh;
use shamitabh;
create table raj(id int,nav varchar(20),age int(10));
insert into raj values( 100,'arjun kapoor',35),
(101,'anil kapoor',65),
(103,'bachhan',75);

select * from raj;

create table mito (id int ,age int(10));
insert into mito values(102,10),
(100,12),
(101,25);

select * from mito;
 
select raj.id,raj.nav,mito.age from raj
inner join mito
on raj.id= mito.id;

# my question below mam
# Q: why id = 1002,nav =bacchan ,age 10:  is not printed in table 
 
 

