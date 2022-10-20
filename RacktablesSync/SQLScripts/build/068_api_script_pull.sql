DROP FUNCTION IF EXISTS racktables_django.068_api_script_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.068_api_script_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_script);
    INSERT INTO 
        racktables_django.api_script (name,content) 
        SELECT 
             old.script_name
            ,old.script_text
        FROM 
             racktables.Script as old
        WHERE 
            script_name NOT IN (SELECT name COLLATE utf8_general_ci FROM racktables_django.api_script);

    SET inserted = (SELECT count(id) FROM racktables_django.api_script) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
