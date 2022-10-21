DROP FUNCTION IF EXISTS racktables_django.003_api_molecule_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.003_api_molecule_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_molecule);
    INSERT INTO 
        racktables_django.api_molecule (oldid, description) 
        SELECT 
             id
            ,'' 
        FROM racktables.Molecule
        WHERE 
            id not in (
                SELECT oldid
                FROM racktables_django.api_molecule
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_molecule) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
