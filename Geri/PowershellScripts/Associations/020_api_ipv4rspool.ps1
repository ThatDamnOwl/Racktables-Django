## Sql Scripts

$020_api_ipv4rspool_push = "
INSERT INTO 
    racktables_django.api_ipv4rspool (oldid, name, vsconfig, rsconfig) 
    SELECT 
         id
        ,name
        ,ifnull(vsconfig,'')
        ,ifnull(rsconfig,'')
    FROM racktables.IPv4RSPool
    WHERE 
        id not in (
            SELECT oldid
            FROM racktables_django.api_ipv4rspool
        )
"

## Hashtable

@{
    "020_api_ipv4rspool" = @{
        "type" = "basic"
        "push" =$020_api_ipv4rspool_push
    }
}