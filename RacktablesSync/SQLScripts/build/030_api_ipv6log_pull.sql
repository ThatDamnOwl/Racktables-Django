DROP FUNCTION IF EXISTS racktables_django.030_api_ipv6log_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.030_api_ipv6log_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6log);
    INSERT INTO 
        racktables_django.api_ipv6log (oldid,date,message,ip_id,user_id) 
        SELECT 
             log.id
            ,date
            ,message
            ,ip.id
            ,user.id
        FROM 
             racktables.IPv6Log AS log
             LEFT JOIN racktables_django.api_ipv6address as ip on ip.oldip = log.ip
             LEFT JOIN racktables_django.api_useraccount as user on user.username = log.user COLLATE utf8_unicode_ci 
        WHERE 
            log.id NOT IN (SELECT oldid FROM racktables_django.api_ipv6log);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6log) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
