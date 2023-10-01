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




-- 13. Rivers in Africa




-- 14. Minimum Average Area Across Continents




-- 15. Countries Without Any Mountains




-- 16. Monasteries by Country✶



-- 17. Monasteries by Continents and Countries✶




-- 18. Retrieving Information about Indexes




-- 19. Continents and Currencies✶




-- 20. The Highest Peak in Each Country✶



