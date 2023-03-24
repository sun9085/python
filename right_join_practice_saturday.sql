use factory;
create table shiv (id int, salary int, pin int);
insert into shiv (id,salary,pin)
values(102,10000,2323),
(101,15000,2424),
(103,16000,2525);
select * from shiv;

create table veena(job varchar(50), lang varchar(50),id int);
insert into veena (job,lang,id)
values("mali","marathi",102),
("engineer","spanish",101),
("ploice","hindi",103),
("teacher","telgu",105);
select * from veena;


select shiv.id,shiv.salary ,veena.job,veena.lang  from shiv
right join veena
on shiv.id=veena.id;
