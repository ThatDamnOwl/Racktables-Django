## Sql Scripts

$010_api_object_push = "
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
        )
"

## Hashtable

@{
    "010_api_object" = @{
        "type" = "basic"
        "push" = $010_api_object_push
    }
}    