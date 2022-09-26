DROP FUNCTION IF EXISTS racktables_django.058_api_vlandomain_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.058_api_vlandomain_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlandomain);
    INSERT INTO 
        racktables_django.api_vlandomain (oldid,parentdomain,description) 
        SELECT 
             id
            ,null
            ,description
        FROM 
             racktables.VLANDomain
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_vlandomain);

    UPDATE
         racktables_django.api_vlandomain as BaseDomain
        ,racktables.VLANDomain as OldDomain
        ,racktables_django.api_vlandomain as ParentDomain
    SET
        BaseDomain.parentdomain = ParentDomain.id
    WHERE 
        BaseDomain.oldid = OldDomain.id AND
        ParentDomain.oldid = OldDomain.group_id;

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlandomain) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
