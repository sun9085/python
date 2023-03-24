create database vaibhav;
use vaibhav;
create table bharate(id int, name varchar(50),city varchar(50),pincode int);
insert into bharate values(1,"sunny","hadapsar",411013),
(2,"sunil","keshavnagar",411212),
(3,"tushar","khed",41215);

describe bharate;

select * from bharate;
update bharate set city="pune" ;

# table column
alter table bharate add addresss varchar(50);

# upadte column data
update bharate set addresss="delhi";

# delete command 
delete from bharate where id=1;
rollback;
select * from bharate;
commit;

# alter command  how to change column name 
alter table bharate rename column  name to nav;

alter table bharate rename column city to india_desh;

alter table bharate rename column pincode to area_code;

alter table bharate rename column id to emp_id;

# how to add column last in table 

alter table bharate add salary int(10);

update bharate set salary=250000;
update bharate set salary=15000 where emp_id=2;
select * from bharate;
update bharate set salary=salary*2 where emp_id=3;
update bharate  set salary =salary/2 where emp_id=2;
update bharate  set salary =salary/2 where emp_id=3;

create table vaibhav2(id int ,city varchar(50),marks int(10), foreign key(emp_id) references bharate (emp_id));
insert into vaibhav2 values(2,"junnar",100),
(1,"jejuri",89),
(3,"khadki",56);
select * from vaibhav2;
select * from bharate;
drop table vaibhav2;