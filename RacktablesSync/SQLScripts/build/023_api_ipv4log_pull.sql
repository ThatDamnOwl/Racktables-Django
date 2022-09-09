DROP FUNCTION IF EXISTS racktables_django.023_api_ipv4log_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.023_api_ipv4log_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4log);
    INSERT INTO 
        racktables_django.api_ipv4log (oldid,date,message,ip_id,user_id) 
        SELECT 
             log.id
            ,date
            ,message
            ,ip.id
            ,user.id
        FROM 
             racktables.IPv4Log COLLATE utf8_unicode_ci AS log
             LEFT JOIN racktables_django.api_ipv4address  COLLATE utf8_unicode_ci as ip on ip.oldip = log.ip
             LEFT JOIN racktables_django.auth_user  COLLATE utf8_unicode_ci as user on user.username = log.user 
        WHERE 
            log.id NOT IN (SELECT oldid FROM racktables_django.api_ipv4log);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4log) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
