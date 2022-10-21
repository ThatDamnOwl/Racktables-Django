DROP FUNCTION IF EXISTS racktables_django.007_api_atom_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.007_api_atom_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_atom);
    INSERT INTO racktables_django.api_atom (xaxis, yaxis, zaxis, molecule_id, rack_id, unit_no)
    SELECT
         7
        ,7
        ,SUM(AtomInt)
        ,molecule_id
        ,rack_id
        ,unit_no
    FROM 
        (
            SELECT
                 molecule.id as molecule_id
                ,rack.id as rack_id
                ,atom.unit_no as unit_no
                ,
                CASE 
                    WHEN atom.atom = 'front' THEN 1
                    WHEN atom.atom = 'interior' THEN 2
                    WHEN atom.atom = 'rear' THEN 4
                END
                AS AtomInt
            FROM 
                racktables.Atom AS atom
                LEFT JOIN racktables_django.api_molecule as molecule on atom.molecule_id = molecule.oldid
                LEFT JOIN racktables_django.api_rack as rack on atom.rack_id = rack.oldid
        ) AS Full_Atom
    WHERE 
        concat(molecule_id,'-',rack_id,'-',unit_no) NOT IN (
            SELECT 
                concat(api_molecule.id,'-',api_rack.id,'-',unit_no)
            FROM racktables_django.api_atom 
                LEFT JOIN racktables_django.api_molecule ON molecule_id = api_molecule.id
                LEFT JOIN racktables_django.api_rack ON rack_id = api_rack.id
        )
    GROUP BY molecule_id,rack_id,unit_no;
    SET inserted = (SELECT count(id) FROM racktables_django.api_atom) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
