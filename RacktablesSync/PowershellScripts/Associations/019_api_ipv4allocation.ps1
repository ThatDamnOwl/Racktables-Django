## Sql Scripts

$019_api_ipv4allocation_check = "
select 
    concat(ip,""-"",object_id)
FROM
    racktables.IPv4Allocation
where
    ip NOT IN (
        SELECT 
            concat(oldip,""-"",obj.oldid)
        FROM
            racktables_django.api_ipv4allocation as ipal
            LEFT JOIN racktables_django.api_ipv4address as ipa on ip_id = ipa.id
            LEFT JOIN racktables_django.api_object as obj on ipal.parentobject_id = obj.id
    )
"

$019_api_ipv4allocation_new_table = "
SELECT 
     concat(oldip,""-"",obj.oldid) AS ComboID
    ,obj.id AS object_id
    ,ipa.ip AS ip
    ,alloc.name
    ,alloctype
FROM
    racktables_django.api_ipv4allocation AS alloc
    LEFT JOIN racktables_django.api_ipv4address as ipa on ip_id = ipa.id
    LEFT JOIN racktables_django.api_object as obj on alloc.parentobject_id = obj.id
"

$019_api_ipv4allocation_old_table = "
SELECT 
     concat(ip,""-"",object_id) AS ComboID
    ,object_id
    ,ip
    ,name
    ,type
FROM
    racktables.IPv4Allocation
"

## Hashtable

@{
    "019_api_ipv4allocation" = @{
        "oldtable" = "IPv4Address"
        "oldkey" = "ComboID"
        "oldkey_newname" = "ComboID"
        "table_type" = "query"
        "old_table_query" = @{
            "query" = $019_api_ipv4allocation_old_table
            "columns" = @( `
                @{"Name" = "ComboID"}, `
                @{"Name" = "object_id"}, `
                @{"Name" = "ip"}, `
                @{"Name" = "name"}, `
                @{"Name" = "type"} `
            )
        }
        "new_table_query" = @{
            "query" = $019_api_ipv4allocation_new_table
            "columns" = @( `
                @{"Name" = "ComboID"}, `
                @{"Name" = "object_id"}, `
                @{"Name" = "ip"}, `
                @{"Name" = "name"}, `
                @{"Name" = "type"} `
            )
        }
        "selfreference" = $false
        "oldselfreferencefield" = $null
        "newselfreferencefield" = $null
        "quick_check" = $019_api_ipv4allocation_check
        "parentobject_id" = @{
            "arguments" = @(@{
                    "lookupdatabase" = "racktables_django"
                    "lookuptable" = "api_object"
                    "oldkey" = "object_id"
                    "newkey" = "oldid"
                    "lookup_value" = $null
                    "outputkey" = "id"
                }
            )
            "reference" = $true
            "referencefield" = "parentobject_id"
            "scriptblock" = $BasicForeignKey
        }
        "ip_id" = @{
            "arguments" = @(
                @{
                    "lookupdatabase" = "racktables_django"
                    "lookuptable" = "api_ipv4address"
                    "oldkey" = "ip"
                    "newkey" = "oldip"
                    "lookup_value" = $null
                    "outputkey" = "id"
                    "CreateKey" = $CreateIP
                }
            )
            "reference" = $true
            "referencefield" = "ip_id"
            "scriptblock" = $BasicForeignKeyPopulateNulls
        }
        "name" = "name"
        "alloctype" = @{
            "arguments" = @(@{
               "oldkey" = "type"
               "lookup_value" = $null
            })
            "reference" = $false
            "referencefield" = $null
            "scriptblock" = $ParseAllocation
        }
    }
}