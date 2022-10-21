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
             pii.id n_iif_id
            ,poi.id n_oif_id
        FROM 
             racktables.PortInterfaceCompat pic
             LEFT JOIN racktables_django.api_portinnerinterface as pii on pii.oldid = iif_id
             LEFT JOIN racktables_django.api_portouterinterface as poi on poi.oldid = oif_id
        WHERE 
            concat(pii.id,"-",poi.id) NOT IN (SELECT concat(portinnerinterface_id,"-",portouterinterface_id) FROM racktables_django.api_portinterfacecompat);
    SET inserted = (SELECT count(id) FROM racktables_django.api_portinterfacecompat) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
