create database mira;
use mira;
create table prachi( id int primary key ,name varchar(50));
insert into prachi values (1,"sharma"),
(2,"dhoma"),
(3,"roma"),
(4,"shona");
select * from prachi;

alter table prachi
drop primary key ;

alter table prachi
add primary key;
