DROP FUNCTION IF EXISTS racktables_django.054_api_patchcableoifcompat_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.054_api_patchcableoifcompat_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableoifcompat);
    INSERT INTO 
        racktables_django.api_patchcableoifcompat (cabletype_id,interfacetype_id) 
        SELECT 
             pct.id as pct_id
            ,poi.id as poi_id
        FROM 
             racktables.PatchCableOIFCompat as old
             LEFT JOIN racktables_django.api_portouterinterface as poi on poi.oldid = old.oif_id
             LEFT JOIN racktables_django.api_patchcabletype as pct on pct.oldid = old.pctype_id
        WHERE 
            concat(pct.id,"-",poi.id) NOT IN (SELECT concat(cabletype_id,"-",interfacetype_id) FROM racktables_django.api_patchcableoifcompat);
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableoifcompat) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
