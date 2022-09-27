DROP FUNCTION IF EXISTS racktables_django.062_api_portallowedvlan_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.062_api_portallowedvlan_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portallowedvlan);
    INSERT INTO 
        racktables_django.api_portallowedvlan (native,port_id,vlan_id) 
        SELECT 
             0
            ,vlan.id
            ,port.id
        FROM 
             racktables.PortAllowedVlan as old
             LEFT JOIN racktables_django.api_vlan as vlan on vlan.id = old.vlan_id
             LEFT JOIN racktables_django.api_object as obj on obj.oldif = old.object_id
             LEFT JOIN racktables_django.api_port as port on port.parentobject_id = obj.id AND port.name = old.port_name
        WHERE 
            concat(domain.id,"-",vlan.id,"-",net.id) NOT IN (SELECT concat(domain_id,"-",vlan_id,"-",net_id)  FROM racktables_django.api_portallowedvlan);

    SET inserted = (SELECT count(id) FROM racktables_django.api_portallowedvlan) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
