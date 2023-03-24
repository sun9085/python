use factory;
create table shiva (id int, salary int, pin int);
insert into shiva (id,salary,pin)
values(102,10000,2323),
(101,15000,2424),
(103,16000,2525),
(108,15452,54645),
(109,45121,45124);
select * from shiva;

create table veenaji(job varchar(50), lang varchar(50),id int);
insert into veenaji (job,lang,id)
values("mali","marathi",102),
("engineer","spanish",101),
("ploice","hindi",103);
select * from veenaji;

#drop table shiva;
select shiva.id,shiva.salary ,veenaji.job,veenaji.lang  from shiva
left join veenaji
on shiva.id=veenaji.id;
