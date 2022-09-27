DROP FUNCTION IF EXISTS racktables_django.073_api_tagipv4vs_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.073_api_tagipv4vs_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagipv4vs);
    INSERT INTO 
        racktables_django.api_tagipv4vs (date,ipv4vs_id,tag_id,user_id) 
        SELECT 
             old.date
            ,obj.id
            ,tag.id
            ,user.id
        FROM 
             racktables.TagStorage as old
             LEFT JOIN racktables_django.api_ipv4vs as obj on obj.oldid = old.entity_id
             LEFT JOIN racktables_django.api_tag as tag on tag.oldid = old.tag_id
             LEFT JOIN racktables_django.api_useraccount as user on user.oldid 
        WHERE
            old.entity_realm = 'ipv4vs'
            concat(obj.id,'-',tag.id,'-',user.id) NOT IN (SELECT concat(ipv4vs_id,'-',tag_id,'-',user_id) FROM racktables_django.api_tagipv4vs)
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagipv4vs) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
