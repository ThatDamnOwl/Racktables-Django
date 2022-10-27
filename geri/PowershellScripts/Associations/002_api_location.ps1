## Sql Scripts

$002_api_location_check = "
select 
    id
FROM
    racktables.Location
where
    id NOT IN (
        SELECT 
            oldid
        FROM
            racktables_django.api_location
    )
"

$002_api_location_push = "
DECLARE counter INT DEFAULT 0; 
WHILE counter < 10
    INSERT INTO racktables_django.api_location (oldid,name,hasproblems,parentlocation_id,comment)
    SELECT
         location.id
        ,location.name
        ,CASE
            WHEN location.has_problems = 'yes' THEN 1
            ELSE 0
        END
        ,parentlocation.id
        ,location.comment
        FROM
            racktables.Location AS location
            LEFT JOIN racktables_django.api_location AS parentlocation on parentlocation.oldid = location.parent_id
        WHERE
            location.id not in (SELECT oldid from racktables_django.api_location)
            AND 
            (
                parent_id in (SELECT oldid from racktables_django.api_location)
                OR ifnull(parent_id,0) = 0
            );

    SET counter = SELECT IF(
        (SELECT COUNT(id) FROM racktables.location as location
        WHERE location.id not in (SELECT oldid from racktables_django.api_location)) = 0,10,(counter + 1))
    );
END WHILE;
"

## Hashtable

@{
    "002_api_location" = @{
        "oldtable" = "Location"
        "oldkey" = "id"
        "oldkey_newname" = "oldid"
        "table_type" = "basic"
        "selfreference" = $true
        "oldselfreferencefield" = "parent_id"
        "newselfreferencefield" = "parentlocation_id"
        "quick_check" = $002_api_location_check
        "oldid" = "id" 
        "name" = "name"
        "hasproblems" = @{
            "arguments" = @(@{
                "oldkey" = "has_problems"
                "lookup_value" = $null
            })
            "reference" = $false
            "scriptblock" = $BasicBoolean
        }
        "parentlocation_id" = @{
            "arguments" = @(@{
                    "lookupdatabase" = "racktables_django"
                    "lookuptable" = "api_location"
                    "oldkey" = "parent_id"
                    "newkey" = "oldid"
                    "lookup_value" = $null
                    "outputkey" = "id"
                }
            )
            "reference" = $true
            "referencefield" = "parent_id"
            "scriptblock" = $BasicForeignKey
        }
        "comment" = "comment"   
    }
}