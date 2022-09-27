DROP FUNCTION IF EXISTS racktables_django.069_api_tag_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.069_api_tag_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_tag);
    INSERT INTO 
        racktables_django.api_tag (oldid,assignable,name,colour,description,parenttag_id) 
        SELECT 
             old.id
            ,CASE
                WHEN old.assignable = 'yes' THEN 1
                ELSE THEN 0
            END
            ,old.name
            ,old.color
            ,old.description
            ,null
        FROM 
             racktables.TagTree
        WHERE 
            script_name NOT IN (SELECT name FROM racktables_django.api_tag);

    UPDATE
        racktables_django.api_tag AS tag
        ,racktables.TagTree AS old
        ,racktables_django.api_tag as parent
    SET 
        tag.parenttag_id = parent.id
    WHERE
        tag.oldid = old.id AND
        parent.oldid = old.parent_id;

    SET inserted = (SELECT count(id) FROM racktables_django.api_tag) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
