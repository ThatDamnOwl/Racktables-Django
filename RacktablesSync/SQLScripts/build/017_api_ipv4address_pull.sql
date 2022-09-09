DROP FUNCTION IF EXISTS racktables_django.017_api_ipv4address_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.017_api_ipv4address_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4address);
    INSERT INTO racktables_django.api_ipv4address (ip,name,comment,reserved,oldip)
        SELECT
            racktables_django.parse_ipv4int(ip) as newip
            ,ifnull(name,'') as name
            ,comment
            ,CASE
                WHEN reserved = 'yes' THEN 1
                ELSE 0
            END as reserved
            ,ip as oldip
        FROM
            racktables.IPv4Address
        WHERE  
            ip not in (select oldip from racktables_django.api_ipv4address);

    INSERT INTO racktables_django.api_ipv4address (ip,name,comment,reserved,oldip)
        SELECT
            newip
            ,ifnull(name,'') as name
            ,'' AS comment
            ,1 AS reserved
            ,racktables_django.parse_ipv4toint(newip) as oldip
        FROM
            (
                SELECT 
                     racktables_django.parse_ipbin(vip) as newip
                    ,name
                FROM racktables.IPv4VS
            ) AS VIPInsert
        WHERE  
            newip not in (select ip from racktables_django.api_ipv4address);

    INSERT INTO racktables_django.api_ipv4address (ip,name,comment,reserved,oldip)
        SELECT
            racktables_django.parse_ipv4int(ip)
            ,ifnull(concat(obj.name,"-",ipal.name),'') as name
            ,'' AS comment
            ,1 AS reserved
            ,ip as oldip
        FROM
            racktables.IPv4Allocation as ipal
            LEFT JOIN racktables.Object as obj on object_id = obj.id
        WHERE  
            ip not in (select oldip from racktables_django.api_ipv4address);

    INSERT INTO racktables_django.api_ipv4address (ip,name,comment,reserved,oldip)
        SELECT
            racktables_django.parse_ipv4int(ip)
            ,''
            ,'' AS comment
            ,0 AS reserved
            ,ip as oldip
        FROM
            racktables.IPv4Log as log
        WHERE  
            ip not in (select oldip from racktables_django.api_ipv4address)
        GROUP BY ip;

    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4address) - inserted;
    RETURN inserted;
END;

$$

DELIMITER ;
