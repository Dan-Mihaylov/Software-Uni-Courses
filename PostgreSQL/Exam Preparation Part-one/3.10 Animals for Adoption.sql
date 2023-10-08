SELECT
    a.name AS "Animal Name",
    EXTRACT(YEAR FROM a.birthdate) AS "Birth Year",
    at.animal_type AS "Animal Type"
FROM
    animals AS a
JOIN
    animal_types AS at ON at.id = a.animal_type_id
WHERE
    a.owner_id IS NULL
        AND
    at.animal_type <> 'Birds'
        AND
    AGE('01/01/2022', a.birthdate) < '5 YEARS'
ORDER BY
    a.name
;
