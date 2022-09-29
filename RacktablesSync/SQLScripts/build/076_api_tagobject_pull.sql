DROP FUNCTION IF EXISTS racktables_django.076_api_tagobject_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.076_api_tagobject_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagobject);
    INSERT INTO 
        racktables_django.api_tagobject (date,object_id,tag_id,user_id) 
        SELECT 
             old.date
            ,obj.id
            ,tag.id
            ,user.id
        FROM 
             racktables.TagStorage as old
             LEFT JOIN racktables_django.api_location as obj on obj.oldid = old.entity_id
             LEFT JOIN racktables_django.api_tag as tag on tag.oldid = old.tag_id
             LEFT JOIN racktables_django.api_useraccount as user on user.oldid 
        WHERE
            old.entity_realm = 'object' AND
            concat(obj.id,'-',tag.id,'-',user.id) NOT IN (SELECT concat(object_id,'-',tag_id,'-',user_id) FROM racktables_django.api_tagobject);
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagobject) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
