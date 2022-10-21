DROP FUNCTION IF EXISTS racktables_django.065_api_rackobject_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.065_api_rackobject_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_rackobject);
    INSERT INTO 
        racktables_django.api_rackobject (oldid,name,label,assetno,hasproblems,comment,objecttype_id,linkedobject_id) 
        SELECT 
             old.id
            ,ifnull(old.name,"")
            ,ifnull(old.label,"")
            ,ifnull(old.asset_no,"")
            ,CASE 
                WHEN old.has_problems = 'yes' THEN 1
                ELSE 0
             END
            ,ifnull(old.comment,"")
            ,objecttype.id
            ,linkedobject.id
        FROM 
             racktables.RackObject as old
             LEFT JOIN racktables_django.api_objecttype as objecttype on objecttype.oldid = old.objtype_id
             LEFT JOIN racktables_django.api_object as linkedobject on linkedobject.name = old.asset_no COLLATE utf8_general_ci
        WHERE 
            old.id NOT IN (SELECT oldid FROM racktables_django.api_rackobject);

    SET inserted = (SELECT count(id) FROM racktables_django.api_rackobject) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
