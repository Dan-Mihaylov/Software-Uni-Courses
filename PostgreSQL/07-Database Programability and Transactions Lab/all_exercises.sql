-- 01. Count Employees By Town

CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT
AS $$
    DECLARE e_count INT;
    BEGIN
        SELECT
            COUNT(employee_id) INTO e_count
        FROM
            employees
        JOIN
            addresses USING (address_id)
        JOIN
            towns USING (town_id)
        WHERE town_name = towns.name; -- CAN DO THE INTO e_count HERE AS WELL.
        RETURN e_count;
    END;
    $$ LANGUAGE plpgsql;

-- 02. Employees Promotion

CREATE PROCEDURE sp_increase_salaries(department_name VARCHAR(50))
LANGUAGE plpgsql
AS $$
    BEGIN
        UPDATE employees
        SET salary = salary * 1.05
        WHERE department_id = (
            SELECT
                d.department_id
            FROM
                departments AS d
            WHERE d.name = department_name
            );
    END;
    $$;

-- 03. Employees Promotion by ID

CREATE PROCEDURE sp_increase_salary_by_id(id INT)
LANGUAGE plpgsql
AS $$

    BEGIN
        UPDATE employees
        SET salary = salary * 1.05
        WHERE employee_id = id;
    END;
$$;


-- Second solution with transaction controls

CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(id INT)
AS $$
    BEGIN
        IF (
            SELECT COUNT(employee_id)
            FROM employees
            WHERE employee_id = id
            ) != 1 THEN
        ROLLBACK;
        ELSE
        UPDATE employees
        SET salary = salary * 1.05
        WHERE employee_id = id;
        END IF;
        COMMIT;
    END;
$$
LANGUAGE plpgsql;

-- 04. Triggered

CREATE TABLE deleted_employees(
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    middle_name VARCHAR(20),
    job_title VARCHAR(50),
    department_id INT,
    salary NUMERIC(10,4)
);

CREATE OR REPLACE FUNCTION trigger_fn_on_employee_delete()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
    BEGIN
        INSERT INTO deleted_employees (first_name, last_name, middle_name, job_title, department_id, salary)
        VALUES
            (OLD.first_name, OLD.last_name, OLD.middle_name, OLD.job_title, OLD.department_id, OLD.salary);
        RETURN NULL;
    END;
$$;

CREATE OR REPLACE TRIGGER tr_deleted_employees
    AFTER DELETE
    ON employees
    FOR EACH ROW
    EXECUTE FUNCTION
        trigger_fn_on_employee_delete();
