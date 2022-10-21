## Sql Scripts

$018_api_ipv4vs_check = "
select 
    id
FROM
    racktables.IPv4VS
where
    id NOT IN (
        SELECT 
            oldid
        FROM
            racktables_django.api_ipv4vs
    )
"

## Hashtable

@{
    "018_api_ipv4vs" = @{
        "oldtable" = "IPv4VS"
        "oldkey" = "id"
        "oldkey_newname" = "oldid"
        "table_type" = "basic"
        "selfreference" = $false
        "oldselfreferencefield" = $null
        "newselfreferencefield" = $null
        "quick_check" = $018_api_ipv4vs_check
        "oldid" = "id"
        "vip" = @{
            "arguments" = @(
                @{
                    "lookupdatabase" = "racktables_django"
                    "lookuptable" = "api_ipv4address"
                    "oldkey" = "vsip"
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
        "vport" = "vport"
        "protocol" = @{
            "arguments" = @(@{
                "oldkey" = "proto"
                "lookup_value" = $null
            })
            "reference" = $false
            "scriptblock" = $ParseProtocol
        }
        "name" = "name"
        "vsconfig" = "vsconfig"
        "rsconfig" = "rsconfig"
    }
}