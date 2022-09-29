DROP FUNCTION IF EXISTS racktables_django.041_api_filelinkrow_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.041_api_filelinkrow_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkrow);
    INSERT INTO 
        racktables_django.api_filelinkrow (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_row as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinkrow) AND
            entity_type = 'row';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkrow) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
