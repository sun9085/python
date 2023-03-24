create database gg;
use gg;
create table abc(id int, game varchar(20), dist varchar(50), pin_code int(20));
insert into abc values (2,"football", "pune",41019),
(3 ,"kho kho","stara",412056),
(4,"cricket","kolhapur",41235),
(1,"tenis","solapur",415665);

select * from abc ;

create table xyz( roll_no int,nav varchar(50),age int ,id int);
insert into xyz values(25,"samir",15,4),
(26,"sima",16,3),
(27,"leena",18,2),
(44,"sagar",45,1);

select * from xyz;

select abc.id ,abc.game,abc.dist, abc.pin_code, xyz.age ,xyz.roll_no from abc
inner join xyz
on abc.id = xyz.id;


