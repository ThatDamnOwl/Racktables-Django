DROP FUNCTION IF EXISTS racktables_django.083_api_vsenabledips_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.083_api_vsenabledips_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vsenabledips);

    INSERT INTO 
        racktables_django.api_vsenabledips (parentobject_id,parentvs_id,rspool_id,vip_id)
        SELECT 
             obj.id
            ,vs.id
            ,rs.id
            ,ip4.id
        FROM 
             racktables.VSEnabledIPs as old
             LEFT JOIN racktables_django.api_object as obj on obj.oldid = old.object_id
             LEFT JOIN racktables_django.api_vs as vs on vs.oldid = old.parentvs_id
             LEFT JOIN racktables_django.api_ipv4rspool as rs on rs.oldid = old.rspool_id
             LEFT JOIN racktables_django.api_ipv4address as ip4 on BIN(ip4.oldip) = old.vip
        WHERE 
            concat(obj.id,'-',ip4.id) NOT IN (SELECT concat(parentobject_id,'-',vip_id) FROM racktables_django.api_vsenabledips);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vsenabledips) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
