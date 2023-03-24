use shersha;
create table pen(price int,brand varchar(20),year int,launch int);
insert into pen (price,brand,year,launch)
values(5,"use&throgh_pen",2010,17),
(10,"cell_open",2005,10),
(15,"gel_pen",2000,22),
(150,"parker",1990,1);

select * from pen;
# use order by query:
select brand , price , launch from pen order by launch;
select brand,price from pen order by price;
select launch , brand ,price,year from pen order by year ;

# year 

select avg(year) from pen;
select max(year) from pen;

# count query use 
select count(year) from pen;
select count(price) from pen;

select count(distinct brand) from pen
where brand like 'P%';

select count(distinct price) from pen 
where price between 0 and 40;

select count(distinct price ) from pen 
where price >100;
select * from pen;
