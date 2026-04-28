CREATE DATABASE company_db;
USE company_db;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10, 2) CHECK (salary > 0),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

SHOW TABLES;

ALTER TABLE employees
ADD hire_date DATE;

ALTER TABLE employees
MODIFY emp_name VARCHAR(150);

ALTER TABLE employees
DROP COLUMN hire_date;

CREATE INDEX idx_salary
ON employees(salary);

DROP INDEX idx_salary ON employees;

TRUNCATE TABLE employees;

DROP TABLE employees;