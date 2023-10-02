-- 01. Booked for Nights

SELECT
    CONCAT(a.address, ' ', a.address_2) AS "Apartment Address",
    b.booked_for AS "Nights"
FROM apartments AS a
JOIN bookings AS b
    USING (booking_id)
ORDER BY
    a.apartment_id;


-- 02. First

SELECT
    a.name AS "Name",
    a.country AS "Country",
    b.booked_at::date AS "Booked at"
FROM apartments AS a
LEFT JOIN bookings AS b
    USING (booking_id)
LIMIT 10;


-- 03. First  10 apartments booked at

SELECT
    b.booking_id AS "Booking ID",
    b.starts_at::date AS "Start Date",
    b.apartment_id AS "Apartment ID",
    CONCAT(c.first_name, ' ', c.last_name) AS "Customer Name"
FROM
    bookings AS b
RIGHT JOIN customers AS c
    USING (customer_id)
ORDER BY
    "Customer Name"
LIMIT 10;


-- 04. Booking Information

SELECT
    b.booking_id AS "Booking ID",
    a.name AS "Apartment Owner",
    a.apartment_id AS "Apartment ID",
    CONCAT(c.first_name, ' ', c.last_name) AS "Customer Name"
FROM
    bookings AS b
FULL JOIN apartments AS a on a.booking_id = b.booking_id
FULL JOIN customers AS c on c.customer_id = b.customer_id
ORDER BY
    "Booking ID", "Apartment Owner", "Customer Name"
;


-- 06. Unassigned Apartments

SELECT
    b.booking_id,
    b.apartment_id,
    c.companion_full_name
FROM bookings AS b
JOIN customers AS c
    USING (customer_id)
WHERE
    b.apartment_id IS NULL;

-- 07. Bookings Made by Lead

SELECT
    b.apartment_id,
    b.booked_for,
    c.first_name,
    c.country
FROM bookings as b
JOIN customers AS c
    USING (customer_id)
WHERE
    c.job_type LIKE('Lead');

-- 08. Hahn`s Bookings

SELECT
    COUNT(b.booking_id) AS count
FROM
    bookings AS b
JOIN customers AS c
    USING (customer_id)
WHERE
    c.last_name = 'Hahn';

-- 09. Total Sum of Nights

SELECT
    a.name AS name,
    SUM(b.booked_for)
FROM apartments AS a
JOIN bookings AS b
    USING (apartment_id)
GROUP BY
    a.name
ORDER BY
    name;

-- 10. Popular Vacation Destination

SELECT
    a.country AS country,
    COUNT(b.booking_id) AS booking_count
FROM
    apartments AS a
JOIN bookings AS b
    USING (apartment_id)
WHERE
    b.booked_at > '2021-05-18 07:52:09.904+03'
    AND
    b.booked_at < '2021-09-17 19:48:02.147+03'
GROUP BY a.country
ORDER BY
    booking_count DESC;


-- 11. Bulgaria's Peaks Higher than 2835 Meters

SELECT
    mc.country_code AS country_code,
    m.mountain_range as mountain_range,
    p.peak_name AS peak_name,
    p.elevation AS elevation
FROM
    mountains AS m
JOIN peaks AS p on m.id = p.mountain_id
JOIN mountains_countries AS mc ON m.id = mc.mountain_id
WHERE
    mc.country_code = 'BG' AND p.elevation > 2835
ORDER BY elevation DESC
;


-- 12. Count Mountain Ranges

SELECT
    mc.country_code,
    COUNT(*) AS mountain_range_count
FROM
    mountains AS m
JOIN
    mountains_countries as mc on mc.mountain_id = m.id
WHERE
    country_code IN ('RU', 'BG', 'US')
GROUP BY
    mc.country_code
ORDER BY
    mountain_range_count DESC
;



-- 13. Rivers in Africa

SELECT
    c.country_name,
    r.river_name
FROM
    countries AS c
LEFT JOIN
    countries_rivers AS cr ON cr.country_code = c.country_code
LEFT JOIN
    rivers AS r ON r.id = cr.river_id
WHERE
    c.continent_code = 'AF'
ORDER BY
    c.country_name ASC
LIMIT 5;



-- 14. Minimum Average Area Across Continents

SELECT
    MIN(average_area) AS min_average_area -- USE THE CREATED COLUMN, NOT THE WHOLE SELECT STATEMENT (average_area) NOT (average)
FROM
    (
        SELECT
            AVG(area_in_sq_km) AS average_area  -- CREATE THE COL IN THE SELECT STATEMENT
        FROM
            countries
        GROUP BY
            continent_code
    ) AS average


-- 15. Countries Without Any Mountains

SELECT
    COUNT(*)
FROM
    countries AS c
LEFT JOIN
    mountains_countries AS mc USING (country_code)
WHERE
    mountain_id IS NULL;


-- 16. Monasteries by Country✶

CREATE TABLE IF NOT EXISTS monasteries (
    id SERIAL PRIMARY KEY,
    monastery_name VARCHAR(255),
    country_code CHAR(2)
);

INSERT INTO monasteries
    (monastery_name, country_code)
VALUES
    ('Rila Monastery ''St. Ivan of Rila', 'BG'),
    ('Bachkovo Monastery ''Virgin Mary"', 'BG'),
    ('Troyan Monastery ''Holy Mother''s Assumption', 'BG'),
    ('Kopan Monastery', 'NP'),
    ('Thrangu Tashi Yangtse Monastery', 'NP'),
    ('Shechen Tennyi Dargyeling Monastery', 'NP'),
    ('Benchen Monastery', 'NP'),
    ('Southern Shaolin Monastery', 'CN'),
    ('Dabei Monastery', 'CN'),
    ('Wa Sau Toi', 'CN'),
    ('Lhunshigyia Monastery', 'CN'),
    ('Rakya Monastery', 'CN'),
    ('Monasteries of Meteora', 'GR'),
    ('The Holy Monastery of Stavronikita', 'GR'),
    ('Taung Kalat Monastery', 'MM'),
    ('Pa-Auk Forest Monastery', 'MM'),
    ('Taktsang Palphug Monastery', 'BT'),
    ('Sümela Monastery', 'TR');

ALTER TABLE
    monasteries
ADD COLUMN
    three_rivers BOOL DEFAULT FALSE;

UPDATE monasteries
SET three_rivers = TRUE
FROM
    (SELECT
        country_code
     FROM
         countries_rivers
    GROUP BY
        country_code
    HAVING
        COUNT(*) > 3) AS results
WHERE
    monasteries.country_code = results.country_code;

SELECT
    monastery_name AS "Monastery",
    country_name AS "Country"
FROM
    monasteries
JOIN
    countries USING (country_code)
WHERE
    three_rivers IS NOT  TRUE
ORDER BY
    monastery_name
;

-- 17. Monasteries by Continents and Countries✶

UPDATE countries
SET country_name = 'Burma'
WHERE country_name = 'Myanmar';

INSERT INTO monasteries
    (monastery_name, country_code)
VALUES
    ('Hanga Abbey', (
        SELECT country_code
        FROM countries
        WHERE country_name = 'Tanzania'
        )),
    ('Myin-Tin-Daik', (
        SELECT country_code
        FROM countries
        WHERE country_name = 'Myanmar'
        ));


SELECT
    continents.continent_name AS "Continent Name",
    countries.country_name AS "Country Name",
    COUNT(monasteries.monastery_name) AS "Monasteries Count"
FROM
    continents
LEFT JOIN
    countries USING (continent_code)
LEFT JOIN
    monasteries USING (country_code)
WHERE
    three_rivers = FALSE OR three_rivers IS NULL
GROUP BY
    continent_name, country_name
ORDER BY
    "Monasteries Count" DESC, countries.country_name ASC;


-- 18. Retrieving Information about Indexes

SELECT
    tablename,
    indexname,
    indexdef
FROM
    pg_indexes
WHERE schemaname ='public'
ORDER BY
    indexname ASC;

-- 19. Continents and Currencies✶




-- 20. The Highest Peak in Each Country✶



