DROP FUNCTION IF EXISTS racktables_django.042_api_filelinkuser_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.042_api_filelinkuser_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkuser);
    INSERT INTO 
        racktables_django.api_filelinkuser (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_useraccount as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinkuser) AND
            entity_type = 'user';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkuser) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
