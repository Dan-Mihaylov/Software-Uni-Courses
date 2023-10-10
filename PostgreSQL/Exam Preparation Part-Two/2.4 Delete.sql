DELETE FROM clients
WHERE
    id IN
        (SELECT cl.id AS value
           FROM clients AS cl
                    LEFT JOIN
                courses AS co ON cl.id = co.client_id
           WHERE co.id IS NULL
             AND LENGTH(cl.full_name) > 3);