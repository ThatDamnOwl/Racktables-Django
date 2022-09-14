DROP FUNCTION IF EXISTS racktables_django.005_api_row_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.005_api_row_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_row);
    INSERT INTO
    racktables_django.api_row (oldid, name, location_id)
    SELECT
         row.id
        ,row.name
        ,location.id
    FROM racktables.Row AS row 
         LEFT JOIN
            racktables_django.api_location AS location ON location_id = oldid
    WHERE row.id NOT IN (
        SELECT oldid
        FROM racktables_django.api_row
    );
    SET inserted = (SELECT count(id) FROM racktables_django.api_row) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
