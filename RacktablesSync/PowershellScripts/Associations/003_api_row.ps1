## Sql Scripts

$003_api_row_push = "
INSERT INTO
    racktables_django.api_row (oldid, name, location_id)
    SELECT
         row.id
        ,row.name
        ,location.id
    FROM racktables.Row AS row 
         LEFT JOIN
            racktables_django.api_location AS location ON location_id = oldid
    WHERE row.id NOT IN (
        SELECT oldid
        FROM racktables_django.api_row
    )
"

## Hashtable

@{
    "003_api_row" = @{
        "type" = "basic"
        "push" = $003_api_row_push
    }
}