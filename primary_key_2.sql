create database pri;
use pri;
create table  x( id int not null auto_increment ,city_nav varchar(20),primary key(id));
insert into x (city_nav)
values("pune"),
("nashik"),
("loni");
select * from x;

create table customer (id_x int , first_name varchar(20),last_name varchar(20),city int not null, primary key(id_x), foreign key(city) references x(id));
insert into y (id_x,first_name,last_name,city)
values(12,"sunny","gaikwad",3),
(13,"amar","gapat",2),
(14,"dinesh","joshi",1);

select * from y;