DROP FUNCTION IF EXISTS racktables_django.063_api_portlog_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.063_api_portlog_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portlog);
    INSERT INTO 
        racktables_django.api_portlog (oldid,date,comment,port_id,user_id) 
        SELECT 
             old.id
            ,old.date
            ,old.comment
            ,port.id
            ,user.id
        FROM 
             racktables.PortAllowedVlan as old
             LEFT JOIN racktables_django.api_useraccount as user on user.oldid = old.user_id
             LEFT JOIN racktables_django.api_port as port on port.oldid = old.port_id
        WHERE 
            old.id NOT IN (SELECT oldid FROM racktables_django.api_portlog);

    SET inserted = (SELECT count(id) FROM racktables_django.api_portlog) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
