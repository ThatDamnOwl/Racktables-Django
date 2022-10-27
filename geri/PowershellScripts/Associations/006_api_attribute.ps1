## Sql Scripts

$006_api_attribute_push = "
INSERT INTO
    racktables_django.api_attribute (attribute_type, name, oldid)
    SELECT
        CASE 
            WHEN type = 'string' THEN 1 
            WHEN type = 'uint' THEN 2
            WHEN type = 'float' THEN 3
            WHEN type = 'dict' THEN 4
            WHEN type = 'date' THEN 5
            ELSE 6
        END
        ,name
        ,id
    FROM
        racktables.Attribute
    WHERE
        id not in (
            SELECT oldid
            FROM racktables_django.api_attribute
        )
"

## Hashtable

@{
    "006_api_attribute" = @{
        "type" = "basic"
        "push" = $006_api_attribute_push
    }
}