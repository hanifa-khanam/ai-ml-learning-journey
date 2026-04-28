create database if not exists college;
use college;

create table Teacher(
	id int primary key,
    name varchar(100),
    subject varchar(100),
    salary int
);

insert into Teacher 
(id, name, subject, salary)
values
(23, 'ajay', 'math', 50000),
(47, 'bharat', 'english', 60000),
(18, 'chetan', 'chemistry', 45000),
(9, 'divya', 'physics', 75000);


select * from Teacher
where salary > 55000;

alter table Teacher
rename column salary to ctc;

update Teacher
set ctc = ctc + ctc * 0.25;

alter table Teacher
add column city varchar(50) default "Gurgaon";

alter table Teacher
drop column ctc;

select * from teacher;



set SQL_SAFE_UPDATES = 0;

create table Student (
	roll_no int primary key,
    name varchar(50),
    city varchar(50),
    marks int
);

insert into Student
(roll_no, name, city, marks)
values
(110, 'adam', 'Delhi', 76),
(108, 'bob', 'Mumbai', 65),
(124, 'casey', 'Pune', 94),
(112, 'duke', 'Pune', 80);

select * from Student
where marks > 75;

select distinct city from Student;

select city 
from student
group by city;

select city, max(marks)
from Student
group by city;

select avg(marks)
from Student;

alter table Student
add column grade varchar(2);

update Student
set grade = "0"
where marks >= 80;

update Student
set grade = "A"
where marks between 70 and 80;

update Student
set grade = "B"
where marks between 60 and 70;


select * from Student;