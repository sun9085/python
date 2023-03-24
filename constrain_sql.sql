#UNIQUE Constraint : meaning  all values in  column are uniqe.
create database u;
use u;

CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    UNIQUE (ID)
);

select * from persons;

# for multiple column  unique constrains :


CREATE TABLE person2 (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CONSTRAINT UC_Person2 UNIQUE (ID,LastName)
);

select * from person2;

CREATE TABLE person4 (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CONSTRAINT UC_Person4 UNIQUE (ID,LastName)
);
select * from person4;

# UNIQUE Constraint on ALTER TABLE;
ALTER TABLE Person4
ADD UNIQUE (ID);

select * from person4;