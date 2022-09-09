DROP FUNCTION IF EXISTS racktables_django.025_api_ipv4network_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.025_api_ipv4network_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4network);
    INSERT INTO 
        racktables_django.api_ipv4network (oldid, ip, oldip, mask, name, comment) 
        SELECT 
              id
             ,INET6_NTOA(ip)
             ,ip
             ,mask
             ,ifnull(name,'')
             ,ifnull(comment,'')
        FROM
            racktables.IPv6Address
        Where
            id not in (SELECT oldid from racktables_django.api_ipv4network);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4network) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
