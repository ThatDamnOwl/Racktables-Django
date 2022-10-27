## Sql Scripts

$001_api_molecule_push = "
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
        )
"

## Hashtable

@{"001_api_molecule" = @{
    "type" = "basic"
    "push" = $001_api_molecule_push
}}