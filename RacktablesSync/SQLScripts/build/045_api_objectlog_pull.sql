DROP FUNCTION IF EXISTS racktables_django.045_api_objectlog_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.045_api_objectlog_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_objectlog);
    INSERT INTO 
        racktables_django.api_objectlog (oldid,date,content,parentobject_id,user_id) 
        SELECT 
               OL.id
              ,OL.date
              ,content
              ,apiobj.id
              ,user.id
        FROM 
             racktables.ObjectHistory as OL
             LEFT JOIN racktables_django.api_object as apiobj on apiobj.oldid = OL.object_id
             LEFT JOIN racktables_django.api_useraccount as user on user.username = OL.user_name 
        WHERE 
            OL.id NOT IN (SELECT oldid FROM racktables_django.api_objectlog)
    SET inserted = (SELECT count(id) FROM racktables_django.api_objectlog) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
