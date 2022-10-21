DROP FUNCTION IF EXISTS racktables_django.084_api_vsenabledports_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.084_api_vsenabledports_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vsenabledports);

    INSERT INTO 
        racktables_django.api_vsenabledports (protocol,parentobject_id,parentvs_id,port_id,rspool_id)
        SELECT 
             CASE
                WHEN old.proto = 'TCP' THEN 1
                WHEN old.proto = 'UDP' THEN 2
                WHEN old.proto = 'MARK' THEN 4
             END
            ,obj.id
            ,vs.id
            ,port.id
            ,rs.id
        FROM 
             racktables.VSEnabledPorts as old
             LEFT JOIN racktables_django.api_object as obj on obj.oldid = old.object_id
             LEFT JOIN racktables_django.api_vs as vs on vs.oldid = old.vs_id
             LEFT JOIN racktables_django.api_ipv4rspool as rs on rs.oldid = old.rspool_id
             LEFT JOIN racktables_django.api_port as port on port.oldid = old.vport
        WHERE 
            concat(obj.id,'-',vs.id,'-',port.id,'-',rs.id) NOT IN (SELECT concat(parentobject_id,'-',parentvs_id,'-',port_id,'-',rspool_id) FROM racktables_django.api_vsenabledports);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vsenabledports) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
