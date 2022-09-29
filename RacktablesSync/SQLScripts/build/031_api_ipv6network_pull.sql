DROP FUNCTION IF EXISTS racktables_django.031_api_ipv6network_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.031_api_ipv6network_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6network);
    INSERT INTO 
        racktables_django.api_ipv6network (oldid,ip,oldip,mask,lastip,oldlastip,name,comment) 
        SELECT 
              id
             ,INET6_NTOA(ip)
             ,ip
             ,mask
             ,INET6_NTOA(last_ip)
             ,last_ip
             ,ifnull(name,'')
             ,ifnull(comment,'')
        FROM 
             racktables.IPv6Network
        WHERE 
            ip NOT IN (SELECT oldip FROM racktables_django.api_ipv6network);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6network) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
