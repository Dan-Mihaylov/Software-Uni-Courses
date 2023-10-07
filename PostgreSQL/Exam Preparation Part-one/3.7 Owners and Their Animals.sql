SELECT
    o.name,
    COUNT(a.owner_id) AS "Count of animals"
FROM
    owners AS o
JOIN
    animals AS a ON o.id = a.owner_id
GROUP BY
    o.name
ORDER BY
    "Count of animals" DESC, o.name
LIMIT 5;