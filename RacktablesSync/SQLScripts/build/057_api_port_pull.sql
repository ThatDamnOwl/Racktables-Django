DROP FUNCTION IF EXISTS racktables_django.057_api_port_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.057_api_port_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_port);
    INSERT INTO 
        racktables_django.api_port (oldid,name,label,comment,l2address,attachedport_id,innerinterface_id,outerinterface_id,parentobject_id,patch_id) 
        SELECT 
             old.id
            ,old.name
            ,ifnull(old.label,'')
            ,ifnull(old.reservation_comment,'')
            ,ifnull(old.l2address,'')
            ,null
            ,ii.id
            ,oi.id
            ,po.id
            ,null
        FROM 
             racktables.Port as old
             LEFT JOIN racktables_django.api_portinnerinterface as ii on ii.oldid = old.iif_id
             LEFT JOIN racktables_django.api_portinterfacecompat as oi on ii.id = oi.portinnerinterface_id
             LEFT JOIN racktables_django.api_object as po on po.oldid = old.object_id
        WHERE
            old.id NOT IN (SELECT oldid FROM racktables_django.api_port);
    SET inserted = (SELECT count(id) FROM racktables_django.api_port) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
