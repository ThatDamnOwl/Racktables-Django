DROP FUNCTION IF EXISTS racktables_django.051_api_plugin_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.051_api_plugin_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_plugin);
    INSERT INTO 
        racktables_django.api_plugin (oldid,name,longname,version,homeurl,state) 
        SELECT 
             name
            ,longname
            ,version
            ,home_url
            ,0
        FROM 
             racktables.Plugin
        WHERE 
            name NOT IN (SELECT name FROM racktables_django.api_plugin);
    SET inserted = (SELECT count(id) FROM racktables_django.api_plugin) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
