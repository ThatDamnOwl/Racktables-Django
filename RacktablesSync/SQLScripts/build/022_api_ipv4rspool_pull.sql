DROP FUNCTION IF EXISTS racktables_django.022_api_ipv4rspool_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.022_api_ipv4rspool_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rspool);
    INSERT INTO 
        racktables_django.api_ipv4rspool (oldid, name, vsconfig, rsconfig) 
        SELECT 
             id
            ,name
            ,ifnull(vsconfig,'')
            ,ifnull(rsconfig,'')
        FROM racktables.IPv4RSPool
        WHERE 
            id not in (
                SELECT oldid
                FROM racktables_django.api_ipv4rspool
            );
        SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rspool) - inserted;
        RETURN inserted;
END;
$$
DELIMITER ;
