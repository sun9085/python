use dhoni;
create table RRR (id int not null auto_increment , nav varchar(50),age int,run int,primary key(id));
insert into RRR (nav,age,run)
values("sachin",40,1000),
("ashwin",35,200),
("virat",32,999),
("yuraj",30,500),
("ashwin",35,200),
("virat",32,999),
("yuraj",30,500),
("ashwin",35,200),
("virat",32,999),
("yuraj",30,500);

select * from RRR;

# use group by command 

select id,nav from RRR group by id;

select age , max(run) from RRR group by age;

select nav, min(run) from RRR group by nav;

# find specific name from table 
select distinct nav from RRR;

select nav,sum(run) from RRR  group by nav;

select age,min(run) from RRR group by age;

# having clause 

select nav ,max(run) from RRR group by nav 
having nav in ("sachin","virat");

select age , min(run) from RRR group by age
having age between 25 and 35;

select min(age) from RRR;
select max(age) from RRR;
select avg(age)from RRR;

# name start with S initial:
select run ,nav from RRR where nav like 'S%' ;

# name  x charatctor  middle in string:
select age,nav, run from RRR where nav like '_n%';

# age access by age column:
select age,run from RRR where age =35;

# using between operator:
select nav,id from RRR where id between 0 and 5;
select nav,id from RRR where id between 2 and 3;

select * from RRR;

#  find max run in table :
select max(run) from RRR;

# find second last max run in table :
select max(run) from RRR where run not in (select max(run) from RRR);

# we can use that having function after agreegate function;

select nav,max(run) from RRR group by nav
having max(run) >920;

# group by and having func
select age, min(run) from RRR group by age
having min(run)<600;
