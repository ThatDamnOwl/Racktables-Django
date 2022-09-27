DROP FUNCTION IF EXISTS racktables_django.078_api_vlanstrule_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.078_api_vlanstrule_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanstrule);

-- this would be a pain to verify so I'm not doing it at the moment

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanstrule) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
