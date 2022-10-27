## Sql Scripts

$008_api_dictionary_push = "
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
        )
"

## Hashtable

@{
    "008_api_dictionary" = @{
        "type" = "basic"
        "push" = $008_api_dictionary_push
    }
}