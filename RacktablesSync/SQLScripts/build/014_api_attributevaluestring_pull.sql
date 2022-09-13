DROP FUNCTION IF EXISTS racktables_django.012_api_attributevaluestring_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.012_api_attributevaluestring_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_attributevaluestring);
    INSERT INTO
        racktables_django.api_attributevaluestring (parentobject_id, attributemap_id, value)
        SELECT
             parentobject.id
            ,attributemap.attrmap_id
            ,string_value
        FROM
            racktables.AttributeValue
            LEFT JOIN racktables_django.api_object as parentobject on object_id = parentobject.oldid
            LEFT JOIN (
                SELECT 
                     objecttype.oldid as objecttype_oldid
                    ,attribute.oldid as attr_oldid
                    ,attributemap.id as attrmap_id
                    ,attribute.attribute_type as attribute_type
                FROM
                    racktables_django.api_attributemap as attributemap
                    LEFT JOIN racktables_django.api_objecttype as objecttype on objecttype_id = objecttype.id
                    LEFT JOIN racktables_django.api_attribute as attribute on attribute_id = attribute.id 
            ) AS attributemap ON attr_oldid = attr_id AND object_tid = objecttype_oldid
        WHERE
            concat(object_id,'-',attr_id) not in (
                SELECT concat(object.oldid,'-',attribute.oldid)
                FROM racktables_django.api_attributevaluestring as AVS
                    LEFT JOIN racktables_django.api_attributemap AS attrmap ON attributemap_id = attrmap.id
                    LEFT JOIN racktables_django.api_attribute AS attribute ON attrmap.attribute_id = attribute.id
                    LEFT JOIN racktables_django.api_object AS object ON AVS.parentobject_id = object.id
            )
            AND attribute_type = 1;
    SET inserted = (SELECT count(id) FROM racktables_django.api_attributevaluestring) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;