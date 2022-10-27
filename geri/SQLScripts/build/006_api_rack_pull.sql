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
