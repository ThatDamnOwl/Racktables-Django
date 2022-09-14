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
            ,user_name
            ,user_realname
            ,''
            ,''
            ,1
            ,1
            ,NOW()
        FROM racktables.UserAccount
        WHERE 
            user_name not in (
                SELECT username
                FROM racktables_django.auth_user
            );
    INSERT INTO
        racktables_django.api_useraccount (oldid, username, realname, old_passhash, user)
        SELECT 
             UA.id
            ,user_name
            ,user_realname
            ,passhash
            ,user.id
        FROM
            racktables.UserAccount as UA
            LEFT JOIN racktables_django.auth_user as user on user.username = UA.user_name
        WHERE 
            UA.id not in (
                SELECT id
                FROM racktables_django.api_useraccount
            );
    SET inserted = (SELECT count(id) FROM racktables_django.api_useraccount) - inserted;
    RETURN inserted;
END;
$$
DELIMITER ;
