DROP FUNCTION IF EXISTS racktables_django.079_api_vlanswitchtemplate_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.079_api_vlanswitchtemplate_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanswitchtemplate);

    INSERT INTO 
        racktables_django.api_vlanswitchtemplate (oldid,revision,description,modifiedby_id) 
        SELECT 
             old.id
            ,old.mutex_rev
            ,old.description
            ,usr.id
        FROM 
             racktables.VLANSwitchTemplate as old
             LEFT JOIN racktables_django.api_useraccount as usr on old.saved_by = usr.username COLLATE utf8_unicode_ci
        WHERE 
            old.id NOT IN (SELECT oldid FROM racktables_django.api_vlanswitchtemplate);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanswitchtemplate) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
