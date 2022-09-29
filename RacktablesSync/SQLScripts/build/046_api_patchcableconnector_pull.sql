DROP FUNCTION IF EXISTS racktables_django.046_api_patchcableconnector_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.046_api_patchcableconnector_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableconnector);
    INSERT INTO 
        racktables_django.api_patchcableconnector (oldid,defaultvalue,connectorname) 
        SELECT
             PatchCableConnector.id
            ,CASE
                WHEN PatchCableConnector.origin = 'default' THEN 1
                ELSE 0
              END
            ,connector
        FROM 
             racktables.PatchCableConnector
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_patchcableconnector);
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableconnector) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
