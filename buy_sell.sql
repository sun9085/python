create database buying;
use buying;
create table buy(id int,name varchar(20),pincode int);
insert into buy values(1,"roma",41212),
(2,"priya",412545),
(3,"akash",41251),
(4,"riya",451254),
(5,"rama",54512);

select * from buy;

create table sell(id int,city varchar(20),mobile int);
insert into sell values(1 ,"machar",989565232),
(2,"khed",8956445),
(3,"jalna",45251),
(4,"patna",4512112),
(5,"bita",78458745),
(6,"jina",89564577),
(7,"nagori",7845154),
(8,"tahne",4512451),
(9,"loni",7845278);

select * from sell;

select buy.id,buy.name,buy.pincode,sell.city,sell.mobile from buy
right join sell
on buy.id=sell.id;




