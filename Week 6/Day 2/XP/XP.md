SELECT * FROM items ORDER BY price;
SELECT * FROM items WHERE price >= 80 ORDER BY price DESC;
SELECT first_name, last_name FROM customers ORDER BY first_name, last_name LIMIT 3;
SELECT last_name FROM customers ORDER BY last_name desc;

DROP TABLE IF EXISTS purchases;
CREATE TABLE purchases(
	purchase_id SERIAL PRIMARY KEY,
	customer_id SMALLINT NOT NULL, 
	item_id SMALLINT NOT NULL,
	CONSTRAINT item_id
		FOREIGN KEY(item_id) 
			REFERENCES items(id),
	CONSTRAINT customer_id
		FOREIGN KEY(customer_id) 
			REFERENCES customers(id)
);

INSERT INTO purchases
	(customer_id, item_id)
VALUES
	(1,NULL);

INSERT INTO purchases
	(customer_id, item_id)
VALUES
	(2,2),
	(2,1),
	(1,2),
	(1,1),
	(3,1);

SELECT * FROM purchases;

SELECT * 
FROM purchases 
LEFT JOIN customers 
ON customers.id = purchases.customer_id;

SELECT * 
FROM purchases as p
LEFT JOIN items as i
ON i.id = p.item_id
WHERE i.name IN ('Large Desk', 'Small Desk');

INSERT INTO items
	(name, price)
VALUES
	('Hard Drive', 100);

INSERT INTO purchases
	(customer_id, item_id)
VALUES
	(3, 4)

SELECT c.first_name, c.last_name, i.name FROM customers c
LEFT JOIN purchases p
ON c.id = p.customer_id
LEFT JOIN items i
ON p.item_id = i.id








SELECT * FROM customer;

SELECT first_name||' '||last_name as full_name FROM customer; 

SELECT DISTINCT create_date FROM customer;

SELECT * FROM customer ORDER BY first_name;

SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate asc;

SELECT a.address, a.district, a.phone
FROM address a
WHERE a.district = 'Texas';

SELECT *
FROM film
WHERE film_id = 15
OR film_id = 150;

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title LIKE '%ove%';

SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10;

SELECT 
	title, 
	rental_rate 
FROM film
ORDER BY rental_rate
OFFSET 10
FETCH FIRST 10 ROWS ONLY;

SELECT p.amount, p.payment_date
FROM customer c
LEFT JOIN payment p
ON c.customer_id = p.customer_id
ORDER BY c.customer_id;

SELECT title
FROM film
WHERE film_id NOT IN (
	SELECT film_id FROM inventory);
	
SELECT ci.city, co.country
FROM city ci
LEFT JOIN country co
ON ci.country_id = co.country_id;



