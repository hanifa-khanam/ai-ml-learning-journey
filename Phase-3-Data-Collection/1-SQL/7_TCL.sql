create database ai_ml;
use ai_ml;

create table accounts (
	id int primary key auto_increment,
    name varchar(50),
    balance decimal(10, 2)
);

insert into accounts (name, balance)
values
('Adam', 500.00),
('Bob', 300.00),
('Charlie', 1000.00);


select * from accounts;

select @@autocommit;
set autocommit = 0;

-- transactions commit

start transaction;
update accounts set balance = balance - 50 where id = 1;
update accounts set balance = balance + 50 where id = 2;
commit;


-- rollback
start transaction;
update accounts set balance = balance - 50 where id = 1;
update accounts set balance = balance + 50 where id = 2;
rollback;

-- savepoints
start transaction;
update accounts set balance = balance + 1000 where id = 1;
savepoint after_wallet_topup;

update accounts set balance = balance + 10 where id = 1;
rollback to after_wallet_topup;
commit;
