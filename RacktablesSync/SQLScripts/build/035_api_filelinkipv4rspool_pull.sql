DROP FUNCTION IF EXISTS racktables_django.035_api_filelinkipv4rspool_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.035_api_filelinkipv4rspool_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv4rspool);
    INSERT INTO 
        racktables_django.api_filelinkipv4rspool (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_ipv4rspool as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinkipv4rspool) AND
            entity_type = 'ipv4rspool';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv4rspool) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
