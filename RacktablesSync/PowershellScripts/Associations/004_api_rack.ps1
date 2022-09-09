## Sql Scripts

$004_api_rack_push = "
INSERT INTO
    racktables_django.api_rack (oldid, name, assetno, hasproblems, comment, height, position, row_id)
    SELECT
         rack.id
        ,rack.name
        ,ifnull(rack.asset_no,'')
        ,
        CASE
            WHEN rack.has_problems = 'yes' THEN 1
            ELSE 0
        END AS has_problems
        ,ifnull(rack.comment,'')
        ,rack.height
        ,rack.sort_order
        ,row.id
    FROM racktables.Rack as rack 
         LEFT JOIN
            racktables_django.api_row as row on row_id = oldid
    WHERE rack.id not in (
            SELECT oldid
            FROM racktables_django.api_rack
        )
"

## Hashtable

@{
    "004_api_rack" = @{
        "type" = "basic"
        "push" = $004_api_rack_push
    }
}