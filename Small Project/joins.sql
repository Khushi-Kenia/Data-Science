/*SELECT orders.customer_id, first_name, last_name
FROM orders
INNER JOIN customers 
	ON orders.customer_id = customers.customer_id;*/
    
-- JOINING ACROSS DATABASES
/*USE sql_store;
SELECT *
FROM order_items oi
JOIN sql_inventory.products
	ON oi.product_id = products.product_id*/

/*USE sql_hr;
-- SELECT *
SELECT e.employee_id, e.first_name, e.last_name, m.first_name AS 'Manager'
FROM employees e
JOIN employees m ON e.reports_to = m.employee_id;*/


-- JOINING MULTIPLE TABLES
USE sql_store;
SELECT o.order_id, o.order_date, c.first_name, c.last_name, os.name AS status
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_statuses os ON o.status = os.order_status_id
ORDER BY order_id;
 
SELECT *
FROM order_items oi
JOIN order_item_notes oin ON oi.order_id = oin.order_id
	AND oi.product_id = oin.product_id; -- COMPOUND JOIN CONDITION

-- OUTER JOINS AMONG MULTIPLE TABLES
SELECT products.product_id, products.name, oi.quantity
FROM order_items oi
RIGHT JOIN products ON products.product_id = oi.product_id
ORDER BY product_id;

-- CROSS JOINS Ex joining multiple colors  with each size of a shirt
SELECT customers.first_name, products.name AS product
FROM customers
CROSS JOIN products -- The keyword cross is not mandatory to be written
