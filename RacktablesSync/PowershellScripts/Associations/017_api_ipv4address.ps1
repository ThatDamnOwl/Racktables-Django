## Sql Scripts

$017_api_ipv4address_check = "
select 
    ip
FROM
    racktables.IPv4Address
where
    ip NOT IN (
        SELECT 
            oldip
        FROM
            racktables_django.api_ipv4address
    )
"

## Hashtable

@{
    "017_api_ipv4address" = @{
        "oldtable" = "IPv4Address"
        "oldkey" = "ip"
        "oldkey_newname" = "oldip"
        "table_type" = "basic"
        "selfreference" = $false
        "quick_check" = $017_api_ipv4address_check
        "ip" = @{
            "arguments" = @(@{
                "oldkey" = "ip"
                "lookup_value" = $null
            })
            "reference" = $false
            "scriptblock" = $ParseIP
        }
        "name" = "name"
        "comment" = "comment"
        "reserved" = @{
            "arguments" = @(@{
                "oldkey" = "reserved"
                "lookup_value" = $null
            })
            "reference" = $false
            "scriptblock" = $BasicBoolean
        }
        "oldip" = "ip"
    }
}