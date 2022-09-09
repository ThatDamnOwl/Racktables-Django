DROP FUNCTION IF EXISTS racktables_django.030_api_config_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.030_api_config_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_config);
    INSERT INTO 
        racktables_django.api_config (name,value,vartype,nullable,hidden,userdefined,description) 
        SELECT 
               varname
              ,varvalue
              ,CASE
                WHEN vartype = 'string' THEN 1
                WHEN vartype = 'uint' THEN 2
              END as vartype
              ,CASE
                WHEN emptyok = 'yes' THEN 1
                ELSE 0
              END as nullable
              ,CASE
                WHEN is_hidden = 'yes' THEN 1
                ELSE 0
              END as hidden
              ,CASE
                WHEN is_userdefined = 'yes' THEN 1
                ELSE 0
              END as userdefined
              ,ifnull(description,'')
        FROM 
             racktables.Config
        WHERE 
            varname NOT IN (SELECT varname FROM racktables_django.api_config);
    SET inserted = (SELECT count(id) FROM racktables_django.api_config) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
