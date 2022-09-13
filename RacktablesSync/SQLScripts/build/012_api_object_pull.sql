DROP FUNCTION IF EXISTS racktables_django.010_api_object_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.010_api_object_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_object);
    INSERT INTO
        racktables_django.api_object (oldid, name, label, assetno, hasproblems, comment, objecttype_id, parentobject_id)
        SELECT
             object.id
            ,ifnull(object.name,'')
            ,ifnull(object.label,'')
            ,ifnull(object.asset_no,'')
            ,
            CASE
                WHEN object.has_problems = 'yes' THEN 1
                ELSE 0
            END
            ,ifnull(object.comment,'')
            ,objecttype.id
            ,NULL
        FROM
            racktables.Object as object LEFT JOIN
            racktables_django.api_objecttype as objecttype on oldid = objtype_id
        WHERE
            object.id not in (
                SELECT oldid
                FROM racktables_django.api_object
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_object) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
