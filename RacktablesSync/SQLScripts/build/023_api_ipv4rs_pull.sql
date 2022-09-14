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
           rs.id
          ,CASE
              WHEN inservice = 'yes' THEN 1
              ELSE 0
          END 
          ,rs.rsip
          ,rs.rsport
          ,rspool.id
          ,ip.id
          ,rs.rsconfig
          ,rs.comment
    FROM
        racktables.IPv4RS AS rs
        LEFT JOIN racktables_django.api_ipv4address as ip on ip.ip = racktables_django.parse_ipv4toint(racktables_django.parse_ipbin(rsip))
        LEFT JOIN racktables_django.api_ipv4rspool as rs on rs.oldid = rspool_id
    WHERE
        rs.id NOT IN (select oldid from racktables_django.api_ipv4rs);

    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rs) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
