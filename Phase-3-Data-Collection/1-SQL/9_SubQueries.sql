use joins_sql;

-- sub-Queries
-- with where
select * 
from orders
where amount > (
	select avg(amount)
    from orders
);

-- with select
select name, (
	select count(*)
    from orders o 
    where o.customer_id = c.customer_id
) as order_count
from customers c;

-- with from
select 
summary.customer_id,
summary.avg_amount
from (
	select
    customer_id,
    avg(amount) as avg_amount
    from orders
    group by customer_id
) as summary;



select * from customers;

select name, customer_id
from customers
where customer_id % 2 = 0;

select name, customer_id
from customers
where customer_id in (
	select customer_id
    from customers
    where customer_id % 2 = 0
);
