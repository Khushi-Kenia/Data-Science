/*USE sql_inventory;
SELECT name AS Name, unit_price AS 'Unit Price', unit_price * 1.1 AS 'New Price'
FROM products;

USE sql_store;
SELECT *
FROM orders
WHERE order_date>= '2019-01-01';

SELECT *
FROM order_items
WHERE order_id = 6 AND
	(quantity * unit_price >= 30);
    
SELECT *
FROM customers
-- WHERE first_name = 'Elka' or first_name = 'Ambur'
WHERE last_name REGEXP 'ey$|on$'
WHERE last_name REGEXP '^my|se'
WHERE last_name REGEXP 'b[ru]'

SELECT *
FROM orders
WHERE shipped_date IS NULL*/

/*USE sql_invoicing;
SELECT payments.client_id, customers.first_name, customers.last_name, payments.invoice_id, payments.date, payments.amount, pm.name AS payment_method
FROM payments
JOIN sql_store.customers ON customers.customer_id = payments.client_id
JOIN payment_methods pm ON pm.payment_method_id = payments.payment_method
ORDER BY client_id*/

SELECT customer_id, first_name, points, 'Bronze' AS type
FROM customers
WHERE points<2000
UNION
SELECT customer_id, first_name, points, 'Silver' AS type
FROM customers
WHERE points>=2000 AND points<3000
UNION 
SELECT customer_id, first_name, points, 'Gold' AS type
FROM customers
WHERE points>=3000
ORDER BY first_name

