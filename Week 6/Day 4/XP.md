SELECT 
	e.first_name as "First Name", 
	e.last_name as "Last Name"
FROM employees e;

SELECT *
FROM employees
WHERE department_id in (
	SELECT department_id
	FROM employees
	GROUP BY department_id
	HAVING count(*) = 1);
	
SELECT *
FROM employees
ORDER BY first_name DESC;

SELECT first_name||' '||last_name as name, salary, salary*0.15 as PF
FROM employees;

SELECT employee_id, first_name||' '||last_name as name, salary
FROM employees
ORDER BY salary;

SELECT sum(salary)
FROM employees;

SELECT min(salary), max(salary)
FROM employees;

SELECT avg(salary)
FROM employees;

SELECT count(employee_id)
FROM employees;

SELECT upper(first_name)
FROM employees;

SELECT LEFT(first_name, 3)
FROM employees;

SELECT first_name||' '||last_name as name
FROM employees;

SELECT first_name||' '||last_name as name, length(first_name||' '||last_name)
FROM employees;

SELECT *
FROM employees
WHERE first_name LIKE '%0%' 
OR first_name LIKE '%[0-9]%';

SELECT *
FROM employees
LIMIT 10;

SELECT first_name||' '||last_name as name, salary
FROM employees
WHERE salary BETWEEN 10000 and 15000;

SELECT first_name||' '||last_name as name, hire_date
FROM employees
WHERE hire_date BETWEEN '01-01-1987' and '12-31-1987';

SELECT first_name
FROM employees
WHERE first_name LIKE '%e%' AND first_name LIKE '%c%';

SELECT e.last_name, j.job_title, e.salary
FROM employees e, jobs j
WHERE e.job_id = j.job_id
AND job_title NOT IN ('Programmer','Shipping Clerk')
AND salary NOT IN (4500,10000,15000);

SELECT last_name
FROM employees
WHERE length(last_name) = 6;

SELECT last_name
FROM employees
WHERE last_name LIKE '__e%';

SELECT DISTINCT j.job_title
FROM employees e
INNER JOIN jobs j
USING (job_id);

SELECT *
FROM employees
WHERE last_name in ('Jones','Blake','Scott','King','Ford');

UPDATE employees
SET email = 'not available'
WHERE department_id = 110;

UPDATE employees
SET email = 'available'
WHERE department_id IN (
	SELECT department_id
	FROM departments
	WHERE department_name = 'Accounting');
	
UPDATE employees
SET salary = 8000
WHERE employee_id = 105
AND salary < 5000;

UPDATE employees
SET salary = salary*1.25
WHERE department_id = 4;
UPDATE employees
SET salary = salary*1.15
WHERE department_id = 9;
UPDATE employees
SET salary = salary*1.1
WHERE department_id = 11;
