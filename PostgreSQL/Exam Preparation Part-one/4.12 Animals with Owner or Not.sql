CREATE OR REPLACE PROCEDURE  sp_animals_with_owners_or_not(
    IN animal_name VARCHAR(30),
    OUT res VARCHAR
)
AS
$$
    BEGIN
        SELECT
            COALESCE(o.name, 'For adoption')
        FROM animals AS a
        LEFT JOIN owners AS o
            ON a.owner_id = o.id
        WHERE a.name = animal_name
        INTO res;
    END;
$$
LANGUAGE plpgsql;