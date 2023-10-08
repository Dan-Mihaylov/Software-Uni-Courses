SELECT
    v.name AS "Volunteers Name",
    v.phone_number AS "Phone Number",
    TRIM(REPLACE(TRIM(v.address), 'Sofia', ''), ' ,') AS "Address"
FROM
    volunteers AS v
JOIN
    volunteers_departments AS vd ON vd.id = v.department_id
WHERE
    vd.department_name = 'Education program assistant'
        AND
    v.address LIKE('%Sofia%')
ORDER BY
    v.name ASC
;