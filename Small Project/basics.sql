-- Not a case sensitive language
USE sql_store;

SELECT * -- returns all the columns
-- SELECT first_name, last_name only displayes first and last name in the order of code or
-- SELECT 
--     last_name AS 'surname'
--     first_name, ...etc
-- Select Clause
-- 
FROM customers
WHERE customer_id = 1; -- this is a comment
-- ORDER BY first_name

SELECT DISTINCT state; -- Distinct keyword removes duplicates
SELECT *
FROM customers
WHERE state IN ('VA', 'GA', 'TX')
WHERE points BETWEEN 1000 AND 3000 -- inclusive limits
WHERE last_name LIKE 'B%' -- % indicates x string
WHERE last_name REGEXP 'b'
-- ^: starts with
-- $: ends with
-- |: or  Ex: WHERE last_name REGEXP 'a|b'
-- []: combination of or with compulsory string REGEXP '[ia]e' returns ie and ae

SELECT *
FROM customers
WHERE phone IS NULL

SELECT first_name, last_name, state
FROM customers
-- ORDER BY birth_date DESC
ORDER BY state, customer_id

SELECT *
FROM customers
-- LIMIT 3 -- if attribute>no. of records everything is displayed
LIMIT 6, 3