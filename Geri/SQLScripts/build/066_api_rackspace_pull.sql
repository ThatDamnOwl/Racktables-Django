DROP FUNCTION IF EXISTS racktables_django.066_api_rackspace_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.066_api_rackspace_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_rackspace);
    INSERT INTO 
        racktables_django.api_rackspace (unitno,state,atom_id,parentobject_id,rack_id) 
        SELECT 
             old.unit_no
            ,CASE
                WHEN state = 'A' THEN 0
                WHEN state = 'U' THEN 1
                ELSE 1
            END as state
            ,atom.id as atom_id
            ,object.id as object_id
            ,rack.id as rack_id
        FROM 
             racktables.RackSpace as old
             LEFT JOIN racktables_django.api_rack as rack on rack.oldid = old.rack_id
             LEFT JOIN racktables_django.api_atom as atom on rack.id = atom.rack_id and old.unit_no = atom.unit_no
             LEFT JOIN racktables_django.api_object as object on object.oldid = old.object_id
        WHERE 
            concat(rack.id,'-',atom.unit_no) NOT IN (SELECT concat(rack_id,'-',unitno) FROM racktables_django.api_rackspace)
            AND ifnull(atom.id,'null') != 'null';

    SET inserted = (SELECT count(id) FROM racktables_django.api_rackspace) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
