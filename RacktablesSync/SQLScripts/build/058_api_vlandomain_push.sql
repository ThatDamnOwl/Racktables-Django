DROP FUNCTION IF EXISTS racktables_django.058_api_vlandomain_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.053_api_portouterinterface_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portouterinterface);
    INSERT INTO 
        racktables_django.api_portouterinterface (oldid,name) 
        SELECT 
             id
            ,oif_name
        FROM 
             racktables.PortOuterInterface
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_portouterinterface)
    SET inserted = (SELECT count(id) FROM racktables_django.api_portouterinterface) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
