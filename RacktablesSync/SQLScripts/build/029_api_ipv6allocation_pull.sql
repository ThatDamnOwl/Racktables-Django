DROP FUNCTION IF EXISTS racktables_django.027_api_ipv6allocation_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.027_api_ipv6allocation_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6allocation);
    INSERT INTO 
        racktables_django.api_ipv6allocation (name, alloctype, ip_id, parentobject_id) 
        select 
             ipal.name
            ,CASE
                WHEN type = 'regular' THEN 1
                WHEN type = 'shared' THEN 2
                WHEN type = 'virtual' THEN 3
                WHEN type = 'router' THEN 4
                WHEN type = 'point2point' THEN 5
                WHEN type = 'sharedrouter' THEN 6
            END as alloctype
            ,ipa.id
            ,obj.id
        FROM
            racktables.IPv6Allocation AS ipal
            LEFT JOIN racktables_django.api_ipv6address as ipa on ipal.ip = ipa.oldip
            LEFT JOIN racktables_django.api_object as obj on object_id = obj.oldid
        where
            concat(ipal.name,"-",ipal.ip,"-",object_id) COLLATE utf8_unicode_ci NOT IN (
                SELECT 
                    concat(ipal.name,"-",ipa.oldip,"-",obj.oldid) COLLATE utf8_unicode_ci
                FROM
                    racktables_django.api_ipv6allocation as ipal
                    LEFT JOIN racktables_django.api_ipv6address as ipa on ip_id = ipa.id
                    LEFT JOIN racktables_django.api_object as obj on ipal.parentobject_id = obj.id);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6allocation) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
