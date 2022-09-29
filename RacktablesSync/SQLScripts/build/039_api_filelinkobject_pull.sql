DROP FUNCTION IF EXISTS racktables_django.039_api_filelinkobject_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.039_api_filelinkobject_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkobject);
    INSERT INTO 
        racktables_django.api_filelinkobject (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_object as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinkobject) AND
            entity_type = 'object';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkobject) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
