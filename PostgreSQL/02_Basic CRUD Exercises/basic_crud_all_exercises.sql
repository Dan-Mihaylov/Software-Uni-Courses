-- 01. Select Cities

SELECT * FROM cities
ORDER BY id ASC;

-- 02. Concatenate

SELECT * FROM cities
ORDER BY id ASC;

-- 03. Remove Duplicate Rows

SELECT
DISTINCT name,
area AS "Area (km2)"
FROM cities
ORDER BY name DESC;

-- 04. Limit Records

SELECT
id AS "ID",
first_name || ' ' || last_name AS "Full Name",
job_title AS "Job Title"
FROM employees
ORDER BY first_name ASC
LIMIT 50;

-- 05. Skip Rows

SELECT
id,
first_name || ' ' || middle_name || ' ' || last_name AS "Full Name",
hire_date AS "Hire Date"
FROM employees
ORDER BY hire_date
OFFSET 9;

-- 06. Find the Addresses

SELECT
id,
number || ' ' || street AS "Address",
city_id
FROM addresses
WHERE id >= 20;

-- 07. Positive Even Number

SELECT
number || ' ' || street AS "Address",
city_id
FROM addresses
WHERE city_id % 2 = 0
ORDER BY city_id ASC;

-- 08. Projects within a Date Range

SELECT
name,
start_date,
end_date
FROM projects
WHERE start_date >= '2016-06-01 07:00:00'
AND end_date < '2023-06-04 00:00:00'
ORDER BY start_date ASC;

-- 09. Multiple Conditions

SELECT
number, street
FROM addresses
WHERE id BETWEEN 50 AND 100
OR number < 1000;

-- 10. Set of Values

SELECT
    employee_id, project_id
    FROM employee_projects
    WHERE employee_id IN (200, 250)
    AND project_id NOT IN (50, 100);

-- 11. Compare Character Values

SELECT
	name, start_date
	FROM projects
	WHERE name IN ('Mountain', 'Road', 'Touring')
	LIMIT 20;

-- 12. Salary

SELECT
	first_name || ' ' || last_name AS "Full Name",
	job_title,
	salary
	FROM employees
	WHERE salary in (12500, 14000, 23600, 25000)
	ORDER BY salary DESC;


-- 13. Missing Value

SELECT
	id, first_name, last_name
	FROM employees
	WHERE middle_name IS NULL
	LIMIT 3;

-- 14. INSERT Departments

INSERT INTO departments
	(id, department, manager_id)
	VALUES
	(10, 'Finance', 3),
	(11, 'Information Services', 42),
	(12, 'Document Control', 90),
	(13, 'Quality Assurance', 274),
	(14, 'Facilities and Maintenance', 218),
	(15, 'Shipping and Receiving', 85),
	(16, 'Executive', 109);

-- 15. New Table

CREATE TABLE company_chart AS
	SELECT
		first_name || ' ' || last_name AS "Full Name",
		job_title AS "Job Title",
		department_id AS "Department ID",
		manager_id AS "Manager Id"
		From employees;

-- 16. Update the Project End Date

UPDATE projects
	SET end_date = start_date + INTERVAL '5 MONTHS'
	WHERE end_date IS NULL;

-- 17. Award Employees with Experience

UPDATE employees
	SET
	salary = salary + 1500,
	job_title = 'Senior' || ' ' || job_title
	WHERE hire_date BETWEEN '1998-01-01' AND '2000-01-05';

-- 18. Delete Addresses

DELETE FROM addresses WHERE city_id IN (5, 17, 20, 30);

-- 19. Create a View


-- 20. Create a View with Multiple Tables


-- 21. ALTER VIEW


-- 22. DROP VIEW


-- 23. UPPER


-- ✶24. SUBSTRING


-- ✶25. LIKE✶


