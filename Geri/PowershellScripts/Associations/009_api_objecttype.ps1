## Sql Scripts

$009_api_objecttype_push = "
INSERT INTO
    racktables_django.api_objecttype (sticky, name, oldid)
    SELECT
        CASE 
            WHEN dict_sticky = 'yes' THEN 1 
            ELSE 0
        END
        ,dict_value
        ,dict_key
    FROM
        racktables.Dictionary
    WHERE
        chapter_id = 1
        AND
        dict_key not in (
            SELECT oldid
            FROM racktables_django.api_objecttype
        )
"

## Hashtable

@{
    "009_api_objecttype" = @{
        "type" = "basic"
        "push" = $009_api_objecttype_push
    }
}