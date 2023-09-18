-- 01. River Info


-- 02. Concatenate Geography Data

CREATE VIEW view_continents_countries_currencies_details AS
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

-- 05. Substring River Length

SELECT
	(REGEXP_MATCHES("River Information", '([0-9]{1,4})'))[1] AS river_length
FROM view_river_info;

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


-- 15. Update iso_code


-- 16. REVERSE country_code


-- 17. Elevation --->> Peak Name


-- 18. Arithmetical Operators


-- 19. ROUND vs TRUNC


-- 20. Absolute Value


-- 22. EXTRACT Booked At


-- 24. Match or Not


-- 25. COUNT by Initial


-- ✶26. SUM


-- ✶27. Average Value✶