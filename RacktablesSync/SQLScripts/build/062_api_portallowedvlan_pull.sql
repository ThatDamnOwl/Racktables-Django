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
             racktables.PortAllowedVLAN as old
             LEFT JOIN racktables_django.api_vlandescription as vlan on vlan.id = old.vlan_id
             LEFT JOIN racktables_django.api_object as obj on obj.oldid = old.object_id
             LEFT JOIN racktables_django.api_port as port on port.parentobject_id = obj.id AND port.name = old.port_name COLLATE utf8_general_ci
        WHERE 
            concat(port.id,"-",vlan.id) NOT IN (SELECT concat(port_id,"-",vlan_id) FROM racktables_django.api_portallowedvlan);

    SET inserted = (SELECT count(id) FROM racktables_django.api_portallowedvlan) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
