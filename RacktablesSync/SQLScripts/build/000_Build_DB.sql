DROP DATABASE racktables_django;
CREATE DATABASE racktables_django;
GRANT ALL on racktables_django.* to django@localhost;
USE racktables_django;

DROP FUNCTION IF EXISTS racktables_django.parse_ipbin;
DROP FUNCTION IF EXISTS racktables_django.parse_ipv4int;
DROP FUNCTION IF EXISTS racktables_django.parse_ipv4toint;

DELIMITER $$
CREATE FUNCTION racktables_django.parse_ipbin (IPAddressBin VARBINARY(16)) 
RETURNS VARCHAR(150)
DETERMINISTIC 
BEGIN
    DECLARE oct INT DEFAULT 0;
    DECLARE seloct INT DEFAULT 0;
    DECLARE IPAddress VARCHAR(150) DEFAULT '';
    
    WHILE oct < LENGTH(IPAddressBin) DO
        SET oct = oct + 1;
        SET IPAddress = concat(IPAddress, conv(HEX(substring(IPAddressBin,oct,1)),16,10),".");
        SET seloct = conv(HEX(substring(IPAddressBin,oct,1)),16,10);
    END WHILE;
    SET IPAddress = REPLACE((TRIM(BOTH '.' FROM IPAddress)),"..",".");
    SET IPAddress = IF(LENGTH(IPAddressBin) = 4, CONCAT("::ffff:",IPAddress), IPAddress);
    RETURN IPAddress;
END;
$$
DELIMITER ;

DELIMITER $$
CREATE FUNCTION racktables_django.parse_ipv4int (IPAddressInt BIGINT)
RETURNS VARCHAR(50)
DETERMINISTIC 
BEGIN
    RETURN (select racktables_django.parse_ipbin(UNHEX(CONV(BIN(CAST(IPAddressInt as UNSIGNED)),2,16))));
END;
$$
DELIMITER ;


DELIMITER $$
CREATE FUNCTION racktables_django.parse_ipv4toint (PureIP VARCHAR(150))
RETURNS INT
DETERMINISTIC 
BEGIN
    DECLARE IPInt INT DEFAULT 0;
    SET PureIP = IF(PureIP LIKE "%:%", substring_index(PureIP,":",-1), PureIP);
    SET IPInt = (CONV(
                concat(
                     LPAD(CONV(substring_index(substring_index(PureIP,".",-4),".",1),10,16),2,'0')
                    ,LPAD(CONV(substring_index(substring_index(PureIP,".",-3),".",1),10,16),2,'0')
                    ,LPAD(CONV(substring_index(substring_index(PureIP,".",-2),".",1),10,16),2,'0')
                    ,LPAD(CONV(substring_index(PureIP,".",-1),10,16),2,'0')
                )
                ,16
                ,10
            ));
    RETURN IPInt;
END;
$$
DELIMITER ;

