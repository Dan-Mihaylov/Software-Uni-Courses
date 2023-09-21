-- 01. River Info


-- 02. Concatenate Geography Data

CREATE OR REPLACE VIEW view_continents_countries_currencies_details AS
SELECT
	CONCAT(c1.continent_name, ': ', c1.continent_code) AS "Continent Details",
	CONCAT_WS(' - ', c2.country_name, c2.capital, c2.area_in_sq_km, 'km2') AS "Country Information",
	CONCAT(c3.description, ' (', c3.currency_code, ')') AS "Currencies"
FROM continents c1
JOIN countries c2 ON c1.continent_code = c2.continent_code
JOIN currencies c3 ON c2.currency_code = c3.currency_code
ORDER BY "Country Information" ASC, "Currencies" ASC;

-- 03. Capital Code
ALTER TABLE countries
ADD COLUMN capital_code CHAR(2);

UPDATE countries
SET capital_code = SUBSTRING(capital, 1, 2);

-- 04. Description

SELECT
	SUBSTRING(description FROM 5) AS "substring"
FROM currencies;

-- SELECT
--     RIGHT(description, -4) as "Right Side"
-- FROM currencies;

-- 05. Substring River Length

SELECT
	(REGEXP_MATCHES("River Information", '([0-9]{1,4})'))[1] AS river_length
FROM view_river_info;

-- SELECT
--     SUBSTRING("River Information", '([0-9]{1,4})') AS "River Length"
-- FROM
--     view_river_info

-- 06. Replace A

SELECT
	REPLACE(mountain_range, 'a', '@') AS "replace_a",
	REPLACE(mountain_range, 'A', '$') AS "replace_A"
FROM mountains;


-- 07. Translate

SELECT
	capital,
	TRANSLATE(capital ,'áãåçéíñóú', 'aaaceinou') AS translated_name
FROM countries;

-- 08. LEADING

SELECT
	continent_name,
	TRIM(LEADING FROM continent_name) AS "trim"
FROM continents;

-- 09. TRAILING

SELECT
	continent_name,
	TRIM(TRAILING FROM continent_name) AS "trim"
FROM continents;

-- 10. LTRIM & RTRIM

SELECT
	LTRIM(peak_name, 'M') as "Left Trim",
	RTRIM(peak_name, 'm') as "Right Trim"
FROM peaks;

-- 11. Character Length and Bits1

SELECT
	CONCAT(m.mountain_range, ' ', p.peak_name) AS "Mountains Information",
	LENGTH(CONCAT(m.mountain_range, ' ', p.peak_name)) AS "Characters Length",
	BIT_LENGTH(CONCAT(m.mountain_range, ' ', p.peak_name)) AS "Bits of a String"
FROM mountains m
JOIN peaks p ON m.id = p.mountain_id;

-- 12. Length of a Number

SELECT
	population,
	LENGTH(CAST(population AS TEXT)) AS "length"
FROM countries;

-- 13. Positive and Negative LEFT

SELECT
	peak_name,
	LEFT(peak_name, 4) AS "Positive Left",
	LEFT(peak_name, -4) AS "Negative Left"
FROM peaks;

-- 14. Positive and Negative RIGHT

SELECT
    peak_name,
    RIGHT(peak_name, 4) AS "Positive Right",
    RIGHT(peak_name, -4) AS "Negative Right"
FROM
    peaks;

-- 15. Update iso_code

UPDATE
    countries
SET
    iso_code = UPPER(SUBSTRING(country_name, 1, 3))
WHERE
    iso_code IS NULL;


-- 16. REVERSE country_code

UPDATE
    countries
SET
    country_code = LOWER(REVERSE(country_code));

-- 17. Elevation --->> Peak Name

SELECT
    CONCAT(elevation, ' ', REPEAT('-', 3), REPEAT('>', 2), ' ', peak_name) AS "Elevation --->> Peak Name"
FROM
    peaks
WHERE
    elevation >= 4884;

-- 18. Arithmetical Operators

CREATE TABLE IF NOT EXISTS
    bookings_calculation
AS SELECT
       booked_for,
       CAST(booked_for * 50 AS NUMERIC) AS "multiplication",
       CAST(booked_for % 50 AS NUMERIC) AS "modulo"
FROM
    bookings
WHERE
    apartment_id = 93;


-- CREATE TABLE
--     bookings_calculation
--     AS
-- SELECT
--     booked_for
-- FROM
--     bookings
-- WHERE
--     apartment_id = 93;
--
-- ALTER TABLE
--     bookings_calculation
-- ADD COLUMN multiplication NUMERIC,
-- ADD COLUMN modulo NUMERIC;
--
-- UPDATE
--     bookings_calculation
-- SET
--     multiplication = booked_for * 50,
--     modulo = booked_for % 50;

-- 19. ROUND vs TRUNC

SELECT
    latitude,
    ROUND(latitude, 2) AS "round",
    TRUNC(latitude, 2) AS "trunc"
FROM
    apartments;

-- 20. Absolute Value

SELECT
    longitude,
    ABS(longitude) AS "abs"
FROM apartments;

-- 21. Billing Day ***

ALTER TABLE bookings
ADD COLUMN
    billing_day TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP;

SELECT
    TO_CHAR(billing_day, 'DD "Day" MM "Month" YYYY "Year" HH24:MI:SS') AS "Billing Day"
FROM
    bookings;


-- 22. EXTRACT Booked At

SELECT
    EXTRACT('year' FROM booked_at) AS "Year",
    EXTRACT('month' FROM booked_at) AS "Month",
    EXTRACT('day' FROM booked_at) AS "Day",
    EXTRACT('hour' FROM booked_at AT TIME ZONE 'UTC') AS "Hour",
    EXTRACT('minute' FROM booked_at) AS "Minute",
    CEILING(EXTRACT('second' FROM booked_at)) AS "Second"
FROM
    bookings;

-- 23. Early Birds ***

SELECT
    user_id,
        AGE(starts_at, booked_at)AS "Early Bird"
FROM
    bookings
WHERE
    starts_at - booked_at >= '10 MONTHS';
--     AGE(starts_at, booked_at) > INTERVAL '10 months';


-- 24. Match or Not

SELECT
    companion_full_name,
    email
FROM
    users
WHERE
    companion_full_name ILIKE('%aNd%')
        AND
    email NOT LIKE('%@gmail');

-- 25. COUNT by Initial

SELECT
    SUBSTRING(first_name, 1, 2) AS "initials",
    COUNT('initials') as "user_count"
FROM
    users
GROUP BY
    initials
ORDER BY
    user_count DESC,
    initials ASC;

-- ✶26. SUM

SELECT
    SUM(booked_for) as "total_value"
FROM
    bookings
WHERE apartment_id = 90;


-- ✶27. Average Value✶

SELECT
    AVG(multiplication) as "average_value"
FROM
    bookings_calculation;
