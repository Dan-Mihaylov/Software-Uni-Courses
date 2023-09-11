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


-- 11. Compare Character Values



-- 12. Salary13. Missing Value


-- 14. INSERT Departments


-- 15. New Table


-- 16. Update the Project End Date


-- 17. Award Employees with Experience


-- 18. Delete Addresses


-- 19. Create a View


-- 20. Create a View with Multiple Tables


-- 21. ALTER VIEW


-- 22. DROP VIEW


-- 23. UPPER


-- ✶24. SUBSTRING


-- ✶25. LIKE✶


