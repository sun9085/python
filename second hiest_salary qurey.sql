use factory;
create table tcs_emp(id int ,name varchar(20),dept varchar(50),salary int);
insert into tcs_emp values(1,"gnaesh","hr",45000),
(2,"mashesh","it",75000),
(3,"ramesh","comp",60000),
(4,"sanita","accoont",54450);

select * from tcs_emp;

# wtite query for max salary from employee table ?
select max(salary)from tcs_emp;

# wtite query for display name & max salary from employees?
select name ,salary from tcs_emp where salary= (select max(salary)from tcs_emp);

# wtite query for display name & min salary from employees?
select name,salary from tcs_emp where salary=(select min(salary)from tcs_emp);

# wtite query for display avg salary from employees?
select avg(salary) from tcs_emp;

# wtite query for display sum /total salary from employees?
select sum(salary) from tcs_emp ;

# wtite query for display second hiegest  salary from employees?

#1 st way
select max(salary) from tcs_emp where salary not in (select max(salary) from tcs_emp);
# 2 nd way
select max(salary) from tcs_emp where salary <>(select max(salary)from tcs_emp);


# wtite query for display name & second hiegest  salary from employees?

# with not in 

select name ,salary from tcs_emp where salary=
(select max(salary) from tcs_emp where salary not in (select max(salary )from tcs_emp));

# with <> not equal to sign

select name ,salary from tcs_emp where salary=
(select max(salary) from tcs_emp where salary <> (select max(salary )from tcs_emp));




select * from tcs_emp;
