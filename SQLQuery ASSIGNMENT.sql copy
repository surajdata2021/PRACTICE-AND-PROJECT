--1, 1. Create a customer table which comprises of these columns - 'customer_id', 'first_name', 'last_name', 'email', 'addr,
create table consumer(customer_id int primary key,
                      first_name varchar(10),
                      last_name varchar(10),
                      email varchar(10),
                      adress varchar(10),
                      city varchar(10),
                      state varchar(10),
                      zip int)

--2.Insert 5 new records into the table 
insert into customer values(8,'gourav','sharma','gourav@gmail','San Jose','California','Usa',67890);
insert into customer values(1,'aman','singh','aman@gmail','NCR','Delhi','Delhi',45678); 
insert into customer values(2,'Ram','kumar','ram@gmail','Kormngla','Banglore','Karnataka',23456);
insert into customer values(3,'Alfrod','Mukesh','Alfrod@outlook','Bandra','Mumbai','Maharshtra',234589);
insert into customer values(4,'Lucid','Ivan','lucid@outlook','NY','NY','USA',156723);

--3. Select only the "first_name' & 'last_name' columns from the customer table

select first_name, last_name from customer

--4. Select those records where 'first_name' starts with "G" and city is 'San Jose' 

select * from customer where first_name like 'G%' and address = 'san jose'



--1. Create an 'Orders' table which comprises of these columns-'order_id', 'order_date', 'amount', 'customer_id 
create table orders (order_id  int primary key,
                    order_date date,
					amount int, customer_id int)
		            insert into orders values (101, '07/31/2022',1500,1); 
                    insert into orders values (102, '01/12/1972',3000,2);
                    insert into orders values (103, '05/07/1975', 2500,3);
                    insert into orders values (104, '08/15/2002',2000,6); 
                    insert into orders values (105, '11/24/2001',1300,9);

--2 Make an inner join on 'Customer' & 'Order' tables on the 'customer_id
select * from customer c 
inner join orders o 
on c.customer_id = o.customer_id

--3. Make left and right joins on 'Customer' & 'Order' tables on the 'customer_id' column
select * from customer c
left join orders o 
on c.customer_id = o. customer_id

--2 Make an inner join on Customer' & 'Order' tables on the customer_id' column
select * from customer c
inner join orders o
on c.customer_id = o. customer_id
--3. Make left and right joins on 'Customer' & 'Order' tables on the 'customer_id' column
select * from customer c 
left join orders o 
on c.customer_id = o. customer_id
select * from customer c
right join orders o 
on c.customer_id = o. customer_id


--4 Update the 'Orders' table, set the amount to be 100 where 'customer_id' is 3
update orders set amount = 100 
where customer_id = 3
select * from orders


-------------------------------------------------------------------------------MODEL 4----------------------------------------------------

--1. Use the inbuilt functions and find the minimum, maximum and average amount from the orders table
select min(amount) as min_amount, max(amount) as max_amount, avg(amount) as avg_amount from orders

--2. Create a user-defined function, which will multiply the given number with 10
 create function mul_ten(@num int)
 returns int
 as begin
 return(@num * 10)
 end
 select dbo.mul_ten(10)


 --3. Use the case statement to check if 100 is less than 200, greater than 200 or equal to 200 and print the corresponding
select
case 
when 100>200 then '100 is smaller than 200'
when 100<200 then '100 is greater than 200'
else '100=200'
end
------------------------------------------------finish--------------------------------