DROP FUNCTION IF EXISTS racktables_django.067_api_rackthumbnail_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.067_api_rackthumbnail_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_rackthumbnail);
    INSERT INTO 
        racktables_django.api_rackthumbnail (data,rack_id) 
        SELECT 
             old.thumb_data
            ,rack.id
        FROM 
             racktables.RackThumbnail as old
             LEFT JOIN racktables_django.api_rack as rack on rack.oldid = old.rack_id
        WHERE 
            rack.id NOT IN (SELECT rack_id FROM racktables_django.api_rackthumbnail);

    SET inserted = (SELECT count(id) FROM racktables_django.api_rackthumbnail) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
