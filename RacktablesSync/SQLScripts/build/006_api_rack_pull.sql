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
