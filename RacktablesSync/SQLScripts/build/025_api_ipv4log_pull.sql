DROP FUNCTION IF EXISTS racktables_django.025_api_ipv4log_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.025_api_ipv4log_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4log);
    INSERT INTO 
        racktables_django.api_ipv4log (oldid,date,message,ip_id,user_id) 
        SELECT 
             IPv4Log.id
            ,date
            ,message
            ,ip4.id
            ,user.id
        FROM 
             racktables.IPv4Log 
             LEFT JOIN racktables_django.api_ipv4address as ip4 on ip4.oldip = IPv4Log.ip COLLATE utf8_unicode_ci 
             LEFT JOIN racktables_django.api_useraccount as user on user.username = IPv4Log.user COLLATE utf8_unicode_ci 
        WHERE 
            IPv4Log.id NOT IN (SELECT oldid FROM racktables_django.api_ipv4log);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4log) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
