## Sql Scripts

$022_api_ipv4lb_push = "
INSERT INTO 
    racktables_django.api_ipv4lb (prio, parentipv4rspool_id, parentipv4vs_id, parentobject_id, rsconfig, vsconfig) 
    SELECT 
         prio
        ,parentip4rspool.id
        ,parentipv4vs.id
        ,parentobject.id
        ,LB.rsconfig
        ,LB.vsconfig
    FROM 
        racktables.IPv4LB as LB
        LEFT JOIN racktables_django.api_ipv4rspool AS parentip4rspool ON rspool_id = parentip4rspool.oldid
        LEFT JOIN racktables_django.api_ipv4vs AS parentipv4vs ON vs_id = parentipv4vs.oldid
        LEFT JOIN racktables_django.api_object AS parentobject ON object_id = parentobject.oldid
    WHERE 
        concat(rspool_id,""-"",vs_id,""-"",object_id) not in (
            SELECT concat(parentip4rspool.oldid,""-"",parentipv4vs.oldid,""-"",parentobject.oldid) AS ComboID
            FROM 
                racktables.IPv4LB as LB
                LEFT JOIN racktables_django.api_ipv4rspool AS parentip4rspool ON rspool_id = parentip4rspool.oldid
                LEFT JOIN racktables_django.api_ipv4vs AS parentipv4vs ON vs_id = parentipv4vs.oldid
                LEFT JOIN racktables_django.api_object AS parentobject ON object_id = parentobject.oldid
        )
"

## Hashtable

@{
    "022_api_ipv4lb" = @{
        "type" = "basic"
        "push" = $022_api_ipv4lb_push
    }
}