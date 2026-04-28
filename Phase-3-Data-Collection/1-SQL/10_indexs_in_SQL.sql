use employees_info;

select * from employee;

-- single index (one column)
create index idx_dep 
on employee(department);

show index from employee;

select * from employee
where department = 'IT';


-- composite index (multiple columns)
create index idx2
on employee(Salary, HireDate);

select * from employee 
where Salary < 5000;