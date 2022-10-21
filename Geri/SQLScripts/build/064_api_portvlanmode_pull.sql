DROP FUNCTION IF EXISTS racktables_django.064_api_portvlanmode_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.064_api_portvlanmode_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portvlanmode);

    INSERT INTO 
        racktables_django.api_portvlanmode (trunk,port_id) 
        SELECT 
             CASE
                WHEN old.vlan_mode = 'trunk' THEN 1
                ELSE 0
              END as trunk
            ,port.id
        FROM 
             racktables.PortVLANMode as old
             LEFT JOIN racktables_django.api_object as object on old.object_id = object.oldid
             LEFT JOIN racktables_django.api_object as port on port.name = old.port_name COLLATE utf8_general_ci
        WHERE 
            port.id NOT IN (SELECT port_id FROM racktables_django.api_portvlanmode);

    SET inserted = (SELECT count(id) FROM racktables_django.api_portvlanmode) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
