
# primary keys for single column constrain

create database kl;
use kl;

CREATE TABLE x (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (ID)
);
insert x values(1,"gaikwad","sunny",25),
(2,"jadhav","nishikant",30),
(3,"waghmare","pavan",35);

select * from x;

#  primary keys for multiple column constrain

CREATE TABLE y (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CONSTRAINT PK_Person PRIMARY KEY (ID,LastName)
);
insert y values (14,"abc","lk",23),
(45,"ewe","rer",50),
(89,"sasa","asas",45);

select * from y;
