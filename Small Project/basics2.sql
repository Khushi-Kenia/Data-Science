SELECT order_id, order_date, 'Active' AS status
FROM orders
WHERE order_date >= '2019-01-01'
UNION -- Combine records from multiple queries across multiple tables (no. of columns gotta be the same)
SELECT order_id, order_date, 'Archive' AS status
FROM orders
WHERE order_date <= '2019-01-01';


INSERT INTO customers
VALUES (DEFAULT, 'Jane', 'Doe', '2000-11-18', NULL, '456 ABC', 'New York', 'NY', '256');

INSERT INTO customers(first_name, last_name, birth_date, address, city, state)
VALUES ('Jane', 'Doe', '2000-11-18','456 ABC', 'New York', 'NY');
SELECT *
FROM customers;


INSERT INTO shippers(name)
VALUES('John'),
	  ('Smith');
SELECT *
FROM shippers;

INSERT INTO orders(customer_id, order_date, status)
VALUES('9', '2020-01-21', 1);
INSERT INTO order_items
VALUES(LAST_INSERT_ID(), 1, 1, 2.95),
		(LAST_INSERT_ID(), 1, 2, 3.95);
-- SELECT LAST_INSERT_ID()
SELECT *
FROM orders
