    SELECT
         parentobject.id
        ,attributemap.attrmap_id
        ,attributemap.attribute_type
        ,attributemap.attr_oldid
        ,string_value
        ,uint_value
        ,float_value
    FROM
        racktables.AttributeValue
        LEFT JOIN racktables_django.api_object as parentobject on object_id = parentobject.oldid
        LEFT JOIN (
            SELECT 
                 objecttype.oldid as objecttype_oldid
                ,attribute.oldid as attr_oldid
                ,attribute.attribute_type as attribute_type
                ,attributemap.id as attrmap_id
            FROM
                racktables_django.api_attributemap as attributemap
                LEFT JOIN racktables_django.api_objecttype as objecttype on objecttype_id = objecttype.id
                LEFT JOIN racktables_django.api_attribute as attribute on attribute_id = attribute.id 
        ) AS attributemap ON attr_oldid = attr_id AND object_tid = objecttype_oldid