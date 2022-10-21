DROP FUNCTION IF EXISTS racktables_django.055_api_portcompat_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.055_api_portcompat_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portcompat);
    INSERT INTO 
        racktables_django.api_portcompat (port1_id,port2_id) 
        SELECT 
             poi1.id
            ,poi2.id
        FROM 
             racktables.PortCompat
             LEFT JOIN racktables_django.api_portouterinterface as poi1 on poi1.oldid = type1
             LEFT JOIN racktables_django.api_portouterinterface as poi2 on poi2.oldid = type2
        WHERE 
            concat(poi1.id,"-",poi2.id) NOT IN (SELECT concat(port1_id,"-",port2_id) FROM racktables_django.api_portcompat);
    SET inserted = (SELECT count(id) FROM racktables_django.api_portcompat) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
