DROP FUNCTION IF EXISTS racktables_django.038_api_filelinkrack_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.038_api_filelinkrack_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkrack);
    INSERT INTO 
        racktables_django.api_filelinkrack (oldid,file_id,parent_id) 
        SELECT 
               id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_rack as apiobj on entity_id = apiobj.oldid
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_filelinkrack) AND
            entity_type = 'ipv4rspool';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkrack) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
