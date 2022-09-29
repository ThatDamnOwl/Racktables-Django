DROP FUNCTION IF EXISTS racktables_django.064_api_portvlanmode_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.064_api_portvlanmode_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portvlanmode);

-- skipped because it's impossible to map stuff with the way that the info is stored in the old version of racktables

    SET inserted = (SELECT count(id) FROM racktables_django.api_portvlanmode) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
