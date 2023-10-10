SELECT
    a.name AS address,
    CASE
        WHEN EXTRACT(HOUR FROM co.start) BETWEEN 6 AND 20 THEN 'Day'
        ELSE 'Night'
    END AS day_time,
    co.bill AS bill,
    cl.full_name AS full_name,
    c.make AS make,
    c.model AS model,
    ca.name AS category_name
FROM
    clients AS cl
JOIN
    courses AS co ON co.client_id = cl.id
JOIN
    addresses AS a ON co.from_address_id = a.id
JOIN
    cars AS c ON c.id = co.car_id
JOIN
    categories AS ca ON ca.id = c.category_id
ORDER BY
    co.id;