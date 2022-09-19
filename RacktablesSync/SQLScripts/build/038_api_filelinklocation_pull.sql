DROP FUNCTION IF EXISTS racktables_django.038_api_filelinklocation_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.038_api_filelinklocation_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinklocation);
    INSERT INTO 
        racktables_django.api_filelinklocation (oldid,file_id,parent_id) 
        SELECT 
               id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_location as apiobj on entity_id = apiobj.oldid
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_filelinklocation) AND
            entity_type = 'location';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinklocation) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
