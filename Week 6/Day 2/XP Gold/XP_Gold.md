UPDATE students
SET birth_date = '02/11/1998'
WHERE first_name||' '||last_name in ('Lea Benichou','Marc Benichou');

UPDATE students
SET last_name = 'Guez'
WHERE first_name = 'David' AND last_name = 'Grez';

DELETE FROM students WHERE first_name = 'Lea' and last_name = 'Benichou';

SELECT COUNT(*) FROM students;

SELECT COUNT(*) FROM students WHERE birth_date > '01/01/2000';

ALTER TABLE students
ADD math_grade SMALLINT;

UPDATE students
SET math_grade = 80 WHERE id = 1;
UPDATE students
SET math_grade = 90 WHERE id IN (2, 4);
UPDATE students
SET math_grade = 40 WHERE id = 6;

SELECT COUNT(*) FROM students WHERE math_grade > 83;

INSERT INTO students
	(first_name, last_name, birth_date, math_grade)
VALUES
	('Omer', 'Simpson', '1980-10-03', 70);
	
SELECT SUM(math_grade) FROM students;
