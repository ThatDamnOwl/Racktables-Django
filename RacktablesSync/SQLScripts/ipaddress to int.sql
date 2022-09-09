select 
    concat(
         LPAD(CONV(substring_index(substring_index(PureIP,".",-4),".",1),10,16),2,'0')
        ,LPAD(CONV(substring_index(substring_index(PureIP,".",-3),".",1),10,16),2,'0')
        ,LPAD(CONV(substring_index(substring_index(PureIP,".",-2),".",1),10,16),2,'0')
        ,LPAD(CONV(substring_index(PureIP,".",-1),10,16),2,'0')
    ) AS IPHEX
    ,CONV(
        concat(
             LPAD(CONV(substring_index(substring_index(PureIP,".",-4),".",1),10,16),2,'0')
            ,LPAD(CONV(substring_index(substring_index(PureIP,".",-3),".",1),10,16),2,'0')
            ,LPAD(CONV(substring_index(substring_index(PureIP,".",-2),".",1),10,16),2,'0')
            ,LPAD(CONV(substring_index(PureIP,".",-1),10,16),2,'0')
        )
        ,16
        ,10
    ) AS IPDEC
FROM
    (
        SELECT 
            Substring_index(ip, "f:", -1) as PureIP
        FROM 
            racktables_django.api_ipv4address
    ) as ProcessedTable
WHERE
    PureIP = '10.8.2.217';
