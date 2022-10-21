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
             old.mutex_rev
            ,old.last_errno
            ,CASE 
                WHEN old.last_error_ts = 0 THEN '1970/01/01 00:00:01'
                ELSE old.last_error_ts
             END as last_error_time
            ,CASE 
                WHEN old.last_change = 0 THEN '1970/01/01 00:00:01'
                ELSE old.last_change
             END as last_change_time
            ,CASE 
                WHEN old.last_push_started = 0 THEN '1970/01/01 00:00:01'
                ELSE old.last_push_started
             END as last_push_started_time
            ,CASE 
                WHEN old.last_push_finished = 0 THEN '1970/01/01 00:00:01'
                ELSE old.last_push_finished
             END as last_push_finished_time
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
