DROP FUNCTION IF EXISTS racktables_django.028_api_ipv6address_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.028_api_ipv6address_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6address);
    INSERT INTO 
        racktables_django.api_ipv6address (ip, oldip, name, comment, reserved) 
        SELECT 
             INET6_NTOA(ip)
             ,ip
             ,ifnull(name,'')
             ,ifnull(comment,'')
             ,CASE
                WHEN reserved = 'yes' THEN 1
                ELSE 0
            END as reserved
        FROM
            racktables.IPv6Address
        Where
            ip not in (SELECT oldip from racktables_django.api_ipv6address);

    INSERT INTO racktables_django.api_ipv6address (ip, oldip, name, comment, reserved) 
        SELECT
            INET6_NTOA(ip)
            ,ip
            ,ifnull(concat(obj.name,"-",ipal.name),'') as name
            ,'' AS comment
            ,1 AS reserved
        FROM
            racktables.IPv6Allocation as ipal
            LEFT JOIN racktables.Object as obj on object_id = obj.id
        WHERE  
            ip not in (select oldip from racktables_django.api_ipv6address);

    INSERT INTO racktables_django.api_ipv6address (ip, oldip, name, comment, reserved) 
        SELECT
            INET6_NTOA(ip)
            ,''
            ,'' AS comment
            ,0 AS reserved
            ,ip as oldip
        FROM
            racktables.IPv6Log as log
        WHERE  
            ip not in (select oldip from racktables_django.api_ipv6address)
        GROUP BY ip;

    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6address) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
