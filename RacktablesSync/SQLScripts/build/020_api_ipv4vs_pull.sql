DROP FUNCTION IF EXISTS racktables_django.020_api_ipv4vs_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.020_api_ipv4vs_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4vs);
    INSERT INTO racktables_django.api_ipv4vs (oldid,oldvip,vport,protocol,name,vsconfig,rsconfig,vip_id)
        SELECT 
                 ipv4vsnewip.id
                ,vip
                ,vport
                ,CASE 
                    WHEN protocol = 'TCP' THEN 1 
                    WHEN protocol = 'UDP' THEN 2
                    WHEN protocol = 'MARK' THEN 4
                END AS protocol
                ,ifnull(ipv4vsnewip.name,'')
                ,ifnull(vsconfig,'')
                ,ifnull(rsconfig,'')
                ,ipal.id
        FROM
            (
                SELECT 
                        id
                       ,vip
                       ,vport
                       ,proto as protocol
                       ,name
                       ,vsconfig
                       ,rsconfig
                       ,racktables_django.parse_ipbin(vip) as newip
                FROM
                    racktables.IPv4VS
            ) AS ipv4vsnewip
            LEFT JOIN
                racktables_django.api_ipv4address as ipal on newip = ipal.ip
        where
            ipv4vsnewip.id NOT IN (
                SELECT 
                    oldid
                FROM
                    racktables_django.api_ipv4vs
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4vs) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
