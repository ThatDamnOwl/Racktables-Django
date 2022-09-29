DROP FUNCTION IF EXISTS racktables_django.056_api_portinterfacecompat_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.056_api_portinterfacecompat_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portinterfacecompat);
    INSERT INTO 
        racktables_django.api_portinterfacecompat (portinnerinterface_id,portouterinterface_id) 
        SELECT 
             pii.id
            ,poi.id
        FROM 
             racktables.PortInterfaceCompat
             LEFT JOIN racktables_django.api_portouterinterface as pii on pii.oldid = iif_id
             LEFT JOIN racktables_django.api_portinnerinterface as poi on poi.oldid = oif_id
        WHERE 
            concat(poi1.id,"-",poi2.id) NOT IN (SELECT concat(port1_id,"-",port2_id) FROM racktables_django.api_portinterfacecompat);
    SET inserted = (SELECT count(id) FROM racktables_django.api_portinterfacecompat) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
