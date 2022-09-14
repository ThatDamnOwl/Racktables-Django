DROP FUNCTION IF EXISTS racktables_django.034_api_filelinkipv4network_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.034_api_filelinkipv4network_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv4network);
    INSERT INTO 
        racktables_django.api_filelinkipv4network (oldid,file_id,parent_id) 
        SELECT 
               id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_ipv4network as apiobj on entity_id = apiobj.oldid
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_filelinkipv4network) AND
            entity_type = 'ipv4net';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv4network) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
