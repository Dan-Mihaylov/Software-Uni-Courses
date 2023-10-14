SELECT
    bg.id,
    bg.name,
    bg.release_year,
    c.name AS category_name
FROM
    board_games AS bg
JOIN
    categories AS c on c.id = bg.category_id
WHERE
    c.name IN ('Wargames', 'Strategy Games')
ORDER BY
    bg.release_year DESC;