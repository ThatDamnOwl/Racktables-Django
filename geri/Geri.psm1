$ModuleFolder = (Get-Module RackTablesSync -ListAvailable).path -replace "RacktablesSync\.psm1"
Write-Verbose "Module folder is $ModuleFolder"
Write-Verbose "Loading all Associations and sub modules"


$ExtraFields = @(
                    "oldtable", `
                    "oldkey", `
                    "selfreference", `
                    "oldselfreferencefield", `
                    "newselfreferencefield", `
                    "table_type", `
                    "old_table_query", `
                    "new_table_query", `
                    "oldkey_newname", `
                    "quick_check"
                )

import-module DjangoTools -force

$Associations = @{"blank" = "blank"}

Function Update-RacktablesAssociations
{
    set-variable -name "Associations" `
                 -value (gci "$ModuleFolder\PowershellScripts" -recurse | where {$_.FullName -notmatch "\\_"} | where {$_.name -match "(ps1|psm|psd)"} | %{Write-Verbose "loading script $($_.Name)" ;. $_.FullName}) `
                 -scope Script
}

Function Invoke-SQLScriptBuild
{
    $OutSQL = @()

    $SQLScripts = gci "$ModuleFolder\SQLScripts\build"

    foreach ($SQLScript in $SQLScripts)
    {
        $OutSQL += get-content $SQLScript.fullname
    }

    $OutSQL | set-content "$ModuleFolder\SQLScripts\build.sql"
}

Function Get-RacktablesAssociations
{
    $Associations 
}

Function Invoke-RacktablesDjangoPull
{
    param
    (
        $Server,
        $Creds
    )
    Write-Verbose "Forming connection to $Server"
    $Connection = Get-MySqlConnection $Creds "$Server" "racktables"
    $Connection.open()
    $Columns = @(
        @{"Name" = "Name"},
        @{"Name" = "DB"}
    )
    $Command = "select routine_name,routine_schema from information_schema.routines where routine_type = 'FUNCTION' AND routine_schema = 'racktables_django';"
    Write-Verbose "Getting Stored pull functions"
    $PullFunctions = Invoke-MySqlQuery $Connection $Command $Columns | where {$_.name -match "_pull"} | sort Name

    $Columns = @(@{"Name" ="Inserted"})

    foreach ($PullFunction in $PullFunctions)
    {
        Write-Verbose "Invoking pull function $($PullFunction.Name)"
        $Command = "select ($($PullFunction.db).$($PullFunction.name) (1))"
        Write-Debug $Command
        $PullResult = Invoke-MySqlQuery $Connection $Command $Columns
        Write-Verbose "$($PullResult.Inserted) rows inserted"
    }

    #Invoke-DjangoPush $Server $Creds $Associations $ExtraFields
}

Update-RacktablesAssociations