use bottle;
create table table1(id int,name varchar(20));
insert into table1 values(1,"shanti"),
(2,"priya");

# if you want to add coumln in existing column the use alter command ?

alter table table1 add city varchar(20);

# if you add multiple column in table ?

alter table table1 add (address varchar(20),salary int,mobile int,emp_id int);


-- drop table table1;

# if you want to remove / delete coulmn in existing table ?

alter table table1 drop emp_id;

# desc show schema / table structure :desc table_name
desc table1;

# if you want to change data type  of data?

alter table table1 modify mobile varchar(50);
alter table table1 modify mobile int;
alter table table1 modify mobile varchar(20);

# if you want to change name column : use rename column querey

alter table table1 rename column mobile to phone_number;
alter table table1 rename column phone_number to telephone_number;
alter table table1 rename column telephone_number to telephonic;

# if you want to change existing_table name to new_table name

alter table table1 rename to table2;

#desc table1; show error bcz table name change table1 to table2
desc table2;
select * from table2;

# how to add constraints : primary,foreign ,notnull ,null

alter table table2 add primary key (name);

desc table2;

