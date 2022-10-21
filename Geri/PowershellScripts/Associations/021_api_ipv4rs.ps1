## Sql Scripts

$021_api_ipv4rs_check = "
SELECT 
     id
FROM racktables.IPv4RS
WHERE 
    id not in (
        SELECT oldid
        FROM racktables_django.api_ipv4rs
    )
"

## Hashtable

@{
    "021_api_ipv4rs" = @{
        "oldtable" = "IPv4RS"
        "oldkey" = "ip"
        "oldkey_newname" = "oldip"
        "table_type" = "basic"
        "selfreference" = $false
        "quick_check" = $021_api_ipv4rs_check
        "oldid" = "id"
        "inservice" = @{
            "arguments" = @(@{
                "oldkey" = "inservice"
                "lookup_value" = $null
            })
            "reference" = $false
            "scriptblock" = $BasicBoolean
        }
        "oldrsip" = "rsip"
        "rsport" = "rsport"
        "rsconfig" = "rsconfig"
        "comment" = "comment"
        "rsip_id" = @{
            "arguments" = @(
                @{
                    "lookupdatabase" = "racktables_django"
                    "lookuptable" = "api_ipv4address"
                    "oldkey" = "rsip"
                    "newkey" = "oldip"
                    "lookup_value" = $null
                    "outputkey" = "id"
                    "CreateKey" = $CreateIP
                }
            )
            "reference" = $true
            "referencefield" = "rsip_id"
            "scriptblock" = $BasicForeignKeyPopulateNulls
        }
        "rspool_id" = @{
            "arguments" = @(@{
                    "lookupdatabase" = "racktables_django"
                    "lookuptable" = "api_ipv4rspool"
                    "oldkey" = "rspool_id"
                    "newkey" = "oldid"
                    "lookup_value" = $null
                    "outputkey" = "id"
                }
            )
            "reference" = $true
            "referencefield" = "rspool_id"
            "scriptblock" = $BasicForeignKey
        }
    }
}