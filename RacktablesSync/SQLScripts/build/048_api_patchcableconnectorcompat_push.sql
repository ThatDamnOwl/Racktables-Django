DROP FUNCTION IF EXISTS racktables_django.048_api_patchcableconnectorcompat_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.048_api_patchcableconnectorcompat_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableconnectorcompat);
    INSERT INTO 
        racktables_django.api_patchcableconnectorcompat (cabletype_id,connector_id) 
        SELECT 
             pct.id,
             pcc.id
        FROM 
             racktables.PatchCableConnectorCompat as pccc
             LEFT JOIN racktables_django.PatchCableConnector as pcc on pccc.connector_id = pcc.oldid
             LEFT JOIN racktables_django.PatchCableType as pct on pccc.pctype_id = pct.oldid
        WHERE 
            contact(pct.id,"-",pcc.id) NOT IN (SELECT contact(cabletype_id,"-",connector_id) FROM racktables_django.api_patchcableconnectorcompat)
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableconnectorcompat) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
