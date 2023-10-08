CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(searched_volunteers_department VARCHAR(30))
RETURNS INT
AS
$$
    DECLARE res INT;
    BEGIN
        res := (
                    SELECT
                        COUNT(*)
                    FROM
                        volunteers AS v
                    JOIN
                        volunteers_departments AS vd ON vd.id = v.department_id
                    WHERE
                        vd.department_name = searched_volunteers_department
                   );
    RETURN res;
    END;
$$
LANGUAGE plpgsql;


-- CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(searched_volunteers_department VARCHAR(30))
-- RETURNS INT
-- AS
-- $$
--     DECLARE result INT;
--     BEGIN
--         SELECT
--             COUNT(*)
--         FROM
--             volunteers AS v
--         JOIN
--             volunteers_departments AS vd ON vd.id = v.department_id
--         WHERE
--             vd.department_name = searched_volunteers_department
--         INTO result;
--     RETURN result;
--     END;
-- $$
-- LANGUAGE plpgsql;