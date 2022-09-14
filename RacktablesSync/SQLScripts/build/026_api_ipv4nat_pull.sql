DROP FUNCTION IF EXISTS racktables_django.026_api_ipv4nat_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.026_api_ipv4nat_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4nat);
    INSERT INTO 
        racktables_django.api_ipv4nat (localip_id, localport, remoteip_id, remoteport, protocol, description) 
        SELECT 
              localip.id
             ,localport
             ,remoteip.id
             ,remoteport
             ,CASE
                WHEN proto = 'tcp' THEN 1
                WHEN proto = 'udp' THEN 2
                WHEN proto = 'mark' THEN 4
            END
             ,description
        FROM 
             racktables.IPv4NAT as nat
             LEFT JOIN racktables_django.api_ipv4address AS localip on localip.oldip = nat.localip
             LEFT JOIN racktables_django.api_ipv4address AS remoteip on remoteip.oldip = nat.remoteip
        WHERE 
            concat(localip.id,"-",remoteip.id) NOT IN (SELECT concat(localip_id,"-",remoteip_id) FROM racktables_django.api_ipv4nat);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4nat) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
