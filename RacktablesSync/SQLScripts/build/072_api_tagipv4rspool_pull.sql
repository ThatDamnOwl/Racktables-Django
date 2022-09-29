DROP FUNCTION IF EXISTS racktables_django.072_api_tagipv4rspool_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.072_api_tagipv4rspool_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagipv4rspool);
    INSERT INTO 
        racktables_django.api_tagipv4rspool (date,ipv4rspool_id,tag_id,user_id) 
        SELECT 
             old.date
            ,obj.id
            ,tag.id
            ,user.id
        FROM 
             racktables.TagStorage as old
             LEFT JOIN racktables_django.api_ipv4network as obj on obj.oldid = old.entity_id
             LEFT JOIN racktables_django.api_tag as tag on tag.oldid = old.tag_id
             LEFT JOIN racktables_django.api_useraccount as user on user.oldid 
        WHERE
            old.entity_realm = 'ipv4rspool' AND
            concat(obj.id,'-',tag.id,'-',user.id) NOT IN (SELECT concat(ipv4rspool_id,'-',tag_id,'-',user_id) FROM racktables_django.api_tagipv4rspool);
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagipv4rspool) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
