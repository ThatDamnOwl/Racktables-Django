DROP FUNCTION IF EXISTS racktables_django.004_api_location_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.004_api_location_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    DECLARE missing INT DEFAULT 1;
    DECLARE existing INT;
    DECLARE counter INT DEFAULT 0;
    SET existing = (select count(id) from racktables_django.api_location);
    WHILE counter < 10 AND missing > 0 DO
        INSERT INTO racktables_django.api_location (oldid,name,hasproblems,parentlocation_id,comment)
        SELECT
             location.id
            ,location.name
            ,CASE
                WHEN location.has_problems = 'yes' THEN 1
                ELSE 0
            END
            ,parentlocation.id
            ,ifnull(location.comment,'')
            FROM
                racktables.Location AS location
                LEFT JOIN racktables_django.api_location AS parentlocation on parentlocation.oldid = location.parent_id
            WHERE
                location.id not in (SELECT oldid from racktables_django.api_location)
                AND 
                (
                    parent_id in (SELECT oldid from racktables_django.api_location)
                    OR ifnull(parent_id,0) = 0
                );
        SET counter = counter + 1;
        SET missing = (SELECT count(id) FROM racktables.Location where id NOT IN (select oldid from racktables_django.api_location));
    END WHILE;
    SET inserted = (select count(id) from racktables_django.api_location);
    SET inserted = (inserted - existing);
    RETURN inserted;
END;
$$
DELIMITER ;
