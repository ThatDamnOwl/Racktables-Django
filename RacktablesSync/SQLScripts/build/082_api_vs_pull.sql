DROP FUNCTION IF EXISTS racktables_django.082_api_vs_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.082_api_vs_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vs);

    INSERT INTO 
        racktables_django.api_vs (oldid,name,vsconfig,rsconfig) 
        SELECT 
             old.id
            ,old.name
            ,old.vsconfig
            ,old.rsconfig
        FROM 
             racktables.VS as old
        WHERE 
            old.id NOT IN (SELECT vlanid FROM racktables_django.api_vs);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vs) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
