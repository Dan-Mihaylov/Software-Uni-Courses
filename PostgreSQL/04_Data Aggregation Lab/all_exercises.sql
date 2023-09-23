-- 01. Departments Info by ID

SELECT
    department_id,
    COUNT(id) AS "employee_count"
FROM
    employees
GROUP BY
    department_id
ORDER BY
    department_id;

-- 02. Departments Info by Salary

SELECT
    department_id,
    COUNT(salary) AS "employee_count"
FROM
    employees
GROUP BY
    department_id
ORDER BY
    department_id;

-- 03. Sum Salaries per Department

SELECT
    department_id,
    SUM(salary) AS "total_salaries"
FROM
    employees
GROUP BY
    department_id
ORDER BY
    department_id;

-- 04. Maximum Salary

SELECT
    department_id,
    MAX(salary) AS "max_salary"
FROM
    employees
GROUP BY
    department_id
ORDER BY
    department_id;

-- 05. Minimum Salary

SELECT
    department_id,
    MIN(salary) AS "min_salary"
FROM
    employees
GROUP BY
    department_id
ORDER BY
    department_id;

-- 06. Average Salary

SELECT
    department_id,
    AVG(salary) AS "avg_salary"
FROM
    employees
GROUP BY
    department_id
ORDER BY
    department_id;

-- 07. Filter Total Salaries
-- The HAVING Clause has to have an aggregate function (Question 1: Why does it have to be an aggregate function
-- and cannot just take the result from the generated column that had ran the aggregate function to generate the res?)

SELECT
    department_id,
    SUM(salary) AS "Total Salary"
FROM
    employees
GROUP BY
    department_id
HAVING
    SUM(salary) < 4200
ORDER BY
    department_id;

--08. Department Names

SELECT
    id,
    first_name,
    last_name,
    salary::NUMERIC(10,2) AS salary,
    department_id,
    CASE
        WHEN department_id = 1 THEN 'Management'
        WHEN department_id = 2 THEN 'Kitchen Staff'
        WHEN department_id = 3 THEN 'Service Staff'
        ELSE 'Other'
    END AS department_name
FROM
    employees
ORDER BY
    id;


/*
 Another way to write CASE
 The previous CASE is called GENERAL CASE
 This one is called SIMPLE CASE.

 SELECT
    CONCAT(first_name, ' ', last_name) AS "Full Name",
    CASE city_id
        WHEN 1 THEN 'Sofia'
        WHEN 2 THEN 'Plovdiv'
        WHEN 3 THEN 'Pernik'
        WHEN 4 THEN 'Bourgas'
        WHEN 5 THEN 'Varna'
        WHEN 6 THEN 'Khaskovo'
    END AS "City"
 FROM
    person;

 WHEN YOU HAVE THE SAME CASE YOU JUST WRITE IT ON TOP ONCE THEN COMPARE THE CONDITIONS.


 SELECT
    e.id,
    e.first_name,
    e.last_name,
    e.salary::NUMERIC(10,2) AS salary,
    e.department_id,
    CASE e.department_id < 4
        WHEN TRUE THEN d.name
        ELSE 'Other'
    END AS department
FROM
    employees e
JOIN departments d ON e.department_id = d.id
ORDER BY
    id;

 */
