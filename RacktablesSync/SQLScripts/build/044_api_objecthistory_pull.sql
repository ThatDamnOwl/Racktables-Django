DROP FUNCTION IF EXISTS racktables_django.044_api_objecthistory_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.044_api_objecthistory_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_objecthistory);
    INSERT INTO 
        racktables_django.api_objecthistory (oldeventid, oldid, name, label, changedobject_id, assetno, changedtime, user_id, hasproblems, comment) 
        SELECT 
               ObjectHistory.event_id
              ,ObjectHistory.id
              ,ObjectHistory.name
              ,ObjectHistory.label
              ,CO.id
              ,ObjectHistory.asset_no
              ,ctime
              ,US.id
              ,CASE
                WHEN has_problems = 'yes' THEN 1
                ELSE 0
              END
              ,ObjectHistory.comment
        FROM 
             racktables.ObjectHistory
             LEFT JOIN racktables_django.api_object as apiobj on apiobj.oldid = ObjectHistory.id
             LEFT JOIN racktables_django.api_useraccount as user on user.username = ObjectHistory.user_name 
        WHERE 
            ObjectHistory.event_id NOT IN (SELECT oldid FROM racktables_django.api_objecthistory);
    SET inserted = (SELECT count(id) FROM racktables_django.api_objecthistory) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
