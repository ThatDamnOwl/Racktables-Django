$022_api_ipv4log_push = "
INSERT INTO 
    racktables_django.api_ipv4log (oldid, ip_id, date, message, user_id) 
    SELECT 
         log.id
        ,ip.id
        ,date
        ,message
        ,user.id
    FROM 
        racktables.IPv4Log AS log
        LEFT JOIN racktables_django.auth_user AS user on log.user COLLATE utf8_general_ci = user.username
        LEFT JOIN racktables_django.api_ipv4address AS ip on log.ip = ip.oldip
    WHERE 
        log.id not in (
            SELECT oldid
            FROM racktables_django.api_ipv4log
        )
"

## Hashtable
## Sql Scripts

$022_api_ipv4log_check = "
SELECT 
     log.id
    ,ip.id
    ,date
    ,message
    ,user.id
FROM 
    racktables.IPv4Log AS log
    LEFT JOIN racktables_django.auth_user AS user on log.user COLLATE utf8_general_ci = user.username
    LEFT JOIN racktables_django.api_ipv4address AS ip on log.ip = ip.oldip
WHERE 
    log.id not in (
        SELECT oldid
        FROM racktables_django.api_ipv4log
    )
"

## Hashtable

@{
    "023_api_ipv4log" = @{
        "oldtable" = "IPv4Log"
        "oldkey" = "id"
        "oldkey_newname" = "oldid"
        "table_type" = "basic"
        "selfreference" = $false
        "quick_check" = $022_api_ipv4log_check
        "oldid" = "id"
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
        "date" = @{
            "arguments" = @(@{
                "oldkey" = "date"
                "lookup_value" = $null
            })
            "reference" = $false
            "scriptblock" = $ParseDate
        }
        "user_id" = @{
            "arguments" = @(@{
                    "lookupdatabase" = "racktables_django"
                    "lookuptable" = "auth_user"
                    "oldkey" = "user"
                    "newkey" = "username"
                    "lookup_value" = $null
                    "outputkey" = "id"
                }
            )
            "reference" = $true
            "referencefield" = "user_id"
            "scriptblock" = $BasicForeignKey
        }
        "message" = "message"
    }
}