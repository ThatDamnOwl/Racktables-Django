DROP FUNCTION IF EXISTS racktables_django.002_api_userconfig_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.002_api_userconfig_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_userconfig);
    INSERT INTO 
        racktables_django.api_userconfig (varname,varvalue,user_id) 
        SELECT 
             varname
            ,varvalue
            ,UA.id
        FROM racktables.UserConfig as UC
            LEFT JOIN racktables_django.api_useraccount as UA on UA.username = UC.user COLLATE utf8_unicode_ci
        WHERE 
            concat(varname,"-",UA.id) not in (
                SELECT concat(varname,"-",user_id) COLLATE utf8_unicode_ci
                FROM racktables_django.api_userconfig
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_userconfig) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
