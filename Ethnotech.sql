CREATE table students(
rollno INT,
name VARCHAR(50),
course VARCHAR(30)
);

SHOW TABLES;

describe students;

INSERT INTO students VALUES
(101,'hello','python');

SELECT * FROM students;

create database employee;
use employee;

create table employees(
emp_id int,
name varchar(50),
emp_salary decimal(10,2)
);

show tables;

desc employees;
insert into employees values(1,'arun',20000);

insert into employees values
(2,'bharath',29000),
(3,'chandra',30000),
(4,'teja',42000),
(5,'mahesh',60000);
select * from employees;




create database vishnu;

CREATE table vishnu(
rollno INT,
name VARCHAR(50),
course VARCHAR(30)
);
desc vishnu;


create database hospital;
use hospital;
create table hospital(
patient_age int,
patient_name varchar(50),
patient_phone varchar(50),
paient_disease varchar(39)
);

insert into hospital values(20,'bharath',9843328248,'fever');
insert into hospital values
(21,'arun',8932756423,'headache'),
(22,'vishnu',8932756723,'stomachpain'),
(21,'arun',8932756423,'cold');

select * from hospital;


create database  E_commerce;
use  E_commerce;
CREATE TABLE product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock INT
);







