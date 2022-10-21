DROP FUNCTION IF EXISTS racktables_django.023_api_ipv4rs_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.023_api_ipv4rs_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rs);
    INSERT INTO racktables_django.api_ipv4rs (oldid,inservice,oldrsip,rsport,rspool_id,rsip_id,rsconfig,comment)
    SELECT 
           old.id
          ,CASE
              WHEN inservice = 'yes' THEN 1
              ELSE 0
          END as inservice
          ,old.rsip
          ,old.rsport
          ,rs.id as rs_id
          ,ip.id as ip_id
          ,old.rsconfig
          ,old.comment
    FROM
        racktables.IPv4RS AS old
        LEFT JOIN racktables_django.api_ipv4address as ip on ip.ip = concat('::ffff:',INET6_NTOA(rsip))
        LEFT JOIN racktables_django.api_ipv4rspool as rs on rs.oldid = rspool_id
    WHERE
        rs.id NOT IN (select oldid from racktables_django.api_ipv4rs);

    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rs) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
