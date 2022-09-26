DROP FUNCTION IF EXISTS racktables_django.060_api_vlanipv4_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.060_api_vlanipv4_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanipv4);
    INSERT INTO 
        racktables_django.api_vlanipv4 (domain_id,vlan_id,ipv4net_id) 
        SELECT 
             domain.id
            ,vlan.id
            ,net.id
        FROM 
             racktables.VLANIPv4 as old
             LEFT JOIN racktables_django.api_vlandomain as domain on old.id = domain.oldid
             LEFT JOIN racktables_django.api_vlan as vlan on vlan.id = old.vlan_id AND domain.id = vlan.domain_id
             LEFT JOIN racktables_django.api_ipv4network as net on old.ipv4net_id = net.oldid
        WHERE 
            concat(domain.id,"-",vlan.id,"-",net.id) NOT IN (SELECT concat(domain_id,"-",vlan_id,"-",net_id)  FROM racktables_django.api_vlanipv4);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanipv4) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
