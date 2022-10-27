DROP FUNCTION IF EXISTS racktables_django.050_api_patchcableheaplog_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.050_api_patchcableheaplog_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableheaplog);
    INSERT INTO 
        racktables_django.api_patchcableheaplog (oldid,date,comment,heap_id,user_id) 
        SELECT 
             old.id
            ,date
            ,old.message
            ,pch.id
            ,ua.id
        FROM 
             racktables.PatchCableHeapLog as old
             LEFT JOIN racktables_django.api_patchcableheap as pch on heap_id = pch.oldid
             LEFT JOIN racktables_django.api_useraccount as ua on user_id = ua.id
        WHERE 
            old.id NOT IN (SELECT oldid FROM racktables_django.api_patchcableheaplog);
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableheaplog) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
