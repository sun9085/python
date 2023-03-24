use factory;
create table new(id int,name varchar(20),age int,address varchar(20),primary key(id));
insert into new (id,name,age,address)
values(1,"shree",20,"p"),
(2,"mohan",21,"m"),
(3,"shila",23,"K"),
(4,"pratik",25,"n");

select * from new;

# delete command : delete row 

delete from new where id=4;

# update command : update any value in table row

update new set age=66 where id=2;

update new set address="bhartmata" where name="shila";


