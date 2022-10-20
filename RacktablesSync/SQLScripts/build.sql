

 ## 000_Build_DB.sql ##

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



 ## 001_api_useraccount_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.001_api_useraccount_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.001_api_useraccount_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_useraccount);
    INSERT INTO 
        racktables_django.auth_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) 
        SELECT 
             ''
            ,0
            ,old.user_name
            ,old.user_realname
            ,''
            ,''
            ,1
            ,1
            ,NOW()
        FROM racktables.UserAccount old
             LEFT JOIN racktables_django.auth_user au on au.username = old.user_name COLLATE utf8_general_ci
        WHERE 
            IFNULL(au.username,'NULL USER') = 'NULL USER';
    INSERT INTO
        racktables_django.api_useraccount (oldid, username, realname, old_passhash, user_id)
        SELECT 
             UA.user_id
            ,user_name
            ,user_realname
            ,user_password_hash
            ,user.id
        FROM
            racktables.UserAccount as UA
            LEFT JOIN racktables_django.auth_user as user on user.username = UA.user_name COLLATE utf8_general_ci
        WHERE 
            UA.user_id not in (
                SELECT oldid
                FROM racktables_django.api_useraccount
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_useraccount) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;


 ## 002_api_userconfig_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.002_api_userconfig_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.002_api_userconfig_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_userconfig);
    INSERT INTO 
        racktables_django.api_userconfig (varname,varvalue,user_id) 
        SELECT 
             varname
            ,varvalue
            ,UA.id
        FROM racktables.UserConfig as UC
            LEFT JOIN racktables_django.api_useraccount as UA on UA.username = UC.user COLLATE utf8_unicode_ci
        WHERE 
            concat(varname,"-",UA.id) not in (
                SELECT concat(varname,"-",user_id) COLLATE utf8_unicode_ci
                FROM racktables_django.api_userconfig
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_userconfig) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;


 ## 003_api_molecule_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.003_api_molecule_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.003_api_molecule_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 004_api_location_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.004_api_location_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.004_api_location_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 005_api_row_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.005_api_row_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.005_api_row_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_row);
    INSERT INTO
    racktables_django.api_row (oldid, name, location_id)
    SELECT
         Row.id
        ,Row.name
        ,location.id
    FROM racktables.Row
         LEFT JOIN racktables_django.api_location AS location ON location_id = location.oldid
    WHERE Row.id NOT IN (
        SELECT oldid
        FROM racktables_django.api_row
    );
    SET inserted = (SELECT count(id) FROM racktables_django.api_row) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;


 ## 006_api_rack_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.006_api_rack_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.006_api_rack_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_rack);

    INSERT INTO
        racktables_django.api_rack (oldid, name, assetno, hasproblems, comment, height, position, row_id)
        SELECT
             Rack.id
            ,Rack.name
            ,ifnull(Rack.asset_no,'')
            ,
            CASE
                WHEN Rack.has_problems = 'yes' THEN 1
                ELSE 0
            END AS has_problems
            ,ifnull(Rack.comment,'')
            ,Rack.height
            ,Rack.sort_order
            ,api_row.id
        FROM racktables.Rack 
             LEFT JOIN racktables_django.api_row ON Rack.row_id = api_row.oldid
        WHERE Rack.id not in (
                SELECT oldid
                FROM racktables_django.api_rack
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_rack) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;


 ## 007_api_atom_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.007_api_atom_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.007_api_atom_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 008_api_attribute_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.008_api_attribute_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.008_api_attribute_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 009_api_chapter_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.009_api_chapter_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.009_api_chapter_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 010_api_dictionary_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.010_api_dictionary_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.010_api_dictionary_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 011_api_objecttype_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.011_api_objecttype_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.011_api_objecttype_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 012_api_object_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.012_api_object_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.012_api_object_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 013_api_attributemap_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.013_api_attributemap_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.013_api_attributemap_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 014_api_attributevaluestring_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.014_api_attributevaluestring_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.014_api_attributevaluestring_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 015_api_attributevalueint_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.015_api_attributevalueint_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.015_api_attributevalueint_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 016_api_attributevaluefloat_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.016_api_attributevaluefloat_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.016_api_attributevaluefloat_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 017_api_attributevaluedict_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.017_api_attributevaluedict_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.017_api_attributevaluedict_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 018_api_attributevaluedate_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.018_api_attributevaluedate_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.018_api_attributevaluedate_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 019_api_ipv4address_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.019_api_ipv4address_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.019_api_ipv4address_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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
            ,0 AS reserved
            ,ip as oldip
        FROM
            racktables.IPv4Log as log
        WHERE  
            ip not in (select oldip from racktables_django.api_ipv4address)
        GROUP BY ip;
    INSERT INTO racktables_django.api_ipv4address (ip,name,comment,reserved,oldip)
        SELECT 
               concat('::ffff:',INET6_NTOA(rsip))
              ,old.comment
              ,''
              ,1
              ,INET_ATON(INET6_NTOA(rsip))
        FROM
            racktables.IPv4RS AS old
        WHERE
            concat('::ffff:',INET6_NTOA(rsip)) NOT IN (select ip from racktables_django.api_ipv4address);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4address) - inserted;
    RETURN inserted;
END;

$$

DELIMITER ;


 ## 020_api_ipv4vs_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.020_api_ipv4vs_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.020_api_ipv4vs_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 021_api_ipv4allocation_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.021_api_ipv4allocation_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.021_api_ipv4allocation_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 022_api_ipv4rspool_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.022_api_ipv4rspool_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.022_api_ipv4rspool_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 023_api_ipv4rs_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.023_api_ipv4rs_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.023_api_ipv4rs_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rs);
    INSERT INTO racktables_django.api_ipv4rs (oldid,inservice,oldrsip,rsport,rspool_id,rsip_id,rsconfig,comment)
    SELECT 
           old.id
          ,CASE
              WHEN inservice = 'yes' THEN 1
              ELSE 0
          END as inservice
          ,old.rsip
          ,old.rsport
          ,rs.id as rs_id
          ,ip.id as ip_id
          ,old.rsconfig
          ,old.comment
    FROM
        racktables.IPv4RS AS old
        LEFT JOIN racktables_django.api_ipv4address as ip on ip.ip = concat('::ffff:',INET6_NTOA(rsip))
        LEFT JOIN racktables_django.api_ipv4rspool as rs on rs.oldid = rspool_id
    WHERE
        rs.id NOT IN (select oldid from racktables_django.api_ipv4rs);

    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4rs) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;


 ## 024_api_ipv4lb_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.024_api_ipv4lb_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.024_api_ipv4lb_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 025_api_ipv4log_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.025_api_ipv4log_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.025_api_ipv4log_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4log);
    INSERT INTO 
        racktables_django.api_ipv4log (oldid,date,message,ip_id,user_id) 
        SELECT 
             IPv4Log.id
            ,date
            ,message
            ,ip4.id
            ,user.id
        FROM 
             racktables.IPv4Log 
             LEFT JOIN racktables_django.api_ipv4address as ip4 on ip4.oldip = IPv4Log.ip COLLATE utf8_unicode_ci 
             LEFT JOIN racktables_django.api_useraccount as user on user.username = IPv4Log.user COLLATE utf8_unicode_ci 
        WHERE 
            IPv4Log.id NOT IN (SELECT oldid FROM racktables_django.api_ipv4log);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv4log) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 026_api_ipv4nat_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.026_api_ipv4nat_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.026_api_ipv4nat_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 027_api_ipv4network_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.027_api_ipv4network_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.027_api_ipv4network_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
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


 ## 028_api_ipv6address_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.028_api_ipv6address_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.028_api_ipv6address_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6address);
    INSERT INTO 
        racktables_django.api_ipv6address (ip, oldip, name, comment, reserved) 
        SELECT 
             INET6_NTOA(ip)
             ,ip
             ,ifnull(name,'')
             ,ifnull(comment,'')
             ,CASE
                WHEN reserved = 'yes' THEN 1
                ELSE 0
            END as reserved
        FROM
            racktables.IPv6Address
        Where
            ip not in (SELECT oldip from racktables_django.api_ipv6address);

    INSERT INTO racktables_django.api_ipv6address (ip, oldip, name, comment, reserved) 
        SELECT
            INET6_NTOA(ip)
            ,ip
            ,ifnull(concat(obj.name,"-",ipal.name),'') as name
            ,'' AS comment
            ,1 AS reserved
        FROM
            racktables.IPv6Allocation as ipal
            LEFT JOIN racktables.Object as obj on object_id = obj.id
        WHERE  
            ip not in (select oldip from racktables_django.api_ipv6address);

    INSERT INTO racktables_django.api_ipv6address (ip, oldip, name, comment, reserved) 
        SELECT
            INET6_NTOA(ip)
            ,''
            ,'' AS comment
            ,0 AS reserved
            ,ip as oldip
        FROM
            racktables.IPv6Log as log
        WHERE  
            ip not in (select oldip from racktables_django.api_ipv6address)
        GROUP BY ip;

    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6address) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 029_api_ipv6allocation_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.029_api_ipv6allocation_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.029_api_ipv6allocation_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6allocation);
    INSERT INTO 
        racktables_django.api_ipv6allocation (name, alloctype, ip_id, parentobject_id) 
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
            racktables.IPv6Allocation AS ipal
            LEFT JOIN racktables_django.api_ipv6address as ipa on ipal.ip = ipa.oldip
            LEFT JOIN racktables_django.api_object as obj on object_id = obj.oldid
        where
            concat(ipal.name,"-",ipa.ip,"-",object_id) COLLATE utf8_unicode_ci NOT IN (
                SELECT 
                    concat(ipal.name,"-",ipa.ip,"-",obj.oldid) COLLATE utf8_unicode_ci
                FROM
                    racktables_django.api_ipv6allocation as ipal
                    LEFT JOIN racktables_django.api_ipv6address as ipa on ip_id = ipa.id
                    LEFT JOIN racktables_django.api_object as obj on ipal.parentobject_id = obj.id);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6allocation) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 030_api_ipv6log_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.030_api_ipv6log_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.030_api_ipv6log_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6log);
    INSERT INTO 
        racktables_django.api_ipv6log (oldid,date,message,ip_id,user_id) 
        SELECT 
             log.id
            ,date
            ,message
            ,ip.id
            ,user.id
        FROM 
             racktables.IPv6Log AS log
             LEFT JOIN racktables_django.api_ipv6address as ip on ip.oldip = log.ip
             LEFT JOIN racktables_django.api_useraccount as user on user.username = log.user COLLATE utf8_unicode_ci 
        WHERE 
            log.id NOT IN (SELECT oldid FROM racktables_django.api_ipv6log);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6log) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 031_api_ipv6network_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.031_api_ipv6network_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.031_api_ipv6network_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6network);
    INSERT INTO 
        racktables_django.api_ipv6network (oldid,ip,oldip,mask,lastip,oldlastip,name,comment) 
        SELECT 
              id
             ,INET6_NTOA(ip)
             ,ip
             ,mask
             ,INET6_NTOA(last_ip)
             ,last_ip
             ,ifnull(name,'')
             ,ifnull(comment,'')
        FROM 
             racktables.IPv6Network
        WHERE 
            ip NOT IN (SELECT oldip FROM racktables_django.api_ipv6network);
    SET inserted = (SELECT count(id) FROM racktables_django.api_ipv6network) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 032_api_config_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.032_api_config_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.032_api_config_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_config);
    INSERT INTO 
        racktables_django.api_config (name,value,vartype,nullable,hidden,userdefined,description) 
        SELECT 
               varname
              ,varvalue
              ,CASE
                WHEN vartype = 'string' THEN 1
                WHEN vartype = 'uint' THEN 2
              END as vartype
              ,CASE
                WHEN emptyok = 'yes' THEN 1
                ELSE 0
              END as nullable
              ,CASE
                WHEN is_hidden = 'yes' THEN 1
                ELSE 0
              END as hidden
              ,CASE
                WHEN is_userdefined = 'yes' THEN 1
                ELSE 0
              END as userdefined
              ,ifnull(description,'')
        FROM 
             racktables.Config
        WHERE 
            varname NOT IN (SELECT varname FROM racktables_django.api_config);
    SET inserted = (SELECT count(id) FROM racktables_django.api_config) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 033_api_file_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.033_api_file_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.033_api_file_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_file);


    INSERT INTO 
        racktables_django.api_file (oldid, name, created, size, modified, accessed, thumbnail, content, comment, filetype)
        SELECT 
               id
              ,name
              ,ctime
              ,size
              ,mtime
              ,atime
              ,thumbnail
              ,contents
              ,ifnull(comment,'')
              ,type
        FROM 
             racktables.File
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_file);
    SET inserted = (SELECT count(id) FROM racktables_django.api_file) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 034_api_filelinkipv4network_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.034_api_filelinkipv4network_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.034_api_filelinkipv4network_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv4network);
    INSERT INTO 
        racktables_django.api_filelinkipv4network (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_ipv4network as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinkipv4network) AND
            entity_type = 'ipv4net';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv4network) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 035_api_filelinkipv4rspool_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.035_api_filelinkipv4rspool_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.035_api_filelinkipv4rspool_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv4rspool);
    INSERT INTO 
        racktables_django.api_filelinkipv4rspool (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_ipv4rspool as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinkipv4rspool) AND
            entity_type = 'ipv4rspool';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv4rspool) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 036_api_filelinkipv4vs_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.036_api_filelinkipv4vs_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.036_api_filelinkipv4vs_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv4vs);
    INSERT INTO 
        racktables_django.api_filelinkipv4vs (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_ipv4vs as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinkipv4vs) AND
            entity_type = 'ipv4vs';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv4vs) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 037_api_filelinkipv6network_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.037_api_filelinkipv6network_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.037_api_filelinkipv6network_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv6network);
    INSERT INTO 
        racktables_django.api_filelinkipv6network (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_ipv6network as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinkipv6network) AND
            entity_type = 'ipv6net';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv6network) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 038_api_filelinklocation_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.038_api_filelinklocation_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.038_api_filelinklocation_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinklocation);
    INSERT INTO 
        racktables_django.api_filelinklocation (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_location as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinklocation) AND
            entity_type = 'location';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinklocation) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 039_api_filelinkobject_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.039_api_filelinkobject_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.039_api_filelinkobject_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkobject);
    INSERT INTO 
        racktables_django.api_filelinkobject (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_object as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinkobject) AND
            entity_type = 'object';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkobject) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 040_api_filelinkrack_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.040_api_filelinkrack_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.040_api_filelinkrack_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkrack);
    INSERT INTO 
        racktables_django.api_filelinkrack (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_rack as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinkrack) AND
            entity_type = 'rack';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkrack) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 041_api_filelinkrow_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.041_api_filelinkrow_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.041_api_filelinkrow_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkrow);
    INSERT INTO 
        racktables_django.api_filelinkrow (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_row as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinkrow) AND
            entity_type = 'row';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkrow) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 042_api_filelinkuser_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.042_api_filelinkuser_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.042_api_filelinkuser_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkuser);
    INSERT INTO 
        racktables_django.api_filelinkuser (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_useraccount as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinkuser) AND
            entity_type = 'user';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkuser) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 043_api_mountoperation_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.043_api_mountoperation_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.043_api_mountoperation_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_mountoperation);
    INSERT INTO 
        racktables_django.api_mountoperation (oldid,changedtime,comment,changedobject_id,new_molecule_id,old_molecule_id,user_id) 
        SELECT 
               old.id
              ,old.ctime
              ,ifnull(old.comment,'')
              ,apiobj.id
              ,oapimol.id
              ,napimol.id
              ,user.id
        FROM 
             racktables.MountOperation as old
             LEFT JOIN racktables_django.api_object as apiobj on apiobj.oldid = old.object_id
             LEFT JOIN racktables_django.api_molecule as oapimol on oapimol.oldid = old.old_molecule_id
             LEFT JOIN racktables_django.api_molecule as napimol on napimol.oldid = old.new_molecule_id
             LEFT JOIN racktables_django.api_useraccount as user on user.username = old.user_name COLLATE utf8_general_ci
        WHERE 
            old.id NOT IN (SELECT oldid FROM racktables_django.api_mountoperation);
    SET inserted = (SELECT count(id) FROM racktables_django.api_mountoperation) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 044_api_objecthistory_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.044_api_objecthistory_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.044_api_objecthistory_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_objecthistory);
    INSERT INTO 
        racktables_django.api_objecthistory (oldeventid, oldid, name, label, changedobject_id, assetno, changedtime, user_id, hasproblems, comment) 
        SELECT 
               ObjectHistory.event_id
              ,ObjectHistory.id
              ,ifnull(ObjectHistory.name,'')
              ,ifnull(ObjectHistory.label,'')
              ,apiobj.id
              ,ifnull(ObjectHistory.asset_no,'')
              ,ctime
              ,user.id
              ,CASE
                WHEN has_problems = 'yes' THEN 1
                ELSE 0
              END
              ,ifnull(ObjectHistory.comment,'')
        FROM 
             racktables.ObjectHistory
             LEFT JOIN racktables_django.api_object as apiobj on apiobj.oldid = ObjectHistory.id
             LEFT JOIN racktables_django.api_useraccount as user on user.username = ObjectHistory.user_name COLLATE utf8_general_ci
        WHERE 
            ObjectHistory.event_id NOT IN (SELECT oldid FROM racktables_django.api_objecthistory);
    SET inserted = (SELECT count(id) FROM racktables_django.api_objecthistory) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 045_api_objectlog_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.045_api_objectlog_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.045_api_objectlog_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_objectlog);
    INSERT INTO 
        racktables_django.api_objectlog (oldid,date,content,parentobject_id,user_id) 
        SELECT 
               OL.id
              ,OL.date
              ,content
              ,apiobj.id
              ,user.id
        FROM 
             racktables.ObjectLog as OL
             LEFT JOIN racktables_django.api_object as apiobj on apiobj.oldid = OL.object_id
             LEFT JOIN racktables_django.api_useraccount as user on user.username = OL.user COLLATE utf8_unicode_ci
        WHERE 
            OL.id NOT IN (SELECT oldid FROM racktables_django.api_objectlog);
    SET inserted = (SELECT count(id) FROM racktables_django.api_objectlog) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 046_api_patchcableconnector_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.046_api_patchcableconnector_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.046_api_patchcableconnector_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableconnector);
    INSERT INTO 
        racktables_django.api_patchcableconnector (oldid,defaultvalue,connectorname) 
        SELECT
             PatchCableConnector.id
            ,CASE
                WHEN PatchCableConnector.origin = 'default' THEN 1
                ELSE 0
              END
            ,connector
        FROM 
             racktables.PatchCableConnector
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_patchcableconnector);
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableconnector) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 047_api_patchcabletype_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.047_api_patchcabletype_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.047_api_patchcabletype_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcabletype);
    INSERT INTO 
        racktables_django.api_patchcabletype (oldid,defaultvalue,cabletype) 
        SELECT 
             id
            ,CASE
                WHEN origin = 'default' THEN 1
                ELSE 0
              END
            ,pctype
        FROM 
             racktables.PatchCableType
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_patchcabletype);
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcabletype) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 048_api_patchcableconnectorcompat_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.048_api_patchcableconnectorcompat_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.048_api_patchcableconnectorcompat_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableconnectorcompat);
    INSERT INTO 
        racktables_django.api_patchcableconnectorcompat (cabletype_id,connector_id) 
        SELECT 
             pct.id,
             pcc.id
        FROM 
             racktables.PatchCableConnectorCompat as pccc
             LEFT JOIN racktables_django.api_patchcableconnector as pcc on pccc.connector_id = pcc.oldid
             LEFT JOIN racktables_django.api_patchcabletype as pct on pccc.pctype_id = pct.oldid
        WHERE 
            concat(pct.id,"-",pcc.id) NOT IN (SELECT concat(cabletype_id,"-",connector_id) FROM racktables_django.api_patchcableconnectorcompat);
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableconnectorcompat) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 049_api_patchcableheap_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.049_api_patchcableheap_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.049_api_patchcableheap_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableheap);
    INSERT INTO 
        racktables_django.api_patchcableheap (oldid,amount,colour,length,description,cabletype_id,end1_id,end2_id) 
        SELECT 
             old.id
            ,old.amount
            ,(X'000000')
            ,old.length
            ,old.description
            ,pct.id
            ,pcc1.id
            ,pcc2.id
        FROM 
             racktables.PatchCableHeap as old
             LEFT JOIN racktables_django.api_patchcabletype as pct on pct.oldid = pctype_id
             LEFT JOIN racktables_django.api_patchcableconnector as pcc1 on pcc1.oldid = end1_conn_id
             LEFT JOIN racktables_django.api_patchcableconnector as pcc2 on pcc2.oldid = end2_conn_id
        WHERE 
            old.id NOT IN (SELECT oldid FROM racktables_django.api_patchcableheap);
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableheap) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 050_api_patchcableheaplog_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.050_api_patchcableheaplog_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.050_api_patchcableheaplog_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableheaplog);
    INSERT INTO 
        racktables_django.api_patchcableheaplog (oldid,date,comment,heap_id,user_id) 
        SELECT 
             old.id
            ,date
            ,old.message
            ,pch.id
            ,ua.id
        FROM 
             racktables.PatchCableHeapLog as old
             LEFT JOIN racktables_django.api_patchcableheap as pch on heap_id = pch.oldid
             LEFT JOIN racktables_django.api_useraccount as ua on user_id = ua.id
        WHERE 
            old.id NOT IN (SELECT oldid FROM racktables_django.api_patchcableheaplog);
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableheaplog) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 051_api_plugin_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.051_api_plugin_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.051_api_plugin_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_plugin);
    INSERT INTO 
        racktables_django.api_plugin (name,longname,version,homeurl,state) 
        SELECT 
             name
            ,longname
            ,version
            ,home_url
            ,0
        FROM 
             racktables.Plugin
        WHERE 
            name NOT IN (SELECT name COLLATE utf8_general_ci FROM racktables_django.api_plugin);
    SET inserted = (SELECT count(id) FROM racktables_django.api_plugin) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 052_api_portinnerinterface_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.052_api_portinnerinterface_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.052_api_portinnerinterface_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portinnerinterface);
    INSERT INTO 
        racktables_django.api_portinnerinterface (oldid,name) 
        SELECT 
             id
            ,iif_name
        FROM 
             racktables.PortInnerInterface
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_portinnerinterface);
    SET inserted = (SELECT count(id) FROM racktables_django.api_portinnerinterface) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 053_api_portouterinterface_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.053_api_portouterinterface_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.053_api_portouterinterface_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portouterinterface);
    INSERT INTO 
        racktables_django.api_portouterinterface (oldid,name) 
        SELECT 
             id
            ,oif_name
        FROM 
             racktables.PortOuterInterface
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_portouterinterface);
    SET inserted = (SELECT count(id) FROM racktables_django.api_portouterinterface) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 054_api_patchcableoifcompat_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.054_api_patchcableoifcompat_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.054_api_patchcableoifcompat_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableoifcompat);
    INSERT INTO 
        racktables_django.api_patchcableoifcompat (cabletype_id,interfacetype_id) 
        SELECT 
             pct.id as pct_id
            ,poi.id as poi_id
        FROM 
             racktables.PatchCableOIFCompat as old
             LEFT JOIN racktables_django.api_portouterinterface as poi on poi.oldid = old.oif_id
             LEFT JOIN racktables_django.api_patchcabletype as pct on pct.oldid = old.pctype_id
        WHERE 
            concat(pct.id,"-",poi.id) NOT IN (SELECT concat(cabletype_id,"-",interfacetype_id) FROM racktables_django.api_patchcableoifcompat);
    SET inserted = (SELECT count(id) FROM racktables_django.api_patchcableoifcompat) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 055_api_portcompat_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.055_api_portcompat_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.055_api_portcompat_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portcompat);
    INSERT INTO 
        racktables_django.api_portcompat (port1_id,port2_id) 
        SELECT 
             poi1.id
            ,poi2.id
        FROM 
             racktables.PortCompat
             LEFT JOIN racktables_django.api_portouterinterface as poi1 on poi1.oldid = type1
             LEFT JOIN racktables_django.api_portouterinterface as poi2 on poi2.oldid = type2
        WHERE 
            concat(poi1.id,"-",poi2.id) NOT IN (SELECT concat(port1_id,"-",port2_id) FROM racktables_django.api_portcompat);
    SET inserted = (SELECT count(id) FROM racktables_django.api_portcompat) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 056_api_portinterfacecompat_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.056_api_portinterfacecompat_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.056_api_portinterfacecompat_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portinterfacecompat);
    INSERT INTO 
        racktables_django.api_portinterfacecompat (portinnerinterface_id,portouterinterface_id) 
        SELECT
             pii.id n_iif_id
            ,poi.id n_oif_id
        FROM 
             racktables.PortInterfaceCompat pic
             LEFT JOIN racktables_django.api_portinnerinterface as pii on pii.oldid = iif_id
             LEFT JOIN racktables_django.api_portouterinterface as poi on poi.oldid = oif_id
        WHERE 
            concat(pii.id,"-",poi.id) NOT IN (SELECT concat(portinnerinterface_id,"-",portouterinterface_id) FROM racktables_django.api_portinterfacecompat);
    SET inserted = (SELECT count(id) FROM racktables_django.api_portinterfacecompat) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 057_api_port_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.057_api_port_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.057_api_port_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_port);
    INSERT INTO 
        racktables_django.api_port (oldid,name,label,comment,l2address,attachedport_id,innerinterface_id,outerinterface_id,parentobject_id,patch_id) 
        SELECT 
             old.id
            ,old.name
            ,ifnull(old.label,'')
            ,ifnull(old.reservation_comment,'')
            ,ifnull(old.l2address,'')
            ,null
            ,ii.id
            ,oi.id
            ,po.id
            ,null
        FROM 
             racktables.Port as old
             LEFT JOIN racktables_django.api_portinnerinterface as ii on ii.oldid = old.iif_id
             LEFT JOIN racktables_django.api_portinterfacecompat as oi on ii.id = oi.portinnerinterface_id
             LEFT JOIN racktables_django.api_object as po on po.oldid = old.object_id
        WHERE
            old.id NOT IN (SELECT oldid FROM racktables_django.api_port);
    SET inserted = (SELECT count(id) FROM racktables_django.api_port) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 058_api_vlandomain_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.058_api_vlandomain_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.058_api_vlandomain_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlandomain);
    INSERT INTO 
        racktables_django.api_vlandomain (oldid,parentdomain_id,description) 
        SELECT 
             id
            ,null
            ,description
        FROM 
             racktables.VLANDomain
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_vlandomain);

    UPDATE
         racktables_django.api_vlandomain as BaseDomain
        ,racktables.VLANDomain as OldDomain
        ,racktables_django.api_vlandomain as ParentDomain
    SET
        BaseDomain.parentdomain_id = ParentDomain.id
    WHERE 
        BaseDomain.oldid = OldDomain.id AND
        ParentDomain.oldid = OldDomain.group_id;

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlandomain) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 059_api_vlandescription_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.059_api_vlandescription_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.059_api_vlandescription_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlandescription);
    INSERT INTO 
        racktables_django.api_vlandescription (domain_id,vlan,vlantype,description) 
        SELECT 
             domain.id
            ,vlan_id
            ,CASE 
                WHEN vlan_type = 'ondemand' THEN 1
                WHEN vlan_type = 'compulsory' THEN 2
                WHEN vlan_type = 'alien' THEN 3
                ELSE 3
            END
            ,description
        FROM 
             racktables.VLANDescription old 
             LEFT JOIN racktables_django.api_vlandomain as domain on old.domain_id = domain.oldid
        WHERE 
            concat(domain.id,"-",vlan_id) NOT IN (SELECT concat(domain_id,"-",vlan_id) FROM racktables_django.api_vlandescription);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlandescription) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 060_api_vlanipv4_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.060_api_vlanipv4_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.060_api_vlanipv4_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanipv4);
    INSERT INTO 
        racktables_django.api_vlanipv4 (vlan_id,ipv4net_id) 
        SELECT 
             vlan.id
            ,net.id
        FROM 
             racktables.VLANIPv4 as old
             LEFT JOIN racktables_django.api_vlandescription as vlan on vlan.vlan = old.vlan_id
             LEFT JOIN racktables_django.api_ipv4network as net on old.ipv4net_id = net.oldid
        WHERE 
            concat(vlan.id,"-",net.id) NOT IN (SELECT concat(vlan_id,"-",ipv4net_id)  FROM racktables_django.api_vlanipv4);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanipv4) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 061_api_vlanipv6_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.061_api_vlanipv6_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.061_api_vlanipv6_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanipv6);
    INSERT INTO 
        racktables_django.api_vlanipv6 (vlan_id,ipv6network_id) 
        SELECT 
             vlan.id
            ,net.id
        FROM 
             racktables.VLANIPv6 as old
             LEFT JOIN racktables_django.api_vlandescription as vlan on vlan.vlan = old.vlan_id
             LEFT JOIN racktables_django.api_ipv6network as net on old.ipv6net_id = net.oldid
        WHERE 
            concat(vlan.id,"-",net.id) NOT IN (SELECT concat(vlan_id,"-",ipv6network_id)  FROM racktables_django.api_vlanipv6);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanipv6) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 062_api_portallowedvlan_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.062_api_portallowedvlan_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.062_api_portallowedvlan_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portallowedvlan);
    INSERT INTO 
        racktables_django.api_portallowedvlan (native,port_id,vlan_id) 
        SELECT 
             0
            ,vlan.id
            ,port.id
        FROM 
             racktables.PortAllowedVLAN as old
             LEFT JOIN racktables_django.api_vlandescription as vlan on vlan.id = old.vlan_id
             LEFT JOIN racktables_django.api_object as obj on obj.oldid = old.object_id
             LEFT JOIN racktables_django.api_port as port on port.parentobject_id = obj.id AND port.name = old.port_name COLLATE utf8_general_ci
        WHERE 
            concat(port.id,"-",vlan.id) NOT IN (SELECT concat(port_id,"-",vlan_id) FROM racktables_django.api_portallowedvlan);

    SET inserted = (SELECT count(id) FROM racktables_django.api_portallowedvlan) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 063_api_portlog_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.063_api_portlog_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.063_api_portlog_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portlog);
    INSERT INTO 
        racktables_django.api_portlog (oldid,date,comment,port_id,user_id) 
        SELECT 
             old.id
            ,old.date
            ,old.message
            ,port.id
            ,user.id
        FROM 
             racktables.PortLog as old
             LEFT JOIN racktables_django.api_useraccount as user on user.username = old.user COLLATE utf8_unicode_ci
             LEFT JOIN racktables_django.api_port as port on port.oldid = old.port_id
        WHERE 
            old.id NOT IN (SELECT oldid FROM racktables_django.api_portlog);

    SET inserted = (SELECT count(id) FROM racktables_django.api_portlog) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 064_api_portvlanmode_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.064_api_portvlanmode_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.064_api_portvlanmode_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_portvlanmode);

    INSERT INTO 
        racktables_django.api_portvlanmode (trunk,port_id) 
        SELECT 
             CASE
                WHEN old.vlan_mode = 'trunk' THEN 1
                ELSE 0
              END as trunk
            ,port.id
        FROM 
             racktables.PortVLANMode as old
             LEFT JOIN racktables_django.api_object as object on old.object_id = object.oldid
             LEFT JOIN racktables_django.api_object as port on port.name = old.port_name COLLATE utf8_general_ci
        WHERE 
            port.id NOT IN (SELECT port_id FROM racktables_django.api_portvlanmode);

    SET inserted = (SELECT count(id) FROM racktables_django.api_portvlanmode) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 065_api_rackobject_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.065_api_rackobject_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.065_api_rackobject_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_rackobject);
    INSERT INTO 
        racktables_django.api_rackobject (oldid,name,label,assetno,hasproblems,comment,objecttype_id,linkedobject_id) 
        SELECT 
             old.id
            ,old.name
            ,ifnull(old.label,"")
            ,ifnull(old.asset_no,"")
            ,CASE 
                WHEN old.has_problems = 'yes' THEN 1
                ELSE 0
             END
            ,old.comment
            ,objecttype.id
            ,linkedobject.id
        FROM 
             racktables.RackObject as old
             LEFT JOIN racktables_django.api_objecttype as objecttype on objecttype.oldid = old.objtype_id
             LEFT JOIN racktables_django.api_object as linkedobject on linkedobject.name = old.asset_no COLLATE utf8_general_ci
        WHERE 
            old.id NOT IN (SELECT oldid FROM racktables_django.api_rackobject);

    SET inserted = (SELECT count(id) FROM racktables_django.api_rackobject) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 066_api_rackspace_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.066_api_rackspace_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.066_api_rackspace_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_rackspace);
    INSERT INTO 
        racktables_django.api_rackspace (unitno,state,atom_id,parentobject_id,rack_id) 
        SELECT 
             old.unit_no
            ,CASE
                WHEN state = 'A' THEN 0
                WHEN state = 'U' THEN 1
                ELSE 1
            END as state
            ,atom.id as atom_id
            ,object.id as object_id
            ,rack.id as rack_id
        FROM 
             racktables.RackSpace as old
             LEFT JOIN racktables_django.api_rack as rack on rack.oldid = old.rack_id
             LEFT JOIN racktables_django.api_atom as atom on rack.id = atom.rack_id and old.unit_no = atom.unit_no
             LEFT JOIN racktables_django.api_object as object on object.oldid = old.object_id
        WHERE 
            concat(rack.id,'-',atom.unit_no) NOT IN (SELECT concat(rack_id,'-',unitno) FROM racktables_django.api_rackspace)
            AND ifnull(atom.id,'null') != 'null';

    SET inserted = (SELECT count(id) FROM racktables_django.api_rackspace) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 067_api_rackthumbnail_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.067_api_rackthumbnail_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.067_api_rackthumbnail_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_rackthumbnail);
    INSERT INTO 
        racktables_django.api_rackthumbnail (data,rack_id) 
        SELECT 
             old.thumb_data
            ,rack.id
        FROM 
             racktables.RackThumbnail as old
             LEFT JOIN racktables_django.api_rack as rack on rack.oldid = old.rack_id
        WHERE 
            rack.id NOT IN (SELECT rack_id FROM racktables_django.api_rackthumbnail);

    SET inserted = (SELECT count(id) FROM racktables_django.api_rackthumbnail) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 068_api_script_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.067_api_script_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.067_api_script_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_script);
    INSERT INTO 
        racktables_django.api_script (name,content) 
        SELECT 
             old.script_name
            ,old.script_text
        FROM 
             racktables.Script as old
        WHERE 
            script_name NOT IN (SELECT name FROM racktables_django.api_script);

    SET inserted = (SELECT count(id) FROM racktables_django.api_script) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 069_api_tag_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.069_api_tag_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.069_api_tag_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_tag);
    INSERT INTO 
        racktables_django.api_tag (oldid,assignable,name,colour,description,parenttag_id) 
        SELECT 
             old.id
            ,CASE
                WHEN old.assignable = 'yes' THEN 1
                ELSE 0
            END
            ,old.name
            ,old.color
            ,old.description
            ,null
        FROM 
             racktables.TagTree
        WHERE 
            script_name NOT IN (SELECT name FROM racktables_django.api_tag);

    UPDATE
        racktables_django.api_tag AS tag
        ,racktables.TagTree AS old
        ,racktables_django.api_tag as parent
    SET 
        tag.parenttag_id = parent.id
    WHERE
        tag.oldid = old.id AND
        parent.oldid = old.parent_id;

    SET inserted = (SELECT count(id) FROM racktables_django.api_tag) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 070_api_tagfile_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.070_api_tagfile_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.070_api_tagfile_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagfile);
    INSERT INTO 
        racktables_django.api_tagfile (date,file_id,tag_id,user_id) 
        SELECT 
             old.date
            ,obj.id
            ,tag.id
            ,user.id
        FROM 
             racktables.TagStorage as old
             LEFT JOIN racktables_django.api_file as obj on obj.oldid = old.entity_id
             LEFT JOIN racktables_django.api_tag as tag on tag.oldid = old.tag_id
             LEFT JOIN racktables_django.api_useraccount as user on user.oldid 
        WHERE
            old.entity_realm = 'file' AND
            concat(obj.id,'-',tag.id,'-',user.id) NOT IN (SELECT concat(file_id,'-',tag_id,'-',user_id) FROM racktables_django.api_tagfile);
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagfile) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 071_api_tagipv4network_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.071_api_tagipv4network_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.071_api_tagipv4network_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagipv4network);
    INSERT INTO 
        racktables_django.api_tagipv4network (date,ipv4net_id,tag_id,user_id) 
        SELECT 
             old.date
            ,obj.id
            ,tag.id
            ,user.id
        FROM 
             racktables.TagStorage as old
             LEFT JOIN racktables_django.api_ipv4network as obj on obj.oldid = old.entity_id
             LEFT JOIN racktables_django.api_tag as tag on tag.oldid = old.tag_id
             LEFT JOIN racktables_django.api_useraccount as user on user.oldid 
        WHERE
            old.entity_realm = 'ipv4net' AND
            concat(obj.id,'-',tag.id,'-',user.id) NOT IN (SELECT concat(ipv4net_id,'-',tag_id,'-',user_id) FROM racktables_django.api_tagipv4network);
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagipv4network) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 072_api_tagipv4rspool_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.072_api_tagipv4rspool_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.072_api_tagipv4rspool_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagipv4rspool);
    INSERT INTO 
        racktables_django.api_tagipv4rspool (date,ipv4rspool_id,tag_id,user_id) 
        SELECT 
             old.date
            ,obj.id
            ,tag.id
            ,user.id
        FROM 
             racktables.TagStorage as old
             LEFT JOIN racktables_django.api_ipv4network as obj on obj.oldid = old.entity_id
             LEFT JOIN racktables_django.api_tag as tag on tag.oldid = old.tag_id
             LEFT JOIN racktables_django.api_useraccount as user on user.oldid 
        WHERE
            old.entity_realm = 'ipv4rspool' AND
            concat(obj.id,'-',tag.id,'-',user.id) NOT IN (SELECT concat(ipv4rspool_id,'-',tag_id,'-',user_id) FROM racktables_django.api_tagipv4rspool);
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagipv4rspool) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 073_api_tagipv4vs_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.073_api_tagipv4vs_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.073_api_tagipv4vs_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagipv4vs);
    INSERT INTO 
        racktables_django.api_tagipv4vs (date,ipv4vs_id,tag_id,user_id) 
        SELECT 
             old.date
            ,obj.id
            ,tag.id
            ,user.id
        FROM 
             racktables.TagStorage as old
             LEFT JOIN racktables_django.api_ipv4vs as obj on obj.oldid = old.entity_id
             LEFT JOIN racktables_django.api_tag as tag on tag.oldid = old.tag_id
             LEFT JOIN racktables_django.api_useraccount as user on user.oldid 
        WHERE
            old.entity_realm = 'ipv4vs' AND
            concat(obj.id,'-',tag.id,'-',user.id) NOT IN (SELECT concat(ipv4vs_id,'-',tag_id,'-',user_id) FROM racktables_django.api_tagipv4vs);
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagipv4vs) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 074_api_tagipv6net_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.074_api_tagipv6net_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.074_api_tagipv6net_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagipv6net);
    INSERT INTO 
        racktables_django.api_tagipv6net (date,ipv4vs_id,tag_id,user_id) 
        SELECT 
             old.date
            ,obj.id
            ,tag.id
            ,user.id
        FROM 
             racktables.TagStorage as old
             LEFT JOIN racktables_django.api_ipv6network as obj on obj.oldid = old.entity_id
             LEFT JOIN racktables_django.api_tag as tag on tag.oldid = old.tag_id
             LEFT JOIN racktables_django.api_useraccount as user on user.oldid 
        WHERE
            old.entity_realm = 'ipv6net' AND
            concat(obj.id,'-',tag.id,'-',user.id) NOT IN (SELECT concat(ipv4vs_id,'-',tag_id,'-',user_id) FROM racktables_django.api_tagipv6net);
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagipv6net) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 075_api_taglocation_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.075_api_taglocation_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.075_api_taglocation_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_taglocation);
    INSERT INTO 
        racktables_django.api_taglocation (date,location_id,tag_id,user_id) 
        SELECT 
             old.date
            ,obj.id
            ,tag.id
            ,user.id
        FROM 
             racktables.TagStorage as old
             LEFT JOIN racktables_django.api_location as obj on obj.oldid = old.entity_id
             LEFT JOIN racktables_django.api_tag as tag on tag.oldid = old.tag_id
             LEFT JOIN racktables_django.api_useraccount as user on user.oldid 
        WHERE
            old.entity_realm = 'location' AND
            concat(obj.id,'-',tag.id,'-',user.id) NOT IN (SELECT concat(location_id,'-',tag_id,'-',user_id) FROM racktables_django.api_taglocation);
    SET inserted = (SELECT count(id) FROM racktables_django.api_taglocation) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 076_api_tagobject_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.076_api_tagobject_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.076_api_tagobject_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagobject);
    INSERT INTO 
        racktables_django.api_tagobject (date,object_id,tag_id,user_id) 
        SELECT 
             old.date
            ,obj.id
            ,tag.id
            ,user.id
        FROM 
             racktables.TagStorage as old
             LEFT JOIN racktables_django.api_location as obj on obj.oldid = old.entity_id
             LEFT JOIN racktables_django.api_tag as tag on tag.oldid = old.tag_id
             LEFT JOIN racktables_django.api_useraccount as user on user.oldid 
        WHERE
            old.entity_realm = 'object' AND
            concat(obj.id,'-',tag.id,'-',user.id) NOT IN (SELECT concat(object_id,'-',tag_id,'-',user_id) FROM racktables_django.api_tagobject);
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagobject) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 077_api_tagrack_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.077_api_tagrack_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.077_api_tagrack_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagrack);
    INSERT INTO 
        racktables_django.api_tagrack (date,rack_id,tag_id,user_id) 
        SELECT 
             old.date
            ,obj.id
            ,tag.id
            ,user.id
        FROM 
             racktables.TagStorage as old
             LEFT JOIN racktables_django.api_rack as obj on obj.oldid = old.entity_id
             LEFT JOIN racktables_django.api_tag as tag on tag.oldid = old.tag_id
             LEFT JOIN racktables_django.api_useraccount as user on user.oldid 
        WHERE
            old.entity_realm = 'rack' AND
            concat(obj.id,'-',tag.id,'-',user.id) NOT IN (SELECT concat(rack_id,'-',tag_id,'-',user_id) FROM racktables_django.api_tagrack);
    SET inserted = (SELECT count(id) FROM racktables_django.api_tagrack) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 078_api_vlanstrule_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.078_api_vlanstrule_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.078_api_vlanstrule_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanstrule);

-- this would be a pain to verify so I'm not doing it at the moment

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanstrule) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 079_api_vlanswitchtemplate_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.079_api_vlanswitchtemplate_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.079_api_vlanswitchtemplate_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanswitchtemplate);

    INSERT INTO 
        racktables_django.api_rackobject (oldid,revision,description,modifiedby_id) 
        SELECT 
             old.id
            ,old.mutex_rev
            ,old.description
            ,usr.id
        FROM 
             racktables.VLANSwitchTemplate as old
             LEFT JOIN racktables_django.api_useraccount as usr on old.saved_by = usr.username COLLATE utf8_unicode_ci
        WHERE 
            old.id NOT IN (SELECT oldid FROM racktables_django.VLANSwitchTemplate);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanswitchtemplate) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 080_api_vlanswitch_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.080_api_vlanswitch_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.080_api_vlanswitch_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanswitch);

    INSERT INTO 
        racktables_django.api_vlanswitch (revision,lasterror,lasterroroccured,changed,pushstarted,pushended,domain_id,parentobject_id,template_id) 
        SELECT 
             old.revision
            ,old.last_errno
            ,old.last_error_ts
            ,old.last_change
            ,old.last_push_started
            ,old.last_push_ended
            ,domain.id
            ,object.id
            ,template.id
        FROM 
             racktables.VLANSwitch as old
             LEFT JOIN racktables_django.api_vlandomain as domain on domain.oldid = old.domain_id
             LEFT JOIN racktables_django.api_object as object on object.oldid = old.object_id
             LEFT JOIN racktables_django.api_vlanswitchtemplate as template on template.oldid = old.template_id
        WHERE 
            concat(domain.id,'-',object.id,'-',template.id) NOT IN (SELECT concat(domain_id,'-',parentobject_id,'-',template_id) FROM racktables_django.api_vlanswitch);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanswitch) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 081_api_vlanvalidid_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.081_api_vlanvalidid_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.081_api_vlanvalidid_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanvalidid);

    INSERT INTO 
        racktables_django.api_vlanvalidid (vlanid) 
        SELECT 
             old.vlan_id
        FROM 
             racktables.VLANValidID as old
        WHERE 
            old.vlan_id NOT IN (SELECT vlanid FROM racktables_django.api_vlanvalidid);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vlanvalidid) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 082_api_vs_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.082_api_vs_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.082_api_vs_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vs);

    INSERT INTO 
        racktables_django.api_vs (oldid,name,vsconfig,rsconfig) 
        SELECT 
             old.id
            ,old.name
            ,old.vsconfig
            ,old.rsconfig
        FROM 
             racktables.VS as old
        WHERE 
            old.id NOT IN (SELECT vlanid FROM racktables_django.api_vs);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vs) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 083_api_vsenabledips_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.083_api_vsenabledips_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.083_api_vsenabledips_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vsenabledips);

    INSERT INTO 
        racktables_django.api_vsenabledips (parentobject_id,parentvs_id,rspool_id,vip_id)
        SELECT 
             obj.id
            ,vs.id
            ,rs.id
            ,ip4.id
        FROM 
             racktables.VSEnabledIPs as old
             LEFT JOIN racktables_django.api_object as obj on obj.oldid = old.object_id
             LEFT JOIN racktables_django.api_vs as vs on vs.oldid = old.parentvs_id
             LEFT JOIN racktables_django.api_ipv4rspool as rs on rs.oldid = old.rspool_id
             LEFT JOIN racktables_django.api_ipv4address as ip4 on BIN(ip4.oldip) = old.vip
        WHERE 
            concat(obj.id,'-',ip4.id) NOT IN (SELECT concat(parentobject_id,'-',vip_id) FROM racktables_django.api_vsenabledips);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vsenabledips) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;


 ## 084_api_vsenabledports_pull.sql ##

DROP FUNCTION IF EXISTS racktables_django.084_api_vsenabledports_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.084_api_vsenabledports_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_vsenabledips);

    INSERT INTO 
        racktables_django.api_vsenabledips (protocol,parentobject_id,parentvs_id,port_id,rspool_id)
        SELECT 
             CASE
                WHEN old.proto = 'TCP' THEN 1
                WHEN old.proto = 'UDP' THEN 2
                WHEN old.proto = 'MARK' THEN 4
             END
            ,obj.id
            ,vs.id
            ,port.id
            ,rs.id
        FROM 
             racktables.VSEnabledPorts as old
             LEFT JOIN racktables_django.api_object as obj on obj.oldid = old.object_id
             LEFT JOIN racktables_django.api_vs as vs on vs.oldid = old.parentvs_id
             LEFT JOIN racktables_django.api_ipv4rspool as rs on rs.oldid = old.rspool_id
             LEFT JOIN racktables_django.api_port as port on port.oldid = old.vport
        WHERE 
            old.id NOT IN (SELECT vlanid FROM racktables_django.api_vsenabledips);

    SET inserted = (SELECT count(id) FROM racktables_django.api_vsenabledips) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
