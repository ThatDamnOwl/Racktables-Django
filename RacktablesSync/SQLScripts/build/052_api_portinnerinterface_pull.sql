DROP FUNCTION IF EXISTS racktables_django.052_api_portinnerinterface_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.052_api_portinnerinterface_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portinnerinterface);
    INSERT INTO 
        racktables_django.api_portinnerinterface (oldid,name) 
        SELECT 
             id
            ,iif_name
        FROM 
             racktables.PortInnerInterface
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_portinnerinterface)
    SET inserted = (SELECT count(id) FROM racktables_django.api_portinnerinterface) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
