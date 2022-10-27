## Sql Scripts

$005_api_atom_old_table = "
SELECT 
     concat(molecule_id,'-',rack_id,'-',unit_no) AS ComboID
    ,molecule_id
    ,rack_id
    ,unit_no
    ,atom 
FROM 
    racktables.Atom
"

$005_api_atom_new_table = "
 SELECT concat(api_molecule.oldid,'-',api_rack.oldid,'-',unit_no) AS ComboID
        ,api_molecule.oldid AS molecule_id
        ,api_rack.oldid AS rack_id
        ,unit_no
        ,zaxis
 FROM racktables_django.api_atom 
      LEFT JOIN racktables_django.api_molecule ON molecule_id = api_molecule.id
      LEFT JOIN racktables_django.api_rack ON rack_id = api_rack.id
"

$005_api_atom_check = "
SELECT 
     concat(molecule_id,'-',rack_id,'-',unit_no) AS ComboID
FROM 
    racktables.Atom
WHERE
    concat(molecule_id,'-',rack_id,'-',unit_no) NOT IN (
        SELECT 
            concat(api_molecule.oldid,'-',api_rack.oldid,'-',unit_no)
        FROM racktables_django.api_atom 
            LEFT JOIN racktables_django.api_molecule ON molecule_id = api_molecule.id
            LEFT JOIN racktables_django.api_rack ON rack_id = api_rack.id
    )
"

$005_api_atom_push = "
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
            concat(api_molecule.oldid,'-',api_rack.oldid,'-',unit_no)
        FROM racktables_django.api_atom 
            LEFT JOIN racktables_django.api_molecule ON molecule_id = api_molecule.id
            LEFT JOIN racktables_django.api_rack ON rack_id = api_rack.id
    )
GROUP BY molecule_id,rack_id,unit_no
"

## Hashtable

@{
    "005_api_atom" = @{
        "oldtable" = "Atom"
        "oldkey" = "ComboID"
        "oldkey_newname" = "ComboID"
        "table_type" = "query"
        "old_table_query" = @{
            "query" = $005_api_atom_old_table
            "columns" = @( `
                @{"Name" = "ComboID"}, `
                @{"Name" = "molecule_id"}, `
                @{"Name" = "rack_id"}, `
                @{"Name" = "unit_no"}, `
                @{"Name" = "atom"} `
            )
        }
        "new_table_query" = @{
            "query" = $005_api_atom_new_table
            "columns" = @( `
                @{"Name" = "ComboID"}, `
                @{"Name" = "molecule_id"}, `
                @{"Name" = "rack_id"}, `
                @{"Name" = "unit_no"}, `
                @{"Name" = "atom"} `
            )
        }
        "selfreference" = $false
        "oldselfreferencefield" = $null
        "newselfreferencefield" = $null
        "quick_check" = $005_api_atom_check
        "unit_no" = "unit_no"
        "xaxis" = 7
        "yaxis" = 7
        "zaxis" = @{
            "arguments" = @(@{
                "lookupdatabase" = "racktables"
                "lookuptable" = "Atom"
                "oldkey" = "ComboID"
                "lookup_value" = $null
                "lookuptype" = "Bunch"
            })
            "reference" = $false
            "scriptblock" = $ParseAtom
        }    
        "molecule_id" = @{
            "arguments" = @(@{
                    "lookupdatabase" = "racktables_django"
                    "lookuptable" = "api_molecule"
                    "oldkey" = "molecule_id"
                    "newkey" = "oldid"
                    "lookup_value" = $null
                    "outputkey" = "id"
                    "lookuptype" = "SingleValue"
                }
            )
            "reference" = $true
            "referencefield" = "molecule_id"
            "scriptblock" = $BasicForeignKey
        }
        "rack_id" = @{
            "arguments" = @(@{
                    "lookupdatabase" = "racktables_django"
                    "lookuptable" = "api_rack"
                    "oldkey" = "rack_id"
                    "newkey" = "oldid"
                    "lookup_value" = $null
                    "outputkey" = "id"
                    "lookuptype" = "SingleValue"
                })
            "reference" = $true
            "referencefield" = "rack_id"
            "scriptblock" = $BasicForeignKey
        }
    }
}