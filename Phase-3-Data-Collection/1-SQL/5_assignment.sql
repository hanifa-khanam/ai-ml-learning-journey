create database if not exists Employees_info;
use Employees_info;

create table employee (
	EmpID int primary key,
    FirstName varchar(30) not null,
    LastName varchar(30),
    Department varchar(30),
    Salary decimal(10, 2),
    HireDate date
);

insert into employee
(EmpID, FirstName, LastName, Department, Salary, HireDate)
values
(101, 'Alice', 'Johnson', 'IT', 6500, '2020-03-15'),
(102, 'Mark', 'Rivera', 'HR', 4800, '2019-07-22'),
(103, 'Sophia', 'Lee', 'Finance', 7200, '2021-01-10'),
(104, 'Daniel', 'Kim', 'IT', 5800, '2018-11-05'),
(105, 'Emma', 'Brown', 'Marketing', 5300, '2022-04-18'),
(106, 'Liam', 'Patel', 'Finance', 6900, '2020-09-29'),
(107, 'Olivia', 'Garcia', 'HR', 4600, '2017-06-30'),
(108, 'Noah', 'Thompson', 'IT', 7500, '2023-02-12'),
(109, 'Ava', 'Martinez', 'Marketing', 5100, '2019-12-02'),
(110, 'Ethan', 'Davis', 'Finance', 8000, '2016-05-14');

-- Write a query to display every employee and all their data
select * from employee;

--  List only the FirstName, LastName, and Salary of every employee
select FirstName, LastName, Salary
from employee;

--  Show all employees who work in the 'IT' department
select * from employee
where department = 'IT';

-- Retrieve employees with a salary greater than 6000
select * from employee 
where salary > 6000;

--  List all employees ordered by HireDate from newest to oldest
select * 
from employee 
order by HireDate desc;

--  Show a list of all unique departments present in the table.
select distinct Department from employee;

--  Find employees whose first name starts with ‘Aʼ
select * from employee
where FirstName like 'A%';

-- Show employees whose salaries are between 4000 and 7000
select * from employee
where salary between 4000 and 7000;

--  Find the average salary of all employees
select avg(Salary) as AverageSalary
from employee;

--  List each department along with the number of employees, but only include departments with more than 3 employees
select department, count(*) as EmployeeCount
from employee
group by department
having count(*) > 3;
 
