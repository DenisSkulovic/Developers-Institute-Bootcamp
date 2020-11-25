SELECT DISTINCT name
FROM language;

SELECT f.title, f.description, l.name
FROM film f, language l
WHERE l.language_id = f.language_id;


SELECT f.title, f.description, l.name
FROM film f
FULL JOIN language l
ON l.language_id = f.language_id;

DROP TABLE IF EXISTS customer_review;
CREATE TABLE customer_review
	(review_id SERIAL PRIMARY KEY,
	film_id SMALLINT REFERENCES film(film_id) ON DELETE CASCADE,
	language_id SMALLINT REFERENCES language(language_id),
	title VARCHAR(50),
	score SMALLINT,
	review_text VARCHAR,
	last_update DATE);
			
INSERT INTO customer_review
	(film_id, language_id, title, score, review_text, last_update)
VALUES
	(1, 1,'Mad Max', 89, 'This movie is garbage, but I like garbage, so I gave a score of 89.', '01-01-2020'),
	(1, 1,'Black Men In Black', 98, 'This movie is complete garbage, but I like complete garbage, so I gave a score of 98.', '01-01-2020');

DELETE FROM film
WHERE film_id = 1;

SELECT * FROM customer_review;






UPDATE film
SET language_id = 2
WHERE film_id=1;

DROP TABLE IF EXISTS customer_review;

SELECT COUNT(*) FROM rental;

SELECT f.title, f.rental_rate 
FROM rental r, film f, inventory i
WHERE i.film_id = f.film_id
AND i.inventory_id = r.inventory_id
ORDER BY rental_rate DESC
LIMIT 30;

SELECT f.title, f.description 
FROM film f, actor a, film_actor fa
WHERE fa.film_id = f.film_id
AND a.actor_id = fa.actor_id
AND a.first_name||' '||a.last_name = 'Penelope Monroe'
AND description LIKE '%umo%';

SELECT f.title 
FROM film f, film_category fc, category c
WHERE f.film_id = fc.film_id
AND fc.category_id = c.category_id
AND f.rating = 'R'
AND f.length < 60
AND c.name = 'Documentary';

SELECT f.title
FROM rental r, film f, inventory i, customer c
WHERE i.film_id = f.film_id
AND r.inventory_id = i.inventory_id
AND c.customer_id = r.customer_id
AND f.rental_rate > 4
AND r.return_date BETWEEN '07-28-2005' AND '08-01-2005'
AND c.first_name||' '||c.last_name = 'Matthew Mahan'