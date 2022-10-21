DROP FUNCTION IF EXISTS racktables_django.060_api_vlanipv4_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.060_api_vlanipv4_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanipv4);
    INSERT INTO 
        racktables_django.api_vlanipv4 (vlan_id,ipv4net_id) 
        SELECT 
             vlan.id
            ,net.id
        FROM 
             racktables.VLANIPv4 as old
             LEFT JOIN racktables_django.api_vlandescription as vlan on vlan.vlan = old.vlan_id
             LEFT JOIN racktables_django.api_ipv4network as net on old.ipv4net_id = net.oldid
        WHERE 
            concat(vlan.id,"-",net.id) NOT IN (SELECT concat(vlan_id,"-",ipv4net_id)  FROM racktables_django.api_vlanipv4);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanipv4) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
