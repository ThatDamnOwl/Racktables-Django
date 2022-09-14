DROP FUNCTION IF EXISTS racktables_django.009_api_chapter_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.009_api_chapter_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_chapter);

    INSERT INTO
        racktables_django.api_chapter (sticky, name, oldid)
        SELECT
            CASE 
                WHEN sticky = 'yes' THEN 1 
                ELSE 0
            END
            ,name
            ,id
        FROM
            racktables.Chapter
        WHERE
            id not in (
                SELECT oldid
                FROM racktables_django.api_chapter
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_chapter) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
