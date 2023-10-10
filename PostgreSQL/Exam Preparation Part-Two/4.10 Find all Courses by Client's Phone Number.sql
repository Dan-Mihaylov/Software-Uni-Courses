CREATE OR REPLACE FUNCTION fn_courses_by_client(phone_num VARCHAR(20))
RETURNS INT
AS
$$
    DECLARE total INT;
    BEGIN
        SELECT
            COUNT(co.id)
        FROM
            clients AS c
        JOIN
            courses AS co ON co.client_id = c.id
        WHERE
            c.phone_number = phone_num
        INTO total;
        RETURN total;
    END;

$$
LANGUAGE plpgsql;
