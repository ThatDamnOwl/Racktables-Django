DROP FUNCTION IF EXISTS racktables_django.013_api_attributemap_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.013_api_attributemap_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_attributemap);
    INSERT INTO
        racktables_django.api_attributemap (objecttype_id, attribute_id, chapter_id, sticky)
        SELECT
             objtype.id
            ,attribute.id
            ,chapter.id
            ,
            CASE
                WHEN AM.sticky = 'yes' THEN 1
                ELSE 0
            END
        FROM
            racktables.AttributeMap as AM
            LEFT JOIN racktables_django.api_objecttype AS objtype ON objtype_id = objtype.oldid 
            LEFT JOIN racktables_django.api_attribute AS attribute ON attr_id = attribute.oldid
            LEFT JOIN racktables_django.api_chapter AS chapter ON chapter_id = chapter.oldid
        WHERE
            concat(attribute.id,objtype.id,chapter.id) not in
            (
                SELECT concat(attribute.id,objtype.id,chapter.id)
                FROM racktables_django.api_attributemap
                    LEFT JOIN racktables_django.api_objecttype AS objtype ON objecttype_id = objtype.id 
                    LEFT JOIN racktables_django.api_attribute AS attribute ON attribute_id = attribute.id
                    LEFT JOIN racktables_django.api_chapter AS chapter ON chapter_id = chapter.id
            );
        SET inserted = (SELECT count(id) FROM racktables_django.api_attributemap) - inserted;
        RETURN inserted;
END;
$$
DELIMITER ;