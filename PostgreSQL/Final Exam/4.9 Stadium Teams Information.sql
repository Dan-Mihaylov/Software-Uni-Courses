CREATE OR REPLACE FUNCTION fn_stadium_team_name(stadium_name VARCHAR(30))
RETURNS TABLE(name VARCHAR)
AS
$$
    BEGIN
        RETURN QUERY
        SELECT
            t.name
        FROM
            teams AS t
        JOIN
            stadiums AS s ON s.id = t.stadium_id
        WHERE
            s.name = stadium_name
        ORDER BY t.name
    ;
    RETURN;
    END;
$$
LANGUAGE plpgsql;

