DROP FUNCTION IF EXISTS racktables_django.009_api_objecttype_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.009_api_objecttype_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_objecttype);

    INSERT INTO
        racktables_django.api_objecttype (sticky, name, oldid)
        SELECT
            CASE 
                WHEN dict_sticky = 'yes' THEN 1 
                ELSE 0
            END
            ,dict_value
            ,dict_key
        FROM
            racktables.Dictionary
        WHERE
            chapter_id = 1
            AND
            dict_key not in (
                SELECT oldid
                FROM racktables_django.api_objecttype
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_objecttype) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
