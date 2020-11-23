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

