UPDATE cars
SET condition = 'C'
WHERE
    make NOT IN ('Mercedes-Benz')
        AND
    (mileage >= 800000 OR mileage IS NULL)
        AND
    year <= 2010;
;