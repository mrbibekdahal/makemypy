CREATE DATABASE college;
USE college;

CREATE TABLE student(
	ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT NOT NULL	
);

INSERT INTO student
(ID,Name,Age) VALUES
(7,"CR7",41),
(10,"Messi",39),
(17,"AB De",38),
(18,"Virat",37);

SELECT * FROM Student;

CREATE DATABASE Company_XYZ;
use Company_XYZ;

CREATE TABLE Employee(
	ID INT primary key,
    Name Varchar(100),
    Salary float(3) NOT NULL
);

insert into Employee
(ID,Name,Salary) values

(1,"Adam",25000.0),
(2,"Bob",30000),
(3,"Casey",40000.07);

select * from employee;