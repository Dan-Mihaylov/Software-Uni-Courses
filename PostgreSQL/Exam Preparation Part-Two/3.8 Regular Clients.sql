SELECT
    c.full_name,
    COUNT(co.car_id) AS count_of_cars,
    SUM(co.bill) AS total_sum
FROM
    clients AS c
JOIN
    courses AS co ON c.id = co.client_id
WHERE
    c.full_name LIKE('_a%')
GROUP BY
    c.full_name
HAVING
    COUNT(co.car_id) > 1
ORDER BY
    c.full_name;