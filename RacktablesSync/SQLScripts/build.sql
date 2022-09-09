DROP DATABASE racktables_django;
CREATE DATABASE racktables_django;
GRANT ALL on racktables_django.* to django@localhost;
USE racktables_django;

DROP FUNCTION IF EXISTS racktables_django.parse_ipv4bin;
DROP FUNCTION IF EXISTS racktables_django.parse_ipbin;
DROP FUNCTION IF EXISTS racktables_django.parse_ipv4int;
DROP FUNCTION IF EXISTS racktables_django.parse_ipv4toint;

DELIMITER $$
CREATE FUNCTION racktables_django.parse_ipbin (IPAddressBin VARBINARY(16))
RETURNS VARCHAR(150)
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
BEGIN
    RETURN (select racktables_django.parse_ipbin(UNHEX(CONV(BIN(CAST(IPAddressInt as UNSIGNED)),2,16))));
END;
$$
DELIMITER ;


DELIMITER $$
CREATE FUNCTION racktables_django.parse_ipv4toint (PureIP VARCHAR(150))
RETURNS INT
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

DROP FUNCTION IF EXISTS racktables_django.001_api_molecule_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.001_api_molecule_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_molecule);
    INSERT INTO 
        racktables_django.api_molecule (oldid, description) 
        SELECT 
             id
            ,'' 
        FROM racktables.Molecule
        WHERE 
            id not in (
                SELECT oldid
                FROM racktables_django.api_molecule
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_molecule) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.002_api_location_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.002_api_location_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    DECLARE missing INT DEFAULT 1;
    DECLARE existing INT;
    DECLARE counter INT DEFAULT 0;
    SET existing = (select count(id) from racktables_django.api_location);
    WHILE counter < 10 AND missing > 0 DO
        INSERT INTO racktables_django.api_location (oldid,name,hasproblems,parentlocation_id,comment)
        SELECT
             location.id
            ,location.name
            ,CASE
                WHEN location.has_problems = 'yes' THEN 1
                ELSE 0
            END
            ,parentlocation.id
            ,ifnull(location.comment,'')
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
        SET counter = counter + 1;
        SET missing = (SELECT count(id) FROM racktables.Location where id NOT IN (select oldid from racktables_django.api_location));
    END WHILE;
    SET inserted = (select count(id) from racktables_django.api_location);
    SET inserted = (inserted - existing);
    RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.003_api_row_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.003_api_row_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_row);
    INSERT INTO
    racktables_django.api_row (oldid, name, location_id)
    SELECT
         row.id
        ,row.name
        ,location.id
    FROM racktables.Row AS row 
         LEFT JOIN
            racktables_django.api_location AS location ON location_id = oldid
    WHERE row.id NOT IN (
        SELECT oldid
        FROM racktables_django.api_row
    );
    SET inserted = (SELECT count(id) FROM racktables_django.api_row) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.004_api_rack_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.004_api_rack_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_rack);

    INSERT INTO
        racktables_django.api_rack (oldid, name, assetno, hasproblems, comment, height, position, row_id)
        SELECT
             rack.id
            ,rack.name
            ,ifnull(rack.asset_no,'')
            ,
            CASE
                WHEN rack.has_problems = 'yes' THEN 1
                ELSE 0
            END AS has_problems
            ,ifnull(rack.comment,'')
            ,rack.height
            ,rack.sort_order
            ,row.id
        FROM racktables.Rack as rack 
             LEFT JOIN
                racktables_django.api_row as row on row_id = oldid
        WHERE rack.id not in (
                SELECT oldid
                FROM racktables_django.api_rack
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_rack) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.005_api_atom_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.005_api_atom_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_atom);
    INSERT INTO racktables_django.api_atom (xaxis, yaxis, zaxis, molecule_id, rack_id, unit_no)
    SELECT
         7
        ,7
        ,SUM(AtomInt)
        ,molecule_id
        ,rack_id
        ,unit_no
    FROM 
        (
            SELECT
                 molecule.id as molecule_id
                ,rack.id as rack_id
                ,atom.unit_no as unit_no
                ,
                CASE 
                    WHEN atom.atom = 'front' THEN 1
                    WHEN atom.atom = 'interior' THEN 2
                    WHEN atom.atom = 'rear' THEN 4
                END
                AS AtomInt
            FROM 
                racktables.Atom AS atom
                LEFT JOIN racktables_django.api_molecule as molecule on atom.molecule_id = molecule.oldid
                LEFT JOIN racktables_django.api_rack as rack on atom.rack_id = rack.oldid
        ) AS Full_Atom
    WHERE 
        concat(molecule_id,'-',rack_id,'-',unit_no) NOT IN (
            SELECT 
                concat(api_molecule.id,'-',api_rack.id,'-',unit_no)
            FROM racktables_django.api_atom 
                LEFT JOIN racktables_django.api_molecule ON molecule_id = api_molecule.id
                LEFT JOIN racktables_django.api_rack ON rack_id = api_rack.id
        )
    GROUP BY molecule_id,rack_id,unit_no;
    SET inserted = (SELECT count(id) FROM racktables_django.api_atom) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.006_api_attribute_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.006_api_attribute_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_attribute);
    INSERT INTO
    racktables_django.api_attribute (attribute_type, name, oldid)
    SELECT
        CASE 
            WHEN type = 'string' THEN 1 
            WHEN type = 'uint' THEN 2
            WHEN type = 'float' THEN 3
            WHEN type = 'dict' THEN 4
            WHEN type = 'date' THEN 5
            ELSE 6
        END
        ,name
        ,id
    FROM
        racktables.Attribute
    WHERE
        id not in (
            SELECT oldid
            FROM racktables_django.api_attribute
        );
    SET inserted = (SELECT count(id) FROM racktables_django.api_attribute) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.007_api_chapter_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.007_api_chapter_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_chapter);

    INSERT INTO
        racktables_django.api_chapter (sticky, name, oldid)
        SELECT
            CASE 
                WHEN sticky = 'yes' THEN 1 
                ELSE 0
            END
            ,name
            ,id
        FROM
            racktables.Chapter
        WHERE
            id not in (
                SELECT oldid
                FROM racktables_django.api_chapter
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_chapter) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.008_api_dictionary_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.008_api_dictionary_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_dictionary);
    INSERT INTO
        racktables_django.api_dictionary (sticky, value, chapter_id, oldid)
        SELECT
            CASE 
                WHEN dict_sticky = 'yes' THEN 1 
                ELSE 0
            END
            ,dict_value
            ,chapter.id
            ,dict_key
        FROM
            racktables.Dictionary LEFT JOIN
            racktables_django.api_chapter AS chapter ON oldid = chapter_id
        WHERE
            dict_key not in (
                SELECT oldid
                FROM racktables_django.api_dictionary
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_dictionary) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.009_api_objecttype_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.009_api_objecttype_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_objecttype);

    INSERT INTO
        racktables_django.api_objecttype (sticky, name, oldid)
        SELECT
            CASE 
                WHEN dict_sticky = 'yes' THEN 1 
                ELSE 0
            END
            ,dict_value
            ,dict_key
        FROM
            racktables.Dictionary
        WHERE
            chapter_id = 1
            AND
            dict_key not in (
                SELECT oldid
                FROM racktables_django.api_objecttype
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_objecttype) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.010_api_object_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.010_api_object_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_object);
    INSERT INTO
        racktables_django.api_object (oldid, name, label, assetno, hasproblems, comment, objecttype_id, parentobject_id)
        SELECT
             object.id
            ,ifnull(object.name,'')
            ,ifnull(object.label,'')
            ,ifnull(object.asset_no,'')
            ,
            CASE
                WHEN object.has_problems = 'yes' THEN 1
                ELSE 0
            END
            ,ifnull(object.comment,'')
            ,objecttype.id
            ,NULL
        FROM
            racktables.Object as object LEFT JOIN
            racktables_django.api_objecttype as objecttype on oldid = objtype_id
        WHERE
            object.id not in (
                SELECT oldid
                FROM racktables_django.api_object
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_object) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.011_api_attributemap_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.011_api_attributemap_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_attributemap);
    INSERT INTO
        racktables_django.api_attributemap (objecttype_id, attribute_id, chapter_id, sticky)
        SELECT
             objtype.id
            ,attribute.id
            ,chapter.id
            ,
            CASE
                WHEN AM.sticky = 'yes' THEN 1
                ELSE 0
            END
        FROM
            racktables.AttributeMap as AM
            LEFT JOIN racktables_django.api_objecttype AS objtype ON objtype_id = objtype.oldid 
            LEFT JOIN racktables_django.api_attribute AS attribute ON attr_id = attribute.oldid
            LEFT JOIN racktables_django.api_chapter AS chapter ON chapter_id = chapter.oldid
        WHERE
            concat(attribute.id,objtype.id,chapter.id) not in
            (
                SELECT concat(attribute.id,objtype.id,chapter.id)
                FROM racktables_django.api_attributemap
                    LEFT JOIN racktables_django.api_objecttype AS objtype ON objecttype_id = objtype.id 
                    LEFT JOIN racktables_django.api_attribute AS attribute ON attribute_id = attribute.id
                    LEFT JOIN racktables_django.api_chapter AS chapter ON chapter_id = chapter.id
            );
        SET inserted = (SELECT count(id) FROM racktables_django.api_attributemap) - inserted;
        RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.012_api_attributevaluestring_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.012_api_attributevaluestring_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_attributevaluestring);
    INSERT INTO
        racktables_django.api_attributevaluestring (parentobject_id, attributemap_id, value)
        SELECT
             parentobject.id
            ,attributemap.attrmap_id
            ,string_value
        FROM
            racktables.AttributeValue
            LEFT JOIN racktables_django.api_object as parentobject on object_id = parentobject.oldid
            LEFT JOIN (
                SELECT 
                     objecttype.oldid as objecttype_oldid
                    ,attribute.oldid as attr_oldid
                    ,attributemap.id as attrmap_id
                    ,attribute.attribute_type as attribute_type
                FROM
                    racktables_django.api_attributemap as attributemap
                    LEFT JOIN racktables_django.api_objecttype as objecttype on objecttype_id = objecttype.id
                    LEFT JOIN racktables_django.api_attribute as attribute on attribute_id = attribute.id 
            ) AS attributemap ON attr_oldid = attr_id AND object_tid = objecttype_oldid
        WHERE
            concat(object_id,'-',attr_id) not in (
                SELECT concat(object.oldid,'-',attribute.oldid)
                FROM racktables_django.api_attributevaluestring as AVS
                    LEFT JOIN racktables_django.api_attributemap AS attrmap ON attributemap_id = attrmap.id
                    LEFT JOIN racktables_django.api_attribute AS attribute ON attrmap.attribute_id = attribute.id
                    LEFT JOIN racktables_django.api_object AS object ON AVS.parentobject_id = object.id
            )
            AND attribute_type = 1;
    SET inserted = (SELECT count(id) FROM racktables_django.api_attributevaluestring) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.013_api_attributevalueint_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.013_api_attributevalueint_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_attributevalueint);
    INSERT INTO
        racktables_django.api_attributevalueint (parentobject_id, attributemap_id, value)
        SELECT
             parentobject.id
            ,attributemap.attrmap_id
            ,uint_value
        FROM
            racktables.AttributeValue
            LEFT JOIN racktables_django.api_object as parentobject on object_id = parentobject.oldid
            LEFT JOIN (
                SELECT 
                     objecttype.oldid as objecttype_oldid
                    ,attribute.oldid as attr_oldid
                    ,attributemap.id as attrmap_id
                    ,attribute.attribute_type as attribute_type
                FROM
                    racktables_django.api_attributemap as attributemap
                    LEFT JOIN racktables_django.api_objecttype as objecttype on objecttype_id = objecttype.id
                    LEFT JOIN racktables_django.api_attribute as attribute on attribute_id = attribute.id 
            ) AS attributemap ON attr_oldid = attr_id AND object_tid = objecttype_oldid
        WHERE
            concat(object_id,'-',attr_id) not in (
                SELECT concat(object.oldid,'-',attribute.oldid)
                FROM racktables_django.api_attributevalueint as AVI
                    LEFT JOIN racktables_django.api_attributemap AS attrmap ON attributemap_id = attrmap.id
                    LEFT JOIN racktables_django.api_attribute AS attribute ON attrmap.attribute_id = attribute.id
                    LEFT JOIN racktables_django.api_object AS object ON AVI.parentobject_id = object.id
            )
            AND attribute_type = 2;
    SET inserted = (SELECT count(id) FROM racktables_django.api_attributevalueint) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.014_api_attributevaluefloat_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.014_api_attributevaluefloat_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_attributevaluefloat);
    INSERT INTO
        racktables_django.api_attributevaluefloat (parentobject_id, attributemap_id, value)
        SELECT
             parentobject.id
            ,attributemap.attrmap_id
            ,float_value
        FROM
            racktables.AttributeValue
            LEFT JOIN racktables_django.api_object as parentobject on object_id = parentobject.oldid
            LEFT JOIN (
                SELECT 
                     objecttype.oldid as objecttype_oldid
                    ,attribute.oldid as attr_oldid
                    ,attributemap.id as attrmap_id
                    ,attribute.attribute_type as attribute_type
                FROM
                    racktables_django.api_attributemap as attributemap
                    LEFT JOIN racktables_django.api_objecttype as objecttype on objecttype_id = objecttype.id
                    LEFT JOIN racktables_django.api_attribute as attribute on attribute_id = attribute.id 
            ) AS attributemap ON attr_oldid = attr_id AND object_tid = objecttype_oldid
        WHERE
            concat(object_id,'-',attr_id) not in (
                SELECT concat(object.oldid,'-',attribute.oldid)
                FROM racktables_django.api_attributevaluefloat as AVF
                    LEFT JOIN racktables_django.api_attributemap AS attrmap ON attributemap_id = attrmap.id
                    LEFT JOIN racktables_django.api_attribute AS attribute ON attrmap.attribute_id = attribute.id
                    LEFT JOIN racktables_django.api_object AS object ON AVF.parentobject_id = object.id
            )
            AND attribute_type = 3;
    SET inserted = (SELECT count(id) FROM racktables_django.api_attributevaluefloat) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.015_api_attributevaluedict_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.015_api_attributevaluedict_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_attributevaluedict);
    INSERT INTO
        racktables_django.api_attributevaluedict (parentobject_id, attributemap_id, dictionaryvalue_id)
        SELECT
             parentobject.id
            ,attributemap.attrmap_id
            ,dictionary.id
        FROM
            racktables.AttributeValue
            LEFT JOIN racktables_django.api_object as parentobject on object_id = parentobject.oldid
            LEFT JOIN (
                SELECT 
                     objecttype.oldid as objecttype_oldid
                    ,attribute.oldid as attr_oldid
                    ,attributemap.id as attrmap_id
                    ,attribute.attribute_type as attribute_type            FROM
                    racktables_django.api_attributemap as attributemap
                    LEFT JOIN racktables_django.api_objecttype as objecttype on objecttype_id = objecttype.id
                    LEFT JOIN racktables_django.api_attribute as attribute on attribute_id = attribute.id 
            ) AS attributemap ON attr_oldid = attr_id AND object_tid = objecttype_oldid
            LEFT JOIN racktables_django.api_dictionary as dictionary ON uint_value = dictionary.oldid
        WHERE
            concat(object_id,'-',attr_id) not in (
                SELECT concat(object.oldid,'-',attribute.oldid)
                FROM racktables_django.api_attributevaluedict as AVD
                    LEFT JOIN racktables_django.api_attributemap AS attrmap ON attributemap_id = attrmap.id
                    LEFT JOIN racktables_django.api_attribute AS attribute ON attrmap.attribute_id = attribute.id
                    LEFT JOIN racktables_django.api_object AS object ON AVD.parentobject_id = object.id
            )
            AND attribute_type = 4;
        SET inserted = (SELECT count(id) FROM racktables_django.api_attributevaluedict) - inserted;
        RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.016_api_attributevaluedate_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.016_api_attributevaluedate_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_attributevaluedate);
    INSERT INTO
        racktables_django.api_attributevaluedate (parentobject_id, attributemap_id, value)
        SELECT
             parentobject.id
            ,attributemap.attrmap_id
            ,from_unixtime(uint_value)
        FROM
            racktables.AttributeValue
            LEFT JOIN racktables_django.api_object as parentobject on object_id = parentobject.oldid
            LEFT JOIN (
                SELECT 
                     objecttype.oldid as objecttype_oldid
                    ,attribute.oldid as attr_oldid
                    ,attributemap.id as attrmap_id
                    ,attribute.attribute_type as attribute_type
                FROM
                    racktables_django.api_attributemap as attributemap
                    LEFT JOIN racktables_django.api_objecttype as objecttype on objecttype_id = objecttype.id
                    LEFT JOIN racktables_django.api_attribute as attribute on attribute_id = attribute.id 
            ) AS attributemap ON attr_oldid = attr_id AND object_tid = objecttype_oldid
        WHERE
            concat(object_id,'-',attr_id) not in (
                SELECT concat(object.oldid,'-',attribute.oldid)
                FROM racktables_django.api_attributevaluedate as AVDa
                    LEFT JOIN racktables_django.api_attributemap AS attrmap ON attributemap_id = attrmap.id
                    LEFT JOIN racktables_django.api_attribute AS attribute ON attrmap.attribute_id = attribute.id
                    LEFT JOIN racktables_django.api_object AS object ON AVDa.parentobject_id = object.id
            )
            AND attribute_type = 5;
        SET inserted = (SELECT count(id) FROM racktables_django.api_attributevaluedate) - inserted;
        RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.017_api_ipv4address_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.017_api_ipv4address_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4address);
    INSERT INTO racktables_django.api_ipv4address (ip,name,comment,reserved,oldip)
        SELECT
            racktables_django.parse_ipv4int(ip) as newip
            ,ifnull(name,'') as name
            ,comment
            ,CASE
                WHEN reserved = 'yes' THEN 1
                ELSE 0
            END as reserved
            ,ip as oldip
        FROM
            racktables.IPv4Address
        WHERE  
            ip not in (select oldip from racktables_django.api_ipv4address);

    INSERT INTO racktables_django.api_ipv4address (ip,name,comment,reserved,oldip)
        SELECT
            newip
            ,ifnull(name,'') as name
            ,'' AS comment
            ,1 AS reserved
            ,racktables_django.parse_ipv4toint(newip) as oldip
        FROM
            (
                SELECT 
                     racktables_django.parse_ipbin(vip) as newip
                    ,name
                FROM racktables.IPv4VS
            ) AS VIPInsert
        WHERE  
            newip not in (select ip from racktables_django.api_ipv4address);

    INSERT INTO racktables_django.api_ipv4address (ip,name,comment,reserved,oldip)
        SELECT
            racktables_django.parse_ipv4int(ip)
            ,ifnull(concat(obj.name,"-",ipal.name),'') as name
            ,'' AS comment
            ,1 AS reserved
            ,ip as oldip
        FROM
            racktables.IPv4Allocation as ipal
            LEFT JOIN racktables.Object as obj on object_id = obj.id
        WHERE  
            ip not in (select oldip from racktables_django.api_ipv4address);

    INSERT INTO racktables_django.api_ipv4address (ip,name,comment,reserved,oldip)
        SELECT
            racktables_django.parse_ipv4int(ip)
            ,''
            ,'' AS comment
            ,1 AS reserved
            ,ip as oldip
        FROM
            racktables.IPv4Log as log
        WHERE  
            ip not in (select oldip from racktables_django.api_ipv4address);

    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4address) - inserted;
    RETURN inserted;
END;

$$

DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.018_api_ipv4vs_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.018_api_ipv4vs_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4vs);
    INSERT INTO racktables_django.api_ipv4vs (oldid,oldvip,vport,protocol,name,vsconfig,rsconfig,vip_id)
        SELECT 
                 ipv4vsnewip.id
                ,vip
                ,vport
                ,CASE 
                    WHEN protocol = 'TCP' THEN 1 
                    WHEN protocol = 'UDP' THEN 2
                    WHEN protocol = 'MARK' THEN 4
                END AS protocol
                ,ifnull(ipv4vsnewip.name,'')
                ,ifnull(vsconfig,'')
                ,ifnull(rsconfig,'')
                ,ipal.id
        FROM
            (
                SELECT 
                        id
                       ,vip
                       ,vport
                       ,proto as protocol
                       ,name
                       ,vsconfig
                       ,rsconfig
                       ,racktables_django.parse_ipbin(vip) as newip
                FROM
                    racktables.IPv4VS
            ) AS ipv4vsnewip
            LEFT JOIN
                racktables_django.api_ipv4address as ipal on newip = ipal.ip
        where
            ipv4vsnewip.id NOT IN (
                SELECT 
                    oldid
                FROM
                    racktables_django.api_ipv4vs
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4vs) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.019_api_ipv4allocation_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.019_api_ipv4allocation_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;

    SET inserted = (SELECT count(id) FROM racktables_django.api_objecttype);

    INSERT INTO racktables_django.api_ipv4allocation (name,alloctype,ip_id,parentobject_id)
    select 
         ipal.name
        ,CASE
            WHEN type = 'regular' THEN 1
            WHEN type = 'shared' THEN 2
            WHEN type = 'virtual' THEN 3
            WHEN type = 'router' THEN 4
            WHEN type = 'point2point' THEN 5
            WHEN type = 'sharedrouter' THEN 6
        END as alloctype
        ,ipa.id
        ,obj.id
    FROM
        racktables.IPv4Allocation AS ipal
        LEFT JOIN racktables_django.api_ipv4address as ipa on ipal.ip = ipa.oldip
        LEFT JOIN racktables_django.api_object as obj on object_id = obj.oldid
    where
        concat(ipal.name,"-",ipal.ip,"-",object_id) COLLATE utf8_unicode_ci NOT IN (
            SELECT 
                concat(ipal.name,"-",ipa.oldip,"-",obj.oldid) COLLATE utf8_unicode_ci
            FROM
                racktables_django.api_ipv4allocation as ipal
                LEFT JOIN racktables_django.api_ipv4address as ipa on ip_id = ipa.id
                LEFT JOIN racktables_django.api_object as obj on ipal.parentobject_id = obj.id);

    SET inserted = (SELECT count(id) FROM racktables_django.api_objecttype) - inserted;

    RETURN inserted;
END;
$$ 
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.020_api_ipv4rspool_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.020_api_ipv4rspool_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rspool);
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
            );
        SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rspool) - inserted;
        RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.021_api_ipv4rs_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.021_api_ipv4rs_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rs);
    INSERT INTO racktables_django.api_ipv4rs (oldid,inservice,oldrsip,rsport,rspool_id,rsip_id,rsconfig,comment)
    SELECT 
           rs.id
          ,CASE
              WHEN inservice = 'yes' THEN 1
              ELSE 0
          END 
          ,rs.rsip
          ,rs.rsport
          ,rspool.id
          ,ip.id
          ,rs.rsconfig
          ,rs.comment
    FROM
        racktables.IPv4RS AS rs
        LEFT JOIN racktables_django.api_ipv4address as ip on ip.ip = racktables_django.parse_ipv4toint(racktables_django.parse_ipbin(rsip))
        LEFT JOIN racktables_django.api_ipv4rspool as rs on rs.oldid = rspool_id
    WHERE
        rs.id NOT IN (select oldid from racktables_django.api_ipv4rs);

    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rs) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.022_api_ipv4lb_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.022_api_ipv4lb_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rspool);
    INSERT INTO 
        racktables_django.api_ipv4lb (prio, vsconfig, rsconfig, parentipv4rspool_id, parentipv4vs_id, parentobject_id) 
        SELECT 
             lb.prio
            ,lb.vsconfig
            ,lb.rsconfig
            ,parentipv4rspool.id
            ,parentipv4vs.id
            ,parentobject.id
        FROM 
             racktables.IPv4LB AS lb
             LEFT JOIN racktables_django.api_ipv4rspool as parentipv4rspool on parentipv4rspool.oldid = lb.rspool_id
             LEFT JOIN racktables_django.api_ipv4vs as parentipv4vs on parentipv4vs.oldid = lb.vs_id
             LEFT JOIN racktables_django.api_object as parentobject on parentobject.oldid = lb.object_id
        WHERE 
            concat(parentipv4rspool.id,"-",parentipv4vs.id,"-",parentobject.id) not in (
                SELECT concat(parentipv4rspool_id,"-",parentipv4vs_id,"-",parentobject_id)
                FROM racktables_django.api_ipv4lb
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rspool) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.023_api_ipv4log_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.023_api_ipv4log_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4log);
    INSERT INTO 
        racktables_django.api_ipv4log (oldid,date,message,ip_id,user_id) 
        SELECT 
             log.id
            ,date
            ,message
            ,ip.id
            ,user.id
        FROM 
             racktables.IPv4Log COLLATE utf8_unicode_ci AS log
             LEFT JOIN racktables_django.api_ipv4address  COLLATE utf8_unicode_ci as ip on ip.oldip = log.ip
             LEFT JOIN racktables_django.auth_user  COLLATE utf8_unicode_ci as user on user.username = log.user 
        WHERE 
            log.id NOT IN (SELECT oldid FROM racktables_django.api_ipv4log);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4log) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.024_api_ipv4nat_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.024_api_ipv4nat_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4nat);
    INSERT INTO 
        racktables_django.api_ipv4nat (localip_id, localport, remoteip_id, remoteport, protocol, description) 
        SELECT 
              localip.id
             ,localport
             ,remoteip.id
             ,remoteport
             ,CASE
                WHEN proto = 'tcp' THEN 1
                WHEN proto = 'udp' THEN 2
                WHEN proto = 'mark' THEN 4
            END
             ,description
        FROM 
             racktables.IPv4NAT as nat
             LEFT JOIN racktables_django.api_ipv4address AS localip on localip.oldip = nat.localip
             LEFT JOIN racktables_django.api_ipv4address AS remoteip on remoteip.oldip = nat.remoteip
        WHERE 
            concat(localip.id,"-",remoteip.id) NOT IN (SELECT concat(localip_id,"-",remoteip_id) FROM racktables_django.api_ipv4nat);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4nat) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
DROP FUNCTION IF EXISTS racktables_django.025_api_ipv4network_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.025_api_ipv4network_pull (ignored BIGINT)
RETURNS INT
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4network);
    INSERT INTO 
        racktables_django.api_ipv4network (oldid, ip, oldip, mask, name, comment) 
        SELECT 
              id
             ,racktables_django.parse_ipv4int(ip)
             ,ip
             ,mask
             ,ifnull(name,'')
             ,ifnull(comment,'')
        FROM
            racktables.IPv4Network
        Where
            id not in (SELECT oldid from racktables_django.api_ipv4network);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4network) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
