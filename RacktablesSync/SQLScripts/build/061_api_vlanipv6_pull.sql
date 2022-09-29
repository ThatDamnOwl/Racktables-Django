DROP FUNCTION IF EXISTS racktables_django.061_api_vlanipv6_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.061_api_vlanipv6_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanipv6);
    INSERT INTO 
        racktables_django.api_vlanipv6 (vlan_id,ipv6net_id) 
        SELECT 
             domain.id
            ,vlan.id
            ,net.id
        FROM 
             racktables.VLANIPv4 as old
             LEFT JOIN racktables_django.api_vlandescription as vlan on vlan.vlan = old.vlan_id
             LEFT JOIN racktables_django.api_ipv6network as net on old.ipv6net_id = net.oldid
        WHERE 
            concat(vlan.id,"-",net.id) NOT IN (SELECT concat(vlan_id,"-",ipv6net_id)  FROM racktables_django.api_vlanipv6);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanipv6) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
