DROP FUNCTION IF EXISTS racktables_django.081_api_vlanvalidid_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.081_api_vlanvalidid_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanvalidid);

    INSERT INTO 
        racktables_django.api_vlanvalidid (vlanid) 
        SELECT 
             old.vlan_id
        FROM 
             racktables.VLANValidID as old
        WHERE 
            old.vlan_id NOT IN (SELECT vlanid FROM racktables_django.api_vlanvalidid);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanvalidid) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
