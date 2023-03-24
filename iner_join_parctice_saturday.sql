use factory;
create table andy (id int, salary int, pin int);
insert into andy (id,salary,pin)
values(102,10000,2323),
(101,15000,2424),
(103,16000,2525);
select * from andy;

create table badsha(job varchar(50), lang varchar(50),id int);
insert into badsha(job,lang,id)
values("mali","marathi",102),
("engineer","spanish",101),
("ploice","hindi",103);
select * from badsha;
#drop table andy;
select andy.id,andy.salary ,badsha.job,badsha.lang  from andy
inner join badsha
on andy.id=badsha.id;
