DROP FUNCTION IF EXISTS racktables_django.037_api_filelinkipv6network_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.037_api_filelinkipv6network_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv6network);
    INSERT INTO 
        racktables_django.api_filelinkipv6network (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_ipv6network as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinkipv6network) AND
            entity_type = 'ipv6net';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv6network) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
