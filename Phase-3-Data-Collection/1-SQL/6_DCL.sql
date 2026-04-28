create database company_db;
use company_db;

create table employees (
	id int primary key,
    name varchar(100), 
    department varchar(50),
    salary decimal(10, 2)
);

create user 'analyst'@'localhost' identified by 'analyst123';
create user 'ml_engineer'@'localhost' identified by 'ml123';

grant select on company_db.employees to 'analyst'@'localhost';

grant select, insert on company_db.employees to 'ml_engineer'@'localhost';

-- apply changes
flush privileges;

-- revoke permission
revoke select on company_db.employees from 'analyst'@'localhost';


CREATE ROLE data_scientist;
GRANT SELECT ON company_db.* TO data_scientist;
GRANT data_scientist TO 'hanifa'@'localhost';
