DROP FUNCTION IF EXISTS racktables_django.044_api_objecthistory_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.044_api_objecthistory_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_objecthistory);
    INSERT INTO 
        racktables_django.api_objecthistory (oldid,changedtime,hasproblems,comment,change,oldvalue,changedobject_id,user_id) 
        SELECT 
               OH.event_id
              ,ctime
              ,CASE
                WHEN has_problems = 'yes' THEN 1
                ELSE 0
              END
              ,comment
              ,change
              ,oldvalue
              ,CO.id
              ,US.id
        FROM 
             racktables.ObjectHistory as OH
             LEFT JOIN racktables_django.api_object as apiobj on apiobj.oldid = OH.id
             LEFT JOIN racktables_django.api_useraccount as user on user.username = OH.user_name 
        WHERE 
            OH.event_id NOT IN (SELECT oldid FROM racktables_django.api_objecthistory)
    SET inserted = (SELECT count(id) FROM racktables_django.api_objecthistory) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
