DROP FUNCTION IF EXISTS racktables_django.049_api_patchcableheap_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.049_api_patchcableheap_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableheap);
    INSERT INTO 
        racktables_django.api_patchcableheap (oldid,amount,colour,length,description,cabletype_id,end1_id,end2_id) 
        SELECT 
             old.id
            ,old.amount
            ,(X'000000')
            ,old.length
            ,old.description
            ,pct.id
            ,pcc1.id
            ,pcc2.id
        FROM 
             racktables.PatchCableHeap as old
             LEFT JOIN racktables_django.api_patchcabletype as pct on pct.oldid = pctype_id
             LEFT JOIN racktables_django.api_patchcableconnector as pcc1 on pcc1.oldid = end1_conn_id
             LEFT JOIN racktables_django.api_patchcableconnector as pcc2 on pcc2.oldid = end2_conn_id
        WHERE 
            old.id NOT IN (SELECT oldid FROM racktables_django.api_patchcableheap);
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableheap) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
