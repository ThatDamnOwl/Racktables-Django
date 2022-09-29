DROP FUNCTION IF EXISTS racktables_django.059_api_vlandescription_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.059_api_vlandescription_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlandescription);
    INSERT INTO 
        racktables_django.api_vlandescription (domain_id,vlan,vlantype,description) 
        SELECT 
             domain.id
            ,vlan_id
            ,CASE 
                WHEN vlan_type = 'ondemand' THEN 1
                WHEN vlan_type = 'compulsory' THEN 2
                WHEN vlan_type = 'alien' THEN 3
                ELSE 3
            END
            ,description
        FROM 
             racktables.VLANDescription old 
             LEFT JOIN racktables_django.api_vlandomain as domain on old.domain_id = domain.oldid
        WHERE 
            concat(domain.id,"-",vlan_id) NOT IN (SELECT concat(domain_id,"-",vlan_id) FROM racktables_django.api_vlandescription);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlandescription) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
