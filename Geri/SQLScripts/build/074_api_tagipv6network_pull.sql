DROP FUNCTION IF EXISTS racktables_django.074_api_tagipv6network_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.074_api_tagipv6network_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagipv6network);
    INSERT INTO 
        racktables_django.api_tagipv6network (date,ipv6network_id,tag_id,user_id) 
        SELECT 
             old.date
            ,obj.id
            ,tag.id
            ,user.id
        FROM 
             racktables.TagStorage as old
             LEFT JOIN racktables_django.api_ipv6network as obj on obj.oldid = old.entity_id
             LEFT JOIN racktables_django.api_tag as tag on tag.oldid = old.tag_id
             LEFT JOIN racktables_django.api_useraccount as user on user.oldid 
        WHERE
            old.entity_realm = 'ipv6net' AND
            concat(obj.id,'-',tag.id,'-',user.id) NOT IN (SELECT concat(ipv6network_id,'-',tag_id,'-',user_id) FROM racktables_django.api_tagipv6network);
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagipv6network) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
