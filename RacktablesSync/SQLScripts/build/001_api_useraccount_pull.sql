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
