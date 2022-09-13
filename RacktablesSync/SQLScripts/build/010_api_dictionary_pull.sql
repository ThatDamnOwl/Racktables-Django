DROP FUNCTION IF EXISTS racktables_django.008_api_dictionary_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.008_api_dictionary_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_dictionary);
    INSERT INTO
        racktables_django.api_dictionary (sticky, value, chapter_id, oldid)
        SELECT
            CASE 
                WHEN dict_sticky = 'yes' THEN 1 
                ELSE 0
            END
            ,dict_value
            ,chapter.id
            ,dict_key
        FROM
            racktables.Dictionary LEFT JOIN
            racktables_django.api_chapter AS chapter ON oldid = chapter_id
        WHERE
            dict_key not in (
                SELECT oldid
                FROM racktables_django.api_dictionary
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_dictionary) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
