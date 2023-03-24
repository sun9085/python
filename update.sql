create database k;
use k;
create table t (id int,nav varchar(50), city varchar(20),e_id int(10));
insert into t values(1,"sunny","mumbai",12),
(2,"amit","pune",14),
(3,"shivam","nashik",15);



update t set nav="gaikwad" where e_id=15;

update t set city="delhi" where id=3;
update t set city="panjab" where id=1;
update t set city ="manali" where id=2;
select * from t;

select * from t;

# how to delete column from table 
alter table t drop column nav;

# how to add column in atble 
alter table  t add  roll_number int;

# how to modify column in current table :
# use add column in current table is called modify column.

