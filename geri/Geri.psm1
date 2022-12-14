$ModuleFolder = (Get-Module Geri -ListAvailable).path -replace "Geri\.psm1"
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

## This will only get the models defined in the python files provided
Function Get-DjangoModelList
{
    param
    (
        $Files
    )

    $Models = @()

    foreach ($File in $Files)
    {
        $Lines = get-content $File

        $NewModel = $null
        $ReadingClass = $False
        foreach ($Line in $Lines)
        {
 
            if ($Line -match "class")
            {
                Write-Verbose "Class detected, checking format"
                $Ignore = $Line -match "class ([^(]*)( |)\("
                $ClassName = $Matches[1]
                if ($Line -match "models\.Model")
                {
                    Write-Verbose "Class is of a model type, decoding"
                    if ($NewModel -ne $null)
                    {
                        $Models += $NewModel
                    }

                    $NewModel = [pscustomobject]@{
                        Name = $ClassName
                        Fields = @()
                    }

                    $ReadingClass = $True
                }
                else
                {
                    Write-Verbose "Unrecognised class"    
                    $ReadingClass = $False
                }
            }
            elseif ($ReadingClass)
            {
                Write-Debug "Checking for class properties for class $($NewModel.Name)"
                if ($Line -match "=")
                {
                    ##models\.([^(]*)\(([^)]*|)\)
                    $Ignore = $Line -match "\s*([^= ]*)(| )=(| )models\.([^(]*)\(([^)]*|)\)"

                    $Name = $Matches[1]

                    $TypeText = $Matches[4]

                    $blank = $null
                    $nullable = $null 
                    $Choices = $null
                    $Length = -1

                    If ($Matches[5] -ne "")
                    {
                        $Settings = $Matches[5] -split ","



                        foreach ($Setting in $Settings)
                        {
                            if (($Setting -match "\d{1,}") -and ($Setting -notcontains "="))
                            {
                                $Length = $Matches[0]
                            }
                            else
                            {
                                $SettingSplit = $Setting -split "="
                                if ($SettingSplit[0] -eq "blank")
                                {
                                    $blank = $SettingSplit[1] -eq "True"
                                }
                                elseif ($SettingSplit[0] -eq "null")
                                {
                                    $nullable = $SettingSplit[1] -eq "True"
                                }
                                elseif ($SettingSplit[0] -eq "choices")
                                {
                                    $Choices = $SettingSplit[1]
                                }
                            }
                        }
                    }

                    if ($Choices -ne $null)
                    {

                    }
                    else
                    {
                        $Type = switch ($TypeText) {
                            "IntegerField" {}
                            "TextField" {
                                if ($Length -lt 100)
                                {
                                    "Textbox"
                                }
                                else
                                {
                                    "TextField"    
                                }
                            }
                            "ForiegnKey" {
                                "ForiegnKeyField"
                            }
                            "BinaryField" {
                                if ($Length -eq 3)
                                {
                                    "ColorPicker"
                                }
                                else
                                {
                                    "File"
                                }
                            }
                            "BooleanField" {
                                "Checkbox"
                            }
                            "SmallIntegerField" {
                                "TextField"
                            }
                            "FloatField" {
                                "TextField"
                            }
                            "DateField" { 
                                "DatePicker"
                            }
                            "GenericIPAddressField" { 
                                "IPAddressField" 
                            }
                            "PositiveBigIntegerField" {

                            }
                            "DateTimeField" { 
                                "DateTimePicker" 
                            }
                            "PositiveSmallIntegerField" { 
                                "MaskField" 
                            }
                        }                       
                    }


                    if ($blank -eq $null)
                    {
                        $blank = $False
                    }

                    if ($nullable -eq $null)
                    {
                        $nullable = $false
                    }



                    $Field = [pscustomobject]@{
                        Name = $Name
                        Type = $Type
                        Blank = $blank
                        Nullable = $nullable
                        Length = $Length
                    }

                    $Field | Write-Verbose

                    $NewModel.Fields += $Field
                }
                else 
                {
                    Write-Verbose "Unrecognised field"
                }
            }
            else {
                Write-Verbose "This should never be hit"
            }
        }
    }

    $Models
}

Function Generate-ReactForms
{
    param
    (
        $ModelTemplate,
        $FieldTemplate,
        $StoragePath,
        $Models
    )



    foreach ($Model in $Models)
    {
        $TemplateModel = get-content $ModelTemplate

        $TemplateModel = $TemplateModel -replace '\$ModelName\$',$Model.name

        $FieldsPopulated = @("pk: 0, `n")
        $FormFieldsPopulated
        foreach ($Field in $Model.Fields)
        {
            $TempFormField = get-content $FieldTemplate
            $TempFormField = $TempFormField -replace '\$FIELDNAME\$',"$($Field.name)"
            $TempFormField = $TempFormField -replace '\$FIELDTYPE\$',"$($Field.type)"

            $FieldsPopulated += "$(Field.name): """", `n"    
        }
        $FieldsPopulated[$FieldsPopulated.count - 1] = $FieldsPopulated[$FieldsPopulated.count - 1] -replace ","

        $TemplateModel = $TemplateModel -replace '\$FIELDSWITHDEFAULTS\$',"$FieldsPopulated"

        $TemplateModel = $TemplateModel -replace '\$FORMFIELDS\$',"$FormFieldsPopulated"
    }


}

Update-RacktablesAssociations