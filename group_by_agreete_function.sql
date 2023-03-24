use factory;
create table emp_wipro(id int,name varchar(20),department varchar(20),salary int);
insert into emp_wipro values(100,"vikas","hr",15000),
(101,"jay","mnger",150000),
(102,"shiv","account",75000),
(103,"nana","mnger",45000),
(104,"gana","hr",80000);
select * from emp_wipro;

# group by clause means : create samll group of each entity

# wrtite query display all the department names  of emp working?

# in gruop by clause only one column name is used form group hence 
# we can use only one column first and last in syntax of group by claues.

select department from emp_wipro group by department;

# wrtite query display all the salary  names  of emp working?

select salary from emp_wipro group by salary;

# wrtite query display all the group emp_id  names  of emp working?

select id from emp_wipro group by id;

# wrtite query display all the group  names  of emp working?

select name from emp_wipro group by name;

# using agreegate function in group by claues : 
# count,max,min,sum	

select department ,count(*) from emp_wipro group by department;
select department ,count(salary) from emp_wipro group by department;
select department ,count(id) from emp_wipro group by department;
select department ,count(name) from emp_wipro group by department;

select department ,min(salary) from emp_wipro group by department;
select department , max(salary) from emp_wipro group by department;
select id , sum(salary) from emp_wipro group by id;