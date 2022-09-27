DROP FUNCTION IF EXISTS racktables_django.080_api_vlanswitch_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.080_api_vlanswitch_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanswitch);

    INSERT INTO 
        racktables_django.api_vlanswitch (revision,lasterror,lasterroroccured,changed,pushstarted,pushended,domain_id,parentobject_id,template_id) 
        SELECT 
             old.revision
            ,old.last_errno
            ,old.last_error_ts
            ,old.last_change
            ,old.last_push_started
            ,old.last_push_ended
            ,domain.id
            ,object.id
            ,template.id
        FROM 
             racktables.VLANSwitch as old
             LEFT JOIN racktables_django.api_vlandomain as domain on domain.oldid = old.domain_id
             LEFT JOIN racktables_django.api_object as object on object.oldid = old.object_id
             LEFT JOIN racktables_django.api_vlanswitchtemplate as template on template.oldid = old.template_id
        WHERE 
            concat(domain.id,'-',object.id,'-',template.id) NOT IN (SELECT concat(domain_id,'-',parentobject_id,'-',template_id) FROM racktables_django.api_vlanswitch);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanswitch) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
