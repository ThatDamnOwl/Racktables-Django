DROP FUNCTION IF EXISTS racktables_django.024_api_ipv4lb_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.024_api_ipv4lb_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rspool);
    INSERT INTO 
        racktables_django.api_ipv4lb (prio, vsconfig, rsconfig, parentipv4rspool_id, parentipv4vs_id, parentobject_id) 
        SELECT 
             lb.prio
            ,lb.vsconfig
            ,lb.rsconfig
            ,parentipv4rspool.id
            ,parentipv4vs.id
            ,parentobject.id
        FROM 
             racktables.IPv4LB AS lb
             LEFT JOIN racktables_django.api_ipv4rspool as parentipv4rspool on parentipv4rspool.oldid = lb.rspool_id
             LEFT JOIN racktables_django.api_ipv4vs as parentipv4vs on parentipv4vs.oldid = lb.vs_id
             LEFT JOIN racktables_django.api_object as parentobject on parentobject.oldid = lb.object_id
        WHERE 
            concat(parentipv4rspool.id,"-",parentipv4vs.id,"-",parentobject.id) not in (
                SELECT concat(parentipv4rspool_id,"-",parentipv4vs_id,"-",parentobject_id)
                FROM racktables_django.api_ipv4lb
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rspool) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
