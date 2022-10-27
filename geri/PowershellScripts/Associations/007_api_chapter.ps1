## Sql Scripts

$007_api_chapter_push = "
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
        )
"

## Hashtable

@{
    "007_api_chapter" = @{
        "type" = "basic"
        "push" = $007_api_chapter_push
    }
}