use factory;
create table emp_wipro1(id int,name varchar(20),department varchar(20),salary int);
insert into emp_wipro1 values(100,"vikas","hr",15000),
(101,"jay","mnger",150000),
(102,"shiv","account",75000),
(103,"nana","mnger",45000),
(104,"gana","hr",80000);
select * from emp_wipro1;

# grouo by with having clause

# write query to display all the department names where no of emp less than 2?

select department from emp_wipro1 group by department having count(*)<2;