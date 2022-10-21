DROP FUNCTION IF EXISTS racktables_django.047_api_patchcabletype_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.047_api_patchcabletype_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcabletype);
    INSERT INTO 
        racktables_django.api_patchcabletype (oldid,defaultvalue,cabletype) 
        SELECT 
             id
            ,CASE
                WHEN origin = 'default' THEN 1
                ELSE 0
              END
            ,pctype
        FROM 
             racktables.PatchCableType
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_patchcabletype);
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcabletype) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
