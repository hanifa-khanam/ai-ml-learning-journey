create database joins_sql;
use joins_sql;

create table customers (
	customer_id int primary key,
    name varchar(50),
    city varchar(50)
);
insert into customers 
values 
(1, 'Alice', 'Mumbai'),
(2, 'Bob', 'Delhi'),
(3, 'Charlie', 'Bangalore'),
(4, 'David', 'Mumbai');

create table orders (
	order_id int primary key, 
    customer_id int, 
    amount int
);

insert into orders
values
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104, 5, 700);

select * from customers;
select * from orders;

-- inner join
 select * 
 from customers c
 inner join orders o
 on c.customer_id = o.customer_id;

-- left join
select * 
from customers c
left join orders o
on c.customer_id = o.customer_id;

-- right join 
select *
from customers c
right join orders o
on c.customer_id = o.customer_id;

-- outer join 
select * 
from customers c
left join orders o
on c.customer_id = o.customer_id
union
select *
from customers c
right join orders o
on c.customer_id = o.customer_id;


-- cross join
select *
from customers
cross join orders;

-- self join
select * 
from customers as A
join customers as B
on a.customer_id = b.customer_id;


-- left exclusive join
select * 
from customers c
left join orders o
on c.customer_id = o.customer_id
where o.customer_id is null;

select * 
from customers c
right join orders o
on c.customer_id = o.customer_id
where c.customer_id is null;
 